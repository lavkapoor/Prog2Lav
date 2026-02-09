# Write your code here
import math
class BMICalculator:
    def __init__(self,weight,height):
        self.weight=weight
        self.height=height
        self._category=""
    @property
    def bmi(self):
        BMI=self.weight/self.height**2
        if BMI<18.5:
            self.category="underweight"
        elif BMI<=25:
            self.category="normal"
        else:
            self.category="overweight"
        return round(BMI,2)
    def category(self):
        return self._category
calc = BMICalculator(80,1.80)
print(calc.bmi)
print(calc.category)


    

    