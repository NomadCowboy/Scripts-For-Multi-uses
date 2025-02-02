import pandas as pd
import re
import pyarabic.araby as araby

# Configuration
INPUT_FILE = "C:/Users/hassa_nbuvynr/Downloads/Book 4.xlsx"
OUTPUT_FILE = "output2.xlsx"
COLUMN_NAME = "الاسم"  # Change to your column name
KEYWORDS = ['الشهرة', 'اللقب', 'قيل', 'يقال']
HAMZA_MAP = {
    'آ': 'ا',
    'أ': 'ا',
    'إ': 'ا',
}

def clean_name(name):
    # Remove brackets and their content
    name = re.sub(r'[\[\(\{].*?[\]\)\}]', '', name)
    
    # Remove Arabic tashkeel
    name = araby.strip_tashkeel(name)
    
    # Replace Hamza characters with their base characters
    for hamza, base in HAMZA_MAP.items():
        name = name.replace(hamza, base)
    
    # Remove keywords and anything after them
    pattern = r'|'.join([re.escape(keyword) for keyword in KEYWORDS])
    name = re.split(pattern, name)[0]
    
    # Split into words and filter
    words = [word.strip() for word in name.split() if word.strip()]
    
    return ' '.join(words)

# Read Excel file
df = pd.read_excel(INPUT_FILE, engine='openpyxl')

# Clean names
df[COLUMN_NAME] = df[COLUMN_NAME].astype(str).apply(clean_name)

# Save results
df.to_excel(OUTPUT_FILE, index=False, engine='openpyxl')

print(f"Processing completed. Saved to {OUTPUT_FILE}")