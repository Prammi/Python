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
_match =re.search(pattern,ph_num)
print(_match)
print(_match.group())



#to get the group elements in the regex pattern after match 
# use the re.compile as re.compile(r'()-()-()')
# so between each of () is tracked as one group 
# using group(index) we can get the group element
#index starts with 1

pattern =re.compile(r'(\d{3,4})-(\d{3,4})-(\d{3,4})')
ph_num="123-123-1234"
_match =re.search(pattern,ph_num)
print(_match)
print(_match.group(1))
print(_match.group(1))
