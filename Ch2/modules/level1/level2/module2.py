
from level1.level2.level3.module3 import Module3

class Module2:
    def method(self):
        print("Hello from Module 2 - Level 2")

class TestImports2:
    def __init__(self, absolute=True):
        self.absolute = absolute

    def level1_from2(self):
        if self.absolute:
            print("Absolute import")
            from level1.module1 import Module1
        else:
            print("Relative import")
            from ..module1 import Module1
        Module1().method()
    
    def level3_from2(self):
        if self.absolute:
            print("Absolute import")
            from level1.level2.level3.module3 import Module3
        else:
            print("Relative import")
            from .level3.module3 import Module3
        Module3().method()