def getBooksFromDictionary(jsonData):
    oldTestament, newTestament = {}, {}
    
    for key in jsonData.keys():
        stringToProcess = jsonData[key]
        listOfBooks = stringToProcess.split('.')[1:]
        
        # str.equals(str1) in java is same as str.__eq__(str1) in python. We can also use str == str1 but where's the fun in that !
        dictionaryToProcess = oldTestament if key.__eq__("The_Old_Testament") else newTestament
        
        for book in listOfBooks:
            bookName = ' '.join(book.split()[:-1])
            dictionaryToProcess[listOfBooks.index(book)+1] = bookName
    
    return oldTestament, newTestament