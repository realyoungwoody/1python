print("Введите имя")
Name = str(input())
print("Введите фамилию")
Surname = str(input())
print("Введите год рождения")
Birth_date = int(input())
print(Name + '_' + Surname + '_' + str(Birth_date))
Name, Surname = Surname, Name
Birth_date += 60
print(Name + '_' + Surname + '_' + str(Birth_date))
input()
