from urllib import urlopen

# Programming challenge: find largest path/sum by adding numbers
# as you traverse a triangle of numbers from top to bottom.

# Summary:
# Read triangle of text and create matrix of numbers.
# Each row of matrix holds corresponding lines of triangle.
# For example, below is the matrix for a 4 row triangle.
#
# Row 0: 5
# Row 1: 9 6
# Row 2: 4 6 8
# Row 3: 0 7 1 5
#
# Parse matrix going across each row left to right. 
# Each element in row 1 and below has at least 1 parent in row above.
# For each element, add value of largest parent to current value.
# This way, each element stores largest total through it from top down.
# Largest value in last row will give max total from top to bottom.

#----------------------------------------------------------------------
# Read text file containing numbers triangle and break it into
# 1-D array with elements that represent lines of characters.

WORD_URL = "https://github.com/waqargithub/pythonPrograms/blob/master/largeNumberTriangle.txt"
WORDS = []

for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())
	
def break_words(line):
#   """This function will break up words for us."""
    words = line.split(' ')
    return words
#----------------------------------------------------------------------
	
# Determine number of lines in triangle.	
	
triangle_height = len(WORDS)

#----------------------------------------------------------------------

# Store lines of characters into 2-D matrix.
# Each number in triangle can now be accessed by row and column.

matrix = [[0 for x in xrange(triangle_height)] for x in xrange(triangle_height)] 

node_count = 0

for row in range(0, triangle_height):
	each_line = break_words(WORDS[row])
	for col in range(0, len(each_line)):
		matrix[row][col] = int(each_line[col])
		
#----------------------------------------------------------------------

# Parse rows of matrix, adding largest parent to each element. 
# Skip row 0 since it has no parents. 
# Iterate for rows 1 through 2nd last row.
# Parse last row separately to avoid unnecessarily checking for
# last row in all rows before it. This optimization may be omitted in
# favor of readability since performance is O(n) either way.
# For larger triangle sizes this optimization might matter.

for row in range(1, triangle_height-1):

#-----------------------------------

	# col 0 is leftmost column.
	# It only has right parent, which is matrix[row-1][col].
	# Add this value to current element.
	# Treating col 0 separately outside of for-loop
	# avoids unnecessary execution of if statement that would
	# otherwise be needed to check for col 0 in all other columns.
	
	col = 0
	matrix[row][col] += matrix[row-1][col]
	node_count += 1
	
#-----------------------------------
	
	# For all columns between and except the leftmost and rightmost:
	# Find left parent and right parent.
	
	for col in range(1, row):
	
		left_parent = matrix[row-1][col-1]				
		right_parent = matrix[row-1][col]
					
		# Determine largest parent, add to current element's value.
		if (left_parent > right_parent):
			matrix[row][col] += left_parent
			node_count += 1		
		else:
			matrix[row][col] += right_parent
			node_count += 1


#-----------------------------------

	# col = row is rightmost column.
	# It only has left parent, which is matrix[row-1][col-1].
	# Add this value to current element.
	# Treating last column separately outside of for-loop
	# avoids unnecessary execution of if statement that would
	# otherwise be needed to check for last column in all other columns.	
	
	col = row
	matrix[row][col] += matrix[row-1][col-1]
	node_count += 1
	

#--------------------------------------------------
	
# Parse last row: add values from larger parent to each element.
# Use max_total to track largest value in last row.

row = triangle_height - 1

#-----------------------------------

# col 0 is leftmost column.
# It only has right parent, which is matrix[row-1][col].
# Add this value to current element.
# Treating col 0 separately outside of for-loop
# avoids unnecessary execution of if statement that would
# otherwise be needed to check for col 0 in all other columns.

col = 0
matrix[row][col] += matrix[row-1][col]
node_count += 1

	
# Variable max_total stores largest total from top to bottom.
# Set it to first column of last row since it is first and so
# far the largest value in the last row.

max_total = matrix[row][col]

#-----------------------------------
	
# For all columns between and except the leftmost and rightmost:
# Find left parent and right parent.
for col in range(1, row):
	
	left_parent = matrix[row-1][col-1]				
	right_parent = matrix[row-1][col]
					
	# Determine largest parent, add to current element's value.
	if (left_parent > right_parent):
		matrix[row][col] += left_parent
		node_count += 1
	else:
		matrix[row][col] += right_parent
		node_count += 1

	# Update max_total if current element's value > current max_total.
	if (matrix[row][col] > max_total):
		max_total = matrix[row][col]	

#-----------------------------------				
				
# col = row is rightmost column.
# It only has left parent, which is matrix[row-1][col-1].
# Add this value to current element.
# Treating last column separately outside of for-loop
# avoids unnecessary execution of if statement that would
# otherwise be needed to check for last column in all other columns.
	
col = row
matrix[row][col] += matrix[row-1][col-1]	
node_count += 1


#-----------------------------------
	
#Check if value of last element > max_total. Update max_total if so.
if (matrix[row][col] > max_total):
	max_total = matrix[row][col]

#----------------------------------------------------------------------		
	
print "The maximum total from top to bottom in the given triangle of numbers is: ", max_total
print "Node count is: ", 	node_count
