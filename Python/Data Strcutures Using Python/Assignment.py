## Question
## Take the following Python code that stores a string:`str = 'Perfect-Plan-B:0.7541' Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number

## Solution :
string = 'Perfect-Plan-B:0.7541'
position = string.find(':')
number = string[(position+1):]
floating_number = float(number)
print(floating_number)