import pandas as pd
from matplotlib import pyplot as plt
import os
import time

with open("YOUR OUTPUT TEXT FILE HERE", "r+") as f:
    old = f.read()  # read everything in the file



import re
non_decimal = re.compile(r'[^\d\n. ]+')
old = non_decimal.sub('', old)


old = old.replace("  9.79930 2   398645.0 32. ", "")
old = old.replace("    22683    295.18 ", "")
old = old.replace("                   0       0                    0", "")
old = old.replace("     2                                 ", "")
# old = old.replace("\n \n", "\n")


old = old.replace("                  ", " ")
old = old.replace("                 ", " ")
old = old.replace("                ", " ")
old = old.replace("               ", " ")
old = old.replace("              ", " ")
old = old.replace("             ", " ")
old = old.replace("            ", " ")
old = old.replace("           ", " ")
old = old.replace("          ", " ")
old = old.replace("         ", " ")
old = old.replace("        ", " ")
old = old.replace("       ", " ")
old = old.replace("      ", " ")
old = old.replace("     ", " ")
old = old.replace("    ", " ")
old = old.replace("   ", " ")
old = old.replace("  ", " ")
old = old.replace(" 4.801\n", "")
old = old.replace(" .\n", "")
old = old.replace(" 5.001 5.501\n", "")
old = old.replace(" \n", "")
old = old.replace("\n\n", "")
# print(old)

file1 = open("YOUR OUTPUT TEXT FILE HERE","w+")
file1.readline()
file1.write(old)
file1.close()
data = pd.read_csv("YOUR OUTPUT TEXT FILE HERE", sep=" ", header=None)
data.columns = ["Null", "Time", "Accel", "Vel", "Height", "HorizDist", "Alpha", "Beta", "Theta", "Pq", "M0+Me"]
del data['Null']
Time = data["Time"]
Accel = data["Accel"]
Vel = data["Vel"]
Height = data["Height"]
HorizDist = data["HorizDist"]
Alpha = data["Alpha"]
Beta = data["Beta"]
Theta = data["Theta"]
Pq = data["Pq"]
M0Me = data["M0+Me"]

# print(data)
plt.subplot(3,1,1)
plt.plot(Time, Accel)
plt.subplot(3,1,2)
plt.plot(Time, Vel)
plt.subplot(3,1,3)
plt.plot(HorizDist, Height)

# plt.subplot(8,1,4)
# plt.plot(Time, Alpha)
# plt.subplot(8,1,5)
# plt.plot(Time, Beta)
# plt.subplot(8,1,6)
# plt.plot(HorizDist, Theta)
#
# plt.subplot(8,1,7)
# plt.plot(Time, Pq)
# plt.subplot(8,1,8)
# plt.plot(Time, M0Me)

plt.show()
