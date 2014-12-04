#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#


import sys, string
import com.xhaus.jyson.JysonCodec as json
import sys
sys.path.append("/Applications/Aptana Studio 3/plugins/org.python.pydev_3.0.0.1388187472/pysrc")
#import pydevd
import urllib

# input variables: auth_code, client_id, client_secret, v1url, v1title, grant_type, redirect_uri, scope, xlruser, xlrpassword

def refreshToken(str):
 print "this is refreshToken function"
 sys.exit(1)

def newConfig():
    print "this is newconfig function"
    ########
    # try to get the access and refresh tokens, if successful then create a configuration storing them.

    altformdata="code="+auth_code+"&grant_type=" + grant_type + "&redirect_uri=" + redirect_uri +"&scope=" +scope+"&client_id="+client_id+"&client_secret="+client_secret
    print altformdata
    
    tokenRequest = HttpRequest({'url': v1url})
    response = tokenRequest.post('/oauth.v1/token',
                           altformdata,    
                           contentType = ('application/x-www-form-urlencoded')) 
    
    print "tokenRequest status :"
    print response.status
    
    data=(json.loads(response.getResponse()))
    print data
    
    print data['access_token']
    
            
    ##### POST /configurations/
    ## create new configurations instance
    
    dict={"type":"versionOne.Server","properties":{"title":v1title,"url":v1url,"oauthRefreshToken": data['refresh_token'], "client_secret": client_secret, "client_id": client_id}}
    jsonPayload=json.dumps(dict)
    request = HttpRequest({'url': 'http://localhost:5516'}, xlruser,xlrpassword)
    response = request.post('/configurations', jsonPayload,contentType = 'application/json')
    

    sys.exit(0)
 
 
 
 
############### 
#  MAIN 
###############
print "starting main"
# Check to see if this configuration exists, create it if needed.  Otherwise, get the CONFIGID
request = HttpRequest({'url': 'http://localhost:5516'}, xlruser,xlrpassword)
response = request.get('/configurations', contentType = 'application/json')
data = json.loads(response.getResponse())

for i in range(0, len(data)):
    print "loop"
    print data[i]['id']
    if v1title == data[i]['properties']['title']:
        refreshToken(data[i]['id'])

newConfig()

