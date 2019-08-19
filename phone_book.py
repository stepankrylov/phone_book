class Contact:
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
Дополнительная информация:{str_args}{str_kwargs}\n"

        return cont

phonebook = [Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com'), \
            Contact('Jack', 'Baker', '+74354567395', True, '+71234567809', '+79874567652'), \
            Contact('Chloe', 'King', '+71234567765', False, '+79874567897', '+71234567396', email='chloe@king.com'), \
            Contact('Lucas', 'Hill', '+74324567475')]

class PhoneBook:
    def __init__(self, name_book):
        self.n_b = name_book
    
    def all_contacts(self):
        for item in self.n_b:
            print(item)
        return self

    def add_contact(self, first_name, last_name, phone_number, favorite_contact=False, *args, **kwargs):
        self.n_b.append(Contact(first_name, last_name, phone_number, favorite_contact, *args, **kwargs))
        for item in self.n_b:
            print(item)

    def del_coctact(self, phone_number):
        count = 0
        for item in self.n_b:
            if item.p_n == phone_number:
                del_num = count
            count += 1
        del self.n_b[del_num]
        for item in self.n_b:
            print(item)

    def find_fav_contact(self):
        for item in self.n_b:
          if item.f_c == True:
            print(item)

    def find_contact(self, first_name, last_name):
        for item in self.n_b:
          if item.f_n == first_name and item.l_n == last_name:
            print(item)

friend = PhoneBook(phonebook)
friend.all_contacts()
print('************************************')
friend.add_contact('Noah', 'Fisfer', '+75434562543', True, twitter='@noah', email='noah@fisher.com')
print('************************************')
friend.del_coctact('+71234567809')
print('************************************')
friend.find_fav_contact()
print('************************************')
friend.find_contact('Lucas', 'Hill')