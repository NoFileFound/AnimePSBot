import json

class Database:
    def __init__(self):
        # Main
        self.Config = self.OpenFile("config.json")
        
        # Knowledge db
        self.badReasonData = self.OpenFile("./knowledge/baninfo.json")
        self.errorCodeData = self.OpenFile("./knowledge/errorc.json")

    def OpenFile(self, file):
        data = ""
        with open(f"./Data/{file}", "r") as F:
            data = json.load(F)
        return data
    
    def Reload(self):
        self.badReasonData = self.OpenFile("./knowledge/baninfo.json")
        self.errorCodeData = self.OpenFile("./knowledge/errorc.json")
    
    def SaveFile(self, file, data) -> None:
        with open(f"./Data/{file}", "w") as F:
            json.dump(data, F)

def Load():
    global db
    db = Database()