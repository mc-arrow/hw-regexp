from pprint import pprint
import re
import csv

with open("phonebook_raw.csv",  encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

transformed_data = []

for item in contacts_list:
  name_parts = ' '.join(item[:3]).split(' ')
  for i in name_parts:
    if i == '':
      name_parts.remove(i)
  for j in name_parts:
    if len(name_parts) > 3:
      name_parts.pop()
  # print(name_parts)
  transformed_item = name_parts + item[3:]
  transformed_data.append(transformed_item)
  
unique_names ={}

for names in transformed_data[1:]:
  key = (names[0], names[1])
  if key not in unique_names:
    unique_names[key] = names
  else:
    for i in range(2, len(names)):
      if names[i] != '':
        unique_names[key][i] = names[i]
data = list(unique_names.values())
data.insert(0, contacts_list[0])

phone_pattern = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
phone_substitution = r'+7(\2)\3-\4-\5\7\8\9'
for column in data:
    column[5] = phone_pattern.sub(phone_substitution, column[5])

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(data)

  print('Данные сохранены в файл phonebook.csv')