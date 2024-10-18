string= 'wwkklmghjklmhgklm'
sub_string= 'klm'
count = 0

for i in range(0,len(string)):
    if string[i:i+len(sub_string)] == sub_string:
        count += 1

print(f'Substring "{sub_string}" is repeated {count} times in the string "{string}"')