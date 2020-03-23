def simplify_fraction(nominator, denominator):
    if nominator>denominator:
        f = denominator
    else:
        f = nominator
    for fact in range(1, f+1):
        if nominator == 1 or denominator == 1:
            break
        else:
            x = nominator % fact
            y = denominator % fact
            if x == 0 and y == 0:
                nominator //= fact
                denominator //= fact
    return(nominator, denominator)


def collect_fractions(fractions):
    def sum_two_fractions(a, b):
        denom = a[1]*b[0] + a[0]* b[1]
        numer = a[1]*b[1]
        return (denom, numer)

    def fract_chunks(fractsList, n):
        for i in range(0, len(fractsList), n):
            yield fractsList[i:i + n]

    def add_pairs_in_list(fractList):
        while len(fractList)>1:
            newlist = []
            for i in fract_chunks(fractList, 2):
                if len(i) == 2:
                    newlist.append(sum_two_fractions(i[0],i[1]))
                else:
                    newlist.append(i[0])
            fractList = newlist[:]    
        return(fractList[0])
    x = add_pairs_in_list(fractions)
    return simplify_fraction(x[0],x[1])

def sort_fractions(fractions, ascending = True):
    if ascending == True:
        sortedFractions = sorted(fractions, key=lambda f: (f[0]/f[1]))
    elif ascending == False:
        sortedFractions = sorted(fractions, key=lambda f: (f[0]/f[1]), reverse = True)
    return sortedFractions
   


def main():
    pass

if __name__ == "__main__":
    main()