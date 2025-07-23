# Password Generator with Graphical Interface

## Overview

This repository provides a **Password Generator with a Graphical Interface**, implemented in Python. The application allows users to generate secure passwords of customizable length using a user-friendly, modern graphical user interface. Additionally, the tool enables users to export generated passwords in various formats and copy them to the clipboard for convenience.

## Features

- **Graphical User Interface (GUI):**  
  Built with `customtkinter`, the app offers a modern and responsive window for user interaction.
- **Customizable Password Generation:**  
  Users can specify the desired length of the password (within supported limits).
- **Diverse Character Set:**  
  Passwords are generated using a broad set of symbols, numbers, and letters for improved security.
- **Export Options:**  
  Generated passwords can be exported to multiple formats:
  - **Text file**
  - **CSV file**
  - **Excel file**
  - **JSON file**
- **Clipboard Support:**  
  Copy passwords directly to the clipboard with a single click.
- **User Feedback:**  
  Informative message boxes notify users of successful actions or input errors.
- **File Utilities:**  
  Helper utilities allow for file creation, deduplication, and management.

## Main Technologies

- **Python** (primary language)
- **customtkinter** (for GUI)
- **openpyxl** (for Excel export)
- **pyperclip** (for clipboard operations)
- **csv**, **json**, **os** (for file operations)

## Key Implementation Details

- **Password Generation Logic:**  
  The core password generation is handled in the `generator_password.py`, using a customizable character set defined in `helper/symbols_for_password.py`.  
  User input is validated for type and range before generating the password.

- **Export Mechanism:**  
  The `ExportFormat` class in `helper/export_format.py` provides methods to export passwords to different formats.  
  The default export directory is the user's Downloads folder.

- **GUI Structure:**  
  - The main window (`App` class) hosts the primary controls.
  - A secondary window (`ToplevelWindow`) appears after password generation, offering export and copy options as buttons.
  - All dialogs and notifications use the `tkinter.messagebox`.

- **Helper Utilities:**  
  - `Helper` class in `helper/helper.py` offers file and directory management and deduplication.
  - Utility methods enable random pauses, file creation from lists, and more.

- **Clipboard Copy:**  
  The `copy_password` function in `helper/utils.py` uses `pyperclip` to copy passwords and informs the user via a message box.

## Example Usage

1. Launch the application.
2. Enter the desired password length.
3. Click to generate a password.
4. After generation, use the secondary window to:
    - Export the password in your preferred format.
    - Copy the password to clipboard.
    - Open the export directory directly.

## Getting Started

Clone the repository and enter the project directory:

```bash
git clone https://github.com/mihaiapostol14/CTKGeneratorPassword.git
cd CTKGeneratorPassword
``` 

Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

## Repository Status

- **Language:** Python
- **License:** Not specified
- **Issues:** No open issues
- **Stars/Forks:** 0/0 (private usage or early stage)
- **Created:** July 2022
- **Last Updated:** July 2025

## Author

- [mihaiapostol14](https://github.com/mihaiapostol14)

---

> This project is suitable for anyone looking for a simple, extensible password generator with multiple export options and a user-friendly GUI.