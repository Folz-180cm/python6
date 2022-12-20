# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# абвгд гдежз жзе абв ыопыпт ->  гдежз жзе ыопыпт

string = 'абвгд гдежз жзе абв ыопыпт'
string = string.split()


result = [i for i in string if "абв" not in i]
print(result)