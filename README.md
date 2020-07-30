# Gentrack-exercise

## What was done
This solution reads in a XML file and generates CSV files corresponding to its CSVIntervalData element. 

### Usage
1. solution.py can be run with any appropriately formatted XML file, simply change the filename in the main method.
2. tests.py can then be used to verify the correctness of the generated CSV files. Once again, simply change the filename in the main method. 

## What wasn't done
I assumed that the header and trailer would always be at the first and last indices of the data, but I could have 
explicitly looped through to find rows that begin with 100 and 900. This may make the code more reliable by picking 
up possible formatting errors in the XML file.

## What would be done with more time
More comprehensive testing, i.e. checking the block of data against more test files. Currently my tests only check that the 
correct number of CSV files were generated, and that they have the expected names, headers and trailers.

