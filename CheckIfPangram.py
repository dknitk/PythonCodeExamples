def checkIfPangram(sentence) -> bool:
    charSet = set()
    for currChar in sentence.lower():
        if currChar.isalpha():
            charSet.add(currChar)
    return len(charSet) == 26

print(checkIfPangram("TheQuickBrownFoxJumpsOverTheLazyDog"))

print(checkIfPangram("This is not a pangram"))