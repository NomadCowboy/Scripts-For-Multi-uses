# Scripts-For-Multi-uses

# Arabic Name Cleaner

This script processes an Excel file containing Arabic names, cleans the names by removing specific characters and keywords, and saves the cleaned data to a new Excel file.

## Requirements

- Python 3.x
- pandas
- re
- pyarabic

## Installation

1. Install the required Python packages:
    ```sh
    pip install pandas pyarabic
    ```

## Configuration

Update the following configuration variables in the script as needed:

- [INPUT_FILE](http://_vscodecontentref_/0): The name of the input Excel file (default: `input.xlsx`).
- [OUTPUT_FILE](http://_vscodecontentref_/1): The name of the output Excel file (default: `output.xlsx`).
- [COLUMN_NAME](http://_vscodecontentref_/2): The name of the column containing the names to be cleaned (default: `الاسم`).
- [KEYWORDS](http://_vscodecontentref_/3): A list of keywords to remove from the names (default: `['الشهرة', 'اللقب', 'قيل', 'يقال']`).
- [HAMZA_MAP](http://_vscodecontentref_/4): A dictionary mapping Hamza characters to their base characters (default: `{'آ': 'ا', 'أ': 'ا', 'إ': 'ا'}`).

## Usage

1. Place your input Excel file in the same directory as the script.
2. Run the script:
    ```sh
    python script_name.py
    ```
3. The cleaned data will be saved to the specified output Excel file.

## Functions

### [clean_name(name)](http://_vscodecontentref_/5)

Cleans a given Arabic name by:
- Removing brackets and their content.
- Removing Arabic tashkeel.
- Replacing Hamza characters with their base characters.
- Removing specified keywords and anything after them.
- Splitting the name into words and filtering out empty words.

### `process_file(input_file, output_file, column_name)`

Processes the input Excel file by:
- Reading the Excel file.
- Cleaning the specified column using the [clean_name](http://_vscodecontentref_/6) function.
- Saving the cleaned data to a new Excel file.

## Example

```python
# Configuration
INPUT_FILE = "input.xlsx"
OUTPUT_FILE = "output.xlsx"
COLUMN_NAME = "الاسم"
KEYWORDS = ['الشهرة', 'اللقب', 'قيل', 'يقال']
HAMZA_MAP = {
    'آ': 'ا',
    'أ': 'ا',
    'إ': 'ا',
}

# Run the script
if __name__ == "__main__":
    process_file(INPUT_FILE, OUTPUT_FILE, COLUMN_NAME)
