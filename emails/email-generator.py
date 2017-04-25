import random

# Words to derive email addresses from
animals = []
adjectives = []

# Dumb host names
hosts = [ "chainMAIL", "corNET", "garNET", "sonNET", "plaNET", "telekiNETic", "cobWEB", "spiderWEB" ]

# tlds
tlds = [ ".com", ".net", ".edu", ".co.uk", ".info" ]

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
	a = random.choice( adjectives ) + "-" + random.choice( animals )
	b = random.choice( hosts )
	c = random.choice( tlds )

	return a + "@" + b + c

ReadFiles()

# Create list

itemCount = input( "How many items? " )

out = open( "emails.txt", "wb" )

for i in range( 0, itemCount ):
    print( "Getting item " + str( i ) + "/" + str( itemCount ) )
    out.write( GetRandomEmail() + "\n" )
    
out.close()
