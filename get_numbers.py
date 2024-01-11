import pandas as pd

file_name = 'phone_numbers.txt'

df = pd.read_excel('vapess_kazakhstan.xlsx')

total_numbers_before = len(df)

df_filtered = df[df['Телефон 1'].apply(lambda x: len(str(x)) > 5)].copy()

df_filtered.loc[:, 'Телефон 1'] = df_filtered['Телефон 1'].astype(str).str[:11]

df_unique_phones = df_filtered.drop_duplicates(subset='Телефон 1')
unique_numbers_count = len(df_unique_phones)

unique_phone_numbers = df_unique_phones['Телефон 1'].tolist()

with open(f'{file_name}', 'w') as file:
    for number in unique_phone_numbers:
        file.write(number + '\n')

print(f'Сохранено как {file_name}.txt')
print("Номеров -", total_numbers_before)
print("Уникальных - ", unique_numbers_count)
