# С помощью вложенных if и чувства меры опишите систему где ответ человека принимается через input и дальшейшее общение продолжается в новом "ключе"
# Сделайте возможным из любого места нажать q и прервать мучения пользователя.

promotion = """\n1.Смачний Безлім 100грн/4 тижні
2.Розваги без меж 175грн/4 тижні
3.Максимальний Безлім 300грн/4 тижні"""

tariffes = '''\n1.Купуйте акційні моделі смартфонів Samsung Galaxy A та отримуйте 15% від вартості на бонусний рахунок.
2.Київстар дарує бонуси до девайсів! Купуйте 4G-смартфон і отримаєте безлімітний інтернет.
3.Купуйте смартфони Galaxy S і Z серії та отримайте до 4000 бонусів на рахунок. '''
oper = '\nСоединяем с оператором, ожидайте'

while True:
    client_1 = str(input(
        'Здравствуй, если хочешь узнать акции нажми 1, если тарифы  2, если вам нужно связаться с оператором 3').lower())

    if (client_1 == '1'):
        print(promotion)
        continue
    elif (client_1 == '2'):
        print(tariffes)
        continue
    elif(client_1 == '3'):
        print(oper)
        continue
    elif(client_1 == 'q'):
        print('Удачи')
        break



