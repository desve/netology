import xml.etree.ElementTree as etree

"""
N = int(input())

<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
</feed>



"""
xml = "<feed xml:lang='en'><title>HackerRank</title><subtitle lang='en'>Programming challenges</subtitle><link rel='alternate' type='text/html' href='http://hackerrank.com/'/><updated>2013-12-25T12:00:00</updated></feed>"

"""
for line in range(N):
    xml += str(input()).lstrip()

print(xml)
"""
tree = etree.ElementTree(etree.fromstring(xml))

count = 0
#count = len(root.attrib)
for element in tree.getroot().iter():
    print(element)
    print(element.attrib)
    
    count += len(element.attrib)
print(count)




       

    


