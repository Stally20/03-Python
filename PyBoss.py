#Bring in operating system and csv reader/writer
import os
import csv

#Read in the two files
empdata1 = os.path.join("employee_data_1.csv")
empdata2 = os.path.join("employee_data_2.csv")

#Set import/output files
files = [empdata1, empdata2]
new_emp_file = 'new_employee_record.csv'

#Create lists to hold employee data
emp_id = []
first = []
last = []
bday = []
ssn = []
state = []

#Create state abbreviation dictionary
state_abr = {'Alabama':'AL', 'Alaska':'AK', 'Arizona':'AZ', 'Arkansas':'AR', 'California':'CA',
			 'Colorado':'CO', 'Connecticut':'CT', 'Delaware':'DE', 'Florida':'FL', 'Georgia':'GA',
			 'Hawaii':'HI', "Hawai'i":'HI', 'Idaho':'ID', 'Illinois':'IL', 'Indiana':'IN', 'Iowa':'IA',
			 'Kansas':'KS', 'Kentucky':'KY', 'Louisiana':'LA', 'Maine':'ME', 'Maryland':'MD', 
			 'Massachusetts':'MA', 'Michigan':'MI', 'Minnesota':'MN', 'Mississippi':'MS', 'Missouri':'MO',
			 'Montana':'MT', 'Nebraska':'NE', 'Nevada':'NV', 'New Hampshire':'NH', 'New Jersey':'NJ',
			 'New Mexico':'NM', 'New York':'NY', 'North Carolina':'NC', 'North Dakota':'ND', 'Ohio':'OH',
			 'Oklahoma':'OK', 'Oregon':'OR', 'Pennsylvania':'PA', 'Rhode Island':'RI',
			 'South Carolina':'SC', 'South Dakota':'SD', 'Tennessee':'TN', 'Texas':'TX', 'Utah':'UT',
			 'Vermont':'VT', 'Virginia':'VA', 'Washington':'WA', 'West Virginia':'WV', 'Wisconsin':'WI',
			 'Wyoming':'WY'}

#Read in and append the files
with open (files, newline='') as csv:
	next(csv)

	#For loop through files
	for row in csv:

		#ID to list
		emp_id.append(row[0])

		#Split names to first and last list
		name = row[1].split(' ')
		first.append(name[0])
		last.append(name[1])

		#DOB split and format to list
		DOB = row[2].split('-')
		bday.append(str(DOB[1]) + '/' + str(DOB[2]) + '/' + str(DOB[0]))

		#SSN split and format to list
		split_ssn = row[3].split('-')
		ssn.append('***-**' + (str(split_ssn[2])))

		#State swap to list
		state.append(state_abr[row[4]])

#Put files in csv format		


#Write the output file
with open (new_emp_file, 'w') as output:
	output.write('Emp ID,First Name,Last Name,DOB,SSN,State')

