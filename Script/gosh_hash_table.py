import unittest
import time
# run
def main():
    # quick test 
    a = gosh_hash_Table()
    a.insert("Ahmet", 90)
    for i in range(11111):
        a.insert(str(i), 1)
    for i in range(11111):
        print(a.contains(str(i)))
    a.insert("Mehmet", 902)
    a.insert("Cihan", 901)
    print(a.contains("Ahmet"))
    print(a.contains("Mehmet"))
    print(a.contains("Cihan"))

class gosh_hash_Table:
    def __init__(self):
        # Arrays for keys and values
        self.keys = [None] * 9999 # key store
        self.Values = [None] * 9999 # value store
        self.temp = 2
        self.len_of_key = len(self.keys)
    # checks whether there is key nor
    def contains(self, key):
        # get index of key
        index_of_key = self.convert_index_int(key)
        # check keys
        if self.keys[index_of_key] == key:
            return True
        else:
            while True:           
                # if key contains in array
                if self.keys[index_of_key] == key:
                    return True
                elif self.keys[index_of_key] == None:
                    return False
                else:
                    index_of_key = (index_of_key + 1) % len(self.keys)

    def insert(self, key, value):
        # try to put value in flat array without subarrays
        index_of_key = self.convert_index_int(key)
        # add value                         
        if self.keys[index_of_key] == None:
            self.keys[index_of_key] = key
            self.Values[index_of_key] = value
        else:
            # try to solve by calculating its mod with one while loop
            # dealing with colliding
            while True:
                if self.Values[index_of_key] == None:
                    self.keys[index_of_key] = key
                    self.Values[index_of_key] = value
                    break
                elif self.keys[index_of_key] == key:
                    self.Values[index_of_key] = value
                    break
                else:
                    index_of_key = (index_of_key + 1) % len(self.keys)
        
        # To do, arras were filled, increase the length of the array
        if None not in self.keys and None not in self.Values:
            # get copy of arrays and insert elements in new keys and values arr which have new length
            copy_of_key = self.keys
            copy_of_value = self.Values

            self.keys = [None] * (self.temp * 9999)
            self.Values = [None] * (self.temp * 9999)
            
            for index in range(len(copy_of_key)):
                index_of_key = self.convert_index_int(copy_of_key[index])
                if copy_of_key[index] != None:
                    while True:
                        if self.keys[index_of_key] == None:
                            self.keys[index_of_key] = copy_of_key[index]
                            self.Values[index_of_key] = copy_of_value[index]
                            break
                        else:
                            index_of_key = (index_of_key + 1) % len(self.keys)
            self.temp += 2
        
    def delete(self, key):
        index_of_key = self.convert_index_int(key)
        if self.keys[index_of_key] == key:
            self.keys[index_of_key] = None
            self.Values[index_of_key] = None
        else:
            while True:
                if self.keys[index_of_key] == key:
                    self.keys[index_of_key] = None
                    self.Values[index_of_key] = None
                    break
                else:
                    index_of_key = (index_of_key + 1) % len(self.keys)
                    
    def get_value(self, key):
        # get value O(1) without colliding
        index_of_key = self.convert_index_int(key)
        if self.keys[index_of_key] == key:
            return self.Values[index_of_key]
        else:
            # GET VALUE CASE OF COLLİDİNG O(N)+
            while True:
                # check same key location
                # pull value in same key location
                if self.keys[index_of_key] == key:
                    return self.Values[index_of_key]
                else:
                    index_of_key = (index_of_key + 1) % len(self.keys)

            raise EnvironmentError("key that you're looking for couldn't be found.")
                        
    # convert index to int
    def convert_index_int(self, index_of_key):
        try:
            index_of_key = hash(index_of_key)
            index_of_key = index_of_key % len(self.keys)
            return index_of_key
        except:
            raise TypeError("type of value is not valid")
# start
if __name__ == "__main__":
    main()