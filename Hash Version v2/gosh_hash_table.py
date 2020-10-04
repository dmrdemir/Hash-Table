# run
def main():
    # test
    a = gosh_hash_Table()
    
class gosh_hash_Table:
    def __init__(self):
        # key store
        self.keys = [None] * 9999 
        # value store
        self.values = [None] * 9999 
         # in order for list to be increased length 
        self.temp = 2
        # it only contains colliding values values 
        self.colliding_indexes_list = [None] * 9999

    # show values keys in a subarray
    def items(self):
        return [[key, self.get_value(key)] for key in self.keys
            if key != None]
    # show values with list
    def values(self):
        return [value for value in self.values if value != None]
    # show keys with list
    def keys(self):
        return [key for key in self.keys if key != None]

    # checks whether there is key nor
    def contains(self, key):
        if key == None:
            raise ValueError("Element is invalid or None")
        # get index of key
        index_key = self.convert_key_to_index(key)
        # when function navigate on all elements it gets where it started and stop navigatin which means it find nothing
        copy_index = index_key
        # check keys
        if self.keys[index_key] == key:
            return True
        # to make sure there is a colliding for [None, None, None, 3] case
        elif self.colliding_indexes_list[index_key] != None:
            while True:
                if self.keys[index_key] == key:
                    return True
                else:
                    index_key = (index_key + 1) % len(self.keys)
                
                if copy_index == index_key:
                    return False
        else:
            # if there is no collision return False the value's already None, not a part of the collision
            if self.colliding_indexes_list[index_key] != None:
                return False

            while True:
                #store colliding indexes in an array to check 
                if self.keys[index_key] == key:
                    return True
                elif self.keys[index_key] == None:
                    return False
                else:
                    index_key = (index_key + 1) % len(self.keys)
                # when original index equated to copy index, it mean's the index navigated whole keys in array
                # by writing if statement bottom to the loop, i take precaution for values.
                if index_key == copy_index:
                    return False
        raise EnvironmentError("key that you're looking for couldn't be found.")

    def insert(self, key, value):
        if value == None or key == None:
            raise ValueError("Element is invalid or None")
        # try to put value in flat array without subarrays
        index_key = self.convert_key_to_index(key)
        # when function navigate on all elements it gets where it started and stop navigatin which means it find nothing
        # add value                         
        if self.keys[index_key] == None:
            self.keys[index_key] = key
            self.values[index_key] = value
        else:
            # try to solve by calculating its mod with one while loop
            # dealing with colliding
            if self.colliding_indexes_list[index_key] != index_key:
                self.colliding_indexes_list[index_key] = index_key

            while True:
                # insert new value and key
                if self.keys[index_key] == None:
                    self.keys[index_key] = key
                    self.values[index_key] = value
                    break
                else:
                    index_key = (index_key + 1) % len(self.keys)

                # for updating value 
                if self.keys[index_key] == key:
                    self.values[index_key] = value
                    break

        # when arrays were filled, increase the length of the array
        if None not in self.keys and None not in self.values:
            # get copy of arrays and insert elements in new keys and values arr which have new length
            copy_of_key = self.keys
            copy_of_value = self.values
            self.keys = [None] * (self.temp * 9999)
            self.values = [None] * (self.temp * 9999)
            
            for index in range(len(copy_of_key)):
                if copy_of_key[index] != None:
                    index_key = self.convert_key_to_index(copy_of_key[index])
                    while True:
                        if self.keys[index_key] == None:
                            self.keys[index_key] = copy_of_key[index]
                            self.values[index_key] = copy_of_value[index]
                            break
                        else:
                            index_key = (index_key + 1) % len(self.keys)
            
            self.colliding_indexes_list = [None] * (9999 * self.temp)
            self.temp += 2
            
    def delete(self, key):
        # raise error
        if key == None:
            raise ValueError("Element is invalid or None")
        index_key = self.convert_key_to_index(key)
        # when function navigate on all elements it gets where it started and stop navigatin which means it find nothing
        copy_index = index_key

        if self.keys[index_key] == key:
            self.keys[index_key] = None
            self.values[index_key] = None
            self.colliding_indexes_list[index_key] = None
            
        elif self.colliding_indexes_list[index_key] != None:
            while True:
                if self.keys[index_key] == key:
                    self.keys[index_key] = None
                    self.values[index_key] = None
                    self.colliding_indexes_list[index_key] = None
                else:
                    index_key = (index_key + 1) % len(self.keys)
                
                if copy_index == index_key:
                    return None
        else:    
            while True:
                if self.keys[index_key] == key:
                    self.keys[index_key] = None
                    self.values[index_key] = None
                    self.colliding_indexes_list[index_key] = None
                    break
                elif self.keys[index_key] == None:
                    break 
                else:
                    index_key = (index_key + 1) % len(self.keys)
                    
                if  copy_index == index_key:
                    return None

    def get_value(self, key):
        if key == None:
            raise ValueError("Element is invalid or None")
        # get value O(1) without colliding
        index_key = self.convert_key_to_index(key)
        # when function navigate on all elements it gets where it started and stop navigatin which means it match nothing
        copy_index = index_key
        # quick get value and key O(1) without collision
        if self.keys[index_key] == key:
            return self.values[index_key]
        # to make sure there is a colliding for [1, None, 3, 4]
        elif self.colliding_indexes_list[index_key] != None:
            while True:
                # check same key location
                if self.keys[index_key] == key:
                    return self.values[index_key]
                else:
                    index_key = (index_key + 1) % len(self.keys)
                
                if copy_index == index_key:
                    return None
        else:
            # used same algorithm logic for searching with o(n)
            while True:
                if self.keys[index_key] == key:
                    return self.values[index_key]
                elif self.keys[index_key] == None:
                    return None
                else:
                    index_key = (index_key + 1) % len(self.keys)

                if index_key == copy_index:
                    return None

    # convert key to index
    def convert_key_to_index(self, index_key):
        # raise ValueError 
        if index_key != None: 
            index_key = hash(index_key)
            index_key = index_key % len(self.keys)
            return index_key

        raise TypeError("type of value is not valid")

# start
if __name__ == "__main__":
    main()