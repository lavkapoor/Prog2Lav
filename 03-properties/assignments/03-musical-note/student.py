class MusicalNote:
    def __init__(self,name,pitch):
        self.name=name
        self.__pitch=pitch
    @property
    def pitch(self):
        return self.__pitch

b=MusicalNote("ka","dfer")
print(b.pitch)