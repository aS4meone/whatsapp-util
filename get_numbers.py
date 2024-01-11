import pandas as pd

file_name_phone = 'phone_numbers.txt'
file_name_whatsapp = 'whatsapp_numbers.txt'

excel_file = input("Введите название Excel файла: ")

df = pd.read_excel(excel_file)

total_numbers_before = len(df)

df_filtered = df[df['Телефон 1'].apply(lambda x: len(str(x)) > 5)].copy()
df_filtered.loc[:, 'Телефон 1'] = df_filtered['Телефон 1'].astype(str).str[:11]
df_unique_phones = df_filtered.drop_duplicates(subset='Телефон 1')
unique_numbers_count = len(df_unique_phones)

df['WhatsApp 1'] = df['WhatsApp 1'].astype(str)
df_whatsapp = df[df['WhatsApp 1'].str.startswith('https://wa.me/')].copy()
df_whatsapp.loc[:, 'WhatsApp 1'] = df_whatsapp['WhatsApp 1'].str.replace('https://wa.me/', '', regex=False)
df_whatsapp_unique = df_whatsapp.drop_duplicates(subset='WhatsApp 1')

with open(file_name_phone, 'w') as file:
    for number in df_unique_phones['Телефон 1']:
        file.write(number + '\n')

with open(file_name_whatsapp, 'w') as file:
    for number in df_whatsapp_unique['WhatsApp 1']:
        file.write(number + '\n')

print(f'Сохранено обычные номера в {file_name_phone} и WhatsApp номера в {file_name_whatsapp}')
print("Всего номеров -", total_numbers_before)
print("Уникальных обычных номеров - ", unique_numbers_count)
print("Уникальных WhatsApp номеров - ", len(df_whatsapp_unique))
