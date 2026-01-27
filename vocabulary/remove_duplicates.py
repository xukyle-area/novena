import os
import glob

# Define directories
csv_dir = '/Users/ganten/workspace/github/novena/csv_exports'

# Track seen words across all files
seen_words = set()
stats = {}

# Process files 01 to 19 in order
for i in range(1, 20):
    file_num = f"{i:02d}"
    csv_file = os.path.join(csv_dir, f"{file_num}.csv")
    
    if not os.path.exists(csv_file):
        continue
    
    # Read all lines from the file
    with open(csv_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Filter out duplicates
    unique_lines = []
    original_count = len(lines)
    removed_count = 0
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Extract the English word (first part before comma)
        parts = line.split(',', 1)
        if len(parts) >= 1:
            english_word = parts[0].strip().lower()
            
            # Check if we've seen this word before
            if english_word not in seen_words:
                seen_words.add(english_word)
                unique_lines.append(line)
            else:
                removed_count += 1
    
    # Write back the unique lines
    with open(csv_file, 'w', encoding='utf-8') as f:
        for line in unique_lines:
            f.write(line + '\n')
    
    stats[file_num] = {
        'original': original_count,
        'unique': len(unique_lines),
        'removed': removed_count
    }
    
    print(f"✓ {file_num}.csv: {original_count} → {len(unique_lines)} words (removed {removed_count} duplicates)")

print(f"\n{'='*60}")
print(f"Summary:")
print(f"Total unique words across all files: {len(seen_words)}")
print(f"{'='*60}")
