from getLol.model import Conexao, Summoner, MatchList, Match

from pprint import pprint

class getSummoner:
    def __init__(self, conexao, nome, regiao='br1'):
        self.nome = nome
        self.conexao = conexao
        self.regiao = regiao

    def getAllSummoner(self):
        sum = Summoner(self.conexao)
        summoner = sum.getSummonerByName(self.nome, self.regiao)
        match_list = MatchList(self.conexao)
        summoner.partidas = match_list.getMatchListByAccount(summoner, self.regiao).partidas

        return summoner

con = Conexao('RGAPI-3165e59d-446a-485d-8a2b-8f5774a4c0b6')
sum = getSummoner(con, 'Rus5o')
summoner = sum.getAllSummoner()


for p in summoner.partidas:
    for a in p.identidadeParticipantes:
        print(a.player.nome)
    print('\n')
