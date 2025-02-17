import unittest

def camel_to_snake(input: str) -> str:
    # firstName
    
    snake = ""
    
    for i in input:
        if i.isupper():
            snake += '_' + i.lower()
        else:
            snake += i
    
    return snake


# Ignore, just for testing
class Test(unittest.TestCase):
    def test_single(self):
        self.assertEqual(camel_to_snake('name'), 'name')
    
    def test_double(self):
        self.assertEqual(camel_to_snake('firstName'), 'first_name')
    
    def test_triple(self):
        self.assertEqual(camel_to_snake('preferredFirstName'), 'preferred_first_name')

if __name__ == '__main__':
    unittest.main()