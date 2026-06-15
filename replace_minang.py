import os
import re

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return
    
    # Replace Sunda with Sunda (Match cases)
    new_content = re.sub(r'Sunda', 'Sunda', content)
    new_content = re.sub(r'sunda', 'sunda', new_content)
    new_content = re.sub(r'SUNDA', 'SUNDA', new_content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")

for root, dirs, files in os.walk('.'):
    # Skip some directories
    if any(x in root for x in ['.git', 'dist', 'build', '__pycache__']):
        continue
    for file in files:
        if file.endswith(('.md', '.py', '.sunda')):
            replace_in_file(os.path.join(root, file))
