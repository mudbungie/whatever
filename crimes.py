# Don't do this

import random

class Crime:
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
    def __hash__(self):
        return int(10000 * random.random())
    def __repr__(self):
        address = super(Crime, self).__repr__()
        return f'Crime object at location {address} but with hash {self.__hash__()}'

if __name__ == "__main__":
    crimes = set()
    crime = Crime()
    for i in range(3):
        # after the first one, this should be a no-op, because adding an object to a set is idempotent
        crimes.add(crime)
    for crime in crimes:
        # ... and yet...
        print(crime)

