class Father(object):
    height=5.9
    @classmethod
    def showheight(cls):
        print("Height is ",cls.height)
class Mother(object):
    eyecolor="brown"
    @classmethod
    def showeyecolor(cls):
        print("eyecolor is ",cls.eyecolor)
class Child(Father,Mother):
    pass

Child.showheight()
Child.showeyecolor()
