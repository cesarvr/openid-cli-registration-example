#!/bin/python3
import requests, os, sys
import json, time

TEMP_TOKEN = ''' 
eyJhbGciOiJIUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI0NDI2NzM0Yi04NmNhLTQ2YTAtYjM0Mi1mZGM2Y2JmNzc0YzAifQ.eyJqdGkiOiIyMzlmNzRmNi04MjJkLTQzM2EtOWZmZS0yZjFhNzdiOWQ1MzgiLCJleHAiOjAsIm5iZiI6MCwiaWF0IjoxNjM2NDYzNzM0LCJpc3MiOiJodHRwczovL3Nzby1jdmFsZGV6ci1kZXYuYXBwcy5zYW5kYm94Lng4aTUucDEub3BlbnNoaWZ0YXBwcy5jb20vYXV0aC9yZWFsbXMvbXlfcmVhbG0iLCJhdWQiOiJodHRwczovL3Nzby1jdmFsZGV6ci1kZXYuYXBwcy5zYW5kYm94Lng4aTUucDEub3BlbnNoaWZ0YXBwcy5jb20vYXV0aC9yZWFsbXMvbXlfcmVhbG0iLCJ0eXAiOiJJbml0aWFsQWNjZXNzVG9rZW4ifQ.dXGUvPOJjovK-AtzQGO2w1DrHHC7hilstSVDIYT338w
'''

def store(data):
    with open('my_client.json', 'w') as fp:
        json.dump(data, fp)

# Retrieves the Well Known Endpoint: https://openid.net/specs/openid-connect-discovery-1_0.html 
def discovery(): 
    host = sys.argv[1]
    realm = sys.argv[2]
    print("host: ", host, " realm: ", realm)

    if not host or not realm:
        print("command usage: client-registration <rhsso-host:port> <realm>")
        sys.exit()
    
    # TODO We use http for illustrative purposes, we should always use https.
    url = "https://" + host + "/auth/realms/" + realm + "/.well-known/openid-configuration" 
    print("URL: ", url)
    resp = requests.get(url=url).json()
    return resp

def load_temporary_token(): 
    return TEMP_TOKEN.strip().replace('\n', '')

#Registration Endpoint 
#https://openid.net/specs/openid-connect-registration-1_0.html#Introduction
def register_new_client(client_registration_endpoint):
    headers = {'Content-type': 'application/json', "Authorization": "Bearer "+load_temporary_token()}

    #Payload 
    #https://openid.net/specs/openid-connect-registration-1_0.html#rfc.section.2
    body = {'redirect_uris': ["http://web1.org/login/callback"], "client_name": "my_client_sample" }

    ret = requests.post(client_registration_endpoint, data=json.dumps(body), headers=headers )

    b = ret.json()
    print('response: ', b)
    return b 


well_known = discovery()
client_registration_endpoint = well_known['registration_endpoint']
token_endpoint = well_known['token_endpoint']

client_data = register_new_client(client_registration_endpoint)
store(client_data)

