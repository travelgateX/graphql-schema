#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "David Amian <damian@xmltravelgate.com>"
__copyright__ = "Copyright (C) 2018, TravelgateX"
__license__ = "GPL-2"

import json
from six.moves import urllib

class GraphQLClient:
    """Class to use GraphQL on Python 3.6.

    """
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.token = None

    def execute(self, query, variables=None):
        return self._send(query, variables)

    def inject_token(self, token):
        self.token = token

    def _send(self, query, variables):
        data = {'query': query,
                'variables': variables}
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}
        if self.token is not None:
            headers['Authorization'] = '{}'.format(self.token)

        data_str = json.dumps(data).replace('"%false%"', 'false').replace('"%true%"', 'true').replace('"%null%"', 'null').encode('utf-8')
        req = urllib.request.Request(self.endpoint, data_str, headers)

        try:
            response = urllib.request.urlopen(req)
            response_json = json.loads(response.read().decode('utf-8'))
            return response_json
        except urllib.error.HTTPError as e:
            print((e.read()))
            raise e
    
    def check_result(self, query, result):
        result_json = self._send(query, None)
        expected_result_json = json.loads(result.decode('utf-8'))
        if json.dumps(result_json, sort_keys=True) == json.dumps(expected_result_json, sort_keys=True):
            return True
        return False
         