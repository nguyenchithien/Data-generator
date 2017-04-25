import random

# Words to derive from
fields = []
titles = []


def ReadFiles():
	with( open( "../data-study-fields.txt" ) ) as fileHandle:
		lines = fileHandle.readlines()
	
	for line in lines:
		line = line.strip('\n').replace( ' ', '-' ).lower()
		fields.append( line )
		
	with( open( "../data-job-titles.txt" ) ) as fileHandle:
		lines = fileHandle.readlines()
	
	for line in lines:
		line = line.strip('\n').replace( ' ', '-' ).lower()
		titles.append( line )

def GetRandomItem():
	return random.choice( fields ) + "-" + random.choice( titles )

ReadFiles()

# Create list

itemCount = input( "How many items? " )

out = open( "job-titles.txt", "wb" )

for i in range( 0, itemCount ):
    print( "Getting item " + str( i ) + "/" + str( itemCount ) )
    out.write( GetRandomItem() + "\n" )
    
out.close()
