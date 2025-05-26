class HashTable:
    def __init__(self,size=7):
        self.data_map=[None]*size
        self.primeNumber=23 ##this could be any prime number 
    
    def __hash(self,key):
        hashKey=0
        for k in key:
            hashKey=(hashKey+ ord(k) *self.primeNumber)%len(self.data_map)
        return hashKey
    
    def print_hashTable(self):
        for index,value  in enumerate(self.data_map):
            print("index "+ str(index) + " " + "value  " + str(value))
        
    
    def set_item(self,key,value):
        index=self.__hash(key)
        if(self.data_map[index]==None):
            self.data_map[index]=[]
        self.data_map[index].append([key,value])
        
    
    def get_item(self,value):
        index=self.__hash(value)
        if self.data_map[index] is not None:
            for i in range(0,len(self.data_map[index])):
                if self.data_map[index][i][0]==value:
                    print(f"the value for the key {value} is "+str(self.data_map[index][i][1]))
                    return self.data_map[index][i][1]
        print(f"there is no value is {value}")
        return None

        
                

dm=HashTable()
dm.set_item("camel",1000)
dm.set_item("giraffe",1200)
dm.set_item("dog",6000)
dm.get_item("dog")
dm.get_item("dogs")

dm.print_hashTable()
            
        
    