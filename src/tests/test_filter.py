import sys
import unittest
from src.data import *
from src.domain import *
from datetime import datetime, timedelta

class FilterTestCase(unittest.TestCase):

    def setUp(self):
        session = ConfigItem(timedelta(days=0), ["session1", "session2"])
        daily = ConfigItem(timedelta(days=1), ["daily1", "daily2"])
        weekly = ConfigItem(timedelta(days=7),["weekly1", "weekly2"])
        monthly = ConfigItem(timedelta(days=30),["monthly1", "monthly2"])
        self.all = [session, daily, weekly, monthly]
        self.config = Config(self.all)


    def test_FirstRun(self):
        # Define
        
        report = Report(0, {})
        filter = Filter(currentTime=datetime.fromtimestamp(100))

        # Run
        folders = filter.evaluate(self.config, report)

        # Assert
        self.assertCountEqual(folders, [entity for item in self.config.items for entity in item.entities])


    def test_SameDay(self):
        # Define
        
        report = Report(95, {
            "session1" : 95,
            "session2" : 95,
            "daily1" : 95,
            "daily2" : 95,
            "weekly1" : 95,
            "weekly2" : 95,
            "monthly1" : 95,
            "monthly2" : 95,
        })
        filter = Filter(currentTime=datetime.fromtimestamp(100))

        # Run
        folders = filter.evaluate(self.config, report)

        # Assert
        self.assertCountEqual(folders, ["session1", "session2"])


    def test_NextDay(self):
        # Define
        
        report = Report(95, {
            "session1" : 95,
            "session2" : 95,
            "daily1" : 95,
            "daily2" : 95,
            "weekly1" : 95,
            "weekly2" : 95,
            "monthly1" : 95,
            "monthly2" : 95,
        })
        filter = Filter(currentTime=datetime.fromtimestamp(100) + timedelta(days=1))

        # Run
        folders = filter.evaluate(self.config, report)

        # Assert
        self.assertCountEqual(folders, ["session1", "session2", "daily1", "daily2"])

    # @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)
    

if __name__ == '__main__':
    unittest.main()