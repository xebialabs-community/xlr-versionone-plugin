#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
import sys, traceback
from versionone.VersionOneClient import VersionOneClient

try:
   v1Client = VersionOneClient.create_v1Client( versionOneServer )
   results = v1Client.getStories( whereClause )
   assets = results['Assets']
   data = {}
   for asset in assets:
      print( asset )
      print( asset['Attributes']['Name'] )
      assetName   = asset['Attributes']['Name']['value']
      print( asset['Attributes']['Number'] )
      assetNumber = asset['Attributes']['Number']['value']
      print( asset['Attributes']['Status.Name'] )
      assetStatus = asset['Attributes']['Status.Name']['value']
      data[assetNumber] = "%s | %s " % (assetName, assetStatus )
   # End for
   print( data )

except :
   traceback.print_exc(file=sys.stdout)
   sys.exit(1)
   # End try