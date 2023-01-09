import xml.etree.ElementTree as ET

name = '''<xml>
            <persons>
                <person>
                    <name>dhrumil</name>
                    <rollno unit="num">10</rollno>
                </person>
                <person>
                    <name>dhruv</name>
                    <rollno unit="num">7</rollno>
                </person>
            </persons>
          </xml>  
       '''
tree = ET.fromstring(name)
lst = tree.findall('persons/person')
for item in lst:
    print('Name is:', item.find('name').text)
    print('ROll no is:', item.find('rollno').text)
    print('attribute is:', item.find('rollno').get('unit'))
    


