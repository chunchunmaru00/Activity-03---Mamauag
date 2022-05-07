class StatsAll():
    #solution
    def HPCalcu(PBase, PIV, PEV, PLevel):
        hp = (((2 * PBase + PIV + (PEV/4) * PLevel) / 100) + PLevel + 10)
        return hp
    
    def AttackCalcu(PBase, PIV, PEV, PLevel, PNature):
        NatureVal=0
        if PNature == 1 or PNature == 2 or PNature == 3 or PNature == 4:
            NatureVal = 1.1
        elif PNature == 5 or PNature == 10 or PNature == 15 or PNature == 20:
            NatureVal = 0.9
        else:
            NatureVal = 1
            attack = ((((2 * PBase + PIV + (PEV/4) * PLevel) / 100) + 5) *PNature)
            return attack

    def DefenseCalcu(PBase, PIV, PEV, PLevel, PNature):
        NatureVal=0
        if PNature == 5 or PNature == 7 or PNature == 8 or PNature == 9:
            NatureVal = 1.1
        elif PNature == 1 or PNature == 11 or PNature == 16 or PNature == 21:
            NatureVal = 0.9
        else:
            NatureVal = 1
            defense = ((((2 * PBase + PIV + (PEV/4) * PLevel) / 100) + 5) *PNature)
            return defense

    def SpeedCalcu(PBase, PIV, PEV, PLevel, PNature):
        NatureVal=0
        if PNature == 10 or PNature == 11 or PNature == 13 or PNature == 14:
            NatureVal = 1.1
        elif PNature == 2 or PNature == 7 or PNature == 17 or PNature == 22:
            NatureVal = 0.9
        else:
            NatureVal = 1
            speed = ((((2 * PBase + PIV + (PEV/4) * PLevel) / 100) + 5) *PNature)
            return speed

    def SPAttackCalcu(PBase, PIV, PEV, PLevel, PNature):
        NatureVal=0
        if PNature == 15 or PNature == 16 or PNature == 17 or PNature == 19:
            NatureVal = 1.1
        elif PNature == 3 or PNature == 8 or PNature == 13 or PNature == 23:
            NatureVal = 0.9
        else:
            NatureVal = 1
            SPAttack = ((((2 * PBase + PIV + (PEV/4) * PLevel) / 100) + 5) *PNature)
            return SPAttack

    def SPDefenseCalcu(PBase, PIV, PEV, PLevel, PNature):
        NatureVal=0
        if PNature == 20 or PNature == 21 or PNature == 22 or PNature == 23:
            NatureVal = 1.1
        elif PNature == 4 or PNature == 9 or PNature == 14 or PNature == 19:    
            NatureVal = 0.9
        else:
            NatureVal = 1
            SPDefense = ((((2 * PBase + PIV + (PEV/4) * PLevel) / 100) + 5) *PNature)
            return SPDefense