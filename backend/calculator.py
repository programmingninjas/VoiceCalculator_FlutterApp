import math
from numerizer import numerize
from sympy import sympify,solve,integrate,diff,symbols

x = symbols('x')

def calculate(input):

    def multiply(*args):

        for i in args:

            if i == args[0]:

                product = 1

            product = i * product

        return product

    def divide(a, b):

        try:

            division = a/b

            return division

        except:

            print('error')

    def factorial(n, x=None):

        try:

            return math.factorial(n)

        except:

            print('Number should be a whole number')

    def subtract(a, b):

        return a-b

    def power(base, raised):

        return math.pow(base, raised)

    def log(x, base=None):

        try:
            try:
                return math.log(x, base)
            except:
                return math.log(x)

        except:
            print('undefined')

    def square_root(x, n=None):

        try:

            return math.sqrt(x)

        except:
            print('square root of a negative number is not defined')


    string = input[:len(input)-1] if input[-1] == '.' else input

    string = string.replace(',','')

    text0 = (string.lower()).split()

    values = []

    numerals = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','billion','million','hundred','thousand']

    for num in numerals:              #converting numerals if present into digits

        if num in text0:

            for i in range(len(text0)):

                try:
                    if not text0[i].isdigit():

                        text0[i] = numerize(text0[i])
                        print(text0)
                except:
                    pass

    try:

        global text
        
        if 'evaluate' in input.lower():

            str_ = input.lower().replace('evaluate','')
            data = (((str_.replace(' ','')).replace('square','**2')).replace('into','*').replace('cube','**3')).lower()
            expr = sympify(data)
            roots = solve(expr)
            text = 'Answer is : ' + str(roots)

        elif 'integrate' in input.lower():

            str_ = input.lower().replace('integrate','')
            data = (((str_.replace(' ','')).replace('square','**2')).replace('into','*').replace('cube','**3')).lower()
            expr = sympify(data)
            value = integrate(expr,x)
            text = 'Answer is : ' + str(value)

        elif 'differentiate' in input.lower():

            str_ = input.lower().replace('differentiate','')
            data = (((str_.replace(' ','')).replace('square','**2')).replace('into','*').replace('cube','**3')).lower()
            expr = sympify(data)
            value = diff(expr,x)
            text = 'Answer is : ' + str(value)

        elif 'add' in input.lower() or '+' in input:

            for i in text0:

                if i.replace('.', '').isdigit():

                    if '.' in i:

                        values.append(float(i))

                    else:

                        values.append(int(i))

            text='Answer is : '+ str(sum(values))
            

        elif 'subtract' in input.lower() or '--' in input:

            for i in text0:

                if i.replace('.', '').isdigit():

                    if '.' in i:

                        values.append(float(i))

                    else:

                        values.append(int(i))

            text='Answer is : '+ str(subtract(values[0], values[1]))

        elif 'multiply' in input.lower() or '*' in input:

            for i in text0:

                if i.replace('.', '').isdigit():

                    if '.' in i:

                        values.append(float(i))

                    else:

                        values.append(int(i))

            text='Answer is : ' + str(multiply(*values))

        elif 'divide' in input.lower() or '/' in input:

            for i in text0:

                if i.replace('.', '').isdigit():

                    if '.' in i:

                        values.append(float(i))

                    else:

                        values.append(int(i))

            text='Answer is : ' + str(divide(values[0], values[1]))


        elif 'raised' in input.lower() or 'power' in input.lower():

            for i in text0:

                if i.replace('.', '').isdigit():

                    if '.' in i:

                        values.append(float(i))

                    else:

                        values.append(int(i))

            text='Answer is : ' + str(power(values[0], values[1]))

        elif 'factorial' in input.lower():

            for i in text0:

                if i.replace('.', '').isdigit():

                    if '.' in i:

                        values.append(float(i))

                    else:

                        values.append(int(i))

            text='Answer is : ' + str(factorial(values[0]))

        elif 'root' in input.lower() or 'sqrt' in input.lower():

            for i in text0:

                if i.replace('.', '').isdigit():

                    if '.' in i:

                        values.append(float(i))

                    else:

                        values.append(int(i))

            text='Answer is : ' + str(square_root(values[0]))

        elif 'log' in input.lower():

            for i in text0:

                if i.replace('.', '').isdigit():

                    if '.' in i:

                        values.append(float(i))

                    else:

                        values.append(int(i))

            try:

                text='Answer is : ' + str(log(values[0],values[1]))

            except:

                text='Answer is : ' + str(log(values[0]))

        
    except:
    
        text = 'Error'
        
    
    return text