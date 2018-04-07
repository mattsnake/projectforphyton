#MATT ANDREW F. SOLATAN
#DICTIONARY

print(" ")
print("SIGNATURE CAR")
print(" ")
CAR = {
            "SORENTO" : "KIA",
            "EVEREST" : "FORD",
            "FORTUNER" : "TOYOTA",
            "ALTERA" : "ISUZU",
            "CIVIC" : "HONDA",
            "Z4" : "BMW",
            "ELANTRA" : "HYUNDAI",
            "288 GTO" : "FERRARI",
            "GT-R" : "NISSAN",
            "MONTERO" : "MITSUBISHI",
            "Nuvolari quattro" : "AUDI",
            "DAKOTA SPORT" : "DODGE",
            "ASCENT" : "SUBARU",
            "RANGE ROVER" : "LAND ROVER",
            "RX" : "LEXUS"
    }

for key, val in CAR.items():
    print(key, "===", val)

#add in dictionary
CAR["COMPASS"] = "JEEP"
CAR["MAZDA 3"] = "MAZDA"
CAR["S60"] = "VOLVO"
CAR["DAWN"] = "ROLLS-ROYCE"
CAR["1500"] = "RAM"
CAR["ILX"] = "ACURA"

print("-"*10)

for key, value in sorted(CAR.items()):     #SORT
    print(key, "===", value)
