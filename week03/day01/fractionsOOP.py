from fractions_task import simplify_fraction, collect_fractions, sort_fractions


class Fractions(object):
    def __init__(self, fractions):
        self.fractions = fractions

    def get_fractions(self):
        return self.fractions

    def sort_fractions(self, ascending = True):
        if ascending == True:
            self.fractions = sorted(self.fractions, key=lambda f: (f[0]/f[1]))
        elif ascending == False:
            self.fractions = sorted(self.fractions, key=lambda f: (f[0]/f[1]), reverse = True)
        
    def sum_fractions(self):
        x = collect_fractions(self.fractions)
        return x

    def __repr__(self):
        return "This is a fractions list, containing fractions: {}".format(self.fractions)


    def __str__(self):
        toprint = ""
        for f in self.fractions:
            num = f[0]
            den = f[1]
            toprint += "{}/{}, ".format(num, den)
        toprint = toprint[:-2]
        return toprint


def main():
    pass


if __name__ == "__main__":
    main()  