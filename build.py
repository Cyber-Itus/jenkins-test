import os
print("Running build script - python")
os.system('aws s3 cp test.txt s3://cyberitus-builds/test.txt')
