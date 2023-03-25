const mongoose = require('mongoose');

const User = new mongoose.Schema({
	user_ID: mongoose.Schema.Types.ObjectId,
	name: String,
	user_name: String,
	password: String,
	email_ID: Array,
	user_score: String, // Like Karma on reddit
	date_joined: Date,
	privileges: Object,
	subscriptions: Object // Categories they subscribe to
});

module.exports = mongoose.model('user', User);
