from pathlib import Path

path = Path('Files\pi_digits.txt')
print(path)
content = path.read_text()
# content = content.rstrip()
lines = content.splitlines()
print(lines)

for line in lines:
    print(line)