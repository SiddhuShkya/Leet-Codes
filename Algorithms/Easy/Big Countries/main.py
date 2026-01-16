import pandas as pd

def big_countries(world):
    filtered_countries = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    result = filtered_countries[['name', 'population', 'area']]
    return result