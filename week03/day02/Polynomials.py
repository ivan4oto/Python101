import sys


class Polynomial:
    def __init__(self, stringfunction):
        self.stringfunction = stringfunction.replace('*','')
        self.elements = self.stringfunction.split('+')

    def get_func_elements(self):
        return self.elements

    def get_derivative(self):
        result = ''

        #derivative of a constant is 0
        if (len(self.elements) == 1) and ('x' not in self.elements[0]):
            return '0'
        #multiplier of 1 and raised to the power of 1
        if self.elements[0] == '1x':
            return '1'

        

        for i in self.elements:
            #if constant
            if 'x' not in i:
                pass

                            
                
            elif 'x^' in i:
                i = i.split('x^')

                #cleans .split leftover
                if '' in i:
                    i.remove('')

                # if multiplier and x raised tothe power of n
                if len(i) == 2:
                    toadd = int(i[0])*int(i[1])
                    toadd2 = int(i[1])-1
                    result = result + "{}x{}".format(str(toadd),str(toadd2))

                #if x to the power of n, without multiplier
                elif len(i) == 1:
                    result = result + "{}x{}+".format(str(int(i[0])),str(int(i[0])-1))

            #if multiplier and x
            elif i[-1] == 'x':
                i = i.split('x')
                result = result + "+{}".format(i[0])

        #cleans leftovers
        def clean_d(d):
            d = d.replace('x1','x')
            d = d.split("+")
            if '1' in d:
                d.remove('1')
            d = '+'.join(d)
            d = d.strip('+')
            return d
        result = clean_d(result)

        return result
    
    def __str__(self):
        b = self.get_derivative().split('+')
        b = ' + '.join(b)
        for i in range(len(b)):
            if b[i]=='x' and b[i-1].isdigit():
                b = b.replace('x','*x')

        b = b.strip('*')
        
        a = self.stringfunction.split('+')
        a = ' + '.join(a)
        for y in range(len(a)):
            if a[y]=='x' and a[y-1].isdigit():
                a = a.replace('x','*x')

        a = a.strip('*')

        b = "The derivative of f(x) = {} is:\nf'(x) = ".format(a) + b
        return b


def main():
    pnm = sys.argv[1]
    p = Polynomial(pnm)
    print(p)

if __name__ == "__main__":
    main()  