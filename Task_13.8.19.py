number_of_tickets = int(input('Укажите, сколько билетов нужно: '))

ages_visitor = []
prise_ticket = 0

for i in range(1, number_of_tickets + 1):
    input_value = int(input(f'Введите возраст участника №{i}:\n'))
    ages_visitor.append(input_value)

for i in ages_visitor:
    if i >= 18 and i < 25:
        prise_ticket += 990
    elif i > 25:
        prise_ticket += 1390

if number_of_tickets > 3:
    prise_ticket = prise_ticket * 0.90

print('Стоимость билетов на', number_of_tickets, 'человек составит - ', prise_ticket, 'руб.')

