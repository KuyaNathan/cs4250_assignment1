CS4250 Web Search and Recommender Systems
Assignment 1; Question 8

Python program that reads 3 lines of text from the collection.csv file and saves each line as its own "document" via lists.
Each document is cleaned up by removing the stopwords, which have been determined to be all pronouns and conjunctions
Once cleaned, the remaining words in each document are stemmed, tying any word variations to a root base form of that word.
After stemmming, the index terms are identified and are used to calculate the tf, df, idf, and tf-idf of the terms in the documents.
The calculated tf-idf values are displayed in a document term matrix, where rows are the documents and columns are the terms.
