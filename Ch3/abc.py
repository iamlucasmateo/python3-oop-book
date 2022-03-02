from abc import ABC, abstractmethod, abstractproperty

# Implementations of interfaces must include the methods

class AudioFile1(ABC):
    @abstractmethod
    def play(self):
        pass

class MP31A(AudioFile1):
    pass

class MP31B(AudioFile1):
    def play(self):
        pass

class MP31C:
    def play(self):
        pass

try:
    MP31A()
except Exception as e:
    print("Trying to instantiate without defining abstract methods")
    print(e)

print(f"Checking isinstance, explicit definition : {isinstance(MP31B(), AudioFile1)}")
print(f"Checking isinstance, duck typing : {isinstance(MP31C(), AudioFile1)}")


# Allowing duck typing in the interface

class AudioFile2(ABC):
    @abstractmethod
    def play(self):
        pass

    @classmethod
    def __subclasshook__(cls, sub):
        if cls is AudioFile2:
            sub_attrs = set(dir(sub))
            cls_attrs = cls.__abstractmethods__
            if cls_attrs <= sub_attrs:
                return True
            return False
        # "NotImplemented" allows subclasses to use the usual __subclasshook__ instead of this one
        return NotImplemented

class Wav2A(AudioFile2):
    def play(self):
        pass

class Wav2B:
    def play(self):
        pass

class Wav2C:
    def play2(self):
        pass

print(f"Implementation via duck typing: {isinstance(Wav2B(),AudioFile2)}")
print(f"Checking with class that does not implement: {isinstance(Wav2C(),AudioFile2)}") 


