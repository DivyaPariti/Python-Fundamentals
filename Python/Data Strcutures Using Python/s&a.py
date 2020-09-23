s = list()
while True:
    a = input("Enter the Number. Input 0 to exit\n")
    if a == '0': break
    b = int(a)
    s.append(b)
average = sum(s)/len(s)
print("Sum of the Numbers is: ",sum(s))
print("Average of the Numbers is: ",average)