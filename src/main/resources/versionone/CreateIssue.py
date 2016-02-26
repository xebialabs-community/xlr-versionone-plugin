#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
import time
from com.versionone.apiclient import V1Connector
from com.versionone.apiclient import Services

if versionOneServer is None:
    print "No VersionOne server provided."
    sys.exit(1)

conn = V1Connector()
connector = conn.withInstanceUrl(versionOneServer['instanceUrl']).withUserAgentHeader("XL Release", str(time.time())).withAccessToken(versionOneServer['accessToken']).build()
services = Services(connector)

print "Received projectId ", projectId
project_id = services.getOid(projectId)
story_type = services.getMeta().getAssetType(assetType)
new_story = services.createNew(story_type, project_id)

for key, value in attributes.iteritems():
    name_attribute = story_type.getAttributeDefinition(key)
    new_story.setAttributeValue(name_attribute, value)

services.save(new_story)

token = new_story.getOid().getToken()

print "Story: [%s]\n" % token
for key, value in attributes.iteritems():
    print "Attribute key [%s] with value [%s]\n" % (key,new_story.getAttribute(story_type.getAttributeDefinition(key)).getValue())