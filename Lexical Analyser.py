# We import Regular Expressions to perform regex 
import re

# used for storing string tokens
tokens = []

# this is where we define the string that is being analysed.
source = 'Hello World 1234'.split()

# Loop through each source code word
for word in source:

    # We check for any data type declaration
    if word in ['str', 'int', 'bool']:
        tokens.append(['DATATYPE', word])

    # We then search for a word identifier
    elif re.match("[a-z]", word) or re.match("[A-Z]",word):
        tokens.append(['STRING',word])

    # We then search for any operator
    elif word in '*+-/%=':
        tokens.append(['OPERATOR', word])
    
    # Finally we look for any integers present and cast them as a number
    elif re.match(".[0-9]", word):
        if word[len(word)-1] == ';':
            tokens.append(["INTEGER", word[:-1]])
            tokens.append(['END_STATEMENT', ';'])
        else:
            tokens.append(["INTEGER", word])

# we then output the tokens array
print(tokens)

