import random as r

class Bear:
    _n_bears = 0

    def __init__(self):
        Bear._n_bears += 1
        self._name = 'Bear' + str(Bear._n_bears)

    def __str__(self):
        return self._name

class Fish:
    _n_fishs = 0

    def __init__(self):
        Fish._n_fishs += 1
        self._name = 'Fish' + str(Fish._n_fishs)

    def __str__(self):
        return self._name

class River:
    def __init__(self, long):
        self._long = long
        self._river = []
        for x in range(long):
            e = r.randint(1, 3)
            match e:
                case 1:
                    self._river.append(Bear())
                case 2:
                    self._river.append(Fish())
                case 3:
                    self._river.append(None)
                case _:
                    self._river.append(None)
    
    def __str__(self):
        return '|'.join(map(str, self._river))

    def advace_time_step(self):
        for idx, element in enumerate(self._river):
            # Si la posición esta vacia o es el final del rio no se mueve.
            if element != None and idx != len(self._river) - 1:
                # Random 50% possibility the animal move.
                if r.random() <= 0.5:
                    print(element, " is moving!")
                    if self._river[idx + 1] == None:
                        self._river[idx + 1] = self._river[idx]
                        self._river[idx] = None
                    elif type(self._river[idx]) is type(self._river[idx + 1]):
                        none_elements = [i for i, x in enumerate(self._river) if x == None]
                        if none_elements:
                            self._river[r.choice(none_elements)] = type(self._river[idx])()
                    elif not isinstance(self._river[idx], type(self._river[idx + 1])):
                        if isinstance(self._river[idx], Fish):
                            print(self._river[idx], " dead by ", self._river[idx + 1])
                            self._river[idx] = None
                        elif  isinstance(self._river[idx + 1], Fish):
                            print(self._river[idx + 1], " dead by ", self._river[idx])
                            self._river[idx + 1] = None

if __name__ == '__main__' :
    river = River(10)
    print(river)
    days = 10
    for _ in range(days):
        river.advace_time_step()
        print(river)
    
                        


    
