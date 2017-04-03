#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import http.client
import urllib
import json

from constants import HOST, PORT
dest = ':'.join([HOST, PORT])


def getBotResponse(response):
    '''
    Parse Json response from server

    response - JSON formated server response
    return   - actual string response from server
    '''
    response_py = json.loads(response)
    return response_py['response']


def client():
    # set up connectin with server
    connection = http.client.HTTPConnection(dest)
    while(1):
        user_input = None
        try:
            user_input = input('user: ')
        except EOFError:
            break

        url_encoded_input = urllib.parse.quote(user_input)
        request_path = ''.join(['askmeanything/?q=', url_encoded_input])
        # send a request to server
        connection.request('get', request_path)
        # read the response
        response = connection.getresponse()
        print(getBotResponse(response.read().decode()))
    print("Conversation ended")


if __name__ == "__main__":
    client()
