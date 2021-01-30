import unittest
from context import dingapi

api = dingapi.ding_requests()

with open('stop_finder.json', 'w') as f:
    f.write(api.stop_finder('heidenheim bahnhof'))
    f.close()
