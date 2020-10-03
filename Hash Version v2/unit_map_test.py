import unittest
import random
from gosh_hash_table import gosh_hash_Table

# inherit from Unittest.Testcase
class test_map(unittest.TestCase):
    def setUp(self):
        self.hash_table = gosh_hash_Table()
    # FAST
    def test_batch_insert(self):

        for i in range(11111):
            self.hash_table.insert(str(i), 1)
        for i in range(11111):
            self.assertEquals(1, self.hash_table.get_value(str(i)))

        for i in range(11111):
            self.hash_table.insert(True, False)
        for i in range(11111):
            self.assertEquals(False, self.hash_table.get_value(True))
            
        for i in range(11111):
            self.hash_table.insert("x", ["x", ("a", "b")])
        for i in range(11111):
            self.assertEquals(["x", ("a", "b")], self.hash_table.get_value("x"))
    # FAST
    def test_batch_delete(self):        
        for i in range(11111):
            self.hash_table.insert(str(i), 1)
        for i in range(11111):
            self.assertEqual(self.hash_table.get_value(str(i)), 1)

        for i in range(11111):
            self.hash_table.delete(str(i))
        for i in range(11111):
            self.assertNotEqual(1, self.hash_table.get_value(str(i)))
    # FAST
    def test_batch_update(self):
        for i in range(11111):
            self.hash_table.insert(str(i), 2)
        for i in range(11111):
            self.assertEquals(2, self.hash_table.get_value(str(i)))

        for i in range(11111):
            self.hash_table.insert(True, True)
        for i in range(11111):
            self.assertEquals(self.hash_table.get_value(True), True)
    # FAST
    def test_complex_test(self):
        for i in range(100000, 999999, 100):
            self.hash_table.insert(i, "test%s"%i)
            
        for i in range(100000, 999999, 100):
            self.assertEquals("test%s"%i, self.hash_table.get_value(i))
        
        for i in range(100000, 999999, 111):
            self.hash_table.delete(i)

        for i in range(100000, 999999, 111):
            self.assertNotEquals("test%s"%i, self.hash_table.get_value(i))
    # SLOW
    def test_heavy_collision(self):
        for i in range(10000):
            self.hash_table.insert(i * 9999, i)

        for i in range(10000):
            self.assertEquals(i, self.hash_table.get_value(i*9999))
    # SlOW
    def test_strong_collision(self):
        for i in range(10000):
            self.hash_table.insert(i ** 9999, i)
        
        for i in range(10000):
            self.assertEquals(i, self.hash_table.get_value(i ** 9999))

        for i in range(10000):
            self.hash_table.delete(i ** 9999)

        for i in range(10000):
            self.assertNotEquals(i, self.hash_table.get_value(i ** 9999))
    # FAST
    def test_collision_contains(self):
        for i in range(10):
            self.hash_table.insert(i * 9999, i)
        self.hash_table.delete(2*9999)

        self.assertTrue(self.hash_table.contains(3*9999))
    # FAST
    def test_hard_delete(self):
        for i in range(0, 10000, 2):
            self.hash_table.insert(str(i), i * 9999)
        
        for i in range(0, 10000, 2):
            self.hash_table.delete(str(i))

        for i in range(0, 10000, 2):
            self.assertFalse(self.hash_table.contains(str(i)))
    # FAST
    def test_insert_none_key(self):
        ''' it raises ValueError in case of key being None '''
        self.assertRaises(ValueError, self.hash_table.insert, None, 3232)
    # FAST
    def test_insert_none_value(self):
        ''' if value is None, raise valueError '''
        self.assertRaises(ValueError, self.hash_table.insert, "2323", None)
    # FAST
    def test_get_none_key(self):
        self.assertRaises(ValueError, self.hash_table.get_value, None)
    # FAST
    def test_delete_none_element(self):
        self.assertRaises(ValueError, self.hash_table.delete, None)
    # FAST
    def test_contains_none_element(self):
        self.assertRaises(ValueError, self.hash_table.contains, None)
# Run
if "__main__" == __name__:
    unittest.main()