from datetime import datetime as dt


def complex_calc_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{time};комплексные числа;{data}\n')

def rational_calc_logger(data):
    time = dt.now().strftime('%H:%M')
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'{time};рациональные числа;{data}\n')

def view_logger():
    with open('log.txt', 'r', encoding='utf-8') as file:
        txt = file.read()
    return txt