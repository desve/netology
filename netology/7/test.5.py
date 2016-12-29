def input_xml():
    import xml.etree.ElementTree as ET
    from pprint import pprint
    file_name = 'xml.xml'
    tree = ET.parse(file_name)
    root = tree.getroot() 
    countriies = {}
    for countriy in root:
        number_keys = len(countriy)
#        countriies.append(countriy.tag)     
        keys = []
        info = []
        for key in range(number_keys):
            keys.append(countriy[key].tag)
            info.append(countriy[key].text)
            countriy_info = dict(zip(keys, info))
#        print(countriy_info)
            countriies[countriy.tag] = countriy_info
  
    pprint(countriies)
    print(keys)
    print(info)

input_xml()
