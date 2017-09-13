import requests

from constants import KIVA_GRAPHQL_URL


class KivaClient():
    @staticmethod
    def query(querystring=''):
        res = requests.get(KIVA_GRAPHQL_URL, params={'query': querystring})

        if not res.ok:
            return res.raise_for_status()

        json = res.json()
        if json.get('errors'):
            raise Exception(res.json()['errors'])

        return json


kiva_client = KivaClient
