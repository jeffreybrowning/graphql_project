import requests

from constants import KIVA_GRAPHQL_URL


class KivaClient():
    @staticmethod
    def query(querystring=''):
        res = requests.get(KIVA_GRAPHQL_URL, params={'query': querystring}).json()
        if res.get('errors'):
            raise Exception(res['errors'])
        return res


kiva_client = KivaClient
