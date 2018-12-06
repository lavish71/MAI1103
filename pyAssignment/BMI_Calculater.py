#BMI Calculater
foot=.3048
inch=.0254

#Enter Your Height in foot
heightFoot=input("Enter your height in foot : ")
#Enter Your Height in inch
heightInch=input("Enter your height in inch : ")
#Enter Your Height in  meter
heightMeter=heightFoot*foot+heightInch*inch
#Enter Your weight in kg
weight=input("Enter your weight in kg : ")
#This is Your BMI
myBmi=(weight)/(heightMeter**2)
print (myBmi)
