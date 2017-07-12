"""
The Logger module is used to cache log commands and write them to file.

Once an object is created, it can accept text arguments in its logAction() 
    method, which stores the action with its add timestamp to the object's
    log_cache variable.

When specified by the calling code, the Logger object can push the updates to
    a log file - it appends to the current data iwthin the log file. It will 
    never clear the log file on its own.
"""
from time import localtime, strftime

class Logger():
    def __init__(self, in_settings):
        """ 
        Initialize the log_path, as well as the declare the cache used to
        store the log messages.
        """
        self.log_path = in_settings['logpath']
        self.log_cache = []

    def logAction(self, inActionText, autoWrite=False):
        """
        The logAction method takes in a error message (or log message) from the 
        calling code and stores the item in its object cache (a list, as the
        log_cache variale).

        It timestamps the input value using the current local time. This creates
        a log item in the format 
            [yyyy-mm-dd hh:mm:ss] log_message
        """
        time_text = '[{}]'.format(strftime('%Y-%m-%d %H:%M:%S', localtime()))
        self.log_cache.append('{} {}\n'.format(time_text, inActionText))
        if autoWrite: self.writeOut()

    def writeOut(self):
        """
        The writeOut method takes the instance cache and writes the contents to
        the log.txt file.

        The write works as an append action; for this reason, the log file will
        never be deleted unless done so manually.
        """
        # write the log cache to file
        with open(self.log_path, 'a') as lpfile:
            for log_item in self.log_cache:
                lpfile.write(log_item)

        # clear the log cache
        self.log_cache = []
