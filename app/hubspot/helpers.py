import json

import requests

from app.core.config import settings

def get_tokens(grant_type: str, code: str=None, refresh_token: str=None) -> dict:
    HS_CLIENT_ID = settings.HS_CLIENT_ID
    HS_CLIENT_SECRET = settings.HS_CLIENT_SECRET
    HS_REDIRECT_URI = settings.HS_REDIRECT_URI

    url = 'https://api.hubapi.com/oauth/v1/token'
    headers = {
        'content-type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': grant_type,
        'client_id': HS_CLIENT_ID,
        'client_secret': HS_CLIENT_SECRET,
        'redirect_uri': HS_REDIRECT_URI
    }
    if code:
        data['code'] = code
    
    if refresh_token:
        data['refresh_token'] = refresh_token
    
    res = requests.post(url=url, data=data, headers=headers)
    if res.ok:
        res = res.json()
        return {
            'access_token': res['access_token'],
            'refresh_token': res['refresh_token'],       
        }
    else:
        return None
    
def get_portal_info(access_token: str) -> dict:
    url = f'https://api.hubapi.com/oauth/v1/access-tokens/{access_token}'

    res = requests.get(url=url)
    if res.ok:
        res = res.json()
        return {
            'hub_id': res['hub_id'],
            'user_id': res['user_id'],
            'hub_domain': res['hub_domain']
        }
    else:
        return None
    

def create_contact(access_token: str, email: str):
    url = 'https://api.hubapi.com/crm/v3/objects/contacts/'
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    data = {
        "properties": {
            "email": email
        } 
    }
    res = requests.post(url, json=data, headers=headers)
    if res.ok:
        return res.json()


def find_contact(access_token: str, email: str):
    url = f'https://api.hubapi.com/crm/v3/objects/contacts/{email}'
    params = {"idProperty": "email"}
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    res = requests.get(url, params=params, headers=headers)
    if res.ok:
        return res.json()['id']
    else:
        contact = create_contact(access_token=access_token, email=email)
        return contact['id']

def create_timeline_event():
    pass


def create_email(access_token: str, hs_contact_id: int, email_direction: str):
    url = 'https://api.hubapi.com/crm/v3/objects/emails'
    headers = {
        'content-type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    email_headers = {
        "from": {
            "email": "from@domain.com",
            "firstName": "FromFirst",
            "lastName": "FromLast"
        },
        "to": [
            {
            "email": "ToFirst ToLast<to@test.com>",
            "firstName": "ToFirst",
            "lastName": "ToLast"
            }
        ],
        "cc": [],
        "bcc": []
    }
    data = {
        "properties": {
            "hs_timestamp": "",
            "hs_email_direction": "",
            "hs_email_subject": "",
            "hs_email_html": "",
            "hs_email_status": "SENT",
            "hs_email_headers": json.dumps(email_headers) # json escaped string https://developers.hubspot.com/docs/api/crm/email#set-email-headers,
        },
        "associations": [
            {
            "to": {
                "id": hs_contact_id
            },
            "types": [
                {
                "associationCategory": "HUBSPOT_DEFINED",
                "associationTypeId": 210
                } ]
            }
        ]
    }
