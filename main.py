# Создание словаря со странами и доменными именами
countries = {'Ukraine': 'UA', 'United States': 'US', 'Germany': 'DE', 'France': 'FR', 'Japan': 'JP'}

# Создание словаря со столицами
capitals = {'UA': 'Kiev', 'US': 'Washington D.C.', 'DE': 'Berlin', 'FR': 'Paris', 'JP': 'Tokyo'}

# Добавление элементов в словари
countries['Great Britain'] = 'GB'
capitals['GB'] = 'London'

# Вывод предложений
for country, domain in countries.items():
    print("Домен для {} - {}.".format(country, domain))

for country, capital in capitals.items():
    print("Столица {} - {}.".format(country, capital))

# Объединение предложений
for country, domain in countries.items():
    capital = capitals.get(domain, 'Unknown')
    print("Домен для {} - {}. Столица - {}.".format(country, domain, capital))

# Добавление дополнительных доменов к значениям списка
for key in countries:
    countries[key] = [countries[key], 'COM', 'GOV']

print(countries)
