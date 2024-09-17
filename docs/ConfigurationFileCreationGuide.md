# Configuration File Creation Guide

This guide explains how to create configuration files for the project structure generator. The generator supports YAML, JSON, and CSV formats for configuration files.

## Table of Contents

1. [General Structure](#general-structure)
2. [YAML Format](#yaml-format)
3. [JSON Format](#json-format)
4. [CSV Format](#csv-format)
5. [Configuration Options](#configuration-options)
6. [Examples](#examples)

## General Structure

Regardless of the format, your configuration file should include the following main components:

- `project_name`: The name of your project (this will be the root directory name)
- `structure`: The directory and file structure of your project
- `root_files`: A list of files to be created in the root directory of your project

## YAML Format

YAML is the recommended format due to its readability and ease of use.

### Basic Structure:

```yaml
project_name: your_project_name
structure:
  directory_name:
    - file1.py
    - file2.py
  another_directory:
    subdirectory:
      - file3.py
root_files:
  - README.md
  - .gitignore
```

## JSON Format

JSON is a good alternative if you prefer a more standardized format.

### Basic Structure:

```json
{
  "project_name": "your_project_name",
  "structure": {
    "directory_name": [
      "file1.py",
      "file2.py"
    ],
    "another_directory": {
      "subdirectory": [
        "file3.py"
      ]
    }
  },
  "root_files": [
    "README.md",
    ".gitignore"
  ]
}
```

## CSV Format

CSV is supported for simple structures, but it's less flexible for complex nested structures.

### Basic Structure:

```csv
project_name,your_project_name
structure,"{'directory_name': ['file1.py', 'file2.py'], 'another_directory': {'subdirectory': ['file3.py']}}"
root_files,"['README.md', '.gitignore']"
```

Note: For CSV, complex structures need to be represented as strings containing valid Python dictionaries or lists.

## Configuration Options

### Project Name

- `project_name`: A string representing the name of your project. This will be used as the name of the root directory.

### Structure

- `structure`: A nested dictionary representing your project's directory and file structure.
  - Keys represent directory names.
  - Values can be:
    - A list of strings (for files in that directory)
    - Another dictionary (for subdirectories)
    - `null` or an empty dictionary `{}` (for empty directories)

### Root Files

- `root_files`: A list of strings representing files to be created in the root directory of your project.

## Examples

### Complex YAML Example

```yaml
project_name: advanced_project
structure:
  src:
    main:
      - app.py
      - utils.py
    models:
      - user.py
      - product.py
    tests:
      unit:
        - test_app.py
      integration:
        - test_database.py
  docs:
    - API.md
    - SETUP.md
  config:
    - settings.yaml
root_files:
  - README.md
  - requirements.txt
  - .gitignore
```

### Equivalent JSON Example

```json
{
  "project_name": "advanced_project",
  "structure": {
    "src": {
      "main": [
        "app.py",
        "utils.py"
      ],
      "models": [
        "user.py",
        "product.py"
      ],
      "tests": {
        "unit": [
          "test_app.py"
        ],
        "integration": [
          "test_database.py"
        ]
      }
    },
    "docs": [
      "API.md",
      "SETUP.md"
    ],
    "config": [
      "settings.yaml"
    ]
  },
  "root_files": [
    "README.md",
    "requirements.txt",
    ".gitignore"
  ]
}
```

Remember to save your configuration file with the appropriate extension (`.yaml`, `.json`, or `.csv`) and provide the correct path when running the project structure generator.
