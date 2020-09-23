fname = input("Enter the file name you want to open: ")
try:
    fhand = open(fname)
except:
    print("Cannot open the file you entered because the file doen't exist!",fname)
    exit()
   
count = 0
for line in fhand:
    if line.startswith("Part:"):
        count = count + 1
print("There are ",count,"part(s) in the file")