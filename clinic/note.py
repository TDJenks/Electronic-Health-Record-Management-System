from datetime import datetime

class Note:
    def __init__(self,code=None,details=None):
        self.code = code
        self.details = details
        self.timestamp = datetime.now()

    # Note can be passed as a string
    def __str__(self):
        return str(self.details) +" " +str(self.code)

    # Returns true if the two Notes have matching codes and details
    def __eq__(self, other):
        return self.code == other.code and self.details == other.details

    