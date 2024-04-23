month_number = input("Введите номер месяца (например, 9): ") 
 
if month_number.isdigit(): 
    month_number = int(month_number) 
    if month_number >= 1 and month_number <= 12: 
        months = ["январь", "февраль", "март", "апрель", "май", "июнь", 
                  "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"] 
        month_name = months[month_number - 1] 
        print("Месяц: " + month_name) 
    else: 
        print("Ошибка ввода данных") 
else: 
    print("Ошибка ввода данных")