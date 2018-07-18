import os

print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
print(str(os.listdir('C:\\Windows\\System32')))
# finding totalsize of directory
totalsize=0
for filename in os.listdir('C:\\Windows\\System32'):
    totalsize = totalsize+os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalsize)