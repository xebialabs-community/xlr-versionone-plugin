#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#


comment = """ ##########
Go to url: https://www6.v1host.com/V1DemoScrum/rest-1.v1/Data/Issue after authenticating to examine XML and find proper scope parameter.
You may need to create an issue in the target project first to use as a reference.

Example API Call to create new issue
 POST  https://www6.v1host.com/V1DemoScrum/rest-1.v1/Data/Issue

 <Asset href="/VersionOne/rest-1.v1/New/Issue">
  <Attribute name="Name" act="set">Test issue 2</Attribute>
  <Relation name="Scope" act="set">
    <Asset href="/VersionOne/rest-1.oauth.v1/Data/Scope/1083" idref="Scope:1083"/>
  </Relation>
 </Asset>


The following is an example of the refresh token request.
POST /v1sdktesting/oauth.v1/token HTTP/1.1
Host: www6.v1host.com
Content-Type: application/x-www-form-urlencoded

refresh_token=-kkK!IAAAAB238jkfViwS9YRTDZaABD5jYQcwj_excjLG2i1KgdltsQAAAAFQ9kAhJjpIgfDaqhfg1MebHOFl5KP4C_X03Rcdghyismthpzak34jw50NFMmnB77-URk3RxHkW7-PN24HMAiJdF2dTHvousrGOBOip7loaXDFnGSUlLgW54gZ4vkMGYYsD8oj5Cyd_RYqUlkSYaHAVOeYq1HbaVBVXqLZSLtjlddbwkJ4lPN5WWMuXo4GZcHnKMPXW7jnFQ8EPb623MeKeEbvQ1Dt0wBqnrRSfatAH1Q&
grant_type=refresh_token&
client_id=client_dkfsegrk&
client_secret=9nrqergr2occj6m3fggd

"""

def getOauthAccessToken(server):
    
    formdata='refresh_token=' + server['oauthRefreshToken']+'&grant_type=refresh_token'+'&client_id='+ server['client_id']+'&client_secret='+ server['client_secret']
    #print formdata

    tokenRequest = HttpRequest({'url': server['url']})
    response = tokenRequest.post('/oauth.v1/token',
                           formdata,    
                           contentType = ('application/x-www-form-urlencoded')) 
    
    print "tokenRequest status :"
    print response.status

    data=(json.loads(response.getResponse()))
    return data['access_token']

    

###############
## MAIN CODE ##
###############
import sys, string
import com.xhaus.jyson.JysonCodec as json
import time

if versionOneServer is None:
    print "No server provided."
    sys.exit(1)
        
#credentials = CredentialsFallback(versionOneServer,oauthRefreshToken,client_id).getCredentials()
#print versionOneServer['oauthRefreshToken']

OauthAccessToken=getOauthAccessToken(versionOneServer)
print OauthAccessToken

payload="""
<Asset href="/VersionOne/rest-1.v1/New/Issue">
<Attribute name="Name" act="set">Test issue 2</Attribute>
<Relation name="Scope" act="set">
<Asset href="/VersionOne/rest-1.oauth.v1/Data/Scope/1083" idref="Scope:1083"/>
</Relation>
</Asset>
"""

# need to add a header: Authorization: Bearer [access token]
header = {'Authorization':'Bearer '+ OauthAccessToken}
#print header

CreateIssueRequest = HttpRequest({'url': versionOneServer['url']})
#CreateIssueRequest = HttpRequest({'url': versionOneServer['url']})
#print "URL: "+ versionOneServer['url']

response = CreateIssueRequest.post('/rest-1.v1/Data/Issue',payload,contentType = ('text/xml'), headers=header) 
#response = CreateIssueRequest.get('/rest-1.v1/Data/Issue', headers=header) 

print "Rest API Request Status: "
print response.status
print response.getResponse()
  
print "CreateIssueRequest status :"



    #data=(json.loads(response.getResponse()))
    #data=response.getResponse()
    #print data

sys.exit(1)
