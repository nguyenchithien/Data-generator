import random

# fields
names = []
emails = []
companies = []
jobTitles = []

def ReadFiles():
	with( open( "names/names.txt" ) ) as fileHandle:
		lines = fileHandle.readlines()
	
	for line in lines:
		line = line.strip('\n').replace( ' ', '-' ).lower()
		names.append( line )
		
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
	return random.choice( names ) + " " + random.choice( names ) + "\n\t" + random.choice( companies ) + "\n\t" + random.choice( jobTitles ) + "\n\t" + random.choice( emails ) + "\n"
	
	
ReadFiles()

# Create list

itemCount = input( "How many items? " )

out = open( "employee-list.txt", "wb" )

for i in range( 0, itemCount ):
    print( "Getting item " + str( i ) + "/" + str( itemCount ) )
    out.write( GetRandomItem() + "\n" )
    
out.close()
