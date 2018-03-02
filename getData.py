

def getPair(line):

    counter = 0
    codeList = []
    commentList = []

    while(counter<len(line)):
        methodInfo = line[counter+0]
        pathToMain = line[counter+1]
        #print(line[1])
        commentLength = int(line[counter+2])

        comment = []
        for i in range(commentLength):
            comment.append(line[counter + i + 3])
        commentString = ' '.join(comment)
        commentList.append(commentString)
        codeLength = int(line[counter+ 3 + commentLength])

        code = []
        for i in range(codeLength):
            code.append(line[counter + i+4+commentLength])
        codeString = ' '.join(code)
        codeList.append(codeString)
        end = counter + commentLength+codeLength+5
        counter = end
        #print(counter)
    return codeList,commentList





with open("C:\\Users\\Kaushal\\Desktop\\DR\\input.txt") as f:
    lines = f.readlines()

    codeList, commentList = getPair(lines)

    print(len(codeList))
    print(len(commentList))



