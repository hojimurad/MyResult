class Time:
    def __init__(self,hour,minute,secund):
        self.hour = hour
        self.minute = minute
        self.secund =secund
        
        
class Mobile(Time):
    def __init__(self,surname,operator,real_time):
        super().__init__(hour = real_time.split(":")[0],minute=real_time.split(":")[1],secund=real_time.split(":")[2])

        self.surname  =  surname
        self.operator = operator

    def __repr__(self):
        pass
    

belline = Mobile("Belline",91,"10:36:20")

