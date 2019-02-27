h=int(input("nhap chieu cao(cm): "))
m=int(input("nhap can nang(kg): "))
h=h/100
BMI=m/(h*h)
if(BMI<16): print("Severely underweight")
elif(BMI<18.5): print("Underweight")
elif(BMI<25): print("Normal")
elif(BMI<30): print("Overweight")
else: print("Obese")