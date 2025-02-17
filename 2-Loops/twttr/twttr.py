import unittest

def twttr(input:str) -> str:
    # _input = input()
    _input = input
    
    # print(_input)

    i:int = 0

    new_word = ""

    for c in _input:
        if c in ['a', 'e', 'i', 'o', 'u']:
            new_word += ''
        else:
            new_word += c
        
        i+=1

    # print(new_word)
    return new_word

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(twttr("Twitter"), "Twttr")
        self.assertEqual(twttr("What's your name?"),"Wht's yr nm?")
        self.assertEqual(twttr("CS50"), "CS50")

if __name__ == '__main__':
    unittest.main()