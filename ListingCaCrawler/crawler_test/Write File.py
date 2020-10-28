
'''
    Python Write File
    "x" Create - will create a file, returns an error if the file exist
    "a" Append - will create a file if the specified file does not exist
    "w" Write - will create a file if the specified file does not exist
'''
f = open("test.csv", "w")

#Title
f.write("Name,Phone,Age\n")
f.write("Sean,647-123-1234,20\n")
f.write("Winnie,647-888-1125,18\n")
f.write("John,647-666-7788,35\n")
f.write("Amy,647-765-4321,23\n")
f.write("May,647-999-1234,68\n")
f.write("Sam,647-787-1258,12\n")
f.write("Sam,647-787-1258,15\n")
f.write("John,647-666-7788,25\n")

f.close()
