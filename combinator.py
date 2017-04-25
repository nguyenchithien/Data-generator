import random

# fields
givennames = []
surnames = []
emails = []
companies = []
jobTitles = []

usedNames = []
usedEmails = []

counter = 0

def ReadFiles():
	with( open( "NameDatabases/NamesDatabases/first names/all.txt" ) ) as fileHandle:
		lines = fileHandle.readlines()
	
	for line in lines:
		line = line.strip('\n').replace( ' ', '-' ).lower()
		givennames.append( line )
		
	
	with( open( "NameDatabases/NamesDatabases/surnames/all.txt" ) ) as fileHandle:
		lines = fileHandle.readlines()
	
	for line in lines:
		line = line.strip('\n').replace( ' ', '-' ).lower()
		surnames.append( line )
		
	with( open( "emails/emails.txt" ) ) as fileHandle:
		lines = fileHandle.readlines()
	
	for line in lines:
		line = line.strip('\n').replace( ' ', '-' ).lower()
		emails.append( line )
		
	with( open( "companies/companies.txt" ) ) as fileHandle:
		lines = fileHandle.readlines()
	
	for line in lines:
		line = line.strip('\n').replace( ' ', '-' ).lower()
		companies.append( line )
		
	with( open( "job-titles/job-titles.txt" ) ) as fileHandle:
		lines = fileHandle.readlines()
	
	for line in lines:
		line = line.strip('\n').replace( ' ', '-' ).lower()
		jobTitles.append( line )

def GetRandomItem():
	# firstname lastname company jobtitle email
	
	# Make it unique
	givenname = random.choice( givennames )
	while ( len( givenname ) == 1 ):
		print( givenname )
		givenname = random.choice( givennames )
	
	surname = random.choice( surnames )
	while( len( surname ) == 1 ):
		print( surname )
		surname = random.choice( surnames )
	
	while ( surname + "-" + givenname in usedNames ):
		givenname = random.choice( givennames )
		while ( givenname is "" ):
			givenname = random.choice( givennames )
		
		surname = random.choice( surnames )
		while( surname is "" ):
			surname = random.choice( surnames )
		
	usedNames.append( surname + "-" + givenname )
	
	
	email = random.choice( emails )
	while ( email in usedEmails ):
		email = random.choice( emails )
	
	usedEmails.append( email )
	
	return givenname + " " + surname + "\n\t" + random.choice( companies ) + "\n\t" + random.choice( jobTitles ) + "\n\t" + email + "\n"
	
	
ReadFiles()

# Create list

itemCount = input( "How many items? " )

out = open( "employee-list.txt", "wb" )

for i in range( 0, itemCount ):
    print( "Getting item " + str( i ) + "/" + str( itemCount ) )
    out.write( GetRandomItem() + "\n" )
    
out.close()
