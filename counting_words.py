from raven import text

"""
Counting Words
"""

# Create a function that returns a
# list of the top 5 words (in accending order)
# used and the number of occerances
# eg. [('the', 56)]

# importing the text of the poem raven
# to variable text

def index(l):
    return l[1]
    
def sort_index(l_o_l, revIt):
    return sorted(l_o_l, key=index, reverse = revIt)

def counting(poem):
    """Count the words in a poem"""
    poemLower = poem
    poemLower = poemLower.replace("\n", " ")
    poemLower = poemLower.replace("\t", " ")

    wordList = poemLower.split(" ")
    wordDict = dict()
    for word in wordList:
        if word != "":
            count = wordDict.get(word, 0)
            if count == 0:
                wordDict.setdefault(word, 1)
            else:
                wordDict[word] = count + 1

    return sort_index(list(wordDict.items()), True)

def top5words(poem):
    wordListSorted = counting(poem)
    return wordListSorted[:5]

topFiveList = top5words(text)   
print(topFiveList)

def alpha_order_7(poem):
    """alpha order string"""
    wordListSorted = counting(poem)

    words = ""
    for wordItem in wordListSorted:
        if wordItem[1] == 7:
            words += wordItem[0]

    wordsList = list(words)
    wordsList.sort()

    print(wordsList)

    return ''.join(wordsList)

alphaOrder7 = alpha_order_7(text)
print(f"alpha = {alphaOrder7}")
