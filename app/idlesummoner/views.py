from django.shortcuts import render
from django.views.generic import View
from idlesummoner.key import RIOT_API_KEY
import requests, json

# {0} Regions: BR1, EUN1, EUW1, JP1, KR, LA1 (LAN), LA2 (LAS), NA1, OC1, TR1, RU
# {1} Summoner Name
# {2} API Keey
BASE_URL = "https://{0}.api.riotgames.com/lol/summoner/v3/summoners/by-name/{1}?api_key={2}"

def generate_url(region, summoner_name):
    return BASE_URL.format(region, summoner_name, api_key)

def get_summoner_name_info(region, summoner_name, api_key = RIOT_API_KEY):
    """
    Calls the Riot API for a user's summoner info.
    Request is made using region, summoner name, and an API key.

    returns summoenr info - {accountId, summonerName, profileIconId, revisionDate}
    """
    url = generate_url(region, summoner_name, api_key)
    response = requests.get(url)
    data = response.json()
    if response.status_code == 404:
        summoner_info = {
            'accountId': -1,
            summonerName: summoner_name,
            'profileIconId': 1,
            'revisionDate': -1
        }
    else:
        summoner_info = {
            'accountId':  data['accountId'],
            'summonerName': data['name'],
            'profileIconId': data['profileIconId'],
            'revisionDate': data['revisionDate']
        }
    return json.dumps(summoner_info)

class SummonerNameInfoView(View):
    """
    View to see the info from a summoner name
    """
    def get(self, request, name, region):
        return get_summoner_name_info(region, name)
