import requests

from getLol.model.Player import Player
from getLol.model.ParticipantIdentity import ParticipantIdentity


class Match:

    season = ''
    queue = ''
    id = ''
    identidadeParticipantes = []
    versao_jogo = ''
    id_plataforma = ''
    modo_jogo = ''
    id_mapa = ''
    tipo_jogo = ''
    equipes = []
    participantes = []
    duracao = ''
    criacao = ''
    mensagem = 200

    def __init__(self, conexao):
        self.conexao = conexao

    def getMatchById(self, id, regiao='br1'):
        url = 'https://' + regiao + '.api.riotgames.com/lol/match/v4/matches/' + id + '?api_key=' + self.conexao.key
        retorno = requests.get(url)

        if retorno.status_code == 200:
            resultado = retorno.json()

            self.season = resultado['seasonId']
            self.queue = resultado['queueId']
            self.id = resultado['gameId']
            identidadeParts = []

            for part in resultado['participantIdentities']:
                player = Player(
                                part['player']['currentPlatformId'],
                                part['player']['summonerName'],
                                part['player']['matchHistoryUri'],
                                part['player']['platformId'],
                                part['player']['currentAccountId'],
                                part['player']['profileIcon'],
                                part['player']['summonerId'],
                                part['player']['accountId']
                                )
                participant_identity = ParticipantIdentity(player, part['participantId'])
                identidadeParts.append(participant_identity)
            self.identidadeParticipantes = identidadeParts
            self.versao_jogo = resultado['gameVersion']
            self.id_plataforma = resultado['platformId']
            self.modo_jogo = resultado['gameMode']
            self.id_mapa = resultado['mapId']
            self.tipo_jogo = resultado['gameType']
            self.equipes = resultado['teams']
            self.participantes = resultado['participants']
            self.duracao = resultado['gameDuration']
            self.criacao = resultado['gameCreation']

            return self
        else:
            self.message = retorno.status_code
            return self
