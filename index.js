const prompt = require("child_process").exec;

var command = "cd ./node_modules/graphql-mocker;yarn run mock ../../&";

//var sleep = require('sleep');
var http = require("http");

var options = {
  host: "localhost",
  port: 9002,
  path: "/graphql",
  method: "POST",
};

prompt(command, function (err, stdout, stderr) {
  if (err) {
    callback(err);
    // var errorLogPath = __dirname + "/errors.log"
    // if(fs.existsSync(errorLogPath)) fs.unlinkSync(errorLogPath);
    // fs.appendFileSync(errorLogPath, err);
    console.log("1");
    return 1;
  }
  //callback(stdout);
  console.log("0");
  // return 0
});

var req = http.request(options, function (res) {
  console.log("STATUS: " + res.statusCode);
  console.log("HEADERS: " + JSON.stringify(res.headers));
  res.setEncoding("utf8");
  res.on("data", function (chunk) {
    console.log("BODY: " + chunk);
  });
});

req.on("error", function (e) {
  console.log("problem with request: " + e.message);
  return 1;
});

// write data to request body
req.write("data\n");
req.write("data\n");
req.end();

// prompt.on('close', (code, signal) => {
//   console.log(
//     `child process terminated due to receipt of signal ${signal} with code ${code}`);
//
// });

// if (prompt.error) {
//         console.log(prompt.error)
//         return 0;
//     }
//     console.log(stdout)
// });
//sleep.sleep(10); // sleep for ten seconds
// setTimeout(function() {
//   prompt.kill('SIGINT')
//   return 0
// }, 3000);
