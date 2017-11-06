#
# Copyright 2017 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import time
from com.versionone.apiclient import V1Connector
from com.versionone.apiclient import Services

if versionOneServer is None:
    print( "No VersionOne server provided." )
    sys.exit(1)

conn = V1Connector()
connector = conn.withInstanceUrl(versionOneServer['url']).withUserAgentHeader("XL Release", str(time.time())).withAccessToken(versionOneServer['accessToken']).build()
services = Services(connector)

print( "Received projectId ", projectId )
project_id = services.getOid(projectId)
story_type = services.getMeta().getAssetType(assetType)
new_story = services.createNew(story_type, project_id)

for key, value in attributes.iteritems():
    name_attribute = story_type.getAttributeDefinition(key)
    new_story.setAttributeValue(name_attribute, value)

services.save(new_story)

token = new_story.getOid().getToken()

print( "Story: [%s]\n" % token )
for key, value in attributes.iteritems():
    print( "Attribute key [%s] with value [%s]\n" % (key,new_story.getAttribute(story_type.getAttributeDefinition(key)).getValue()) )