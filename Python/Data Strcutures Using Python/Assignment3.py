## Question
## Create a file named "file.txt" with the following text mentioned below. You are requested to extract Day i.e. Sat, Sun etc from this file and print the days so that your output looks like: SatSunMonTueWed. (Print the output in new lines i.e. Sat then next line Sun then next line Mon etc.)


## Solution

han = open ('file.txt')

for line in han:
     line = line.rstrip()
     wds = line.split()
     if len(wds)<3 or wds[0]!='From' :
          continue
     print(wds[2])