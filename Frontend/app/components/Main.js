import React, { Component } from 'react';
import { Link }  from 'react-router';

export default class Main extends Component {
	render() {
		console.log("main....");
		return (
			<div className="container">
	      		<div className="jumbotron">
		        	<h2><strong>TownSquare</strong></h2>
					<Link to="/newpost">Create New Post</Link>
					<Link to="/viewcomments">viewcomments</Link>
					<Link to="/comments/:id">comments/:id</Link>
					<Link to="/:scategoryId">:categoryId</Link>
	      		</div>

		      	<div className="row">
		        	{/* This code will dump the correct 
		        	Child Component */}
		        	{/* {console.log(this.props.children)} */}
		        	{this.props.children}
		      	</div>
	    	</div>
		);
	}
}
