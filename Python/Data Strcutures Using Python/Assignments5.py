## Question:
# Create a file named "file.txt" and copy paste the following information in the file :"the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car. Studying python is very important. perfect Plan B makes us perfect in python and Machine Learning". Count the number of words i.e each word comes how many times using dictionaries. For example, the comes 7 times, clown 2 times and so on. Thereafter, sort the words on the basis of frequency from highest to lowest i.e. the 7 would be first, then car 3 and so on. The output should be as follows:"Enter File file.txt the 7 car 3 and 3 clown 2 ran 2 tent 2 python 2 perfect 2 after 1 into 1 fell 1 down 1 on 1 Studying 1 is 1 very 1 important 1 plan 1 B 1 makes 1 us 1 in 1 and 1 Machine 1 Learning 1".



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

tmp = list()
for k,v in di.items() :
    newt = (v,k)
    tmp.append(newt)

tmp = sorted(tmp, reverse=True)

for v,k in tmp[:5] :
    print(k,v)