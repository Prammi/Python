
#####COUNTERS#######

from collections import Counter

my_list=[1,2,1,2,12,12,12,12,12,12,12]

count=Counter(my_list)
print(list(count.items()))
#counter output is a dictionary and can show items ,key, values
for k,v in count.items():
    print('k ==' +str(k) +' ' +'V=='+str(v))
    
    
    
### SPLIT """"

my_sentence="hello this is my sentence"
print(list(my_sentence))
listofwords=my_sentence.split()
print(len(listofwords))
list(map(lambda x : print(len(x)),listofwords))



from collections import defaultdict


default_dic=defaultdict(lambda:0)
default_dic['10']=10

print(default_dic['10'])
print(default_dic['100'])


