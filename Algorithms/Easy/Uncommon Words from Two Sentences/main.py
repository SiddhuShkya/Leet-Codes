

def uncommonFromSentences(s1, s2):
    from collections import Counter
    # Split sentences into words
    wordsA = s1.split()
    wordsB = s2.split()
    # Count occurrences in both sentences
    countA = Counter(wordsA)
    countB = Counter(wordsB)
    # Find uncommon words
    res = []
    # Check words in first sentence
    for word in countA:
        if countA[word] == 1 and countB[word] == 0:
            res.append(word)
    # Check words in second sentence
    for word in countB:
        if countB[word] == 1 and countA[word] == 0:
            res.append(word)
    return res
    

print(uncommonFromSentences("this apple is sweet", "this apple is sour"))