class Equipe():

    def __init__(self, firstDragon, firstInhibitor, bans, baronKills, firstRiftHerald, firstBaron, riftHeraldKills, firstBlood,
                 teamId, firstTower, vilemawKills, inhibitorKills, towerKills, dominionVictoryScore, win, dragonKills):
        self.primeiro_drag = firstDragon
        self.primeiroInib = firstInhibitor
        self.bans = bans
        self.kills_barao = baronKills
        self.primeiro_arauto = firstRiftHerald
        self.primeiro_baron = firstBaron
        self.kills_arauto = riftHeraldKills
        self.first_blood = firstBlood
        if teamId == 100:
            self.cor_time = 'azul'
        else:
            self.cor_time = 'vermelho'
        self.primeira_torre = firstTower
        self.vilemaw_kills = vilemawKills
        self.inib_kills = inhibitorKills
        self.torres_kills = towerKills
        self.dominion_pontos = dominionVictoryScore
        if win == 'Win':
            self.vitoria = 1
        else:
            self.vitoria = 0
        self.drag_kills = dragonKills