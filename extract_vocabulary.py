import re
import os

# Define input and output directories
vocab_dir = '/Users/ganten/workspace/github/novena/vacabulaury'
output_dir = '/Users/ganten/workspace/github/novena/csv_exports'

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

def extract_vocabulary(md_file_path):
    """Extract English words and Chinese meanings from markdown table"""
    words = []
    
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all table rows with pattern: | word | phonetic | chinese | example |
    # Match lines that start with | and have at least 3 |
    lines = content.split('\n')
    
    for line in lines:
        # Skip header lines and separator lines
        if line.startswith('|') and '---' not in line and '英文' not in line:
            parts = [p.strip() for p in line.split('|')]
            # Valid data row should have at least 4 parts (including empty start/end)
            if len(parts) >= 5:
                english = parts[1].strip()
                chinese = parts[3].strip()
                
                # Skip empty entries
                if english and chinese and english != '英文' and chinese != '中文':
                    words.append((english, chinese))
    
    return words

# Process files 01 to 19
for i in range(1, 20):
    file_num = f"{i:02d}"
    input_file = os.path.join(vocab_dir, f"{file_num}-*.md")
    
    # Find the actual file (since they have descriptive names)
    import glob
    matching_files = glob.glob(input_file)
    
    if matching_files:
        input_file = matching_files[0]
        output_file = os.path.join(output_dir, f"{file_num}.csv")
        
        try:
            words = extract_vocabulary(input_file)
            
            # Write to CSV
            with open(output_file, 'w', encoding='utf-8') as f:
                for english, chinese in words:
                    f.write(f"{english},{chinese}\n")
            
            print(f"✓ Processed {file_num}: {len(words)} words -> {output_file}")
        except Exception as e:
            print(f"✗ Error processing {file_num}: {e}")
    else:
        print(f"✗ File not found: {file_num}")

print(f"\n✓ All files processed. Output directory: {output_dir}")
