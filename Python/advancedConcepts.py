#advacned strings
s="hellostrings"
ss="hello strings" ##s.isapha is false as space exists ; #isalnum 
print(len(s))
print('h' in s)
print(s.index('h'))
print(s.find('h'))
print('Hello \t Hi')
print(s)
print(s.isalpha()) #check for alpha
print(s.isalnum()) #check for alpha numerics 
print(s.islower())
print(s.isspace())


_text="hellomyworldsmyworld"
print(_text.split('my'))
print(_text.partition('my')) # before text after partitions



#advacned sets 

set_one={1,2,3,4,5,6,7,8}
set_two={1,2,3,4,5,6,7}
set_two.add(12)
print(set_one.difference(set_two)) # bigger always first
print(set_two.difference(set_one)) # empty result



#advanced dictionarty


dict={x:x**2 for x in range(10)}
print(dict.items())

#advanced list 
list=[1,1,1,1,2,3,4,5]
print(len(list))
# list.append([6,7])
list.extend([8,9])# add elements to the list
print(list)
list.index(1)
list.insert(11,12) # 11 is index (add at an index )
print(list)
list.pop() # removes last value
list.pop(0) # removes value at index 
list.remove(5) # removes this value 5
print(list)
list.reverse()
print(list)
list.sort()
print(list)
print(list.count(1)) #counts the occurences of the value 1 in the list 

