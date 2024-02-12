#-------------------------------------------------------------------------
# AUTHOR: Nathaniel Battad
# FILENAME: indexing.py     collection.csv
# SPECIFICATION: Reads 3 lines from the collection.csv file and stores them each as their own document
#                as lists within a list. Each document is then cleaned using stopword removal, where the
#                the stopwords are pronouns and conjunctions. The cleaned documents are then stemmed,
#                essentially matching word variations to a base word. From there, the index terms are identified
#                and the tf, df, idf, are found in order to calculate the tf-idf. The tf-idf values for
#                each word with respect to the documents are displayed in a document term matrix, in which
#                each row is a document and each column is an index term.
# FOR: CS 4250- Assignment #1
# TIME SPENT: About 1 hour on the program and 2 hours on the rest of the assignment, so about 3 hours total.
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard arrays

#Importing some Python libraries
import csv
import math

documents = []

#Reading the data in a csv file
with open('hw1\collection.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
         if i > 0:  # skipping the header
            documents.append (row[0].lower())


#Conducting stopword removal. Hint: use a set to define your stopwords.
stopWords = {'i', 'and', 'she', 'her', 'they', 'their'}
cleaned = []

for entry in documents:
    cleanUp = [word for word in entry.split() if word not in stopWords]
    cleaned.append(cleanUp)


#Conducting stemming. Hint: use a dictionary to map word variations to their stem.
stemming = {'loves': 'love', 'cats': 'cat', 'dogs': 'dog'}
stemmed = []

for entry in cleaned:
    match = [stemming.get(word, word) for word in entry]
    stemmed.append(match)


#Identifying the index terms.
terms = []

for entry in stemmed:
    for word in entry:
        if word not in terms:
            terms.append(word)


#Building the document-term matrix by using the tf-idf weights.
docTermMatrix = []
numOfDocs = len(stemmed)

for document in stemmed:
    matrixSpot = []
    for term in terms:   
        tf = document.count(term) / len(document)
        df = sum(1 for doc in stemmed if term in doc)
        idf = round(math.log10(numOfDocs / df) if tf > 0 and df > 0 else 0, 4)
        tfidf = round(tf * idf, 4)

        matrixSpot.append(tfidf)
    
    docTermMatrix.append(matrixSpot)


#Printing the document-term matrix.
print("love\tcat\tdog")
for row in docTermMatrix:
    print(row)