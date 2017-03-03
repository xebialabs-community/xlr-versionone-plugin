#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
import sys, traceback
from versionone.VersionOneClient import VersionOneClient

try:
   versionOneServer = { 'url': configuration.url, 'username' : configuration.username, 'password': configuration.password,  'proxyHost': configuration.proxyHost, 'proxyPort': configuration.proxyPort, "accessToken": configuration.accessToken, "uriBase": configuration.uriBase, "StoryStatus": configuration.StoryStatus }
   v1Client = VersionOneClient.create_v1Client( versionOneServer )
   results = v1Client.getStoryStatusList()
   print results
except :
   traceback.print_exc(file=sys.stdout)
   sys.exit(1)
   # End try