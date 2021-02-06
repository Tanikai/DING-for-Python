import requests

URL_STOPFINDER = 'XML_STOPFINDER_REQUEST?coordOutputFormat=WGS84%5Bdd.ddddd%5D&name_sf={name_sf}&outputFormat=JSON&type_sf=stop'


class dingapi:
    base_url = 'https://www.ding.eu/ding/'
    output_format = '' # XML, JSON, XSLT

    def set_global_params(self, url: str) -> str:
        pass
    
    def stop_finder_request(self, stop_name: str) -> str:
        results = requests.get(self.base_url + URL_STOPFINDER.format(name_sf=stop_name))
        return results.text

    def dm_request(self, stop_id: int) -> str:
        pass

    def trip_request(self, origin_id: int, destination_id: int) -> str:
        pass
    
