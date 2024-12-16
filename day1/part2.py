# Open and Read from the file
arrayOfFirstColumn = []
arrayOfSecondColumn = []

# Open the file and read each line
with open('data.txt', 'r') as file:
    for line in file:
        # Split the line into two numbers
        num1, num2 = map(int, line.split())
        # Add the numbers to the respective arrays
        arrayOfFirstColumn.append(num1)
        arrayOfSecondColumn.append(num2)

# Sort the rows
arrayOfFirstColumn.sort()
arrayOfSecondColumn.sort()

# Sum the values
similarityScore  = 0
for firstColumnNumber in arrayOfFirstColumn:
    
    occurances = arrayOfSecondColumn.count(firstColumnNumber)
    similarityScore = similarityScore + (occurances * firstColumnNumber)


print(f'The distance is: {similarityScore}')






