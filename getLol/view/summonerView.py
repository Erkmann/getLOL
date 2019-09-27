from getLol.model import Conexao, Summoner, MatchList, Match

from pprint import pprint

class getSummoner:
    def __init__(self, nome, conexao, regiao='br1'):
        self.nome = nome
        self.conexao = conexao
        self.regiao = regiao

    def getAllSummoner(self):
        sum = Summoner(self.conexao)
        summoner = sum.getSummonerByName(self.nome, self.regiao)
        match_list = MatchList(self.conexao)
        summoner.partidas = match_list.getMatchListByAccount(summoner, self.regiao).partidas

        return summoner


c = Conexao('RGAPI-4695ca5c-0e1b-43ee-a55b-a673dda3a044')
a = getSummoner('Rus5o', c, 'br1')
summoner = a.getAllSummoner()

for partida in summoner.__dict__['partidas']:
    pprint(partida.__dict__)
