name='Daniyar'
age=22
savings_otbasy=2000000
deposit=1000000

total_savings = savings_otbasy + deposit

print(f'Привет, меня зовут {name}, мне {age} лет. У меня есть сбережения в размере {total_savings} тенге.')
print('Я планирую потратить часть своих сбережений на покупку квартиры и машины.')

if total_savings >= 2000000:
    print('У меня достаточно сбережений для покупки квартиры и машины.')
else:
    print('Мне нужно накопить больше сбережений, чтобы купить квартиру и машину.')

current_savings=int(input('Введите текущую сумму сбережений(tg): '))
monthly_desopsit=int(input('Введите ежемесячный депозит(tg): '))
target_price=int(input('Введите целевую сумму(tg): '))

months=0
while current_savings < target_price:
    current_savings += monthly_desopsit
    months += 1
    print(f'Месяц {months}: текущие сбережения = {current_savings} тенге')
print('-------------------------------')

print(f'Для достижения целевой суммы вам нужно {months} месяцев. ({round(months/12)} лет)')