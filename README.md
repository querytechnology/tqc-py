# tqc-py

Command line interface written in Python for the TinyQueries&trade; Compiler

## Installation

- Make sure you have an API key for the TinyQueries&trade; Compiler. You can get one here: https://tinyqueries.com/signup. You can choose to add `TINYQUERIES_API_KEY` to your ENV variables.
- Make sure you have Python and pip installed
- run `pip install tqc`

## Setup TinyQueries&trade; for your project

It is assumed you have a folder for your project. It can be an empty folder or a folder which contains other code as well.
- Create a folder inside your project folder (for example `tinyqueries`) in which you put your TinyQueries source queries
- Create a folder inside your project folder (for example `sql`) in which you want the compiler to put your compiled queries
- Create a config file `tinyqueries.json` or `tinyqueries.yaml` in the root of your project folder. For example:
```yaml
project:
  label: my-project-label
compiler:
  dialect: mysql
  input: ./tinyqueries
  output: ./sql
```

For a more detailed description of config files please check https://compile.tinyqueries.com

## Compile your queries

Once you have setup your project you just have to execute
```
tqc
```
from your project folder each time you want to compile your source files
