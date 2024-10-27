import json

with open('disks.json', 'r') as file:
    disks = json.load(file)

disk_prices = [(disk['name'], disk['price'] / disk['memory']) for disk in disks]
cheapest_disk = min(disk_prices, key=lambda x: x[1])
most_expensive_disk = max(disk_prices, key=lambda x: x[1])

print(f"\nНайвигідніший диск: {cheapest_disk[0]}, Ціна за одиницю ємності: {cheapest_disk[1]:.2f} UAH")
print(f"Найневигідніший диск: {most_expensive_disk[0]}, Ціна за одиницю ємності: {most_expensive_disk[1]:.2f} UAH")
