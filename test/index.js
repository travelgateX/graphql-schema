const prompt = require('child_process').spawn('node',['node_modules/graphql-mocker/tools/graph_mocker/index.js',' ../']);
//var sleep = require('sleep');



prompt.on('close', (code, signal) => {
  console.log(
    `child process terminated due to receipt of signal ${signal} with code ${code}`);
    return code;

});


    // if (prompt.error) {
    //         console.log(prompt.error)
    //         return 0;
    //     }
    //     console.log(stdout)
    // });
//sleep.sleep(10); // sleep for ten seconds
setTimeout(function() {
  prompt.kill('SIGINT')
  return 0
}, 3000);
