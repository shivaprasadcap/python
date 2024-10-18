from pathlib import Path

path = Path('Files\language.txt')
content = path.read_text()
print(content)

print(content.replace('Python', 'C'))