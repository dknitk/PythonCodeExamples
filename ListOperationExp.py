# List Operation Example
def listFunction():
    myList = [1,2,3,4,5,6,7,8,9]
    #List Slicing
    print('Original List:', myList)
    print('First Element:', myList[0])
    print('Second Element:', myList[1])
    print('Elements from 0th Index to 4th Index:', myList[0:5])
    print('Elements at -7th Index:', myList[-7])

    #To append an element to a list
    myList.append(10)
    print('Append:', myList)

    # to find the index of a particular element
    print('Index of element\'6\' :', myList.index(6))

    #To sort the list
    myList.sort()

    #To pop element
    print('Poped Element:', myList.pop())

    #To remove an element from the List
    myList.remove(6)
    print('After removing \'6\':', myList)

    #To insert an element at a specific Index
    myList.insert(5,13)
    print('Inserted elements at 5th place :', myList)

    #To count number of occurances of a element in the list
    print('No of occurances of \'1\' :', myList.count(1))

    myList.extend([15,2,5,6])
    print('Extending List :', myList)

    #To reverse a list
    myList.reverse()
    print('Reversed List ::', myList)

    #To sort
    myList.sort()
    print('Sorted List ::', myList)

if __name__ == '__main__':
    listFunction()
    print("End of the Program")