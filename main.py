# users - это список пользователей, где каждый пользователь - это словарь.
# Нужно вернуть список имен пользователей, которым больше 18 лет.

def get_adult_users_names(users_data):
    
    names_list = []
    
    for user in users_data:
        # Проверяем, есть ли ключ 'age' и больше ли он 18
        if 'age' in user and user['age'] > 18:
            names_list.append(user['name'])
            
    return names_list

# Пример данных для проверки
all_users = [
    {'name': 'Иван', 'age': 25},
    {'name': 'Мария', 'age': 17},
    {'name': 'Петр', 'age': 32},
    {'name': 'Анна'} # У этого пользователя нет ключа 'age'
]

adult_names = get_adult_users_names(all_users)
print(f"Имена совершеннолетних пользователей: {adult_names}")

# правка для ПР
