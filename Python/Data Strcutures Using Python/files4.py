f = open("demo.txt")
for line in f:
    line  = line.rstrip() ## Strips away the extra spaces printed in the output 
    if line.startswith("Today"):
        print(line)  
      
f = open("demo.txt")
for line in f:
    line = line.rstrip()
    if not line.startswith("Parts:"):
        continue
    print(line)