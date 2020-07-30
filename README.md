# Gentrack-exercise

## What was done
This solution reads in a XML file and generates CSV files corresponding to its CSVIntervalData element.

## What wasn't done
I assumed that the header and trailer would always be at the first and last indices of the data, but I could have 
explicitly looped through to find rows that begin with 100 and 900, which may make the code more reliable.

## What would be done with more time
More comprehensive testing, i.e. checking the block of data. Currently my tests only check that the 
correct number of CSV files were generated, and that they have the expected names, headers and trailers.
