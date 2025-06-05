# Input: text = gotxxotgxdogt, word = got
# Output : 3

def anagramCheck(text,word):
    d={}
    d[word]=0
    l=len(word)
    for i in range(len(text)-(l-1)):
        temp=text[i:i+l]
        if isAnagram(temp,word):
            d[word]+=1

    return d[word]

def isAnagram(s1, s2):
    return sorted(s1) == sorted(s2)

if __name__=="__main__":
     text ="listen"
     word='silent'
     i=anagramCheck(text,word)
     print(i)