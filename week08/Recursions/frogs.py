def make_swamp(brownfrogs, greenfrogs, n):
    brownfrogs = brownfrogs*n
    greenfrogs = greenfrogs*n
    return  brownfrogs + '_' + greenfrogs

def move_frog(swamp):
    swamp = [i for i in swamp]
    swampstates = []
    for i in range(len(swamp)):
        if swamp[i] == '_':
            tempswamp = swamp[:]
            if swamp[i-1] == '>':
                tempswamp[i-1] = '_'
                tempswamp[i] = '>'
                swampstates.append(''.join(tempswamp))
                tempswamp = swamp[:]
                
            if swamp[i-2] == '>':
                tempswamp[i-2] = '_'
                tempswamp[i] = '>'
                swampstates.append(''.join(tempswamp))
                tempswamp = swamp[:]
            if i+1 < len(swamp):
                if swamp[i+1] == '<':
                    tempswamp[i+1] = '_'
                    tempswamp[i] = '<'
                    swampstates.append(''.join(tempswamp))
                    tempswamp = swamp[:]
            if i+2 < len(swamp):
                if swamp[i+2] == '<':
                    tempswamp[i+2] = '_'
                    tempswamp[i] = '<'
                    swampstates.append(''.join(tempswamp))
                    tempswamp = swamp[:]               
            return swampstates
    return swampstates

def find_states(start, final):
    next = []
    for frogset in start:
        newstates = move_frog(frogset[-1])            
        for state in newstates:
            frogset_list = [frogset]
            frogset_list.append(state)
            if ( state == final ):
                return frogset_list
            next.append(frogset_list)
    return next

def find_pattern(start, final):
    temp=[[start]]

    while(temp[-1] != final):
        temp = find_states(temp, final)
    return temp

def frogs_puzzle(n):
    swamp = make_swamp('>','<', n)
    fin = make_swamp('<','>', n)

    return(find_pattern(swamp, fin))

if __name__ == "__main__":
    pass


