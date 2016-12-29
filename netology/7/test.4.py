def input_xml():
    import xml.etree.ElementTree as ET
    from pprint import pprint
    file_name = 'xml.xml'
    tree = ET.parse(file_name)
    root = tree.getroot() 
    countriies = []
    for line_1 in root:
        countriies.append(line_1.tag)
        
    keys = []
    info = []
    number_keys = len(line_1)
    for line_2 in range(number_keys):
        keys.append(line_1[line_2].tag)
        info.append(line_1[line_2].text)
        
#        info = line_1[line_2].tag
#        print(line_1[line_2].text)
#        print('info=', info)
        
#    info = []
#    for line_3 in range(len(line_1[line_2])):
#        info.append(line_2[line_3].tag)
  
    print(countriies)
    print(keys)
    print(info)



      

     


input_xml()
