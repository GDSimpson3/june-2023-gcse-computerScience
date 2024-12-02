# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
SPECIFIED_MATERIAL = "Copper"

# =====> Add the correct input file name
INPUT_FILE = "Screws.txt"

# =====> Add the correct extension to this file name
OUTPUT_FILE = "Bricks"

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
# =====> Complete the line with the correct variable name for the array of bricks
brickTable = ["Rustic", "Heather",
              "Staffordshire", "Tudor", "Hampton",
              "Norman", "Northcote",
              "Tuscan", "Regency",
              "Concrete Common",
              "Old English",
              "Hadrian Gold"]

inFile = ""
outFile = ""
foundCount = 0

# =====> Choose the correct value to initialise the variable
total = 0.0
#total - ""
#total = 0
#total = True

# =====> Choose the correct value to initialise the variable
#outLine = False
outLine = ""
#outLine = 0.0
#outLine = 0

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------

# Process the screws

# =====> Choose the correct line to open the file
#inFile = open ("Screws", "r")
#inFile = open ("Screws", "a")
#inFile = open (INPUT_FILE, "a")
inFile = open (INPUT_FILE, "r")

for line in inFile:
    # =====> Choose the correct line to locate the
    #        substring in the line
    #if (line.find (SPECIFIED_MATERIAL) == -1):
    if (line.find (SPECIFIED_MATERIAL) != -1):
    #if (line.find (SPECIFIED_MATERIAL) == False):
    # if (line.find (SPECIFIED_MATERIAL) == True):
        foundCount = foundCount + 1
# =====> Complete the line to increment total
    total = total + 1

# =====> Choose the correct line to close the file
inFile.close ()
#Screws.close ()
#INPUT_FILE.close ()
#outFile.close ()

# =====> Choose the correct line to display the output
#print ("Total screws: ", foundCount, "SPECIFIED_MATERIAL", total)
#print ("Total screws: ", total)
#print ("Total screws: " + str (foundCount) + "Copper" + str (total))
print ("Total screws: " + str (total) + " " + SPECIFIED_MATERIAL + " screws: " + str (foundCount))

# Process the bricks

# =====> Choose the correct line to open the bricks file
#outFile = open (OUTPUT_FILE, "r")
#outFile = open (OUTPUT_FILE, "w")
#outFile = open ("Bricks", "r")
outFile = open (OUTPUT_FILE, "a")

for brick in brickTable:
    # =====> Choose the correct line to convert the case
    brick = brick.upper ()
    #brick = brick.isalpha ()
    #brick = brick.format ("{}")
    #brick = brick.isupper ()

    # =====> Choose the correct line to complete the output line
    #outLine = brick
    # outLine = brick + "\r"
    outLine = brick + "\n"
    #outLine = brick + ","

    # =====> Choose the correct line to write the line to the file
    #outFile.writelines (brickTable)
    outFile.write (outLine)
    #outFile.writelines (brick)
    #outFile.write (brick)

outFile.close ()

# =====> Choose the correct line to display the output
# print ("Wrote", len (brickTable), "brick names to file")
#print ("Wrote", total, "brick names to file")
print ("Wrote {:^5.2f} brick names to file".format (len (brickTable)))
#print ("Wrote {:^5.2f} brick names to file".format (total))