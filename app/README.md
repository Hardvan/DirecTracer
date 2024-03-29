# DirecTracer

DirecTracer is a Python script that generates a directory structure in both text and Markdown formats. It can be used to visualize the hierarchy of folders and files in a given directory, while also excluding specific folders and file extensions.

## Features

- Generates a directory structure in text and Markdown formats.
- Supports ignoring specific directories and file extensions.
- Outputs clickable links in the Markdown file for easy navigation.

## Usage

Install the DirecTracer package using the following command:

```bash
pip install DirecTracer
```

OR

Clone this repository using the following command:

```bash
git clone https://github.com/Hardvan/DirecTracer
cd DirecTracer
pip install .
```

Call the `save_directory_structure` function from the `DirecTracer` module to generate the directory structure.

```python
from DirecTracer import save_directory_structure
import os


# Generate the directory structure in text and Markdown formats
save_directory_structure(
   root_dir=os.getcwd(),
   text_output_file="directory_structure.txt",
   markdown_output_file="directory_structure.md",
   animation=True
)
```

The function accepts the following parameters:

- **root_dir (str):** The root directory to start scanning from. Defaults to the current working directory.
- **text_output_file (str):** The name of the text output file. Defaults to "directory_structure.txt".
- **markdown_output_file (str):** The name of the Markdown output file. Defaults to "directory_structure.md".
- **ignored_directories (list, optional):** List of directories to ignore. Defaults to [".git", ".vscode", "venv", ".venv", ".idea", "out"].
- **ignored_extensions (list, optional):** List of file extensions to ignore. Defaults to [".exe"].
- **animation (bool, optional):** Enable/Disable the loading animation. Defaults to False.


