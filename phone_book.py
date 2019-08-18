class Contact():
    def __init__(self, first_name, last_name, phone_number, favorite_contact=False, *args, **kwargs):
        self.f_n = first_name
        self.l_n = last_name
        self.p_n = phone_number
        self.f_c = favorite_contact
        self.args = args
        self.kwargs = kwargs
    def __str__(self):
        if self.f_c == True:
            f_c = "да"
        elif self.f_c == False:
            f_c = "нет"

        str_args = ''
        for item in self.args:
            str_args += '\n' + 10*' ' + item

        str_kwargs = ''
        for item in self.kwargs:
            str_kwargs += '\n' + 10*' ' + item + ': ' + self.kwargs[item]

        if str_args == '' and str_kwargs == '':
            str_args = ' нет'
            
        cont = f"Имя: {self.f_n}\n\
Фамилия: {self.l_n}\n\
Телефон: {self.p_n}\n\
В избранных: {f_c}\n\
Дополнительная информация:{str_args}{str_kwargs}"

        return cont

jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
jack = Contact('Jack', 'Baker', '+74354567395', False, '+71234567809', '+79874567652')
chloe = Contact('Chloe', 'King', '+71234567765', False, '+79874567897', '+71234567396', email='chloe@king.com')
lucas = Contact('Lucas', 'Hill', '+74324567475')
print(jhon)
print(jack)
print(chloe)
print(lucas)