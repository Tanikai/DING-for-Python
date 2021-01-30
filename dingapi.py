import requests

URL_STOPFINDER = 'https://www.ding.eu/ding/XSLT_STOPFINDER_REQUEST?coordOutputFormat=WGS84%5Bdd.ddddd%5D&name_sf={name_sf}&outputFormat=JSON&type_sf=stop'

class ding_requests:

    def stop_finder(self, stop_name):
        results = requests.get(URL_STOPFINDER.format(name_sf=stop_name))
        return results.text
