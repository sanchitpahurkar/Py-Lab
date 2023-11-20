filename = "sample.txt"
try :
    with open(filename, 'r') as file :
        fileContent = file.read()
        print(fileContent)
except :
    print("File not found")