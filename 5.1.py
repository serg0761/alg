#Пользователь вводит данные о количестве предприятий, их наименования
# и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

#! Ничего не сказано про компании с годовой прибылью равной среднему. 
# Отнес их к "хорошим".

from collections import namedtuple

numbers_of_company = int(input('Введите количество компаний: '))
if numbers_of_company == 0:
    print('Работникам ПВО большой привет!')
else:
    companies = []
    full_summ = 0
    company = namedtuple('company','name, years_profit')
    
    for i in range(numbers_of_company):
        company_name = (str(input(f'Введите название компании {i + 1}:')))
        year_summ = quarter_summ = 0
        for i in range(4):
            quarter_profit = int(input(
                    f'Введите ее прибыль за {i + 1} квартал: '))
            year_summ += quarter_profit
            full_summ += quarter_profit
        companies.append(company(company_name, year_summ))
    average_summ = full_summ / numbers_of_company
    
    good_company = []
    bad_company = []
    
    for comp in companies:
        if comp.years_profit >= average_summ:
            good_company.append(comp.name)
        else:
            bad_company.append(comp.name)
    
    print('Средняя сумма составила:', int(average_summ))
    print('Компании с прибылью выше среднего:')
    print(*good_company, sep=', ')
    print('Koмпании с прибылью ниже среднего:')
    print(*bad_company, sep=', ')