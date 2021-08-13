import os
os.environ["PATH"] += ";" + r"C:\Program Files\Java\jre1.8.0_221\bin\server"
os.environ['JAVA_HOME'] = r"C:\Program Files\Java\jdk1.8.0_221\bin"

from jnius import autoclass

Stack = autoclass('java.util.Stack')
stack = Stack()
stack.push('hello')
stack.push('world')

print(stack.pop()) # --> 'world'
print(stack.pop()) # --> 'hello'