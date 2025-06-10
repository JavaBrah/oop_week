import csv
import os

class Expenses():
    def __init__(self, living_exp = 0.00, food_exp = 0.00, 
                 travel_exp = 0.00, leisure_exp = 0.00, savings = 0.00):
        self.living_exp = living_exp
        self.food_exp = food_exp
        self.travel_exp = travel_exp
        self.leisure_exp = leisure_exp
        self.savings = savings
    
    @property
    def living_exp(self):
        return self._living_exp
    
    @living_exp.setter
    def living_exp(self, living_exp: float):
        if isinstance(living_exp, float) and living_exp > 0:
            self._living_exp = round(living_exp, 2)
        else:
            raise ValueError("Input numbers: Living")
        return self._living_exp
    
    @property
    def food_exp(self):
        return self._food_exp
    
    @food_exp.setter
    def food_exp(self, food_exp: float):
        if isinstance(food_exp, float) and food_exp > 0:
            self._food_exp = round(food_exp, 2)
        else:
            raise ValueError("Input numbers: Food")
        return self._food_exp
    
    @property
    def travel_exp(self):
        return self._travel_exp
    
    @travel_exp.setter
    def travel_exp(self, travel_exp: float):
        if isinstance(travel_exp, float) and travel_exp > 0:
            self._travel_exp = travel_exp
        else:
            raise ValueError("Input numbers: Travel")
        return self._travel_exp
    
    @property
    def leisure_exp(self):
        return self._leisure_exp
    
    @leisure_exp.setter
    def leisure_exp(self, leisure_exp):
        if isinstance(leisure_exp, float) and leisure_exp > 0:
            self._leisure_exp = leisure_exp
        else:
            raise ValueError("Input numbers: Leisure")
        
    @property
    def savings(self):
        return self._savings
    
    @savings.setter
    def savings(self, savings):
        if isinstance(savings, float) and savings > 0:
            self._savings = savings
        else: 
            raise ValueError("Input numbers: Savings")


    def update_expense(self, expense_name, new_amount = None, filename="expenses.csv"):
        

        

e = Expenses("fk")
e.sayHi()
print(e.living_exp)