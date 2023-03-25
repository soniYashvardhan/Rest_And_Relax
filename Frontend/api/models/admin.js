const mongoose = require('mongoose');

const Admin = new mongoose.Schema({
	admin_ID: mongoose.Schema.Types.ObjectId,
	name: String,
	category: String,
	position: String,
	user_name: String,
	password: String,
	email_ID: Array,
	admin_score: String, // Like Karma on reddit
	date_joined: Date,
	privileges: Object,
	admin_of: Object // Categories they belong to
});

module.exports = mongoose.model('admin', Admin);
