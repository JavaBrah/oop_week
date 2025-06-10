

class CarManager():
    list_of_managers = []
    all_cars = {}
    total_cars = 0
    id = 0

    @classmethod
    def add_manager(cls, manager_name):
        manager_name = CarManager(manager_name)
        cls.list_of_managers.append(manager_name)

    @classmethod
    def view_managers(cls):
        for i, manager in enumerate(cls.list_of_managers):
            print(i, manager.name)

    @classmethod
    def adjust_id(cls):
        cls.id += 1
    
    @classmethod
    def add_to_total_cars(cls):
        cls.total_cars += 1
    
    @classmethod
    def view_total_cars(cls):
        print(cls.all_cars)

    @classmethod
    def add_car_to_all_cars(cls, car_info_func):
        cls.adjust_id()
        cls.all_cars[cls.id] = car_info_func
        cls.add_to_total_cars()    

    def __init__(self, name):
        self.name = name
        self._managers_cars = {}
        self._managers_total_cars = 0
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else:
            raise ValueError("Input Letters for Name")
    
    @property
    def managers_total_cars(self):
        return self._managers_total_cars
    
    @property
    def managers_cars(self):
        return self._managers_cars

    def view_managers_cars(self):
        print(self._managers_cars)
   
    def add_to_managers_cars(self, car_info_func):
        try:
            CarManager.add_car_to_all_cars(car_info_func)
            self._managers_total_cars += 1
            self._managers_cars[CarManager.id] = car_info_func
        except:
            print("Did not add car")

    def car_info(self, make, model, year, mileage, services):
        
        car_dict = {
            'make': make, 
            'model': model, 
            'year': year, 
            'mileage': mileage, 
            'services': services
            }
        return car_dict
    
    @staticmethod
    def present_menu():
        print("""
    1. Look at total cars
    2. Look at cars by Manager
    3. Add Car by Manager
    """)
        user_choice = int(input("Select one of the options"))
        match user_choice:
            case 1:
                CarManager.view_total_cars()
                CarManager.present_menu()
            case 2:
                CarManager.view_managers()
                i = int(input("Select Manager by number"))
                CarManager.list_of_managers[i].view_managers_cars()
                CarManager.present_menu()
            case _:
                print("Later")




CarManager.add_manager("keg")
CarManager.add_manager("k")
 
CarManager.list_of_managers[0].add_to_managers_cars(
    CarManager.list_of_managers[0].car_info("a", "d", "d", "d", 'd'))

CarManager.list_of_managers[1].add_to_managers_cars(
    CarManager.list_of_managers[1].car_info("123", "132", "123", "132", '132'))

CarManager.list_of_managers[1].view_managers_cars()

CarManager.present_menu()