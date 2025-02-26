#circle,rectangle,triangle
#calculate circle area
import math
def calculate_area(shape,dimension1,dimension2=0):
    if shape=="circle":
     pi = math.pi
     area=pi * dimension1 * dimension1
     print(area)

#calculate rectangle area
    elif shape=="rectangle":
      area=dimension1*dimension2
      print(area)

#calculate triangle area
    else:
      area=1/2 * dimension1 * dimension2
      print(area)

#call function
calculate_area("circle",7)
calculate_area("rectangle",3,5)
calculate_area("triangle",8,9)
calculate_area("circle",56)
