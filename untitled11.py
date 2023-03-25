# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yNGxpwoG2zm6pJU_8yAKBH3rb0ZAs-QV
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
df = pd.read_csv('/content/drive/MyDrive/Hashcode/zomato1.csv',usecols=["name","rate","dish_liked","cuisines","reviews_list","location","approx_cost(for two people)","votes"])

for index, row in df.iterrows():
    temp = row['reviews_list'].split(", (")
    result =[]
    for i in  range(0,len(temp)):
      temp[i]= temp[i][:-2]
      temp1 = ((temp[i].split(',')[0]).split(' ')[1]).strip("'")
      result.append(float(temp1))
    print(result)
    # break
# review_list_str

df['reviews_list'] = df['reviews_list'].str.replace('\n', ' ').str.replace("'", '"')

temp = df['reviews_list'][10].split(", (")
result =[]
for i in  range(0,len(temp)):
  temp[i]= temp[i][:-2]
  result.append(temp[i])
print(result[2])

df["reviews_list"] = df["reviews_list"].apply(lambda x: x.replace("', '", ", "))
df["reviews_list"] = df["reviews_list"].apply(lambda x: x.replace("[('", ""))
df["reviews_list"] = df["reviews_list"].apply(lambda x: x.replace("', '", ","))
df["reviews_list"] = df["reviews_list"].apply(lambda x: x.replace("')]", ""))

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# # Load the dataset
# df = pd.read_csv('path/to/your/dataset.csv')

# Drop irrelevant columns
# df = df.drop(['url', 'address', 'phone', 'menu_item', 'listed_in(type)', 'listed_in(city)'], axis=1)

# Convert 'approx_cost(for two people)' column to numeric
df['approx_cost(for two people)'] = pd.to_numeric(df['approx_cost(for two people)'], errors='coerce')

# Drop rows with missing values
df = df.dropna()

# Convert 'votes' column to numeric
df['votes'] = pd.to_numeric(df['votes'], errors='coerce')

# Use TfidfVectorizer to convert text data into numerical vectors
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['cuisines'] + ' ' + df['dish_liked'] + ' ' + df['reviews_list'])

# Compute pairwise cosine similarities between all restaurants
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

import numpy as np

def get_recommendations(food_item):
    # Get all restaurants that serve the given food item
    restaurants_with_food_item = df[df['cuisines'].str.contains(food_item, case=False) | df['dish_liked'].str.contains(food_item, case=False)]

    if restaurants_with_food_item.empty:
        return []

    # Compute average rating and total number of votes for each restaurant
    ratings = []
    votes = []
    for index, row in restaurants_with_food_item.iterrows():
        restaurant_reviews = row['reviews_list']
        temp = row['reviews_list'].split(", (")
        result =[]
        # for i in  range(0,len(temp)):
        #   temp[i]= temp[i][:-2]
        #   temp1 = (temp[i].split(',')[0]).split(' ')[1]
        #   result.append(float(temp1))
        restaurant_votes = row['votes']
        # if type(restaurant_reviews) == str:
        #   ratings_list = restaurant_reviews.split(',')
        #   ratings = [float(rating.replace("'", "").strip()) for rating in result]
        #   avg_rating = sum(ratings) / len(ratings) if len(ratings) > 0 else 0
        # else:
        avg_rating = 0

        votes.append(restaurant_votes)
    restaurants_with_food_item['rating'] = ratings
    restaurants_with_food_item['votes'] = votes

    # Compute pairwise cosine similarities between restaurants that serve the given food item
    indices = restaurants_with_food_item.index.values
    cosine_sim_subset = cosine_sim[np.ix_(indices, indices)]

    # Compute scores for each restaurant based on cosine similarities and number of votes
    scores = pd.Series(restaurants_with_food_item.index, index=restaurants_with_food_item['name'])
    for i in range(len(cosine_sim_subset)):
        cosine_sim_subset[i] *= restaurants_with_food_item.iloc[i]['votes']
    cosine_sim_sum = cosine_sim_subset.sum(axis=0)
    scores = scores.iloc[cosine_sim_sum.argsort()[::-1]]

    # Return top 5 recommended restaurants
    return [{scores.index[i]: {'rating': restaurants_with_food_item.loc[scores.iloc[i]]['rating'], 'votes': restaurants_with_food_item.loc[scores.iloc[i]]['votes']}} for i in range(min(len(scores), 5))]

get_recommendations("masala dosa")

# Preprocess the data
df.dropna(subset=['dish_liked',"cuisines"], inplace=True)
df['dishes_cuisines'] = df['dish_liked'] + ' ' + df['cuisines']
# data = data.drop(columns=['votes'])

# Create TF-IDF matrix for the dishes and cuisines
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['dishes_cuisines'])
# tfidf_matrix.shape
# Get cosine similarity scores
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
# Define a function to get top 5 similar restaurants based on dish
def get_recommendations(dish, cosine_sim=cosine_sim, data=df):
    idx = data[data['dish_liked'].str.contains(dish, case=False)].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    print(sim_scores)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    restaurant_indices = [i[0] for i in sim_scores]
    sorted_idx = list(restaurant_indices)
    sorted_idx.sort(key=lambda x: df.loc[x, "votes"])
    return data.iloc[restaurant_indices][['name', 'reviews_list', 'location']]

# # Take input from user
# dish = input("Enter a dish to get restaurant recommendations: ")

# # Get restaurant recommendations based on the given dish
recommendations = get_recommendations("masala")

# # Print the recommendations
# print("Recommendations based on the dish '{}':".format(dish))
# print(recommendations.to_string(index=False))

import chardet

with open('/content/drive/MyDrive/Hashcode/zomato.csv', 'rb') as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']
    print(f"Detected encoding: {encoding}")

# with open('filename.csv', encoding=encoding) as f:
#     # your code here