"""
This test is used to ensure that that logger.Logger class functions as it is
supposed to.

The logger is used to write error messages and the like to a log.txt file.
"""
import unittest
import package.code.logger as logger


class TestLogger(unittest.TestCase):
    LOG_FILE = 'test-logger.txt'
    def setUp(self):
        """
        Set up the Logger item for testing. This involves creating the Logger
        object, adding the logger items (via the logAction() method), and then
        clearing out the test-log.txt file.
        """
        # initialize the object
        self.logger = logger.Logger({'logpath': self.LOG_FILE})

        # load the logger object with the test items
        self.log_items = ['these', 'are', 'test', 'items']
        for item in self.log_items:
            self.logger.logAction(item)

        # clear out the test-log.txt file
        with open(self.LOG_FILE, 'w') as tfile:
            tfile.write('')
    def test_log_cache(self):
        """
        Test the logCache; ensure that adding an item via the logAction method
        correctly added the item to its cache.
        """
        for i,loaded_item in enumerate(self.logger.log_cache):
            item_split = loaded_item.split("] ")[1].split("\n")[0]
            self.assertEqual(self.log_items[i], item_split)
    def test_write_out(self):
        """
        Test the writeOut method; ensure that the log cache was, in fact, 
        written to the log.txt file.
        """
        # call the writeOut() method
        self.logger.writeOut()

        # open up the log.txt file, read in the contents, and make sure that it
        # matches the input parameters.
        with open(self.LOG_FILE, 'r') as lfile:
            written_data = lfile.read().split("\n")

            # loop through each row in the log.txt file
            for i,w in enumerate(written_data):
                if len(w) > 0:
                    self.assertEqual(self.log_items[i], w.split("] ")[1])
                    
# if __name__ == '__main__':
#     unittest.main()