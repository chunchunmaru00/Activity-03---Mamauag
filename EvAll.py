class EvAll():

    def EVAttack(evstat, evBase, evIV, evEV, evLevel, evNature):
        nature = 1.0
        if evNature == 1 or evNature == 2 or evNature == 3 or evNature == 4:
            nature == 1.1
        else:
            nature == 0.9
        a = ((2 * evBase + evIV +(evEV / 4))*evLevel/100)
        evattack = (((((evstat / evNature)-a) * 400)/evLevel) /4)*4
        return evattack

    def EVDefense(evstat, evBase, evIV, evEV, evLevel, evNature):
        nature = 1.0
        if evNature == 5 or evNature == 7 or evNature == 8 or evNature == 9:
            nature == 1.1
        else:
            nature == 0.9
        a = ((2 * evBase + evIV +(evEV / 4))*evLevel/100)
        evdefense = (((((evstat / evNature)-a) * 400)/evLevel) /4)*4
        return evdefense

    def EVSpeed(evstat, evBase, evIV, evEV, evLevel, evNature):
        nature = 1.0
        if evNature == 10 or evNature == 11 or evNature == 13 or evNature == 14:
            nature == 1.1
        else:
            nature == 0.9
        a = ((2 * evBase + evIV +(evEV / 4))*evLevel/100)
        evspeed = (((((evstat / evNature)-a) * 400)/evLevel) /4)*4
        return evspeed

    def EVSpAttack(evstat, evBase, evIV, evEV, evLevel, evNature):
        nature = 1.0
        if evNature == 15 or evNature == 16 or evNature == 17 or evNature == 19:
            nature == 1.1
        else:
            nature == 0.9
        a = ((2 * evBase + evIV +(evEV / 4))*evLevel/100)
        evspattack = (((((evstat / evNature)-a) * 400)/evLevel) /4)*4
        return evspattack

    def EVSpDefense(evstat, evBase, evIV, evEV, evLevel, evNature):
        nature = 1.0
        if evNature == 20 or evNature == 21 or evNature == 22 or evNature == 23:
            nature == 1.1
        else:
            nature == 0.9
        a = ((2 * evBase + evIV +(evEV / 4))*evLevel/100)
        evspdefense = (((((evstat / evNature)-a) * 400)/evLevel) /4)*4
        return evspdefense