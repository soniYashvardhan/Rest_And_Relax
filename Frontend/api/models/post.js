const mongoose = require('mongoose');

const Post = new mongoose.Schema({
	post_Id: mongoose.Schema.Types.ObjectId,
	author: String,
	comments: Array,
	content: String,
	category: String,
	title: String,
	created_at: Date,
	updated_at: Date
	// Picture
	// Geo Tag
	// Tags (#BBMP, #BWSSB, ...)
});

module.exports = mongoose.model('post', Post);
