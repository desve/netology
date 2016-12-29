def input_json():
    import json
    from pprint import pprint

    file_name = 'json.json'
    with open(file_name) as file:
        countries = json.load(file)
        pprint(countries)
        
    return countries
