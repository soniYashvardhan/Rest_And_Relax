const mongoose = require('mongoose');

// Define the schema for the City model
const CitySchema = new mongoose.Schema({
  name: { type: String, required: true },
  country: { type: String, required: true },
  latitude: { type: Number, required: true },
  longitude: { type: Number, required: true },
  timezone: { type: String, required: true },
  currency: { type: String, required: true },
  places: [
    {
      name: { type: String, required: true },
      address: { type: String, required: true },
      latitude: { type: Number, required: true },
      longitude: { type: Number, required: true },
      categories: [{ type: String, required: true }],
      rating: { type: Number },
      reviews: [
        {
          author: { type: String, required: true },
          text: { type: String, required: true },
          rating: { type: Number, required: true },
          timestamp: { type: Date, default: Date.now }
        }
      ]
    }
  ],
  areas: {
    type: Map,
    of: {
      name: { type: String, required: true },
      latitude: { type: Number, required: true },
      longitude: { type: Number, required: true }
    }
  }
});

// Create the City model
const City = mongoose.model('City', CitySchema);

module.exports = City;
	