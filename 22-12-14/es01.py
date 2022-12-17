"""Function that implements abs function"""

import unittest

def abs_custom(value):
    """Function that returns the abs of a given number"""
    if not isinstance(value,(int, float, bool)):
        raise TypeError("wrong tye input")
    if value<0:
        return -value
    else:
        return value
def power_of_number(value, exp_value):
    """function that returns value^exp_value"""
    return value**exp_value
class TestAbsFunction(unittest.TestCase):
    def test_abs_function(self):
        """Test function for nominal case and negative one"""
        self.assertEqual(abs_custom(3.0), 3.0)
        self.assertEqual(abs_custom(-3.0), 3.0)
    def test_abs_function_exc(self):
        with self.assertRaises(TypeError):
            abs_custom("pippo")
    def test_pwr(self):
        """Test of power function"""
        self.assertAlmostEqual(power_of_number(2.0,2),4.0)
if __name__ =="main":
    unittest.main()