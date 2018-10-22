# Testing Gateway

This document is intended to understand how works our testing system

## Usage

For use the testing system you only need execute the next command
```sh
python test_gateway.py
```

This python is in “scripting/gateway” path. The script has two params

* **Path to search**: That arg is required and define the path to search recursively the gist files. This path is relative to repository
* **Verbose**: Enable the verbose output

![alt text](http://pix.toile-libre.org/upload/original/1540191451.png "Run script")

## How works

The testing system find all files with .gist extension into the path passed by arg recursively. Then for each file it parsed it and get info about that test, that info contains the query to test and the result or callback to check if the query works fine.

## Gist Files

The gist files (file.gist) is a JSON file contains info about the test to execute and how check is result. The queries associated to the gist file, are store into a gist from GitHub.

The gist form GitHub is a system to store and version snippets code, here you can see a [example](https://gist.github.com/amian84/4a68199534c133021c432a1bd94ec41a)

![alt text](http://pix.toile-libre.org/upload/original/1540192142.png "Gist from Github 1")

Into the Gist you can have one or more files, for our propose you must have **query.graphql** file that contains the query to test, for the check the result you should have one of these two files **result.json** or **callback.py**. With **result.json** you check the complete result of request with that expected result. If would you like more specific to check the result then you need **callback.py** file that contains a python callback function to check the result.

![alt text](http://pix.toile-libre.org/upload/original/1540192215.png "Gist from Github 2")

### Gist File Contains

The gist file are JSON file. The name of file should be related to object type of GraphQL schema to test, this is not mandatory but advisable. Then if we would like test any query from IAM then we make file "common_AdminQuery.gist" into path “admin/iam/commons”

![alt text](http://pix.toile-libre.org/upload/original/1540195523.png "Gist file 1")

The file contains

![alt text](http://pix.toile-libre.org/upload/original/1540195590.png "Gist file 2")

The "gists" key is a list of gist test info

* **id**: Numeric index
* **user**: Gist user from GitHub
* **gist-id**: Gist ID from GitHub (is in the URL)
* **gist-bck**: Gist ID of backup
* **level**: Criticality level
  - **0**: Low  
  - **1**: Medium
  - **2**: Critical
* **type**: The gist type, we can use gist for QA and for Documentation or both
  - **0**: QA
  - **1**: Doc
  - **2**: Both
* **check-type**: Type to check the result
  - **0**: Check with the result.json expected
  - **1**: Check with callback from callback.py

Each gist from the same file is for each test in the same scope

![alt text](http://pix.toile-libre.org/upload/original/1540197517.png "Gist file 3")

### Callback

If we can check the result of query with a callback we need write a callback function into our gist with the name **callback.py**, this must have that name and contains a function called callback

![alt text](http://pix.toile-libre.org/upload/original/1540197937.png "callback 1")

Always we import **utils** module cause here utils module is in charge on some parts need to write into our logger. Callback function always has the same parameters:

* **gistObject**: This is a gist object with all info about the gist
* **result**: This is the JSON result of request with the query
* **logger**: Instance of our logger

#### Gist Object

This is the attributes for the gist object

* **query**: The query to test
* **result**: 'None' cause we checking the result with a callback. Normally contains the expected result
* **callback**: Python code of callback
* **gist_info**: The info of gist from JSON:
  - **idJson**: Index of gist into JSON
  - **user**: User of gist
  - **gid**: Id of gist from GitHub
  - **gidbk**: Id of backup gist from GitHub
  - **type**: type of gist
    - **0**: QA
    - **1**: Doc
    - **2**: Both
  - **level**: Criticality level
    - **0**: Low
    - **1**: Medium
    - **2**: Critical
  - **check_type**: Check type to check the result
    - **0**: Check with expected result
    - **1**: Check with callback

#### Result

The object with a JSON parse of request result. For people unfamiliar with python we define the more typical uses

#### Access to value

To get value from JSON in python we do with the next code

```python
result['data']
```

We can concatenate the accesses

```python
result['data']['admin']
```

For that access we have this part of JSON

![alt text](http://pix.toile-libre.org/upload/original/1540198671.png "Access value")

#### List Iterate 

Sometimes we have a list from the result. The list in python we can iterate with the next code

```python
for item in vble_list:
    do_something(item)
```

For example if we can print code of organizations we do:

```python
for org in result['data']['admin']['organizations']['edges']:
    print (org['node']['code'])
```

#### Know if exist a key into object

To know if the JSON has a key we can use two way


```python
result.has_key("errors") # => return True or False
```
or 
```python
"errors" in result # => return True or False
```

### Logger

The object logger contains functions to write in our log, the functions are:

* **writeLog(message, level=log)**: That function write the message into the loglevel file, the log levels are defined into utils module

```python
logger.writeLog("some text")
logger.writeLog("some text", utils.LOG_LEVEL.ERROR)
```

### Utils

This is the functionality of utils module

* **LOG_LEVEL**: Log level
  - **ERROR**: Error level
  - **LOG**: Log level
  - **WARN**: Warning level
* **GIST_TYPE**: Type of gist
  - **QA**: Type for testing
  - **DOC**: Type for documentation
  - **BOTH**: Type for both (doc and test)
* **GIST_CHECK_TYPE**: Type of check result
  - **JSON**: Check with expected result
  - **CALLBACK**: Check with callback
* **GIST_LEVEL**: Criticality level
  - **LOW**
  - **MEDIUM**
  - **CRITICAL**
* **getVerbose()**: Get value of verbose (true or false)
* **setVerbose(value)**: Set value of verbose to the param value
  
 



