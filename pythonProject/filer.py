import os
with open('/Users/jakecranor/Desktop/sample6.txt', mode='w+') as my_file:
    my_file.write("new line")
    my_file.seek(0)
    #print(my_file.read())

# print(os.path.getsize('/Users/jakecranor'))
# print(os.path.basename('/Users/jakecranor'))
# print(os.path.split('/Users/jakecranor'))
# print(os.path)

for a, b, c, in os.walk('/Users/jakecranor/Desktop'):
    print(a)
    print(b)
    print(c)
print(os.environ.get("HOME"))
print(os.path.join(os.environ.get('HOME'), 'Desktop', 'my_file'))

print(os.getcwd())
print(os.listdir())