#
# Copyright 2019 XEBIALABS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

import com.xhaus.jyson.JysonCodec as json
from xlrelease.HttpRequest import HttpRequest

STATUS_OK = 200

class VersionOneClient( object ):
   def __init__(self, v1CI ):
      self.Token = v1CI['accessToken']
      self.uriBase = v1CI['uriBase']
      self.storyStatus = v1CI['StoryStatus']
      self.httpConnection = v1CI
      self.httpRequest = HttpRequest( v1CI )
      self.optionHeader = {"Accept" : "application/json",
                           "Authorization" : "Bearer %s" % self.Token}
   # End def

   @staticmethod
   def create_v1Client( v1CI ):
      return VersionOneClient( v1CI )
   # End def
   
   def getStories(self, whereClause=None):
      uri = "%s/rest-1.v1/Data/Story" % self.uriBase
      if whereClause is not None:
         uri = "%s?where=%s" % ( uri, whereClause )
      # End if
      print( "getStories uri = %s" % uri )
      print( "Headers = %s" % self.optionHeader )
      response = self.httpRequest.get( uri, headers=self.optionHeader )
      reqStatus = response.getStatus()
      print( "Request Status %s" % reqStatus )
      if reqStatus == STATUS_OK:
         return json.loads( response.getResponse() )
      # End if
      raise ValueError('Error getting stories', reqStatus )
   # End def
   
   def updateStoryStatus(self, ticket, status):
      whereClause="Number='%s'" % ticket
      data = self.getStories( whereClause )
      uri = data['Assets'][0]['href']
      xml = "<Asset> <Relation name=\"Status\" act=\"set\"> <Asset idref=\"StoryStatus:%s\" /> </Relation> </Asset>" % self.storyStatus[status]
      print( "Update Status uri = %s" % uri )
      print( "Update Status XML ~%s~" % xml )
      print( "Update Status Headers = %s" % self.optionHeader )
      response = self.httpRequest.post( uri, xml, headers=self.optionHeader )
      reqStatus = response.getStatus()
      print( "Request Status %s" % reqStatus )
      if reqStatus == STATUS_OK:
         return
      # End if
      raise ValueError('Error getting stories', reqStatus )
   # End def
   
   def get_story_status_list(self):
      uri = "%s/rest-1.v1/Data/StoryStatus" % self.uriBase
      print( "getStoryStatus uri = %s" % uri )
      print( "Headers = %s" % self.optionHeader )
      response = self.httpRequest.get( uri, headers=self.optionHeader )
      req_status = response.getStatus()
      print( "Request Status %s" % req_status )
      if req_status == STATUS_OK:
         return json.loads( response.getResponse() )
      # End if
      raise ValueError('Error getting stories', req_status )
   # End def
# End class
