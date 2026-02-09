class Tea:
    def __init__(self, name, temperature):
        self.name = name
        self.__temperature=temperature
    @property
    def temperature(self):# deze temperzture is the setter en wordt overal gebruikt ( boven ook)
        return self.__temperature
    @property
    def tempinfarhenheit(self): #enkel readonly je kan geen a.farhenheit=3 doen op dit moment als je geen stter hebt
        return self.__temperature * 30
    @tempinfarhenheit.setter
    def tempinfarhenheit(self,value):
        self.temperature=value/30
    @temperature.setter
    def temperature(self, value):
        if(value <= 0 or value >= 100):
            raise ValueError("Tea must be liquid")
        self.__temperature = value
    def __repr__(self):
        return f"{self.name} + {self.temperature}"
a=Tea("dd",45)
a.temperature=9
a.name="haha"
a.tempinfarhenheit=10
print(a.tempinfarhenheit)
print(a.temperature)
