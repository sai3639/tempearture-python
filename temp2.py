# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 20:24:31 2021

@author: saira

"""
usertemp = float(input("Enter a temperature between 0 and 260 deg C: "))
templist = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260]
volume = [0.0009977, 0.0009996, 0.0010057, 0.0010149, 0.0010267, 0.0010410, 0.0010576, 0.0010769, 0.0010988, 0.0011240, 0.0011531, 0.0011868, 0.0012268, 0.0012755]
energy = [0.04, 83.61, 166.92, 250.29,333.82, 417.65, 509.91, 586.8, 672.55, 759.47, 847.92, 938.39, 1031.6, 1128.5]
enthalpy = [5.03, 88.61,171.95, 255.36, 338.96, 422.85, 507.19, 592.18, 678.04, 765.09, 853.68, 944.32, 1037.7, 1134.9]
entropy = [0.0001, 0.2954, 0.5705, 0.8287, 1.0723, 1.3034, 1.5236, 1.7344, 1.9374, 2.1338, 2.3251, 2.5127, 2.6983, 2.8841]
#x = 0

#find the temp min and temp max
tempMin = 0
tempMax = 0
min_index = 0
max_index = 0
for x in range(len(templist)):
    min_index +=1
    max_index +=1
    if templist[x] < usertemp and templist[x+1] > usertemp:
        tempMin = templist[x]
        tempMax = templist[x+1]
        #max_index +=1
        actual_max = max_index
        #print(actual_max)
        min_index -= 1
        actual_min = min_index

# find the volume values
vol1 = 0
vol2 = 0
#actual_vol = 0
for vol in range(len(volume)):
    vol1 = volume[actual_min]
    vol2 = volume[actual_max]
    slope = (vol2 - vol1)/(tempMax-tempMin)
actual_vol = (vol2 - vol1)/(tempMax-tempMin)*(usertemp - tempMin) + vol1

# find energy vals
ene1 = 0
ene2 = 0
for ene in range(len(energy)):
    ene1 = energy[actual_min]
    ene2 = energy[actual_max]
    slope = (ene2 - ene1)/(tempMax-tempMin)
#print(slope)
#print(ene1)
#print(ene2)
actual_ene = (ene2 - ene1)/(tempMax-tempMin)*(usertemp - tempMin) + ene1

#find enthalpy vals
enth1 = 0
enth2 = 0
for enth in range(len(enthalpy)):
    enth1 = enthalpy[actual_min]
    enth2 = enthalpy[actual_max]
actual_enth = (enth2 - enth1)/(tempMax-tempMin)*(usertemp - tempMin) + enth1

# find entropy vals
ent1 = 0
ent2 = 0

for ent in range(len(entropy)):
    ent1 = entropy[actual_min]
    ent2 = entropy[actual_max]
actual_ent = (ent2 - ent1)/(tempMax-tempMin)*(usertemp - tempMin) + ent1


#print(actual_vol, actual_ene, actual_enth, actual_ent)

print("Properties at {:.1f}".format(usertemp), "deg C are:")
print("Specific volume (m^3/kg): {:.7f}".format(actual_vol))
print("Specific internal energy (kJ/kg): {:.2f}".format(actual_ene))
print("Specific enthalpy (kJ/kg): {:.2f}".format(actual_enth))
print("Specific entropy (kJ/kgK): {:.4f}".format(actual_ent))