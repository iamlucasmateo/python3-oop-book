from level1.module1 import Module1, TestImports1
from level1.level2.module2 import TestImports2
from level1.level2.database import database, init_db

def main():
    print("Testing direct import from main.py")
    Module1().method()
    print("\nTesting imports from module 1")
    TestImports1(absolute=True).level2_from1()
    TestImports1(absolute=True).level3_from1()
    print("\nTesting absolute imports from module 2")
    abs_imports = TestImports2(absolute=True)
    abs_imports.level1_from2()
    abs_imports.level3_from2()
    print("\nTesting relative imports from module 2")
    relative_imports = TestImports2(absolute=False)
    relative_imports.level1_from2()
    relative_imports.level3_from2()
    print("\nTesting initialization from a different module")
    print("Database before init:", database)
    init_db()
    print("Database after init:", database)

if __name__ == "__main__":
    main()


