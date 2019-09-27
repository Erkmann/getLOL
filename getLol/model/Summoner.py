from Conexao import Conexao
import requests

class Summoner():

    icon_id = ''
    nome = ''
    puuid = ''
    level = ''
    id_conta = ''
    id_geral = ''
    data_revisao = ''


    def __init__(self, conexao, nome):
        self.apiKey = conexao.key
        self.nome = nome


    def getSummoner(self):
        result = requests.get('https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+ self.nome +'?api_key=' + self.apiKey)
        resultado = result.json()
        
        self.nome = resultado['name']
        self.icon_id = resultado['profileIconId']
        self.puuid = resultado['puuid']
        self.level = resultado['summonerLevel']
        self.id_geral = resultado['id']
        self.id_conta = resultado['accountId']
        self.data_revisao = resultado['revisionDate']

        return self
