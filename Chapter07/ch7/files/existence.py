import os


filename = 'fear.txt'
path = os.path.dirname(os.path.abspath(filename))


print(os.path.isfile(filename))  # True
print(os.path.isdir(path))  # True
print(path)  # /Users/fab/srv/lpp/ch7/files
