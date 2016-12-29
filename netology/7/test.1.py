def input_yaml():
    import yaml
    from pprint import pprint

    file_name = 'yaml.yaml'
    with open(file_name) as file:
        countries = yaml.load(file, Loader = yaml.Loader)
        pprint(countries)
        
    return countries
    
input_yaml()