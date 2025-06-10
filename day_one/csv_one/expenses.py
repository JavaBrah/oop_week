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
        if isinstance(living_exp, float) and living_exp >= 0:
            self._living_exp = round(living_exp, 2)

        else:
            raise ValueError("Input numbers: Living")
        
    
    @property
    def food_exp(self):
        return self._food_exp
    
    @food_exp.setter
    def food_exp(self, food_exp: float):
        if isinstance(food_exp, float) and food_exp >= 0:
            self._food_exp = round(food_exp, 2)
        else:
            raise ValueError("Input numbers: Food")    
    
    @property
    def travel_exp(self):
        return self._travel_exp
    
    @travel_exp.setter
    def travel_exp(self, travel_exp: float):
        if isinstance(travel_exp, float) and travel_exp >= 0:
            self._travel_exp = travel_exp
        else:
            raise ValueError("Input numbers: Travel")
    
    @property
    def leisure_exp(self):
        return self._leisure_exp
    
    @leisure_exp.setter
    def leisure_exp(self, leisure_exp):
        if isinstance(leisure_exp, float) and leisure_exp >= 0:
            self._leisure_exp = leisure_exp
        else:
            raise ValueError("Input numbers: Leisure")
        
    @property
    def savings(self):
        return self._savings
    
    @savings.setter
    def savings(self, savings):
        if isinstance(savings, float) and savings >= 0:
            self._savings = savings
        else: 
            raise ValueError("Input numbers: Savings")
        
    def add_expense(expense, amount, filename="expenses"):
        


    def update_expense(self, expense_name, new_amount = None, filename="expenses.csv"):
        expense = []
        update = False
        
        with open(filename, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Expense'] == expense_name:
                    if new_amount:
                        row["Amount"] = str(round(new_amount, 2))
                    update = True
                expense.append(row)

        if update:
            with open(filename, "w", newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=["Expense", "Amount"])
                writer.writeheader()
                writer.writerows(expense)
        else:
            print("Expenses not found.")



e = Expenses(20.00)
e.update_expense("Living", e.living_exp)
print(e.living_exp)