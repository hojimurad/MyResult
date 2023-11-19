
# 24 soat ga qnacha qolganini hisoblash

class Time:
    def __init__(self,hour,minute,sekund):
        self.hour = hour
        self.minute = minute
        self.sekund = sekund


    def get_time(self):
        return f"{23-(self.hour%24)} : {59-(self.minute%60)} : {60-(self.sekund%60)}"
    def set_time(self):
        if self.minute>=20:
            self.hour+=2
            self.minute+=60
            self.minute%=60
        else:
            self.hour+=1
            self.minute +=40
        self.hour =self.hour%24
        return f"{self.hour} : {self.minute}: {self.sekund}"
t1 =Time(22,17,20)
print(t1.set_time())