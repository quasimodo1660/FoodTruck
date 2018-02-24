// Import express and path modules.
var express = require( "express");
var path = require( "path");
// Create the express app.
var app = express();
// Define the static folder.
// app.use(express.static(path.join(__dirname, "./static")));
// // Setup ejs templating and define the views folder.
// app.set('views', path.join(__dirname, './views'));
// app.set('view engine', 'ejs');
// Root route to render the index.ejs view.
// app.get('/', function(req, res) {
//  res.render("index");
// })
// Start Node server listening on port 8000.
app.listen(6789, function() {
 console.log("listening on port 6789");
})