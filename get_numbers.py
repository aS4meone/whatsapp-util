import pandas as pd

df = pd.read_excel('vapess_kazakhstan.xlsx')
print('загрузка данных')

df_filtered = df[df['Телефон 1'].apply(lambda x: len(str(x)) > 5)]
print('фильтрация')

df_unique = df_filtered.drop_duplicates(subset='Наименование')
print('удаление дубликатов')

phone_numbers = []
for index, row in df_unique.iterrows():
    phone_number = str(row['Телефон 1'])[:11]
    print(row['Наименование'], phone_number)
    phone_numbers.append(phone_number)


# Сохраняем номера телефонов в текстовый файл
with open('phone_numbers.txt', 'w') as file:
    print('saved as phone_numbers.txt')
    for number in phone_numbers:
        file.write(number + '\n')
