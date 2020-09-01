import unittest
import random
from good_hash_table import good_hash_table
# To Do, 
# add more corner cases to find bugs or crash and describe it on github 
# add more test methods

# unit test class
# a test class included bunch of methods to check whether hash table works well nor. 
class test_map(unittest.TestCase):
    def setUp(self):
        self.hash_table = good_hash_table()

    def insertInstanceForTest(self):
        for i in range(11111):
            self.hash_table.insert(str(i), 1)

    #test insert 11111 values
    def test_batch_insert(self):
        # string value as immutable it has been written in another fucntion so that another test function can access this insert method to test
        self.insertInstanceForTest()
        # adding immutable valuse in to the hash table
        # tuple
        for i in range(11111):
            self.hash_table.insert((1, 1), 444)
        # Boolean values
        for i in range(11111):
            self.hash_table.insert(True, False)
        # immutable integer value
        for i in range(11111):
            self.assertEquals(1, self.hash_table.get_value(str(i)))
        
        for i in range(11111):
            self.assertEquals(self.hash_table.get_value((1, 1)), 444)

        for i in range(11111):
            self.assertEquals(False, self.hash_table.get_value(True))
        
    # test delete all values and keys also None
    def test_batch_delete(self):        
        self.insertInstanceForTest()

        for i in range(11111):
            self.hash_table.delete(str(i))

        for i in range(11111):
            self.assertFalse(self.hash_table.contains(str(i)))

    # test update 1 values to 2
    def test_batch_update(self):
        self.insertInstanceForTest()

        for i in range(11111):
            self.hash_table.insert(str(i), 2)

        for i in range(11111):
            self.assertEquals(self.hash_table.get_value(str(i)), 2)

    # test contains
    def test_batch_contains(self):
        self.insertInstanceForTest()

        for i in range(11111):
            self.hash_table.contains(str(i))

    # test None keys 
    def test_inserting_none_key(self):
        # special explanation:
        # these assert raises will throw values because key can not be None         
        with self.assertRaises(ValueError):
            self.hash_table.insert(None, None)
    
        with self.assertRaises(ValueError):
            self.hash_table.insert(None, 123123)

# Run
if "__main__" == __name__:
    unittest.main()
