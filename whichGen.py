import os
import datetime


def find_gen(userRes):
    current_year = datetime.datetime.now().year
    res = int(userRes)
    if res >= 1433 and res < 1460:
        return 'Arthurian'
    elif res >=1461 and res < 1483:
        return 'Humanist'
    elif res >=1483 and res < res < 1512:
        return 'Reformation'
    elif res >= 1512 and res < 1540:
        return 'Reprisal'
    elif res >= 1541 and res <1565:
        return 'Elizabethan'
    elif res >= 1566 and res < 1587:
        return 'Palrliamentary'
    elif res >= 1587 and res < 1618:
        return 'Puritan'
    elif res >= 1618 and res < 1648:
        return 'Cavalier'
    elif res >= 1648 and res < 1674:
        return 'Glorious'
    elif res >= 1674 and res < 1701:
        return 'Enlightenment'
    elif res >= 1701 and res < 1724:
        return 'Awakening'
    elif res >= 1724 and res < 1742:
        return 'Liberty'
    elif res >= 1742 and res <1767:
        return 'Republican'
    elif res >= 1767 and res <1792:
        return 'Compromise'
    elif res >= 1792 and res <1822:
        return 'Transcendental'
    elif res >= 1822 and res <1843:
        return 'Gilded'
    elif res >= 1843 and res <1860:
        return 'Progressive'
    elif res >= 1860 and res <1883:
        return 'Missionary'
    elif res >= 1883 and res <1901:
        return 'Lost'
    elif res >= 1901 and res <1928:
        return 'Greatest (AKA G.I)'
    elif res >= 1928 and res <1946:
        return 'Silent'
    elif res >= 1946 and res < 1965:
        return 'Baby Boomer'
    elif res >= 1965 and res <1981:
        return 'Gen X'
    elif res >= 1981 and res <1997:
        return 'Millennial'
    elif res >= 1997 and res < 2013:
        return 'Gen Z'
    elif res >= 2013 and res < current_year:
        return 'Generation Alpha'
    elif res < 1433:
        return 'Monkeyboiiii'
    elif res > current_year:
        return "IDK that's the future bro"
    else:
        return 'Try again'



def main_function():
    while True:
        res = input('Enter year of birth> ')
        if res.upper() == 'Q' or res.upper() == 'QUIT':
            return False
        elif res.upper() == 'CLEAR':
            os.system('cls')
            return main_function()
        elif isinstance(int(res), int) != True:
            try:
                print('Error. Try using and integer!')
            finally:
                return True
        print(find_gen(res))
        
main_function()
