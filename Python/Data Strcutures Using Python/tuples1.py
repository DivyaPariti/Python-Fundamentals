## Sorting tuples. When we sort the tuples using sorting method the tuples are sorted based on their keys not based on their values. To sort them according their values we use the below small trick

a = {'p':20, 'q':30, 'r':10}
temp = list()
for keys,values in a.items():
    temp.append((values,keys))
print(temp) # prints the values first then the keys as list
temp = sorted(temp)
print(temp) # prints us the output in increasing order of values 
temp = sorted(temp, reverse = True)
print(temp) # prints the decending order of values