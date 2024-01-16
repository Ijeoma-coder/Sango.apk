import os
import sys
#p1v1, this function is used to display boyle's law
def boyles_law():
      import os
      print (" Boyle's law states that",'\n'
      ,"the pressure of an ideal gas is inversely proportional to the volume, given that temperature is constant.")
      print ('\033[1;3m'+  "(P1 V1)=(P2 V2)" + '\033[0m')


#charles law =v/t
def charles_law():
    print ("It seems like you looking for charles law")
    charles_law=("States that the volume of an ideal gas is directly proportional to it's temperature provided that the pressure is constant")
    charles_equation = ( ''' V = Volume of gas 
    T = temperature ''')
    print(charles_law ,'\n', charles_equation)
    print (" (V1/T1)=(V2/T2)  ")

#function for ideal gas equation
def ideal():
      import os
      ideal_gas=('''''  
 PV=nRT 
    where,
 N=no. of moles, 
 t= temperature 
 p= pressure in Hg
 v= volume in cm**3
 ''''')
      print (ideal_gas)

#function for equations of motion 
def motion_equ():
    equ_1='\033[1;3m' + "v= u + at".upper() + '\033[0m'     
    equ_2='\033[1;3m' + "S= ut + 1/2a(t^2)".upper() + '\033[0m'
    equ_3='\033[1;3m' +  "V^2= u^2 + 2as".upper()  + '\033[0m'

    print("Welcome to the Equations of motions window! You can DISPLAY equations of motions here.")

    a=['v','u','a','t']
    b= ['s','u','a','t']
    c=['v','u','a','s']

 #allow the user to input 4 different values/ characters
 # Initialize an empty list
    empty_list = []

 # Ask the user to input 4 elements
    for i in range(4):
        element = input("Please enter your given values " + str(i+1) + ": ")
        empty_list.append(element)

    print(empty_list)

    if empty_list == a:
        print(equ_1)
    elif empty_list == b:
        print(equ_2)
    elif empty_list == c:
        print(equ_3)

#function for ohm's law
def ohm():
      import os

      print('\033[1m' + "Ohm's law states that the potential difference of a circuit is directly proportional to it's resistance provided the current remains constant"
      '\033[0m')
      print('\033[3m' + "V = IR" + '\033[0m')
      print("where V= Potential Difference",'\n',
      "I= Current",'\n',
      "R= Resistance")



  # Plac   statements at the top

#function for the display of the other available laws 
def print_law():
      import string
      laws = {
        "newtons laws of motion": "These laws govern how the motion of physical objects change. They define the fundamental relationship between the acceleration of an object and the forces acting upon it.",
        "law of universal gravitation": "This law, proposed by Sir Isaac Newton, states that an object attracts another object in direct proportion to their combined mass and inversely related to the square of the distance between them.",
        "conservation of mass and energy": "This principle, introduced by Albert Einstein, states that mass and energy can neither be created nor destroyed.",
        "laws of thermodynamics": "These laws are specific manifestations of the law of conservation of mass-energy as it relates to thermodynamic processes.",
        "archimedes principle": "According to this principle, when a body is partially or totally immersed in a liquid, it experiences a thrust force, which is equal to the weight of the liquid displaced by it."
    }

      law_name = input("Enter a law name: ")  # Get user input
      law_name = law_name.lower()  # Convert input to lowercase
      law_name = law_name.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation

      if law_name in laws:
           print(laws[law_name])
   
      else:
        print("Law not found. Please enter a valid law name.")



#function that serves as a hub to all other functions concerning the equations and law window 
def display_equ():
    print ('--------------------------------')

    print("Welcome to the Equations and law Window.") ,'\n',
    print (''''The available laws are listd below  ''''')

    equ_list = ["Charle's law","Boyle's law","Ideal gas law","Ohm's law","Equations of motion","newtons laws of motion",
 "law of universal gravitation","conservation of mass and energy","laws of thermodynamics","archimedes principle"]

    for i in range (10): 
        print (equ_list[i])

    print ("If you desire the last 5 on the list, please select 'Other' to continue.")

    desire_equation=str(input("Which equations/law do you want to display  ")).lower()

    if desire_equation == "charle's law" :
           charles_law()
    elif desire_equation == "equations of motion" :
           motion_equ()
    elif desire_equation == "boyle's law" or  desire_equation == "boyle law" :
           boyles_law()
    elif desire_equation == "ideal gas equation" :
           ideal()
    elif desire_equation ==  desire_equation == "ohm law" or desire_equation == "ohm's law":
           ohm()   
    elif  desire_equation == 'other':
           print_law()  
    else:
        print("Unavailable equation or law")








print ('\033[1m'  +  " Welcome to Sango, your solution to the headache of physics.", '\n' , "Please know that this is a beta release,",'\n',
"There will be some unavailable things but please be patient with us", '\n',
"From yours truly, Ij" + '\033[0m')

#allow user to pick function 
'\n'
print ("Please bear with us as  Sango an only only offer two functions which are solving questions and displaying laws and equtions")

answer=int(input(''''' What do you want Sango to do for you?
If you wanna Solve, type '1' 
OR
If you wanna Display laws and equations, type '2'___ '''''))

if answer == 1 :
      import solve_formula
elif answer == 2:
      display_equ() 