'''Program For Copying The Contents:
Developed by: A NAVEEN KUMAR
RegisterNumber: 21004621 '''


print("Enter the Name of Source File: ")
sFile = input()
print("Enter the Name of Target File: ")
tFile = input()
fileHandle = open(sFile,"r")
texts = fileHandle.readlines()
fileHandle.close()

fileHandle = open(tFile, "w")
for s in texts:
    fileHandle.write(s)
fileHandle.close()

print("\nFile Copied Successfully!")
