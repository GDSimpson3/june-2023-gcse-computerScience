# -------------------------------------------------------------------
# Import libraries
# -------------------------------------------------------------------
import random
# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
exerciseTable = ["squats", "planks", "pushups", "lunges", "burpees"]
index = 0
name = ""
numExercises = 0
# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
print ("Here is the exercise table")

for exercise in exerciseTable:
    print (exercise)

numExercises = int (input ("How many exercises do you need (1-5)? "))

for count in range (numExercises):
    
    index = random.randint(0,4)
    name = exerciseTable[index]

    print (name)
