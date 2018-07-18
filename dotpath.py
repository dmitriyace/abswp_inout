import os

print(os.path.abspath('..//..'))
print(os.path.abspath('../..'))
print(os.path.abspath('..\\..'))
print(os.path.abspath('..\..'))
print(os.path.abspath('..'))
print(os.path.abspath('.'))

print(os.path.relpath('C:\\Users\\chist\\PycharmProjects\\inout',
                      'C:\\Windows\\System32'))
print(os.path.basename('C:\\Windows\\System32\\calc.exe'))
print(os.path.dirname('C:\\Windows\\System32\\calc.exe'))
print(os.path.split('C:\\Windows\\System32\\calc.exe'))