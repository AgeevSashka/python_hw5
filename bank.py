def bank():
    purch = 0
    purch_history = []
    purchases = {
        'Еда': 200,
        'Кино': 300,
        'Уборка': 100
    }
    while True:
        check = int(input('Выберете действие: \n1. пополнить счет\n2. покупка\n3. история покупок\n4. выход\n'))

        if check == 1:
            gold = int(input('Введите сумму на которую хотите пополнить :'))
            purch += gold
            print(f'Вы пополнели счет на {gold}, ваш счет составляет {purch}')
            purch_history.append(f'Вы пополнили счет на {gold}')
        elif check == 2:
            pch = input('Введите , что вы хотите купить : \n1. Еда\n2. Кино\n3. Уборка\n')
            for k, v in purchases.items():
                if pch == k:
                    if purch > 0 or purch >= purchases[pch]:
                        purch -= purchases[pch]
                        purch_history.append(f'Вы купили {k}')
                    else:
                        print(f'Недастаточно средств, ваш баланс {purch}')
        elif check == 3:
            for hist in purch_history:
                print(hist)
        elif check == 4:
            print('Вы закончили работу с банковским счетом')
            break
        elif check == 5:
            print(f'Текущий баланс равен {purch}')
        else:
            print('Ввод должен содержать число от 1-5')

