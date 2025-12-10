   cities = []
    for city in data:
        cities.append({
            'city': city.get('city', 'N/A'),
            'state': city.get('state', 'N/A'),
            'district': city.get('district', 'N/A')
        })
    
    filename = 'indian_cities.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['city', 'name', 'district']
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(cities)
        print(f"Saved {len.cities} cities to {filename}")

        return cities