import requests


class dingapi:
    # ding, ding2, ding3 is possible (not sure about the differences tho)
    base_url = 'https://www.ding.eu/ding/'
    output_format = ''  # XML, JSON, XSLT

    def set_global_params(self, url: str) -> str:
        pass

    # get stop id by stop name
    def stop_finder_request(self, stop_name: str) -> str:
        url = self.base_url + \
            'XML_STOPFINDER_REQUEST?coordOutputFormat=WGS84%5Bdd.ddddd%5D&name_sf={name_sf}&outputFormat=JSON&type_sf=stop'
        results = requests.get(url.format(name_sf=stop_name))
        return results.text

    # get departure times of stop
    def dm_request(self, stop_id: int) -> str:
        url = self.base_url + \
            'XML_DM_REQUEST?typeInfo_dm=stopID&nameInfo_dm={nameInfo_dm}&deleteAssignedStops_dm=1&useRealtime=1&mode=direct&outputFormat=JSON'
        results = requests.get(url.format(nameInfo_dm=str(stop_id)))
        return results.text

    # get planned trips from origin stop to destination stop
    def trip_request(self, origin_id: int, destination_id: int) -> str:
        url = self.base_url + 'XML_TRIP_REQUEST2?SpEncId=0&itdLPxx_useJs=1&std3_suggestMacro=std3_suggest&std3_commonMacro=trip&itdLPxx_contractor=&std3_contractorMacro=&type_origin=any&nameInfo_origin={nameInfo_origin}&type_destination=any&nameInfo_destination={nameInfo_destination}&itdDateDayMonthYear=10.01.2021&itdTime=17%3A10&itdTripDateTimeDepArr=dep&includedMeans=checkbox&useRealtime=1&inclMOT_0=true&inclMOT_1=true&inclMOT_3=true&inclMOT_4=true&inclMOT_5=true&inclMOT_6=true&inclMOT_10=true&inclMOT_11=true&lineRestriction=400&routeType=LEASTTIME&trITMOTvalue100=10&name_via=&nameInfo_via=invalid&type_via=any&dwellTimeMinutes=0&itdLPxx_snippet=1&itdLPxx_template=tripresults_pt_trip&computationType=sequence&_=1610295030347&outputFormat=JSON'
        results = requests.get(url.format(nameInfo_origin=str(origin_id), nameInfo_destination=str(destination_id)))
        return results.text
