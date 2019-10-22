class Participant:
    def __init__(self, stats, participantId, runes, timeline, teamId, spell2Id, masteries,
                 highestAchievedSeasonTier, spell1Id, championId):
        self.stats = stats
        self.id = participantId
        self.runas = runes
        self.timeline = timeline
        self.idTime = teamId
        self.spell2Id = spell2Id
        self.maestrias = masteries
        self.rank_mais_alto_season = highestAchievedSeasonTier
        self.spell1Id = spell1Id
        self.id_champ = championId