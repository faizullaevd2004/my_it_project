skills=['Python', 'JavaScript', 'SQL', 'HTML/CSS']
print("Мои навыки: на прокачку")
for skill in skills:
    print(f'изучаю {skill}')

user_profile={
    'name': 'Daniyar',
    'age': 22,
    'specialty': 'information systems',
    'gpa': 3.36,
    'taret_jot':'Jonior Python Developer',
}
print('Профиль пользователя:')
print(f'Имя: {user_profile["name"]}')
print(f'Возраст: {user_profile["age"]}')
print(f'Специальность: {user_profile["specialty"]}')
print(f'Средний балл: {user_profile["gpa"]}')
print(f'Целевая должность: {user_profile["taret_jot"]}')

