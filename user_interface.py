import logger as log
import complex_calc as cc
import rational_calc as rc
from easygui import *


def complex_view():
    data = enterbox(
        msg='Вы находитесь в меню расчета комплексных чисел.\nВведите выражение: ')
    msgbox(msg=f'Ответ: {cc.do_it(data)}')
    log.complex_calc_logger(data)
    return data


def rational_view():
    a, b = enterbox('Введите первое число: '), enterbox(
        'Введите второе число: ')
    c = enterbox('Введите знак + - * /: ')
    data = rc.do_it(a, b, c)
    msgbox(f'Ответ: {data}')
    log.rational_calc_logger(data)


def menu():
    number = integerbox(
        'Вас приветствует калькулятор комплексных и рациональных чисел! =)\n'
        '---------------------------------------------\n'
        'Варианты работы программы:\n'
        '1. Вычисление комплексных чисел\n'
        '2. Вычисление рациональных чисел\n'
        '3. Вывод лога работы программы\n'
        '4. Выход из программы\n'
        'Для перехода в конкретное меню нажмите соответствующую цифру, указанную напротив названия меню\n'
        'Введите номер: ')
    if number == 1:
        complex_view()
        ch = ["Назад", "Назад в главное меню", "Выход"]
        action = buttonbox("Выберите действие:", choices=ch)
        if action == "Назад":
            complex_view()
        elif action == "Назад в главное меню":
            menu()
        else:
            exit()
    if number == 2:
        rational_view()
        ch = ["Назад", "Назад в главное меню", "Выход"]
        action = buttonbox("Выберите действие:", choices=ch)
        if action == "Назад":
            complex_view()
        elif action == "Назад в главное меню":
            menu()
        else:
            exit()
    if number == 3:
        msgbox(log.view_logger())
        ch = ["Назад", "Назад в главное меню", "Выход"]
        action = buttonbox("Выберите действие:", choices=ch)
        if action == "Назад":
            complex_view()
        elif action == "Назад в главное меню":
            menu()
        else:
            exit()
    if number == 4:
        exit()


menu()
