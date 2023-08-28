      
def Fibonacci_Generator():
    Number1=0
    Number2=1  
    Range=int(input(' Enter range of the Fibonacci series: '))
    if Range<=0:
        print(' Please enter range greater than 0')
        Fibonacci_Generator()
    else:
        for traverse in range(0,Range):
            Carry= Number2
            Number2 = Number1 + Number2
            Number1 = Carry
            print(Number2,end=',')

Fibonacci_Generator()