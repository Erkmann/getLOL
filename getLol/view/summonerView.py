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

con = Conexao('RGAPI-57234896-991f-4f7e-b7b4-1aa7a0edec0c')
sum = getSummoner(con, 'Rus5o')
summoner = sum.getAllSummoner()


# for p in summoner.partidas:
#     for a in p.identidadeParticipantes:
#         print(a.player.nome)
#     print('\n')
