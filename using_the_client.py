import requests, os, sys
import json, time

# Retrieves the Well Known Endpoint: https://openid.net/specs/openid-connect-discovery-1_0.html 
def discovery(): 
    host = 'sso-cvaldezr-dev.apps.sandbox.x8i5.p1.openshiftapps.com' 
    realm = 'my_realm'
    print("host: ", host, " realm: ", realm)

    if not host or not realm:
        print("command usage: client-registration <rhsso-host:port> <realm>")
        sys.exit()
    
    # TODO We use http for illustrative purposes, we should always use https.
    url = "https://" + host + "/auth/realms/" + realm + "/.well-known/openid-configuration" 
    print("URL: ", url)
    resp = requests.get(url=url).json()
    return resp


# We use here the "Direct Access Grants" this method require to send user/password, in real scenarios we should stick 
# with the "Standard Flow" applications should never manipulate credentials.
def get_token(token_endpoint, client_id = None, client_secret = None):

    print("Getting Token For --> client_id: ", client_id, " secret: ", client_secret)

    #headers = {"Authorization": "Bearer "+load_temporary_token()}
    body = {
                "client_id": client_id, 
                "username": "john", 
                "password":"admin1234", 
                "grant_type":"password",
                "client_secret": client_secret 
            }
    
    ret = requests.post(token_endpoint, data=body)
    code = ret.status_code
    if code != 200:
        print("Error: Client Status",code)
        print("Content: ",ret.content)
        return None
    else:
        _token = ret.json()["access_token"]
        print("Token: ", _token)
        return _token 

def get_user_info(endpoint, token):
    headers = {"Authorization": "Bearer "+ token}
    ret = requests.get(endpoint, headers=headers)

    print("status ->", ret.status_code)
    print("content ->", ret.json())





well_known = discovery()
token = get_token(well_known['token_endpoint'], '1b1b5882-c4a3-470e-983a-7f2e1a7f28c7' ,'815cda16-629d-4efc-a975-8e456e375f5c' )


print('token: ', token)

get_user_info(well_known['userinfo_endpoint'], token)
