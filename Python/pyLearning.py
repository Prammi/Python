


import timeit

def func_one(n):
      return [str(num) for num in range(n)]

def func_two(n):
      return list(map(str,range(n)))

first_statement='''func_one(100)'''
second_statement='''func_two(100)'''
first_setup='''
def func_one(n):
      return [str(num) for num in range(n)]
      '''
second_setup='''
def func_two(n):
      return list(map(str,range(n)))
      '''

first_time=timeit.timeit(first_statement,first_setup,number=100000) #syntax
second_time=timeit.timeit(second_statement,second_setup,number=100000)#syntax

print(first_time)
print(second_time)



print("=====================================END OF TIMING=====================================")

from collections import Counter
my_list = [1,2,3,4,5]
print(Counter(my_list))


import re;
my_text= "searching for regex,this is my second regex"
print(re.search("regex",my_text));

for match in re.finditer('regex',my_text):
   (a,b)= match.span()
   print(a)
   print(match)

for match in re.findall('regex',my_text):
      print(match)



pattern ="\d+"
ph_num="123123123"
_match =re.search(pattern,ph_num)#important
print(_match)
print(_match.group())



#to get the group elements in the regex pattern after match 
# use the re.compile as re.compile(r'()-()-()')
# so between each of () is tracked as one group 
# using group(index) we can get the group element
#index starts with 1

pattern =re.compile(r'(\d{3,4})-(\d{3,4})-(\d{3,4})')   #important
ph_num="123-123-1234"
_match =re.search(pattern,ph_num)
print(_match)
print(_match.group(1))
print(_match.group(1))
print("=====================================END OF REGEX=====================================")
