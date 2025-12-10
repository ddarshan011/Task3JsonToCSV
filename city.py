import requests
import json
import csv

def indian_cities():
    url = "https://github.com//fayazara//Indian-Cities-API//raw//master//cities.json"

    response = requests.get(url)
    data = response.json()
    # print(data)


    # data format received is json format like in dictionary and list
    # {
    #     cities = [
    #         {dict}
    #     ]
    # }
    
    if isinstance(data, dict):
        # the common keys that have the cities list
        cities_list = data.get('cities') #getting list from dict
        if isinstance(cities_list, list):
            data = cities_list  # Now data is the list we need
        else:
            print("No cities list found in dict. Keys:", list(data.keys()))
            return []

    cities = []
    for city in data:  # Now it's guaranteed to be a list
        cities.append({
            'city': city.get('City', 'N/A'),
            'state': city.get('State', 'N/A'),
            'district': city.get('District', 'N/A')
        })
    
    filename = 'indian_cities.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['city', 'state', 'district']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cities)
        print(f"Saved {len(cities)} cities to {filename}")

        return cities

cities_list = indian_cities()