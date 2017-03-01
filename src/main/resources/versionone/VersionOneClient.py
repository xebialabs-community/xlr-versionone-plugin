#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#
import sys, traceback
import com.xhaus.jyson.JysonCodec as json
from xlrelease.HttpRequest import HttpRequest

STATUS_OK = 200

class VersionOneClient( object ):
   def __init__(self, v1CI ):
      self.Token = v1CI['accessToken']
      self.uriBase = v1CI['uriBase']
      self.httpConnection = v1CI
      self.httpRequest = HttpRequest( v1CI )
   # End def
      
   @staticmethod
   def create_v1Client( v1CI ):
      return VersionOneClient( v1CI )
   # End def
   
   def getStories(self, whereClause=None):
      data = {"data" : "FAIL"}
      uri = "%s/rest-1.v1/Data/Story" % self.uriBase
      optionHeader = {"Accept" : "application/json",
                      "Authorization" : "Bearer %s" % self.Token}
      #if whereClause is not None:
      #   uri = "%s&%s" % ( uri, whereClause )
      # End if
      print "getStories uri = %s" % uri
      print "Headers = %s" % optionHeader
      response = self.httpRequest.get( uri, headers=optionHeader )
      reqStatus = response.getStatus()
      print "Request Status %s" % reqStatus
      if reqStatus == STATUS_OK:
         return json.loads( response.getResponse() )
      # End if
      raise ValueError('Error getting stories', reqStatus )
   # End def
# End class
