# Summary:
# Read tab delimited table and generate sql code needed to insert
# these rows into table

# This program was first created to automate the process of entering data
# into an oracale database. This data was provided as text tables and was
# initially added by manually typing in a series of INSERT commands using SQL.

# This program was written for the type of text files that were provided and for
# my own use. Thus, it does not check for user errors or different file formats.

# I wrote a second program using Java that could be used by others. I used Java
# because other potential users were using Java and it would be easier for them to use.
# I did account for user errors in that version.


# PROGRAM REQUIRES:
# 1. Two arguments:
#	a) Name of table.
# 	b) A list that indicates the type of each column, n for number, t for text type
#
#	So if table is procedure_table, and its three columns are varchar2, char, number
#	The call would be python convert_table_to_sql_code_autoquote.py procedure_table "t,t,n"

#2. A file named table_name+_file.txt that holds data for table.
#	a) It assumes that each column is separate by 1 tab
#	b) It assumes that first row is headings and there is now blank row between
#	heading row and first row of data.
#
#	So if table is procedure_table then program expects to find procedure_table_file.txt


from sys import argv

# Read arguments provided to get table name and types of data in columns
table_name = argv[1]
column_types = argv[2].split(',')

# construct name and path of file with data. Open data file and new file to write SQL script.

#THE FOLDER PATH IS A DUMMY PATH. Update as needed.
folder = 'C:\\Users\\User\\Documents\\Work\\Training\\ACC\\Courses\\1345\\Labs\\tablefiles\\'
file = folder + table_name + '_file.txt'
sql_file = folder + table_name +'_sql.txt'
source = open(file)
target = open(sql_file, 'w')


def break_words(line):
#	This function will break up words for us.

#	Code on hand to deal with files that use different separators
#   words = line.split(' ')
#	words = "','".join(line.split("\t"))

	words = line.split("\t")
	return words

#Text table has numerical and string data. String data must be put into
#quotes to enter into database. This function returns the argument
#in single quotes.
def enquote(string):
	return "'"+string+"'"

	
# read contents of table into WORDS[]	
WORDS = []	
for word in source.readlines():
    WORDS.append(word.strip())	
	
	
#----------------------------------------------------------------------
	
# Determine number of row and columns in table.	
	
no_of_rows = len(WORDS)
current_row = break_words(WORDS[0])
no_of_columns = len(current_row)

#----------------------------------------------------------------------

# Skip row 0 since it has headers

#For each other row
for row in range(1, no_of_rows):

	#Read row and break its contents into an array
	current_row = break_words(WORDS[row])
	
	#Prepare first line for SQL script
	line1_to_write = "insert into "+table_name+" values\n"
	
	#Prepare second line for SQL script by assembling value for
	#different columns of table.
	line2_to_write = "("
	for col in range(0, no_of_columns):
		#Check if column type is text. If so, enquote data.
		if ((column_types[col] == 't') or (column_types[col] == 'T')):
			current_row[col] = enquote(current_row[col])
			
		# For every column after the first,
		#insert a comma before writing its value	
		if col > 0:
			line2_to_write += ","
		line2_to_write += current_row[col]
	line2_to_write += ");\n"
	
	#Lines 1 and 2 are now prepared. Write them to file.
	target.write(line1_to_write)
	target.write(line2_to_write)

#Close files now that the task is done.
target.close()
source.close()

