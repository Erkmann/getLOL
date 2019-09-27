import Conexao
import requests

class Summoner():

    icon_id = ''
    nome = ''
    puuid = ''
    level = ''
    id_conta = ''
    id_geral = ''
    data_revisao = ''
    message = ''


    def __init__(self, conexao):
        self.apiKey = conexao.key


    def getSummonerByName(self, nome=None, regiao='br1'):
        result = requests.get('https://' + regiao +'.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+ nome +'?api_key=' + self.apiKey)
        if result.status_code == 200:
            resultado = result.json()
            self.nome = resultado['name']
            self.icon_id = resultado['profileIconId']
            self.puuid = resultado['puuid']
            self.level = resultado['summonerLevel']
            self.id_geral = resultado['id']
            self.id_conta = resultado['accountId']
            self.data_revisao = resultado['revisionDate']

            return self

        else:
            self.message = result.status_code
            return self

# con = Conexao('RGAPI-4695ca5c-0e1b-43ee-a55b-a673dda3a044')

# sum = Summoner(con)
from Conexao import 
# print(sum.getSummonerByName('Rus5o').id_conta)
