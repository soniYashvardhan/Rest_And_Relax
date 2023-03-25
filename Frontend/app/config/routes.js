import React from 'react';
import { IndexRoute, Route, Router, hashHistory } 
  from 'react-router';

import Main from '../components/Main';
import Listing from '../components/category/Listing';
import NewPost from '../components/Form/NewPost';
import Comments from '../components/Form/Comments';
import DetailForm from '../components/category/DetailForm';
import ViewComments from '../components/category/ViewComments';

module.exports = (
  <Router history={hashHistory}>
    <Route path="/" component={Main} >
  		<Route path="/newpost" component={NewPost} />
      <Route path="/viewcomments" component={ViewComments} />
  		<Route path="/comments/:id" component={Comments} />
  		<Route path="/:categoryId" component={Listing} />
  		<IndexRoute component={Listing} />
    </Route>
  </Router>
);
