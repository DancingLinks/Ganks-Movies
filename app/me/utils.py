import json
import requests

__author__ = 'jx-pc'


class Utils(object):

    @staticmethod
    def get_json_response(url):
        response = requests.get(url)
        return json.loads(response.text)


    @staticmethod
    def json_to_dict(data):
        data_dict = Utils.get_empty_dict()
        for x in data['category']:
            if x == '\u778e\u63a8\u8350':
                name = 'xiatuijian'
            elif x == '\u524d\u7aef':
                name = 'front'
            else:
                name = x
            data_dict['check_' + name] = True
            data_dict[name] = []
            for gank in data['results'][x]:
                data_dict[name].append(gank)
        return data_dict


    @staticmethod
    def get_empty_dict():
        data_dict = {}
        data_dict['check_Android'] = data_dict['check_iOS'] = data_dict['check_\u524d\u7aef'] = False
        data_dict['check_\u778e\u63a8\u8350'] = data_dict['check_App'] = False
        return data_dict