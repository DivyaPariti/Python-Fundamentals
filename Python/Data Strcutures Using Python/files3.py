f= open("demo.txt")
for line in f:
    line  = line.rstrip() ## Strips away the extra spaces printed in the output 
    print(line)