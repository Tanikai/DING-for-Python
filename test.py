from ding import dingapi

api = dingapi()

with open('stop_finder.json', 'w') as f:
    f.write(api.stop_finder('heidenheim bahnhof'))
    f.close()
