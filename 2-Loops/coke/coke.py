import unittest

def main():
    total:int = 50
    
    while total > 0:
        total -= coin(input())

def coin(coin_input):
    print("Insert Coin: ")
    # _input = input()
    
    print(coin_input)
    
    _inserted = int(coin_input)
    
    if _inserted != 10 and _inserted != 25 and _inserted != 5:
        return -1
    
    due = 50 - _inserted
    # due -= _inserted
    
    if due < 0:
        # change = due * -1
        print(f"Change Owed: {due * -1}")
        return due
    else:
        print(f"Amount due: {due}")
        return due
    

class Test(unittest.TestCase):
    
    def test_error(self):
        self.assertEqual(coin(30), -1)
        
    def test(self):
        self.assertEqual(coin(5), 45)
        self.assertEqual(coin(10), 40)
        self.assertEqual(coin(25), 25)

if __name__ == '__main__':
    unittest.main()