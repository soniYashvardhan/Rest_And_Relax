import React, { Component } from 'react';
import { Link }  from 'react-router';

import Comments from '../Form/Comments';
import AddData from '../Form/NewPost';
import ListItem from '../category/ListItem';

{/*	console.log("DetailForm props",props); */}

export default class DetailForm extends Component {
	constructor(props){
		super(props);
		console.log("DetailForm props",(props));
		this.state=props.params;
		var comments = this.props.data.comments;
	}
	render() {
		return (
			<div>
				<h2>{this.props.data.title}</h2>

				<p>{this.props.data.content}</p>
				<p>{this.props.data.comments}</p>
				
			</div>
		);
	}
}