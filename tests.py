import csv
from solution import parse_XML

def run_tests(file):
    test_data = parse_XML(file) # Gets the CSVIntervalData
    expected_files = [] # Will contain the names of CSVs that should have been generated
    
    for row in test_data:
        row = row.split(',')
        if row[0] == '100':
            expected_header = row
        if row[0] == '200':
            expected_name = row[1]
            expected_files.append(expected_name) 
        if row[0] == '900':
            expected_trailer = row
        
    success = True    
    for filename in expected_files:
        try: 
            with open(filename + '.csv') as file:
                reader = csv.reader(file)
                rows = list(reader)
                if rows[0] != expected_header:
                    print('Header did not match what was expected')
                    success = False
                if rows[-1] != expected_trailer:
                    print('Trailer did not match what was expected')
                    success = False
        except FileNotFoundError:
            print('Expected file missing')
            success = False
        
    if success: 
        print('Tests passed')

    
def main():
    """Verifies that the CSVs were generated with the correct names, headers and trailers
    """
    run_tests('testfile.xml')
    
        
if __name__ == "__main__":
    main()

            
            
