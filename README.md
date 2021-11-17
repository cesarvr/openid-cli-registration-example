# Intro 

Quick example on how to registrate OIDC clients using the public [client registration](https://openid.net/specs/openid-connect-registration-1_0.html) endpoint using RHSSO (Keycloak). 

## Client Registration 


<img src="https://github.com/cesarvr/openid-cli-registration-example/blob/main/help2.png?raw=true" alt="drawing" width="500"/>

First you need to generate a ``temporary token`` in the realm where you want to install the OIDC client, once created then you need to visit the [script file](https://github.com/cesarvr/openid-cli-registration-example/blob/main/client-registration.py) at [line 6](https://github.com/cesarvr/openid-cli-registration-example/blob/main/client-registration.py#L6) and replace this line with the ``temporary token``.

Next you just need to run the script (make sure you are using [Python 3](https://www.python.org/downloads/)) like this: 

```sh
python client-registration.py <rhsso/keycloak host URL> <realm-name> 
``` 

### Client Definition 

The script will send the following payload to the server: 
```
    json {'redirect_uris': ["http://web1.org/login/callback"], "client_name": "my_client_sample" } 
```

> For more information on the accepted [payload](https://github.com/cesarvr/openid-cli-registration-example/blob/main/client-registration.py#L39) for client registration you can visit [the OIDC Client Registration RFC](https://openid.net/specs/openid-connect-registration-1_0.html#rfc.section.2). 


To the following endpoint: 

```
https://host:port/auth/realms/my_realm/clients-registrations/openid-connect
```

> For more information on how to discover this URL [click here](https://openid.net/specs/openid-connect-discovery-1_0.html#WellKnownRegistry)




## Using The Client

Once the client has being registered, the server will return a description in the form of a JSON response similiar to this: 

```yaml
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
}
```

> This should provide enough information to start using the client in the application.

### Getting A Token
You can run the script [using_the_client.py](https://github.com/cesarvr/openid-cli-registration-example/blob/main/using_the_client.py#L59) to get a token using the client registered above, just make sure to:
- Setup the host for the [RHSSO instance](https://github.com/cesarvr/openid-cli-registration-example/blob/main/using_the_client.py#L6)
- Use the [right credentials](https://github.com/cesarvr/openid-cli-registration-example/blob/main/using_the_client.py#L28-L34)
- Configure the correct [client id + secret](https://github.com/cesarvr/openid-cli-registration-example/blob/main/using_the_client.py#L59) (see the payload above on where to find those).  
- Finally and for demo purposes modify the client to allow **direct access grant** (this unnecessary in realm world applications).  

<img src="https://github.com/cesarvr/openid-cli-registration-example/blob/main/help.png?raw=true" alt="drawing" width="500"/>

> This option can be found by opening the registered client on the Keycloak dashboard. 


Then run the script like this: 

```sh
python using_the_client.py
```


