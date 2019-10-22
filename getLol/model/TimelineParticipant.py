class TimelineParticipant:
    def __init__(self, lane, participantId, csDiffPerMinDeltas, goldPerMinDeltas,
                 xpDiffPerMinDeltas, creepsPerMinDeltas, xpPerMinDeltas, role,
                 damageTakenDiffPerMinDeltas, damageTakenPerMinDeltas):
        self.lane = lane
        self.id_participant = participantId
