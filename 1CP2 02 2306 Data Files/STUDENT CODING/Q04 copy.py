# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# =====> Write your code here

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Write your code here
# Take three decimal inputs from the user
b = float(input('Enter the Base of the prism'))
h = float(input('Enter the Height of the prism'))
l = float(input('Enter the length of the prism'))
# Check for invalid inputs, using relational and logical operators

invalid = [False,'','']

def inputFunc():
    if not b > 0.0:
        invalid = [True,'Bad Input, Please enter a decimal above 0 for B','B']
    if not h > 0.0: 
        invalid = [True,'Bad Input, Please enter a decimal above 0 for H','H']
    if not l > 0.0:
        invalid = [True,'Bad Input, Please enter a decimal above 0 for L','L']
    else:
        invalid = [False,'','']
    return invalid
 


# Display an error message if any input is invalid
# Invalid input should not be processed

while not inputFunc()[0] ==True:
    print(invalid[1])
    if invalid[2] == "B":
        b = float(input('Enter the Base of the prism'))
    elif invalid[2] == "H":
        h = float(input('Enter the Height of the prism'))
    elif invalid[2]== "L":
        l = float(input('Enter the length of the prism'))


    if not b > 0.0:
        invalid = [True,'Bad Input, Please enter a decimal above 0 for B','B']
    if not h > 0.0:
        invalid = [True,'Bad Input, Please enter a decimal above 0 for H','H']
    if not l > 0.0:
        invalid = [True,'Bad Input, Please enter a decimal above 0 for L','L']
    else:
        invalid = [False,'A','A']




# Process all valid inputs
# Calculate the area of the triangle

# Display the area of the triangle, rounded to two decimal places

# Calculate the volume of the prism

# Display the volume of the prism using the <string>.format() function
# in eight columns with two decimal places

# In all cases, display a goodbye message just before terminating

