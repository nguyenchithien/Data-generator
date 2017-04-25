import random

# Words to derive from
buzzA = []
buzzB = []
incorp = [ "LLC", "Inc","Incorporated" ]


def ReadFiles():
	with( open( "../data-buzzwords-adjectives.txt" ) ) as fileHandle:
		lines = fileHandle.readlines()
	
	for line in lines:
		line = line.strip('\n').replace( ' ', '-' ).lower()
		buzzA.append( line )
		
	with( open( "../data-buzzwords-nouns.txt" ) ) as fileHandle:
		lines = fileHandle.readlines()
	
	for line in lines:
		line = line.strip('\n').replace( ' ', '-' ).lower()
		buzzB.append( line )

def GetRandomItem():
	return random.choice( buzzA ) + "-" + random.choice( buzzB ) #+ "-" + random.choice( incorp )

ReadFiles()

# Create list

itemCount = input( "How many items? " )

out = open( "companies.txt", "wb" )

for i in range( 0, itemCount ):
    print( "Getting item " + str( i ) + "/" + str( itemCount ) )
    out.write( GetRandomItem() + "\n" )
    
out.close()
