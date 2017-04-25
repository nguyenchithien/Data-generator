import random

# Words to derive email addresses from
animals = []
adjectives = []

# Dumb host names
hosts = [ "chainMAIL", "corNET", "garNET", "sonNET", "plaNET", "telekiNETic", "cobWEB", "spiderWEB" ]

# tlds
tlds = [ ".com", ".net", ".edu", ".co.uk", ".info" ]

used = []

def ReadFiles():
	with( open( "../data-animals.txt" ) ) as fileHandle:
		lines = fileHandle.readlines()
	
	for line in lines:
		line = line.strip('\n').replace( ' ', '-' ).lower()
		animals.append( line )
		
	with( open( "../data-adjectives.txt" ) ) as fileHandle:
		lines = fileHandle.readlines()
	
	for line in lines:
		line = line.strip('\n').replace( ' ', '-' ).lower()
		adjectives.append( line )

def GetRandomEmail():
	a = random.choice( adjectives ) + "-" + random.choice( animals ) + "-" + str( random.randint( 0, 3000 ) )
	b = random.choice( hosts )
	c = random.choice( tlds )
	
	email = a + "@" + b + c
	
	while ( email in used ):
		a = random.choice( adjectives ) + "-" + random.choice( animals ) + "-" + str( random.randint( 0, 3000 ) )
		b = random.choice( hosts )
		c = random.choice( tlds )
		
		email = a + "@" + b + c
	
	used.append( email )

	return email

ReadFiles()

# Create list

itemCount = input( "How many items? " )

out = open( "emails.txt", "wb" )

for i in range( 0, itemCount ):
    print( "Getting item " + str( i ) + "/" + str( itemCount ) )
    out.write( GetRandomEmail() + "\n" )
    
out.close()
