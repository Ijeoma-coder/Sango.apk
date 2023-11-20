#('this file if for mastering formula in python')
#1.) list out all constants in the planned formulas
#2.) create all formulas and name as functions which can be used in the main coode and in subsidiary codes as well
#3.) connect formulas to conditions, in the snse that if user types a name, the outline or the requirements for the formula are presented to him for input
#4.) display equations and laws of several things e.g gas laws and equations of law

#function for finding kinetic energy
def kinetic_energy():

    m=int(input("What's your mass?__",))
    v=int(input("What's your velocity?__",))
    solution= ((0.5*m)*(v**2)) 
    print('Your answer is :', solution)
    return solution

#function for finding potential energy
def potential_energy():
    import os
    m=int(input('whats your mass?__',))
    h=int(input("what's your height?___", ))
    g=10
    Answer=m*g*h
    print('Your answer is :', Answer)
    return Answer    

#function for finding electric heat
def electricheat():
    import os
    os.system('color')
    i =int(input("What's your current?__", ))
    '\n'
    v =int(input("What's your voltage?__", )) 
    '\n'
    t=int(input("What's your time?__",))
    '\n'
    #trying to put the notice in italic
    print('\033[1;3m' + 'recall that P=I*V'+ '\033[0m')
    P= int(input("What's your power?__" , )) 
    yes= True
    no= False
    Q= (P*t)
    print("The answer(Q) is :", Q,'W')

#function for finding latent heat
def latent_heat():
    import os
    m=int(input("What's your mass?__",))
    l=int(input("What's your latent heat?__"))
    Q=m*l
    print('Your answer is :', Q)
#Q HAS UP T

#function for finding specific latent heat
def specific_lh():
    import os
    m=int(input("What's your mass?" ,))
    temp2=int(input('Final Temperature'))
    temp1=int(input('Initial Temperature'))
    c=int (input("What's your specific heat capacity"))  
    c_i_p= temp2-temp1
    Q =(m*c)*c_i_p
    print("Your answer is", Q)
    return Q

#fuction that serves as a junction to all other heat solving functions 
def solve_heat():
    print('The available options are:')

    #a list of heat options in normal case
    options=['Electric heat','Heat w SHC','Heat w latent heat']
    for option in options:
         print(f'• {option}')

    #a list of heat options in lowercase
    set_option1=[item.lower() for item in options]

    #a list for heat options in uppercase 
    set_option2=[item.upper() for item in options]

    hope=input(''' Choose from the above___''').lower()

    if  hope == set_option1[0] or hope == set_option2[0] or hope == options[0] :
         specific_lh()
    elif  hope == set_option1[1] or hope == set_option2[1] or hope == options[1] :
        electricheat()
    elif  hope == set_option1[2] or hope == set_option2[2] or hope == options[2] :
        latent_heat()
    else:
        print("Unavailable....")    

#function for finding power 
def power():
    import os
    print("Power is the ratio of work to time taken," '\n''The si unit is watt(W)')
    force=int(input("what's your force?__",))
    d=int(input("What's your distance?__",))
    que=input("Is your distance in m or km?__",)
    m=True
    km=False
    if que==m : 
        m=m
    elif que== km :
        m/=1000
#choose between min hrs and mls        
    t=int(input("What's the time taken?"))
    print("Please select your time unit from the characters in the bracket ")        
    que_2=input("Is your time in Seconds(S)," '\n'
 "Minutes(Min),"   
 " Hours(Hrs),"
 "Or Milliseconds(Ms)" ,)
    if que_2 == 'S' or 's': 
        t=t
    elif que_2 == 'Min' or 'min' : 
        t*=60
    elif que_2 == 'Hrs' or 'hrs' : 
        t*=3600
    elif que_2 == 'Ms' or 'ms'   : 
        t/=1000
    p=float((force*d)/t)
    print ('Your power is,' '\n', p,'Watts(W)')

