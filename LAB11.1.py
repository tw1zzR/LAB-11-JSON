import csv

with open('temperatures.csv', 'r') as file:
    reader = csv.reader(file, delimiter=';')
    temperatures = list(reader)

print("Дані про температуру повітря за Січень:")
for row in temperatures:
    print(row)

temperatures_data = []
for row in temperatures[1:]:
    day = int(row[0])
    temperature = int(row[1].strip())
    temperatures_data.append((day, temperature))

max_temp_day = max(temperatures_data, key=lambda x: x[1])
min_temp_day = min(temperatures_data, key=lambda x: x[1])

print(f"\nДень с найбільшою температурою: День {max_temp_day[0]}, Температура {max_temp_day[1]}°C")
print(f"День с наймешною температурою: День {min_temp_day[0]}, Температура {min_temp_day[1]}°C")
