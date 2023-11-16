

class Worker:
    def __init__(self,surname,position,salary):
        self._surname =surname

        if self._surname.startswith("Abdulla"):
            self._position = "Injiner  " + position
        else:
            self._position =position
        self._salary =salary+ (salary/100)*15


    def get_surneme(self):
        return self._surname

    def get_position(self):
        return self._position

    def get_salary(self):
        return self._salary



w1 =Worker("sda","manager",100)
print(w1.get_salary())
print(w1.get_position())



