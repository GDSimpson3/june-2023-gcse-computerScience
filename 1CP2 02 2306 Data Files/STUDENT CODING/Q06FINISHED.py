# -------------------------------------------------------------------
# Global variables
# -------------------------------------------------------------------
userTable = [["LArmstrong3", "RedChair"],
             ["SBarrett7", "PurpleDesk"],
             ["EChisholm4", "YellowStool"],
             ["VDunn1", "OrangeFuton"],
             ["DElms5", "GreenCouch"],
             ["EFirsova13", "PinkMattress"],
             ["JGolland6", "GreenTable"],
             ["FHartley13", "BrownMirror"],
             ["DJohnstone12", "GoldBed"],
             ["GKirkhope8", "WhiteNights"],
             ["LLemon8", "BeigeDresser"],
             ["HMacCunn6", "GreyOttoman"],
             ["PNewland10", "BlackWardrobe"],
             ["AOldham5", "OrangeFuton"],
             ["JPook8", "YellowStool"]]

# =====> Write your code here

username = str(input('Enter Username '))
password = str(input('Enter Password '))


badInput = True
while badInput:
    if (username == ''):
        username = str(input('Cannot be empty::: reEnter Username '))
        # password = str(input('reEnter Password'))
    elif (password == ''):
        password = str(input('Cannot be empty::: reEnter Password' ))

    else: badInput =False

# -------------------------------------------------------------------
# Main program
# -------------------------------------------------------------------


Found= False

# =====> Write your code here
for user in userTable:
    if user[0] == username and user[1] == password:    #USERNAME
        print('Logged In')
        Found = True
        break
    elif user[0] == username and (not user[1] == password):
        print('Incorrect Password')
        Found = True
        break

    # elif not user[0] == username:
    #     Found = False

if Found == False:
    print('UserName not found')