# Program to count character frequency

def charFreq(userInput):
    """This function helps to count the char frequency in the given string """
    userInput = userInput.lower()
    dict = {}
    for char in userInput:
        keys = dict.keys()
        if char == ' ':
            continue
        elif char in keys:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


if __name__ == '__main__':
    userInput = str(input('Enter a string:'))
    print(charFreq(userInput))
