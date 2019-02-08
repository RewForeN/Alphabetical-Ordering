
import os
from time import sleep

## Order list in alphabetical order ##
def OrderAlphabetically():    

    for i in range(0, len(f_contents)):
        for j in range(0, len(f_contents)):
        
            if (j == i):
                break

            # If there is a duplicate
            if (f_contents[i] == f_contents[j]):
                print("Duplicate")
                print("Line " + str(j + 1) + ": " + f_contents[j], end="")
                print("Line " + str(i + 1) + ": " + f_contents[i])
                break

            if (f_contents[i][0] < f_contents[j][0]):
                f_contents[i], f_contents[j] = f_contents[j], f_contents[i]
            elif (f_contents[i][0] == f_contents[j][0]):
                if (OrderSameStart(f_contents[i], f_contents[j]) == 1):
                    f_contents[i], f_contents[j] = f_contents[j], f_contents[i]


## Order two item of the same start ##
def OrderSameStart(str1, str2):
    
    for i in range(1, len(str1)):
        if (str1[i] < str2[i]):
            return 1
        elif (str2[i] < str1[i]):
            return 0
    return


## Main ##

file = 'list.txt'
newfile = 'newlist.txt'

if (os.path.exists(file)):

    with open(file, 'r') as fp:
        # Read file lines
        f_contents = fp.readlines()
            
    for k in range(0, len(f_contents)):
        f_contents[k] = f_contents[k].strip("")    

    OrderAlphabetically()

    # Open newlist for writing
    with open(newfile, 'w') as fp:
        # Write lines in file
        for i in range(0, len(f_contents)):
            print(f_contents[i], end="")
            fp.write(f_contents[i])

    print()

else:
    print("File \"list\" does not exist")
    sleep(1)