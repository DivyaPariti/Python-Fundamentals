## Question:
## Create a file named "file.txt" and copy paste the following information in the file :"the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car. Studying python is very important. perfect Plan B makes us perfect in python and Machine Learning". Count the number of words i.e each word comes how many times using dictionaries. For example, the comes 7 times, clown 2 times and so on. Thereafter, calculate the the word coming largest number of times. The output should be as follows:"Enter File file.txt the 7 clown 2 ran 2 after 1 car 3 and 3 into 1 tent 2 fell 1 down 1 on 1 Studying 1 python 2 is 1 very 1 important 1 perfect 2 plan 1 B 1 makes 1 us 1 in 1 and 1 Machine 1 Learning 1 Done the 7".



## Solution:
fname = input('Enter File ')
if len(fname) < 1: fname = 'file.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
         di[w] = di.get(w,0) + 1

largest = -1
theword = None
for k,v in di.items():
    print(k,v)
    if v > largest :
         largest = v
         theword = k


print('Done',theword,largest)