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

print ("3D Volume Calculator")
print ("What shape would you like to calculate the volume of?")
print ("Prism, Sphere, Cone, or Cylinder?")
shape = str(input())
if (shape == "Prism"):
    print ("Triangular, Rectangular, or Cuboid?")
    prism = str(input())
    if (prism == "Triangular"):
        #Difine Base Value
        print ("Input base value")
        b = int(input())
        #Difine Height Value
        print ("Input height value")
        h = int(input())
        #Difine Length Value
        print ("Input length value")
        l = int(input())
        v = 0.5*b*h*l
        print (str("the volume is ") + str(v))