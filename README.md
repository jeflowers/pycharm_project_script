# Multi-format Configuration Python Script for Project Structure Generation

## Overview

This Python script generates a project directory structure based on a configuration file. It supports multiple configuration file formats (YAML, JSON, and CSV) for flexibility and ease of use.

## Features

- Supports YAML, JSON, and CSV configuration file formats
- Creates directories and files based on the specified structure
- Allows specifying root files to be created in the project directory
- Provides command-line interface for easy use
- Includes error handling and informative error messages

## Requirements

- Python 3.8+
- PyYAML library

## Installation

1. Ensure you have Python 3.8 or higher installed.
2. Install the required PyYAML library:

   ```
   pip install PyYAML
   ```

3. Download the `create_structure.py` script to your local machine.

## Usage

Run the script from the command line with the following syntax:

```
python create_structure.py path/to/config_file [--output path/to/output/directory]
```

- `path/to/config_file`: The path to your configuration file (YAML, JSON, or CSV format)
- `--output`: (Optional) The directory where the project structure will be created. If not specified, the current directory will be used.

## Configuration File Formats

The script supports the following configuration file formats:

### YAML

```yaml
project_name: your_project_name
structure:
  src:
    - file1.py
    - file2.py
  tests:
    - test1.py
    - test2.py
root_files:
  - README.md
  - .gitignore
```

### JSON

```json
{
  "project_name": "your_project_name",
  "structure": {
    "src": ["file1.py", "file2.py"],
    "tests": ["test1.py", "test2.py"]
  },
  "root_files": ["README.md", ".gitignore"]
}
```

### CSV

```
project_name,your_project_name
structure,"{'src': ['file1.py', 'file2.py'], 'tests': ['test1.py', 'test2.py']}"
root_files,"['README.md', '.gitignore']"
```

## Example

1. Create a configuration file named `config.yml`:

   ```yaml
   project_name: example_project
   structure:
     src:
       - main.py
       - utils.py
     tests:
       - test_main.py
   root_files:
     - README.md
     - requirements.txt
   ```

2. Run the script:

   ```
   python create_structure.py config.yml --output ./projects
   ```

   This will create the project structure in the `./projects` directory.

## Error Handling

The script includes error handling for common issues such as:

- Unsupported file formats
- Missing configuration files
- Invalid configuration structures

In case of an error, the script will print an informative error message.

## Extending the Script

You can easily extend the script to support additional file formats or add more complex structure creation logic by modifying the `load_config` and `create_directory_structure` functions.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or have found any bugs.

## License

This script is released under the MIT License. See the LICENSE file for details.
