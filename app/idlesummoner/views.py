from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests, json

from pfaw import Fortnite, Platform, Mode
from idlesummoner.key import FORTNITE_TOKEN, LAUNCHER_TOKEN, PASSWORD, EMAIL


#fortnite = Fortnite(fortnite_token=FORTNITE_TOKEN, launcher_token=LAUNCHER_TOKEN, password=PASSWORD, email=EMAIL)

def get_fortnite_id(username):
    player = fortnite.player(username)
    id = player.id
    if id is None:
        id = -1

    #id = "00000000"
    return id

class FortniteNameView(APIView):
    def get(self, request, *args, **kwargs):
        username = kwargs.get('username', '')
        return Response(get_fortnite_id(username))

    def put(self, request, *args, **kwargs):
        pass
