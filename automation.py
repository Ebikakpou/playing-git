import os

files = os.listdir('.')
for file in files:
    print(file)
with open('login.txt', 'w') as f:
    f.write("automation is successful")