#function for finding force
def force():

    import os
    newton_1st_law=('\033[3m' + 'Remember kids, Newtons 2nd law states that, \n, "The force of an object is directly proportional to its acc, given that the mass is constant"' +'\033[0m' )
    print (newton_1st_law)
    m=int(input("What's your mass?(g)"))
    g =True
    kg =False
    que=input('IS your mass in g(grams) or kg(kilograms)?')
    if que== True:
        m=m
    elif  que== False :
        m/=1000
    a=int(input("What's your acceleration in ms^-2(metre per second squared)"))
    force=(m*a)    
    print ('YOUR force is , \n ', force,'N')
    print('But how dont you know how to find force tho?')

#function for finding work
def work():
    print ("Work is equals to force times distance, the si unit joules (J)")
    f=int(input("What's your force?(N)"))
    d=int(input("What's your distnace?(m)"))
    w=(f*d)
    print("Yor work is," '\n' , w, 'Joules')
    return w

def velocity():
    import os
    print('\033[1;3m'+"Recall keeds, distance is usually in metres.." + '\033[0m')
    d=int(input("What's your distance/ displacement?_",))
    t=int(input("What's your time?"))
    que_3=input('''WHAT IS THE UNIT OF YOUR TIME,
    CHOOSE FROM THE UNITS IN THE BRACKETS BELOW
    SECONDS(S),
    MINUTES(MIN)
    HOURS(HRS),
    MILLISECONDS(ms)
    MEGASECONDS(Ms)''')
    if que_3 == 's' or 'S' :
        t=t
    elif que_3=='MIN' or'Min' or 'min' :
        t*=60
    elif que_3== 'HRS' or 'Hrs' or 'hrs' :
        t*=3600
    elif que_3== 'ms':
        t*=1000
    elif que_3 == 'MS' or 'Ms' :
        t/=1000   
    velo_city=(d/t)
    print ("Your velocity is"'\n', velo_city,'ms^-1')               
    return velo_city

def acc_ler8():
    #function used to calc the acceleration
    v2=int(input("What is your final velocity?(ms^-2)"))
    #takes in the final velocity

    v1=int(input("What is your initial velocity?(ms^-2)"))  
    #takes in th einitial velocity

    t=int(input("What's your time?"))

    que_3=input('''WHAT IS THE UNIT OF YOUR TIME,
    CHOOSE FROM THE UNITS IN THE BRACKETS BELOW
    SECONDS(S),
    MINUTES(MIN)
    HOURS(HRS),
    MILLISECONDS(ms)
    MEGASECONDS(Ms)''')
    #finds seconds in appropriate unit from the provided unit
    if que_3 == 's' or 'S' :
        t=t
    elif que_3=='MIN' or'Min' or 'min' :
        t*=60
    elif que_3== 'HRS' or 'Hrs' or 'hrs' :
        t*=3600
    elif que_3== 'ms':
        t*=1000
    elif que_3 == 'MS' or 'Ms' :
        t/=1000   
    change_in_v=(v2-v1)
    acceleration=(change_in_v/t)
    print("Your acceleration is,", '\n',  acceleration,'ms^-2')






g= 10
c=1800
h= 6.7*(10**-7)
available=['Potential energy','Kinetic energy','Heat energy','Work','Power','Velocity','Acceleration']

print ("The available formulas are:")
for i in range(7):
    print('\033[1;3m'+ available[i]+ '\033[0m')




Formula=input('Which formula you wanna use?_______').lower()


if Formula == 'potential energy':
     potential_energy()
elif  Formula == 'kinetic enrgy':
     kinetic_energy()
elif  Formula == 'heat energy' :
     solve_heat()
elif  Formula == 'work':
      work()
elif  Formula == 'power':
      power()
elif  Formula == 'velocity':
     velocity()
elif  Formula == 'acceleration':
     acc_ler8()
else : 
    print("Unfrotunately, the formula you requested is unavailable..")     