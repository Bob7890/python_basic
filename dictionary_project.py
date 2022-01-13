"""
Dictionary Values
"""

# Create a function that checks if the 
# values of a dictionary are int or str
# if int -> returns [max, min, and sum(of remaining ints)]
# if str -> returns dicipered string
# use key as offest like we used in ord/chr
# eg. d[4]:"_]p" -> 'cat'

def math_or_dicipher(d):
    """Values int or str"""
    newDict = dict()
    for key, value in d.items():
        if isinstance(value, str):
            # ord/chr
            newStr = ""
            for letter in value:
                newStr += chr(ord(letter) + key)
            newDict[key] = newStr
        else:
            # max/min/sum
            valueList = [int(x) for x in str(value)]
            maxV = max(valueList)
            minV = min(valueList)
            myList = []
            myList.append(maxV)
            myList.append(minV)
            myList.append(sum(valueList))
            newDict[key] = myList

    return newDict
    
theDict = dict()
theDict[1] = 52324
theDict[4] = "_]p"
theDict[7] = 4432
theDict[8] = 3222
theDict[9] = 6222
theDict[2] = "abc"

resultDict = math_or_dicipher(theDict)
print(resultDict)
