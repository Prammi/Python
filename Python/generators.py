def func_printnumbers():
    for i in range(100):
        yield i
        


print(func_printnumbers()) ## tels its an gen function <generator object func_printnumbers at 0x000002203D3AFF40>

print([func_printnumbers()]) ### still tells  its an gen function <generator object func_printnumbers at 0x000002203D3AFF40>

print(list(func_printnumbers())) ## prints the numbers as list calls the iterator multiple times  automatically.



# this is the prime diff between list and array
# list conversion has to be used when iterators are used if not then user [] 


# alternatively for also forces iteration
gen =func_printnumbers()
for i in gen:
    print(i) #even this forces iteration  
    

gen =func_printnumbers()

# next calls the next yield value result one at a time till the next iterator throws and error of no value present 
# for actually does the same and handles it automatically
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
#output for above will 
# 1
# 2
# 3
# 4
# 5