f=open('sample.txt','w+')
f.write('sample text from python files ')
f.close()

import os 
print(os.getcwd())
print(os.listdir('C:\\Users\\Pramod\\MyWork\\Python'))

##move the files


import shutil
#moves this files from this location or src to destination
# shutil.move('sample.txt','C:\\Users\\Pramod\\MyWork')