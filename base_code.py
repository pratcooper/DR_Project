import math
#"fsdf"

document1 = "This code prints Hello World to the console"

document2 = "public static void printHello(){ System.out.println(\"Hello world\"); "

document3 = "Never stop learning"

document4 = "life learning"

q_docs = []
q_docs.append(document4)

all_docs = []
all_docs.append(document1)
all_docs.append(document2)
all_docs.append(document3)

term = "life learning"

def termFrequency(term, document):
    normalizeDocument = document.lower().split()
    return normalizeDocument.count(term.lower()) / float(len(normalizeDocument))


def inverseDocumentFrequency(term, allDocuments):
    numDocumentsWithThisTerm = 0
    for doc in allDocuments:
        if term.lower() in doc.lower().split():
            numDocumentsWithThisTerm = numDocumentsWithThisTerm + 1

    if numDocumentsWithThisTerm > 0:
        return 1.0 + math.log(float(len(allDocuments)) / numDocumentsWithThisTerm)
    else:
        return 1.0


for eachTerm in term.lower().split():
    print(termFrequency(eachTerm,document4))


print(inverseDocumentFrequency("life",q_docs))