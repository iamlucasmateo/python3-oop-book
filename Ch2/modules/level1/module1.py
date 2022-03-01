

class Module1:
    def method(self):
        print("Hello from Module1 - Level 1")

class TestImports1:
    def __init__(self, absolute=True):
        self.absolute = absolute
    
    def level2_from1(self):
        from level1.level2.module2 import Module2
        Module2().method()

    def level3_from1(self):
        from level1.level2.level3.module3 import Module3
        Module3().method()


