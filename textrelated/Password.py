import json
import random

from basicfunctions.StringFunctions import length


# vars
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
passwordGenerated = ""
desiredLength = 11
# /vars

# Generate a random password
for i in range(desiredLength):
    passwordGenerated += alphabet[random.randint(0, length(alphabet)-1)]

# Save the generated password to a JSON file
with open('generatedfiles/passwords.json', 'w') as file:
    json.dump(passwordGenerated, file)