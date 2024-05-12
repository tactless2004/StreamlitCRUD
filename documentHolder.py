class DocumentHolder:
    def __init__(self):
        self.documents = {}
        self.currentID = 0

    def getNewID(self):
        returnID = self.currentID
        self.currentID += 1
        return returnID
    
    def insert(self, body):
        id = self.getNewID()
        self.documents[id] = (id, body)
        return True

    def read(self, id):
        id = int(id)
        if id in self.documents:
            var = self.documents[id]
        else:
            return "Document does not exist!"

        return var[1]
    
    def update(self, id, newbody):
        id = int(id)
        if id in self.documents:
            self.documents[id] = (id,newbody)
            return True
        else:
            return False
        
    def delete(self, id):
        id = int(id)
        if self.documents[id] is not None:
            del self.documents[id]
            return True
        else:
            return False
        
    def clear(self):
        self.documents = {}
        self.currentID = 0

    def listAll(self):
        HEADER = "ID            Record "
        print(HEADER)
        print("-"*30)
        for id in self.documents.keys():
            print("{0}{1}".format(str(self.documents[id][0]).ljust(14), self.documents[id][1].ljust(25)))
        

    
        