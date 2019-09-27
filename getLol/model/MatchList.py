import requests

from . import Match, Conexao, Summoner

class MatchList:

    partidas = []
    partidas_totais = 0
    index_comeco = 0
    index_fim = 15
    message = 200

    def __init__(self, conexao):
        self.conexao = conexao

    def getMatchListByAccount(self, summoner, regiao='br1'):
        url = 'https://' + regiao + '.api.riotgames.com/lol/match/v4/matchlists/by-account/' + summoner.id_conta + \
              '?endIndex=' + str(self.index_fim) + '&api_key=' + self.conexao.key
        retorno = requests.get(url)
        if retorno.status_code == 200:
            resultado = retorno.json()
            for p in resultado['matches']:
                partida = Match(self.conexao)
                p = partida.getMatchById(str(p['gameId']))
                self.partidas.append(p)

            self.partidas_totais = resultado['totalGames']
            self.index_comeco = resultado['startIndex']
            self.index_fim = resultado['endIndex']

            return self

        else:
            self.message = retorno.status_code
            return self
