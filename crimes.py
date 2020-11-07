# Don't do this

import random

class Crime:
    def __eq__(s, other):
        return s.__hash__() == other.__hash__()
    def __hash__(s):
        return int(10000 * random.random())
    def __repr__(s):
        address = super(Crime, s).__repr__()
        return f'Crime object at location {address} but with hash {s.__hash__()}'

if __name__ == "__main__":
    crimes = set()
    crime = Crime()
    for i in range(3):
        # after the first one, this should be a no-op, because adding an object to a set is idempotent
        crimes.add(crime)
    for crime in crimes:
        # ... and yet...
        print(crime)

