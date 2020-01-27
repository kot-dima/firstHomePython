# gn = "good night"
# gd = "good day"
# ge = "good evening"
# gm = "good morning"

# timeits = int(input("Введіть годину : "))

# if timeits >= 0 and timeits <= 6:
#     print(gn)
# elif timeits > 6 and timeits < 12:
#     print(gm)
# elif timeits >= 12 and timeits <= 20:
#     print(gd)
# elif timeits > 20 and timeits < 24:
#     print(gn)
# else:
#     print("Error")


d = 2.54

option = input("Дюйми в сантиметри натисніть 1 , сантиметри в дюйми натисніть 2 :")

if option == "1":
    a = float(input("Введіть число в дюймах :"))
    print(a*d, " сантиметрів")
elif option == "2":
    b = float(input("Введіть число в сантиметрах :"))
    print(b/d, " дюймів")
else:
    print("некоректне введення")