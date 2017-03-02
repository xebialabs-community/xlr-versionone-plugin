#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
import sys, traceback
from versionone.VersionOneClient import VersionOneClient

try:
   data = {}
   v1Client = VersionOneClient.create_v1Client( versionOneServer )
   v1Client.updateStoryStatus( ticket, status )
   whereClause="Number='%s'" % ticket
   results = v1Client.getStories( whereClause )
   asset = results['Assets'][0]
   data['Name'] = asset['Attributes']['Name']['value']
   data['Number'] = asset['Attributes']['Number']['value']
   data['Status'] = asset['Attributes']['Status.Name']['value']
   print data
except :
   traceback.print_exc(file=sys.stdout)
   sys.exit(1)
   # End try