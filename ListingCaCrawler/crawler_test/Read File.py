
'''
    Python Read File
    "r" Read - Default value. Opens a file for reading, error if the file does not exist
    Mode:
        "t" - Text - Default value. Text mode
        "b" - Binary - Binary mode (e.g. images)
'''
import os

#Name Set
names = set()

if os.path.isfile("./test.csv"):
    f = open("test.csv", "rt")

    #Read Title
    print(f.readline())

    #Read data
    rows = f.readlines()

    for row in rows:
        data = row.split(",")
        if data[0] not in names:
            names.add(data[0])

print(names)
