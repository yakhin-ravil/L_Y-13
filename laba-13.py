#Определить суммарную стоимость билетов взрослых(=>18) , севших в порту Квинстаун, в возрастном интервале мода ± 10 позиций 

import csv
from statistics import mode

# Открываем csv файл
with open('titanic.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Создаем списки для хранения нужных данных
    ticket_costs = []
    ages = []
    
    # Читаем данные из файла и заполняем списки
    for row in reader:        
        if row["Embarked"] == "Q" and row["Age"]!="" and float(row['Age']) >= 18 and row["Fare"]!='':
            age = float(row['Age'])
            ages.append(age)
            ticket_cost = float(row['Fare'])
            ticket_costs.append(ticket_cost)

    # Находим моду возраста пассажиров
    age_mode = mode(ages)
    
    # Создаем возрастной интервал
    lower_limit = age_mode - 10
    upper_limit = age_mode + 10
    
    # Фильтруем билеты в нужном возрастном интервале
    filtered_ticket_costs = [cost for cost, age in zip(ticket_costs, ages) if lower_limit <= age <= upper_limit]

    # Находим суммарную стоимость билетов
    total_ticket_cost = sum(filtered_ticket_costs)

    # Выводим результат
    print(f"Мода = {age_mode}\nСуммарная стоимость билетов взрослых в порту Квинстауна в возрастном интервале мода ± 10 позиций:", round(total_ticket_cost, 4))