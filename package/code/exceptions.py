class MPBaseException(Exception):
    def __str__(self):
        return ""
class MPArgvException(Exception):
    def __str__(self):
        return "Passed in argument does not match any accepted sys args."