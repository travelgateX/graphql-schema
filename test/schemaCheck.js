const { describe, it } = require("mocha");
const chai = require("chai");
const fs = require("fs");
const { makeExecutableSchema } = require("@graphql-tools/schema");

let schemaString = "";

chai.should();
describe("Test Schema", () => {
  before(() => {
    console.log("Load schema from files ...");
    const filesCollection = getRecursiveFiles("./");

    schemaString = "";
    filesCollection.forEach((file) => {
      schemaString += fs.readFileSync(file, "utf8") + "\n\n";
    });
  });

  it("Check make schema", () => {
    chai.assert.isNotNull("1", "not null");
    try {
      makeExecutableSchema({ typeDefs: [schemaString] });
    } catch (e) {
      console.log(e);

      if (e.locations && e.locations.length > 0) {
        let errorLine = e.locations[0].line;
        const lines = schemaString.split("\n");
        errorLine -= 5;
        for (let i = 0; i < 11; i++) {
          console.log(errorLine + i + ":" + lines[errorLine + i]);
        }
      } else {
        console.log("Could not locate the error.");
      }


      //Generate test error.
      chai.assert.isNotNull(null, "Error creating Graphql schema");

    }
  });
});

function getRecursiveFiles(dirname) {
  const folderExceptions = [
    ".git",
    ".github",
    ".nyc_output",
    "coverage",
    "node_modules",
    "test",
    "_skel",
    ".lh",
    ".history",
  ];
  const extensionsToInclude = ["graphql"];
  let filesCollection = [];

  fs.readdirSync(dirname, "utf8").forEach((file) => {
    if (!folderExceptions.includes(file)) {
      pathFile = dirname + file;
      if (fs.lstatSync(pathFile).isDirectory()) {
        const ret = getRecursiveFiles(pathFile + "/");
        filesCollection = filesCollection.concat(ret);
      } else {
        const ext = file.split(".").filter(Boolean).slice(1).join(".");

        if (extensionsToInclude.includes(ext.toLowerCase())) {
          filesCollection.push(pathFile);
        }
      }
    }
  });

  return filesCollection;
}
