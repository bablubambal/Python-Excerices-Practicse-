""""
Author: Bablu Bambal
Date : 27 July 2019
Purpose: "To practise the python problem"
Python Practice problem 7 (Medium, 20 points)

Search Engine

You are given few sentences as a list (Python list of sentences).
Take a query string as an input from the user.
You have to pull out the sentences matching this query inputted by the user
in decreasing order of relevance after converting every word in the query and the sentence to lowercase.
Most relevant sentence is the one with the maximum number of matching words with the query.

Sentences = [“This is good”, “python is good”, “python is not python snake”]

Input:

Please input your query string

“Python is”

Output:

3 results found:

1.      python is not python snake

2.      python is good

3.      This is good

"""
def matchingwordsfunction(sentence1,sentence2):
    #strip function removes the extra white spaces
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    matchingwords = 0
    for word1 in  words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                matchingwords +=1
            #print(f"Matching {word1} with {word2}")
    return matchingwords
# print(matchingwordsfunction("This is good and this is great python", "python is good"))

if __name__ == '__main__':
    Sentences = ["This is good", "python is good", "python is not python snake", "This is working",
                 "Python good language", "work is god and it is the best thing is easy"]

    querystring = input("Enter the Query Sting\n")
    # the below function will return the scores of the sentence which will match no of words in the Both the query
    # and the Sentences list
    scores = []
    for sentence in Sentences:
        scores.append(matchingwordsfunction(querystring,sentence))
    # this  the oneliner of the above code
    # scores = [matchingwordsfunction(querystring,sentence) for sentence in Sentences ]

    #the following is onelineer and in this we return a tuple with maximum score at the first
    # sortedSentenceScore = [sentScore for sentScore in sorted(zip(scores,Sentences), reverse =  True) if sentScore[0]!=0]

    sortedSentenceScore = []
    for sentScore in sorted(zip(scores,Sentences)):
        #print(sentScore)
        if sentScore[0]==0:
            continue
        sortedSentenceScore.append(sentScore)
    sortedSentenceScore.reverse()


    #print(sortedSentenceScore)

    #print(scores)
    print(f"{len(sortedSentenceScore)} Results found\n")
    for score,item in sortedSentenceScore:
        print(f" \" {item} \" : with a word matching of {score}")


