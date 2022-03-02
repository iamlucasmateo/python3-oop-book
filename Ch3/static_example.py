class Static1:
    @staticmethod
    def example():
        return "example"

print(Static1().example())
print(Static1.example())

class Static2:
    def example(self):
        return "example"
    example = staticmethod(example)


print(Static2().example())
print(Static2.example())
