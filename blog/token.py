# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 17:48:20 2023

@author: PC
"""

import requests
username = 'Muzzocourt'
token = 'f21cb99b7e499eee59db798b9dd7cd7edd5ef326'

response = requests.get(
    'https://www.pythonanywhere.com/api/v0/user/{username}/cpu/'.format(
        username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))