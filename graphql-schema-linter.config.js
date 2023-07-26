const fs = require("fs");

const fullSchemaFileName = __dirname + "/full_schema.graphql";
if (fs.existsSync(fullSchemaFileName)) {
  fs.unlinkSync(fullSchemaFileName);
}

let schemaString = "";
const filesCollection = getRecursiveFiles("./");

schemaString = "";
filesCollection.forEach((file) => {
  schemaString += fs.readFileSync(file, "utf8") + "\n\n";
});

fs.writeFileSync(fullSchemaFileName, schemaString);

const schemaPaths = [fullSchemaFileName];
console.log(schemaPaths);

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

module.exports = {
  rules: ["defined-types-are-used"],  
  schemaPaths: schemaPaths,
  //customRulePaths: ['path/to/my/custom/rules/*.js'],
  rulesOptions: {},
};
