import math

"""

#Basic Math

#Addition Practice
sum_add = 2 + 14
#Subtraction Practice
diffrerence = 2 - 14
#Multiplication Practice
product = 3 * 7
#Division Practice
quotient = 24 / 6
#Square Root Practice
sqaure = math.sqrt(9)
#Exponent Practice
exponent = 3**2
print (str(sum_add) + " " + str(diffrerence) + " " + str(product) + " " + str(quotient) + " " + str(sqaure) + " " + str(exponent))
print (" ")

#Tileable Discriminant

#Difine "a" Value
print ("Input a value")
a = int(input())
#Difine "b" Value
print ("Input b value")
b = int(input())
#Difine "c" Value
print ("Input c value")
c = int(input())
#Discriminent Equation
An = b**2-4*a*c
print (str("the Discriminant is ") + str(An))
print (" ")

"""

#3D Volume Calculator

print (" ")
print ("My 3D Volume Calculator")
print (" ")
print ("What shape would you like to calculate the volume of?")
print ("Prism, Sphere, Cone, or Cylinder?")
print (" ")
shape = str(input())
print (" ")
if (shape == "Prism"):
    print ("Triangular, Rectangular, or Cuboid?")
    print (" ")
    prism = str(input())
    print (" ")
    if (prism == "Triangular"):
        #Difine Base Value
        print ("Input base value")
        b = int(input())
        print (" ")
        #Difine Height Value
        print ("Input height value")
        h = int(input())
        print (" ")
        #Difine Length Value
        print ("Input length value")
        l = int(input())
        print (" ")
        v = 0.5*b*h*l
        print (str("The volume is ") + str(v))
    if (prism == "Rectangular"):
        #Difine length Value
        print ("Input length value")
        l = int(input())
        print (" ")
        #Difine Width Value
        print ("Input width value")
        w = int(input())
        print (" ")
        #Difine Height Value
        print ("Input height value")
        h = int(input())
        print (" ")
        v = l*w*h
        print (str("The volume is ") + str(v))
    if (prism == "Cuboid"):
        #Difine Side Length Value
        print ("Input side length value")
        sl = int(input())
        print (" ")
        v = sl**3
        print (str("The volume is ") + str(v))
if (shape == "Sphere"):
    #Difine Radius Value
    print ("Input radius value")
    r = int(input())
    print (" ")
    v = (4/3)*math.pi*r**3
    print (str("The volume is ") + str(v))
if (shape == "Cone"):
    #Difine Radius Value
    print ("Input radius value")
    r = int(input())
    print (" ")
    #Difine Height Value
    print ("Input height value")
    h = int(input())
    print (" ")
    v = (h/3)*math.pi*r**2
    print (str("The volume is ") + str(v))
if (shape == "Cylinder"):
    #Difine Radius Value
    print ("Input radius value")
    r = int(input())
    print (" ")
    #Difine Height Value
    print ("Input height value")
    h = int(input())
    print (" ")
    v = h*math.pi*r**2
    print (str("The volume is ") + str(v))
print (" ")
print (str("Thank you for using my volume calculator!"))
print (" ")