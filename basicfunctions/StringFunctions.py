msg = "Hello world!"



def length(input1):
    #var
    letters = 0
    # /var

    for char in str(input1):
        if char == " ":
            continue
        else:
            letters += 1
    return letters

# Functions: lettercount(stringToCheck, characterLookingFor)[0 - Count, 1 - strToCheck, 2 - charLookingFor]
def letterCount(input1, input2): 
    # var
    count = 0
    strToCheck = input1
    charLookingFor = str(input2)
    # /var
    
    # Iterate through the string we're looking through (input1) to find the character (input2)
    for char in str(strToCheck): 
        if charLookingFor == char: 
            count =+ 1
    return count, strToCheck, charLookingFor




#print(msg) # Returns "Hello world!"
#print(f"There is {letterCount(msg, "H")[0]} instance of {letterCount(msg, "H")[2]} in {letterCount(msg, "H")[1]}") # There is 1 instance of H in Hello world!
#print(f"There are {length(msg)} letters in {msg} Not counting spaces.") # There are 11 letters in Hello world! Not counting spaces.