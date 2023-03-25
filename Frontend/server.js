const express = require('express');
const MongoClient = require('mongoose')
const app = express();
const bodyParser = require("body-parser");

const posts = require('./api/routes/posts');

const PORT = 3000;
const PORT1 = 27017;

var db = {};
var mongoDbUri = `mongodb://localhost:${PORT1}`


console.log('Connecting...')

app.use(express.static('public'));
app.use(bodyParser.json());
//app.use(bodyParser.urlencoded({ extended: false }));
app.use('/posts', posts);
//mongoose.connect('mongodb://heroku_q6dxjtf3:jdbs3ma67kv6mt1ie7umfh3i0a@ds111549.mlab.com:11549/heroku_q6dxjtf3');
// mongoose.connect('mongodb://localhost/reddit');
// mongoose.connect(mongoURI);

MongoClient.connect(mongoDbUri, {reconnectTries : 500,  autoReconnect : true,  useMongoClient: true }, function(err, dbref) {
  if (!err) {
    console.log("MongoDB Server connected");
    db = dbref;
  }else{
    console.log("Error while connecting to mongoDB" + err);
  }
});
var db = MongoClient.connection;
//Show any mongoose errors
db.on("error",function(error){
	console.log("Mongoose Error: ",error);
});

// Once logged in to the db through mongoose, log a success message
db.once("open", function() {
  console.log("Mongoose connection successful.");
});

app.listen(PORT, (err) => {
  if (err) {
    return console.log('something bad happened on port:'+PORT, err)
  }
	console.log('Client running on port: ', PORT);
  console.log('Server running on port: ', PORT1);
});
