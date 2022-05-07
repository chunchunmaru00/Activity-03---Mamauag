import math
import StatsAll as sts
import EvAll as ev

#status calculator
def main():
    HP_base = int(input("Pokemon Health Points(HP): "))
    HP_iv = int(input("Pokemon Individual Value(IV) [0-31]: "))
    if HP_iv > 31:
        print("Choose only at 0-31, Thank you")
        main()
        
    HP_ev = int(input("Pokemon Effort Value(EV) [0-25]: "))
    if HP_ev > 255:
        print("Choose only at 0-31, Thank you")
        main()
        
    HP_lvl = int(input("Poekmon Level: "))
    print("        Pokemon Nature")
    print("0 - Hardy     5 - Bold      10 - Timid      15 - Modest     20 - Calm")
    print("1 - Lonely    6 - Docile    11 - Hasty      16 - Mild       21 - Gentle")
    print("2 - Brave     7 - Relaxed   12 - Serious    17 - Quiet      22 - Sassy")
    print("3 - Adamant   8 - Impish    13 - Jolly      18 - Bashful	   23 - Careful")
    print("4 - Naughty   9 - Lax       14 - Naive      19 - Rash       24 - Quirky")
    InputNature = int(input("Pokemon Nature: "))
    if InputNature > 24:
        print("Choose only at 0-24, Thank you")
        main()

    HPStatus = sts.StatsAll.HPCalcu(HP_base, HP_iv, HP_ev, HP_lvl, HP_lvl)
    AttackStatus = sts.StatsAll.AttackCalcu(HP_base, HP_iv, HP_ev, HP_lvl, InputNature)
    DefenseStatus = sts.StatsAll.DefenseCalcu(HP_base, HP_iv, HP_ev, HP_lvl, InputNature)
    SpeedStatus = sts.StatsAll.SpeedCalcu(HP_base, HP_iv, HP_ev, HP_lvl, InputNature)
    SPAttackStatus = sts.StatsAll.SPAttackCalcu(HP_base, HP_iv, HP_ev, HP_lvl, InputNature)
    SPDefenceStatus = sts.StatsAll.SPDefenseCalcu(HP_base, HP_iv, HP_ev, HP_lvl, InputNature)

    print("Health Points(HP): ", HPStatus)
    print("Attack Damage: ", AttackStatus)
    print("Defence: ", DefenseStatus)
    print("Speed: ", SpeedStatus)
    print("Special Attack: ", SPAttackStatus)
    print("Special Defense: ", SPDefenceStatus)

def EVcal():
    #input
    inputLevel = int(input("Level of the Pokemon: "))
    inputBase = int(input("Value of Stat: "))
    inputIV = int(input("Indivisual Value (0-31): "))
    if inputIV > 31:
        print("Choose only at 0-31, Thank you")
        EVcal()
    inputEV = int(input("Effort Value (0-255): "))
    if inputEV > 255:
        print("Choose only at 0-255, Thank you")
        EVcal()
    print("        Pokemon Nature")
    print("0 - Hardy     5 - Bold      10 - Timid      15 - Modest     20 - Calm")
    print("1 - Lonely    6 - Docile    11 - Hasty      16 - Mild       21 - Gentle")
    print("2 - Brave     7 - Relaxed   12 - Serious    17 - Quiet      22 - Sassy")
    print("3 - Adamant   8 - Impish    13 - Jolly      18 - Bashful	   23 - Careful")
    print("4 - Naughty   9 - Lax       14 - Naive      19 - Rash       24 - Quirky")
    evnature = int(input("Pokemon Nature: "))
    if evnature > 24:
        print("Choose only at 0-24, Thank you")
        EVcal()

    sts_AttackStatus = sts.StatsAll.AttackCalcu(inputBase, inputIV, inputEV, inputLevel, evnature)
    sts_DefenseStatus = sts.StatsAll.DefenseCalcu(inputBase, inputIV, inputEV, inputLevel, evnature)
    sts_SpeedStatus = sts.StatsAll.SpeedCalcu(inputBase, inputIV, inputEV, inputLevel, evnature)
    sts_SPAttackStatus = sts.StatsAll.SPAttackCalcu(inputBase, inputIV, inputEV, inputLevel, evnature)
    sts_SPDefenceStatus = sts.StatsAll.SPDefenseCalcu(inputBase, inputIV, inputEV, inputLevel, evnature)

    ev_Attack = ev.EvAll.EVAttack(sts_AttackStatus, sts_DefenseStatus, sts_SpeedStatus, sts_SPAttackStatus, sts_SPDefenceStatus)
    ev_Defense = ev.EvAll.EVDefense(sts_AttackStatus, sts_DefenseStatus, sts_SpeedStatus, sts_SPAttackStatus, sts_SPDefenceStatus)
    ev_Speed = ev.EvAll.EVSpeed(sts_AttackStatus, sts_DefenseStatus, sts_SpeedStatus, sts_SPAttackStatus, sts_SPDefenceStatus)
    ev_SPAttack = ev.EvAll.EVSpAttack(sts_AttackStatus, sts_DefenseStatus, sts_SpeedStatus, sts_SPAttackStatus, sts_SPDefenceStatus)
    ev_SPDefense = ev.EvAll.EVSpDefense(sts_AttackStatus, sts_DefenseStatus, sts_SpeedStatus, sts_SPAttackStatus, sts_SPDefenceStatus)

    pick = int(input("[1] - Single Stat\n [2] - All of the Stats\n"))
    if pick > 2:
        print("Choose only from 1 & 2, Thank you")
        EVcal()
    elif pick == 1:
        single = int(input("[1] - Attack\n [2] - Defense\n [3] - Speed\n [4] - Special Attack\n [5] - Special Defense"))
        if single > 5:
            print("Choose only from 1-5, Thank you")
            EVcal()
        elif single == 1:
            print("Attack : " , ev_Attack)
        elif single == 2:
            print("Defense : ", ev_Defense)
        elif single == 3:
            print("Sp.Attack : " , ev_Speed)
        elif single == 4:
            print("Sp.Defense : ", ev_SPAttack)
        elif single == 5:
            print("Speed : ", ev_SPDefense)
    elif pick == 2:
        print("Attack : " , ev_Attack)
        print("Defense : " , ev_Defense)
        print("Sp.Attack : " , ev_Speed)
        print("Sp.Defense : " , ev_SPAttack)
        print("Speed : " , ev_SPDefense)

def Menu():
    print("Choose what you want to calculate with your Pokemon!!!")
    print("[1] - HP or Other stats Calculator \n[2] - EV Calculator")
    choose = int(input(" Select from 1 and 2: "))
    if choose == 1:
        main()
    elif choose == 2:
        EVcal()
    else:
        print("Choose only from 1 or 2, Thank you")
        Menu()

Menu()

user1=input("Want to try again? y/n: ")

if user1 == "y":
    Menu()
else:
    print("Thank you! Gotta catch 'em all!")
    exit()
