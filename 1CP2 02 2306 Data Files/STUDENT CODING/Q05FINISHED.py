import re
# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
lastName = ""
firstName = ""
dob = ""
myID = ""

# -------------------------------------------------------------------
# Subprograms
# -------------------------------------------------------------------
# =====> Change the names of the local variables to distinguish them
#        from the global variables with the same name
def makeID (lastNameParam, firstNameParam, dobParam):
    namePart = ""
    numberPart = 0

    namePart = lastNameParam + firstNameParam[0]  # Letter part

    # =====> Correct the logic error caused by using the int() function
    #        in the number part calculation rather than using a function
    #        that returns the ASCII value of the character
    for character in str(dobParam):
        # print(numberPart)
        # print(character)
        numberPart = numberPart + ord(character)

    yourID = namePart + str (numberPart)

    return (yourID)

# =====> Add a procedure, with no parameters, to display a
#        welcome message for the user
def welcome():
    print('Welcome to the User ID generation program')
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
# =====> Call the welcome procedure before taking input from the user
welcome()
# Get last name and first name from the user
firstName = input ("Enter your first name: ")
lastName = input ("Enter your last name: ")

# =====> Convert last name and first name to lowercase after they
#        are inputted by the user
lastName = lastName.lower()
firstName = firstName.lower()


# def DOBValidation():
    # Get date of birth from the user
dob = input ("Enter your date of birth (ddmmyyyy): ")

    # =====> Check that only the digits 0 to 9 appear in the date of birth

def find(value):
    z = re.findall("[0-9]",value)
    if len(z) == 8:
        return True
    else: return False



validation = "^[0-9]{8}"
while not re.match(validation,dob):
# while  find(dob) == False:
    # =====> Call the makeID() function, if the date of birth is valid
       
    # =====> Tell the user, if the date of birth is invalid
    # else:
        # while re.match(validation,dob) == False:
    
    print('Invalid DOB')
    dob = input ("Enter your date of birth (ddmmyyyy): ")

    # DOBValidation()
        # dob = input ("Invalid DOB. reEnter your date of birth (ddmmyyyy): ")

# DOBValidation()

myID = makeID (lastName, firstName, str(dob))
print (myID)