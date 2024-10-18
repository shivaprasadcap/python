from pathlib import Path

path = Path('Files/programming.txt')

message = 'I love programming.'
message += '\nI am currently learning Python.'
message += '\nI already know C, C++, C#.'

path.write_text(message)

content = path.read_text()
print(content)