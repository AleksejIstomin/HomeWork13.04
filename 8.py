# 8. Izveidot programmu, kura prasa lietotājam sekunžu skaitu. Sekundes tiek pārveidotas par
#     “x hours y minutes z seconds” tipa tekstu.
# Rezultāts tiek parādīts konsolē.

user_input = int(input("Enter seconds:"))
hours = user_input//3600
hours1 = user_input%3600
minutes = hours1//60
seconds = hours1%60
print(hours,"hours",minutes,"minutes",seconds,"seconds")

