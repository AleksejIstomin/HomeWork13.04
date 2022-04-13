# 7.   Izveidot programmu, kura prasa lietotājam ievadīt cilindra rādiusu un tā augstumu,
#           tiek aprēķināts cilindra laukums un tilpums. Rezultāts tiek parādīts konsolē.
#  Formulas:
#  tilpums = 3.14 * rādiuss * rādiuss * augstums
#  laukums = 2 * (3.14 * rādiuss * rādiuss) + augstums * (2 * 3.14 * rādiuss)

user_height = input("Enter height:")
user_radius = input("Enter radius:")
print("Volume:",3.14*int(user_radius)*int(user_radius)*int(user_height))
print("Area:",(2*(3.14*int(user_radius)*int(user_radius))+int(user_height)*(2*3.14*int(user_radius))))