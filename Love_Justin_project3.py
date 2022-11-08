#Justin Love
#Project 3
#Garden Size
#9/21/22

import math
def welcome():                                      #my  welcome function
    print("Welcome to the garden plot calculater")
def total_square(length):                                 #the total square foot of the garden function
    a=length**2
    return (round(a,1))
def fountain(r):                                     #the area of the fountion 
    b=math.pi*(r**2)
    return (round(b,1))
def flower_bed(a,b):                                   #the square foot of the garden function 
    c = a - b
    return (round(c,1))
def soil(flower_bed ,depth):                                         #the amount of soil you would need
    d = flower_bed*depth
    return (round(d,1))

def main():
    
    #asking user for there input
    welcome()
    length= float(input("Please enter the length of one of the sides of the garden: "))
    r = float(input("Please enter the radius of the fountain: "))
    depth = float(input("Please enter the depth of the flower bed: "))
    area = total_square(length)
    total = fountain(r)
    circle = flower_bed(area,total)
    x = soil(circle,depth)
    #print the output
    print("The total square footage of the garden is",area)
    print("The square footage of the fountain is", total)
    print("The square footage of the flower bed is",circle)
    print("The flower bed need",x,"cubic feet of soil")

main()                                  #call the main function
