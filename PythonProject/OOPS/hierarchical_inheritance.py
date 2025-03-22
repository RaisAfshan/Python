class College():
    def __init__(self,cname):
        self.cname =cname

class Studentone(College):
    def __init__(self,sname1,cname):
        self.sname1 = sname1
        super().__init__(cname,)

    def display(self):
        print("name-->",self.sname1,"collegename-->",self.cname)

class Studenttwo(College):
    def __init__(self,cname,sname2):
        self.sname2 = sname2
        super().__init__(cname)

    def display(self):
        print("name-->", self.sname2, "collegename-->", self.cname)

obj = Studentone("john","TKMCE")
obj.display()

obj2 = Studenttwo("Tkmce","mike")
obj2.display()




