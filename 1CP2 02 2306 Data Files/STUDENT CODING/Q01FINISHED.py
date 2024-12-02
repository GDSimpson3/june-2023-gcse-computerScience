# -------------------------------------------------------------------
# Constants
# -------------------------------------------------------------------
DISCOUNT_5 = 0.05           # 5% discount
DISCOUNT_10 = 0.10          # 10% discount

# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
theTemperatures = [27.7, 29.8, 33.0, 31.6, 28.4, 28.0, 27.9]
aCost = 0.0
total = 0.0

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------
for temp in theTemperatures:        # Display temperatures
    print (temp)

# Add up costs until the user enters zero
aCost = float (input ("Enter a cost: "))
while (aCost != 0.0):
    total = total + aCost
    aCost = float (input ("Enter a cost : "))

# Calculate discount based on the total of numbers entered by the user
if (total > 100.00):
    total = (1 - DISCOUNT_10) * total       # Get 10% discount
else:
    total = (1 - DISCOUNT_5) * total        # Get 5% discount

print (total)
# -------------------------------------------------------------------
# =====> Write your answers here in the right-hand column
# Left                                          # Right
# -------------------------------------------------------------------
# Name of a constant used in the program        # DISCOUNT_5
# Name of an array used in the program          # theTemperatures
# Line number of an initialisation of a
#      variable with a real number              # 11
# Line numbers for a selection construct        # 27
# Line number(s) for a repetition construct     # 22
# Line number(s) for an iteration construct     # 17
# Line number for an instruction that outputs
#      information to the screen                # 32
