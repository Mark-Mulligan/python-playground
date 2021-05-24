
def findLetters(arr, targetLetter):
    foundItems = []
    for item in arr:
        if item == targetLetter:
            foundItems.append(item)
    
    return foundItems

print(findLetters(['a', 'b', 'c', 'a'], 'a'))
