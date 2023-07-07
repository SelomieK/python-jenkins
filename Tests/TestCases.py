import os
import sys
import unittest



root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(root_dir)
from src.various_methods import VariousMethods

vm = VariousMethods()  # instance of class VariousMethods


class TestCase(unittest.TestCase):
    """Test cases for ConvertToAtlasCopcoString"""

    def test_ConvertToAtlasCopcoString1(self):
        """Boundary value assert"""
        print('Boundary Value Tests')
        self.assertEqual(vm.ConvertToAtlasCopcoString(1), '1')
        self.assertEqual(vm.ConvertToAtlasCopcoString(100), 'Copco')
        self.assertEqual(vm.ConvertToAtlasCopcoString(99), 'Atlas')
        self.assertEqual(vm.ConvertToAtlasCopcoString(15), 'AtlasCopco')

    """Exception Handling Tests: Test if value and type assertion error gets raised"""

    def test_ConvertToAtlasCopcoString2(self):
        print('Value exception handling test')
        with self.assertRaises(ValueError):
            self.assertRaises(vm.ConvertToAtlasCopcoString(-1))
            self.assertRaises(vm.ConvertToAtlasCopcoString(101))

    def test_ConvertToAtlasCopcoString3(self):
        print('Type exception handling test')
        with self.assertRaises(TypeError):
            self.assertRaises(vm.ConvertToAtlasCopcoString(15.5))
            self.assertRaises(vm.ConvertToAtlasCopcoString(15.0))
            self.assertRaises(vm.ConvertToAtlasCopcoString('AtlasCopco'))

    def test_ConvertToAtlasCopcoString4(self):
        """Check if the return is always string for proper input ranges"""
        print('Return type test')
        self.assertEqual(type(vm.ConvertToAtlasCopcoString(11)), str)
        self.assertEqual(type(vm.ConvertToAtlasCopcoString(30)), str)

    """Test Cases for ReverseString"""

    def test_ReverseString1(self):
        """Some random  value tests"""
        print('Random value reverse string tests')
        self.assertEqual(vm.ReverseString('AtlasCopco'), 'ocpoCsaltA')
        self.assertEqual(vm.ReverseString('Atlas Copco'), 'ocpoC saltA')

    def test_ReverseString2(self):
        """try string palindromes and other scenarios"""
        print('Test palindromes and special character string')
        self.assertEqual(vm.ReverseString('level'), 'level')
        self.assertEqual(vm.ReverseString('a'), 'a')
        self.assertEqual(vm.ReverseString('Atlas copco@Python test'), 'tset nohtyP@ocpoc saltA')

    """ValueError and TypeError handling test"""

    def test_ReverseString3(self):
        print('ValueError exception test ')
        with self.assertRaises(ValueError):
            self.assertRaises(vm.ReverseString(None))
            self.assertRaises(vm.ReverseString(""))

    def test_ReverseString4(self):
        print('TypeError exception handling')
        with self.assertRaises(TypeError):
            self.assertRaises(TypeError, vm.ReverseString(123))
            self.assertRaises(TypeError, vm.ReverseString(["Atlas"]))

    def test_ReverseString5(self):
        """Check return type string"""
        print('Return type test')
        self.assertTrue(type(vm.ReverseString('123')), str)
        with self.assertRaises(TypeError):
            self.assertEqual(vm.ReverseString(1221))

    def test_ReverseString6(self):
        print('Test text with different space character')
        self.assertEqual(vm.ReverseString('  Atlas   Copco  '), '  ocpoC   saltA  ')
        self.assertEqual(vm.ReverseString("  "), "  ")

    """Test Cases for IsItFibonacci"""

    def test_IsItFibonacci1(self):
        print('Boundary test for IsItFibonacci')
        self.assertTrue(vm.IsItFibonacci(2))
        self.assertFalse(vm.IsItFibonacci(24))

    def test_IsItFibonacci2(self):
        print('Value exception error test')
        with self.assertRaises(ValueError):
            self.assertRaises(ValueError, vm.IsItFibonacci(-1))
            self.assertRaises(ValueError, vm.IsItFibonacci(26))
        with self.assertRaises(TypeError):
            self.assertRaises(vm.IsItFibonacci('dfff'))


if __name__ == '__main__':
    unittest.main()
