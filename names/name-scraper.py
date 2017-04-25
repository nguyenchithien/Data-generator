# http://www.behindthename.com/random/random.php?number=1&gender=both&surname=&all=yes

import urllib2

def GetRandomName():
    url = "http://www.behindthename.com/random/random.php?number=1&gender=both&surname=&all=yes"

    response = urllib2.urlopen( url )
    html = response.read()

    posA = html.find( '<span class="heavyhuge">' ) + 56
    posB = html.find( '</a> </span></p>' )

    text = html[posA:posB]
    posC = text.find( '">' ) + 2
    posD = len( text )
    
    name = text[posC:posD]
    return name

# Create list

nameCount = input( "How many names? " )

out = open( "names.txt", "wb" )

for i in range( 0, nameCount ):
    print( "Getting name " + str( i ) + "/" + str( nameCount ) )
    out.write( GetRandomName() + "\n" )
    
out.close()
