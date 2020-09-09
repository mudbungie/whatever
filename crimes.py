# Don't do this

import random

class Crime:
    def __eq__(s, other):
        return s.__hash__() == other.__hash__()
    def __hash__(s):
        return int(10000 * random.random())
    def __repr__(s):
        return str(s.__hash__())

if __name__ == "__main__":
    crimes = set()
    crime = Crime()
    for i in range(10):
        crimes.add(crime)
    print(crimes)
