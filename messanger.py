

class Messanger:
    def __init__(self,user,input_message,output_message,status,password):
        self.user = user
        self.input_message = input_message
        self.output_message = output_message
        self.status = status
        self.password = password

    def send_message(self,other):
        self.status = "Yuborildi"


    def read_message(self):
        self.status  = "oqildi"

    def sent_file(self):

