const { main } = require('./gr_faker')

console.log("Check " + __dirname + "/errors.log to see if any error occurred.")
main(process.argv[2], callback, process.argv[3], process.argv[4]);

function callback(text) {
    console.log(text);
}