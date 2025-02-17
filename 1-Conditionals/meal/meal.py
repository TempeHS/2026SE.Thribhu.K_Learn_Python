import unittest

def convert(input: str) -> str:
    time = input.split(':')
    
    hours = int(time[0])
    minutes = int(time[1])
    
    if 0 < minutes >= 60:
        print("Not possible to have that many minutes")
        return 'nothing'
    
    if 0 < hours >= 24:
        print("Not possible to have that many hours")
        return 'nothing'
    
    if hours == 7:
        return 'breakfast time'
    
    if hours == 12:
        return 'lunch time'
    
    if hours == 18:
        return 'dinner time'
    
    return 'nothing'

# Make it easier for testing instead of doing it everytime
class Test(unittest.TestCase):
    def test_breakfast_hour_only(self):
        self.assertEqual(convert('7:00'), 'breakfast time')
    
    def test_breakfast_hour_and_minute(self):
        self.assertEqual(convert('7:30'), 'breakfast time')
    
    def test_lunch_24_hr_time(self):
        self.assertEqual(convert('12:42'), 'lunch time')
    
    def test_dinner_24_hr_time(self):
        self.assertEqual(convert('18:32'), 'dinner time')
    
    def test_nothing(self):
        self.assertEqual(convert('11:11'), 'nothing')


if __name__ == '__main__':
    unittest.main()