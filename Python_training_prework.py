# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:53:06 2015

@author: AGAN26R
"""

# Affectations
x,y,z = 1,2,3
print x
print y
print z


# Boucles
for i in [1,2,3,4,5,6]:
    print "The value of i is ",i," ..."

for value in range(50):
    print "My value is", value
    
x = 10
while x >= 0:
    print "x is still not negative.", x
    x = x-1    
    
# saisies    
    
n = raw_input("What's your name ?")
print "Hello ", n

n = input("What's your age ?")
print "So you are ", n, " years old"

# Définitions de listes
name = ["Cleese", "John"]
y = 5
z = 8
x = [[1,2,3],[y,z],[[[]]]]

#accès par index
print name[1], name[0] # Prints "John Cleese"
name[0] = "Smith"
print name[1], name[0] # Prints "John Smith"

# accès par slice
x = ["spam","spam","spam","spam","spam","eggs","and","spam","bacon"]
print x[5:7] # Prints the list ["eggs","and"]
y = [x[5:7], x[8]]
print y[0:4] # Prints the list ["eggs","and"],"bacon"]

print y[-1] # Prints "bacon"

#Dictionnaires
{ "Alice" : 23452532, "Boris" : 252336,
  "Clarice" : 2352525, "Doris" : 23624643}

person = { 'first name': "Robin", 'last name': "Hood",
           'occupation': "Scoundrel" }
           
print person['first name']           
print person['last name']           
person['last name']="Hero"
print person['first name'], person['last name']           

# fonctions
def square(x):
    return x*x

print square(2) # Prints out 4

def change(some_list): # renverse la liste
    x = some_list[0]
    some_list[0] = some_list[2]
    some_list[2] = x;
    
x = [1,2,3]
change(x)
print x # Prints out [3,2,1]


# Portée des variables
def nochange(x):
    x = 0; # Variable locale
    print "X", x;

y = 1
nochange(y)
print y # Prints out 1

# Les fonctions sont aussi des valeurs
queeble = square
print queeble(2) # Prints out 4


# Jouons avec les classes

# Le panier
class Basket:

    # Always remember the *self* argument
    def __init__(self,contents=None):
        self.contents = contents or []

    def add(self,element):
        self.contents.append(element)

    def print_me(self):
        result = ""
        for element in self.contents:
            result = result + " " + `element`
        print "Contains:"+result

    # un getter pour accéder à un élement du panier
    def __getitem__(self,index):
        return self.contents[index]
        
        
#instanciation du Panier

# premier test
print "Premier test\n"

b = Basket()
b.print_me()
b.add("Test")
b.print_me()


class VideoGame :
    
    def __init__(self,Console,price,Name="Unkwnown"):
        self.Name = Name
        self.Console = Console
        self.price = price
    
    def print_me(self):
        print "The game ", self.Name , " for ", self.Console, "costs ", self.price, " euros" 
    
    
    def __str__(self):
        print "The game ", self.Name , " for ", self.Console, "costs ", self.price, " euros" 


v = VideoGame("PS3",40,"GTA V")
b.add(v)
print "Basket ", b.print_me(),"\n"

# différents accès
print "Second test\n"

print b.contents[0]
# accès avev le __getitem__
print b[0]

# accès avec le __getitem__
print b[1] # ce n'est pas une chaîne - Peut-on typer?
print b.contents[1].print_me()
         
# J'achète des jeux
panier = Basket()
jeu1 = VideoGame("PS VITA",40,"FIFA 2016")     
jeu2 = VideoGame("PS3",60,"GTA V")     
jeu3 = VideoGame("PS3",25,"UNCHARTED 3")     

panier.add(jeu1)
panier.add(jeu2)
panier.add(jeu3)

# Show object list         
panier.contents[0:3]          

# Print list elements          
for elements in panier:
    elements.print_me()
         
# Les exceptions
def unsafe_division(a,b):
    return a/b

def safe_division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return None
        
print safe_division(10,2)        
print safe_division(10,0)  

print unsafe_division(10,2)        
print unsafe_division(10,0)  # Oupsss une exception  

dir(panier)
help(panier)
