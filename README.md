# Intro 

Quick example on how to registrate OIDC clients using the public [client registration](https://openid.net/specs/openid-connect-registration-1_0.html) endpoint using RHSSO (Keycloak). 

## Client Registration 

Generate a temporary token in the realm where you want to install the OIDC client, then visit the python script and paste the token on [line 6](https://github.com/cesarvr/openid-cli-registration-example/blob/main/client-registration.py#L6) in the ``[client_registration.py](https://github.com/cesarvr/openid-cli-registration-example/blob/main/client-registration.py)``, then you just need to run the script (make sure you are using python 3) like this: 

```sh
python client-registration.py <rhsso/keycloak host URL> <realm-name> 
``` 

> For more information on the accepted [payload](https://github.com/cesarvr/openid-cli-registration-example/blob/main/client-registration.py#L39) for client registration you can visit [the OIDC Client Registration RFC](https://openid.net/specs/openid-connect-registration-1_0.html#rfc.section.2). 


## Using The Client

Once the client has being registered, the server will return a description in the form of a JSON response similiar to this: 

```json
{
    "client_id": "8ee8a2d5-2098-469f-b261-34bdcece597d",
    "client_id_issued_at": 1636463749,
    "client_name": "my_client_sample",
    "client_secret": "4c3e3463-9d45-483b-8ec9-96879ee3d818",
    "client_secret_expires_at": 0,
    "grant_types": [
        "authorization_code",
        "refresh_token"
    ],
    "redirect_uris": [
        "http://web1.org/login/callback"
    ],
    "registration_access_token": "<big-token-here>",
    "registration_client_uri": "https://<your-keycloak-instance>/auth/realms/your_realm/clients-registrations/openid-connect/8ee8a2d5-2098-469f-b261-34bdcece597d",
    "response_types": [
        "code",
        "none"
    ],
    "subject_type": "public",
    "tls_client_certificate_bound_access_tokens": false,
    "token_endpoint_auth_method": "client_secret_basic"
}``` 


> This should provide enough information to start using the client in the application.


You can run the script [using_the_client.py](https://github.com/cesarvr/openid-cli-registration-example/blob/main/using_the_client.py#L59) to get a token using the client registered above, just make sure to setup the host for the [RHSSO instance](https://github.com/cesarvr/openid-cli-registration-example/blob/main/using_the_client.py#L6), the [right credentials](https://github.com/cesarvr/openid-cli-registration-example/blob/main/using_the_client.py#L28-L34), set the [client id + secret](https://github.com/cesarvr/openid-cli-registration-example/blob/main/using_the_client.py#L59) and finally and for demo purposes just make sure that the client allow direct access grant (only for test purposes, this will allow the script to get a token by just passing user and password).  

Then run the script like this: 

```sh
python using_the_client.py
```


