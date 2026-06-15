import os
import re

replacements = {
    r'\bkalas\b': 'kelas',
    r'\bbuek\b': 'jieun',
    r'\bawak\b': 'sorangan',
    r'\bcetak\b': 'citak',
    r'\bcubo\b': 'coba',
    r'\bangkek\b': 'angkat',
    r'\bkacuali\b': 'iwal',
    r'\bakhirnyo\b': 'tungtungna',
    r'\bambiak\b': 'candak',
    r'\bdari\b': 'ti',
    r'\bbasamo\b': 'babarengan',
    r'\btunggu\b': 'antosan',
    r'\bcocok\b': 'cocog',
    r'\bkasus\b': 'kaayaan',
    r'\bkok\b': 'lamun',
    r'\bsalamo\b': 'salami'
}

for root, dirs, files in os.walk('.'):
    if any(x in root for x in ['.git', 'dist', 'build', '__pycache__']):
        continue
    for file in files:
        if file.endswith(('.md', '.py', '.sunda')):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                continue
            
            new_content = content
            for pattern, replacement in replacements.items():
                new_content = re.sub(pattern, replacement, new_content)
                
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated keywords in: {filepath}")

