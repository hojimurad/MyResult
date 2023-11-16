


class Employee:

    """Employee classi"""
    def __init__(self,surname,position,salary):
        self._surname = surname
        self._position = position
        self._salary = salary

    def __repr__(self):
        return  self._surname

    def get_position(self):
        return  self._position

    def get_salary(self):
        return self._salary

    def set_surname(self,a):
        self._surname = a

    def set_position(self,a):
        self._position= a

    def set_salary(self,a):
        """this method create new salary with  raiting"""
        self._salary = a





class Enterprise_employee(Employee):
    def __init__(self,surname,position,salary,rating):
        super().__init__(surname,position,salary)

        self.rating =rating



        if self.rating in list(range(60,75)):
            self._salary = self._salary + (self._salary / 100) * 20
        elif self.rating in list(range(75,90)):
            self._salary = (self._salary + (self._salary / 100) * 40)
        elif self.rating in list(range(90,101)):
            self._salary  = self._salary(self._salary/100)*60



e1 =Enterprise_employee("Tillayev","manager",1000000,71)
e2 = Enterprise_employee("Soliyev","qoravul",10000,10)
