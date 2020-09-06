import re
import pdb


def g_to_gib(g):
    return g * (10 ** 9) / (2 ** 30)


def gib_to_g(gib):
    return gib * (2**30) / (10 ** 9)


def parser():
    print("##############################################################")
    print("# Size, use K,M,G,T,P at the end for the type. Example: 600G #")
    print("##############################################################\n")
    res = 0.0
    while res == 0.0:
        txt = input()
        amount = int(re.split("\D", txt)[0])
        unit = re.search("\D", txt)
        if unit and unit.group() in ["G", "K", "M", "T", "P"]:
            unit = unit.group()
            if unit == "G":
                res = amount * (10 ** 9) / (2 ** 30)
            if unit == "K":
                res = amount * (10 ** 3) / (2 ** 10)
            if unit == "M":
                res = amount * (10 ** 6) / (2 ** 20)
            if unit == "T":
                res = amount * (10 ** 12) / (2 ** 40)
            if unit == "P":
                res = amount * (10 ** 15) / (2 ** 50)
        else:
            print('invalid value, try again!')
    return f'{int(res)} {unit}iB'


def calculo_simple(storage, inc_percent, years):
    return (storage*inc_percent)*years+storage


def crecimiento_total(storage, inc_percent, years):
    total_increase = (1+inc_percent)**years
    return total_increase*storage


print("# Opciones:\n# parser()\n# g_to_gib\n# gib_to_g")
print("# calculo_simple(storage,inc_percent, years)")
print("# crecimiento_total(storage,inc_percent, years)")
print("###############################################")
pdb.set_trace()
