#
# Copyright 2017 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import sys
from versionone.VersionOneClient import VersionOneClient

try:
    version_one_server = {'url': configuration.url, 'username': configuration.username,
                        'password': configuration.password, 'proxyHost': configuration.proxyHost,
                        'proxyPort': configuration.proxyPort, "accessToken": configuration.accessToken,
                        "uriBase": configuration.uriBase, "StoryStatus": configuration.StoryStatus}
    v1_client = VersionOneClient.create_v1Client(version_one_server)
    results = v1_client.get_story_status_list()
    print results
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
