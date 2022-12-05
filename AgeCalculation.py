import inflect
from datetime import date, datetime, timedelta
from num2words import num2words

# dnes = date.today() stores the current date in a variable, and can be accessed dnes.year, dnes.month, dnes.day
# prompt user for birthday, I can split on "-" which is stored in a list, that I can access via indexing.
# I can substract dnes.year -

rojdenden = input("Koga si roden be?: ")

data_rojden = rojdenden.split("-")
godina = int(data_rojden[0])
mesec = int(data_rojden[1])
den = int(data_rojden[2])


dnes = date.today()

testovo = datetime.today() - datetime(1990,1,1)
print(testovo)


zero_or_one = (dnes.month, dnes.day) < (mesec, den)
#if zero_or_one == True:
#    broi_godini = dnes.year - godina - 1
#    broi_meseci = abs(dnes.month - mesec)
#    broi_dni = dnes.day - den
#else:
#    broi_godini = dnes.year - godina
#    broi_meseci = abs(dnes.month - mesec)
#    broi_dni = dnes.day - den

broi_godini = dnes.year - godina - zero_or_one
broi_meseci = abs(dnes.month - mesec)
broi_dni = dnes.day - den

age_in_days = broi_godini

print(f"{num2words(broi_godini)} godini, {broi_meseci} meseca, {broi_dni} dni")

#print(dnes.month == mesec)

print(zero_or_one)

aww = 800 - (5>4)
print(num2words(aww))

