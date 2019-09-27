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
        print(summoner.id_conta)
        match_list = MatchList(self.conexao)
        summoner.partidas = match_list.getMatchListByAccount(summoner, self.regiao).partidas

        return summoner

# con = Conexao('RGAPI-4695ca5c-0e1b-43ee-a55b-a673dda3a044')
# sum = getSummoner(con, 'Rus5o')
# summoner = sum.getAllSummoner()
#
#
# for p in summoner.partidas:
#     for a in p.identidadeParticipantes:
#         print(a.player.nome)
#     print('\n')
