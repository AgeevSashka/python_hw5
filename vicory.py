import random

def victory(party):
    i = 0
    while i < party:
        writers = {
            'Пушкин': '26.11.1799',
            'Тютчев': '23.11.1803',
            'Гоголь': '20.03.1807',
            'Лермонтов': '03.10.1814',
            'Некрасов': '10.12.1821',
            'Толстой': '28.08.1828',
            'Бу́нин': '22.10.1870',
            'Ахма́това': '11.07.1889',
            'Шекспир': '26.04.1564',
            'Достоевский': '11.11.1821',
        }
        new_list = []
        for key in writers.keys():
            new_list.append(key)

        answers_writers = random.sample(new_list, 5)
        entered_correctly = 0
        entered_incorrectly = 0

        for wr in answers_writers:
            answer = input(f'Когда родился {wr} , введите в формате  dd.mm.yyyy\n')
            if answer == writers[wr]:
                print('Верно')
                entered_correctly += 1
            else:
                entered_incorrectly += 1
                print('Не верно')

        print(f'Верных ответов: {entered_correctly}\nНеверных ответов: {entered_incorrectly}')
        i += 1
        if i < party:
            print('Начинается новая партия')
        else:
            print('Конец игры')



