module.exports = {
    main: main
};

const prompt = require('child_process').exec;
const { printMockerHelp } = require('./help');
const fs = require("fs");

function main(schemaPath, callback, port, extend) {
     //If --h/--help, show help and exit
     if (schemaPath === "--h" || schemaPath === "--help") {
        printFakerHelp();
        return;
    }

    var command ='graphql-faker '+ schemaPath;
    //Add options
    command = (port)   ? command + " -p " + port   : command;
    command = (extend) ? command + " -e " + extend : command;

    //Run faker
    prompt(command, function (err, stdout, stderr) {
        if (err) { 
            callback(err); 
            var errorLogPath = __dirname + "/errors.log"
            if(fs.existsSync(errorLogPath)) fs.unlinkSync(errorLogPath);
            fs.appendFileSync(errorLogPath, err); 
            return; 
        }
        callback(stdout); 
    });
}
