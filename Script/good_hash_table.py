# TO BE GOOD HASH TABLE

# getting value by index
# getting int by key
# getting integer from key using hash function
# use hash function to get intex from key
# don't use any loop and .index()

# for converting index
#   in order to get value from valeus[index]
#   get index by key
#   fit in numbers in a range by taking MOD

# for  Collision 
#   adding linked list to array is perfectly fine method to resolve such problem
#   expect map is O(1) but in types of problem such as (collision) 
#   it's supposed to use O(N) way to get rid of types of collision problems
#   for instance : 0, 1, 2, 3, 4, 5... N

# for out of index
#   copy elements without problem
#   length of list always will be change
#   need to copy elements from perivous list to new list and increase length of list

# explanation about Unit Test
#these arrays are occured to check true value type, string for keys and int for values
# i'll put "unit" on every parts being related to unit test

class good_hash_table:
    def __init__(self):
        # Arrays for keys and values
        self.keys = [None] * 9999 # key store
        self.Values = [None] * 9999 # value store
        self.temp = 2

    # delete key and value
    def delete(self, key):
        # unit
        index_of_key = self.convert_index_int(key)
        for element in range(len(self.keys[index_of_key])):
            if key == self.keys[index_of_key][element]:
                self.keys[index_of_key].pop(element)
                self.Values[index_of_key].pop(element)
                break

    # checks whether there is key nor
    def contains(self, key):
        # get index of key
        index_of_key = self.convert_index_int(key)
        # if the address is already None it returns False
        if self.keys[index_of_key] != None:
            for element in self.keys[index_of_key]:
                if key == element:
                    return True
        return False

    def insert(self, key, value):
        # describe global keys and values
        index_of_key = self.convert_index_int(key)
        # create list in array
        if self.keys[index_of_key] == None:
            self.keys[index_of_key] = [] 
            self.Values[index_of_key] = []
         # add key into list
        if self.contains(key) == False:
            self.keys[index_of_key].append(key)
            self.Values[index_of_key].append(value)
        else:
            # for colliding values
            for element in range(len(self.keys[index_of_key])):
                if self.keys[index_of_key][element] == key:
                    self.Values[index_of_key][element] = value
                    break

        # solution of out of index
        if None not in self.keys and None not in self.Values:
            # copy of key
            copyArr = self.keys
            # copy of array
            copyValue = self.Values
            # new key and values
            self.keys =  [None] * (9999 * self.temp)
            self.Values = [None] * (9999 * self.temp)
            # new keys and values
            # it gets index from copy array and it convert the key in copy[index_of_subArr],
            # then put  from keys and values in previous array to new array 
            for index_of_subArr in range(len(copyArr)):
                if copyArr[index_of_subArr] != None: 
                    for elementKey in copyArr[index_of_subArr]:
                        index_of_key = self.convert_index_int(elementKey)
                        self.keys[index_of_key], self.Values[index_of_key] = [], []
                        break
                    for elementKey, elementValue in zip(copyArr[index_of_subArr], copyValue[index_of_subArr]):
                        self.keys[index_of_key].append(elementKey)
                        self.Values[index_of_key].append(elementValue)
            self.temp += 2
       
    # get value from hash
    def get_value(self, key):
        # it gets value that is in same order with key
        index_of_key = self.convert_index_int(key)
        if self.keys[index_of_key] != None and self.Values[index_of_key] != None:
            for element in range(len(self.keys[index_of_key])-1, -1, -1):
                if key == self.keys[index_of_key][element]:
                    return self.Values[index_of_key][element]
        raise EnvironmentError("key that you're looking for couldn't be found.")

    # convert index to int
    def convert_index_int(self, index_of_key):
        try:
            index_of_key = hash(index_of_key)
            index_of_key = index_of_key % len(self.keys)
            return index_of_key # test
        except:
            raise TypeError("type of value is not valid")