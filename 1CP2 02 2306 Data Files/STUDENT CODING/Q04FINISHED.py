# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# =====> Write your code here

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
b = float(input('Enter the Base of the prism '))
h = float(input('Enter the Height of the prism '))
l = float(input('Enter the length of the prism '))
# Check for invalid inputs, using relational and logical operators

def checker(value):
    if not type(value) == float:
        return False
    elif value < 0.0:
        return False
    else:
        return True
   
valid = False


while not valid == True:
    if checker(b) == False:
        valid = False
        b = float(input('INVALID INPUT::::: reEnter the Base of the prism '))


    elif checker(h) == False:
        valid = False
        h = float(input('INVALID INPUT::::: reEnter the Height of the prism '))


    elif checker(l) == False:
        valid = False
        l = float(input('INVALID INPUT::::: reEnter the length of the prism '))

    else:
        valid = True


# Display an error message if any input is invalid
# Invalid input should not be processed



# Process all valid inputs
# Calculate the area of the triangle
area = b * h * 0.5
# Display the area of the triangle, rounded to two decimal places
print(f"Area of Triangle is {round(area,2)} ")
# Calculate the volume of the prism
volume = area * l
# Display the volume of the prism using the <string>.format() function
layout = "{:^5.2f} {:11}"
print(layout.format(volume,"Cubic Units"))
# OutputString = 
# in eight columns with two decimal places

# In all cases, display a goodbye message just before terminating

