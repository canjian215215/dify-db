## dify-db

**Author:** fly
**Version:** 0.0.1
**Type:** tool

## Description

This is a dify-db tool make it easy to query data from existing databases.

You can get different format of data, like json, csv, yaml, xlsx, html, md etc. Also support use a url to get those data.

## Features

*   **Supports Multiple Databases**: dify-db is compatible with a wide range of databases, including MySQL, Doris, Oracle, PostgreSQL, and SQLite.
*   **Versatile Data Formats**: The tool allows you to convert data into various formats, such as JSON, CSV, YAML, XLSX, HTML, and Markdown.
*   **Data Retrieval via URL**: dify-db supports fetching data through URLs.

## Usage

### Database Connection Strings

*   MySQL/Doris: `mysql+pymysql://username:password@host:port/database`
*   PostgreSQL: `postgresql+psycopg2://username:password@host:port/database`
*   Oracle: `oracle+oracledb://scott:tiger@localhost:1521/orcl`
*   SQLite: `sqlite:///database.db`

### Tools

*   `sql`: This tool is used to execute SQL queries against the database.
*   `query`: This tool translates user input into a valid SQL query.
*   `endpoint`: This feature allows you to retrieve data via URL requests.

### Example URL Request

```bash
curl -X POST 'http://localhost/e/ami75gr7a832qyw9/sql' \
  -H 'Content-Type: application/json' \
  -d '{"query":"select * from test", "format": "json"}'
```

## Installation

[Installation Link](#)

### References

*   [dify-plugin-tools-dbquery on GitHub](https://github.com/junjiem/dify-plugin-tools-dbquery)
*   [database on Dify AI Marketplace](https://marketplace.dify.ai/plugins/hjlarry/database?language=zh-Hans)

## Version History

*   0.0.1 (Initial Release)