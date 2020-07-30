import xml.etree.ElementTree as ET

def parse_XML(file):
    """Returns the CSVIntervalData from the provided XML file as a list of strings
    """
    tree = ET.parse('testfile.xml')
    root = tree.getroot()
    for data in root.findall('./Transactions/Transaction/MeterDataNotification/CSVIntervalData'):
        required_data = data.text.strip().split()
 
    return required_data


def process_data(data):
    """Creates a CSV for each block of data that starts with 200
    Each CSV will have the 100 row as a header, and the 900 row as the trailer
    Each CSV will be named from the second field in the 200 row
    """    
    header = data.pop(0)
    trailer = data.pop()
    
    i = 0
    while i < len(data):
        if data[i].split(',')[0] == '200':
            name = data[i].split(',')[1]
            data_block = [header, data[i]] 
            i += 1
            while i < len(data) and data[i].split(',')[0] != '200':
                data_block.append(data[i])
                i += 1   
        data_block.append(trailer)
        create_CSV(name, data_block)


def create_CSV(name, data):
    """Writes a new CSV file
    """
    with open(name + '.csv', 'w') as file:
        for line in data:
            file.write(line + '\n') 
    file.close()


def convertXMLtoCSV(file):
    """Wrapper function for easy use
    """
    required_data = parse_XML(file)
    process_data(required_data)
    
    
def main():
    convertXMLtoCSV('testfile.xml')
    
if __name__ == "__main__":
    main()
    
