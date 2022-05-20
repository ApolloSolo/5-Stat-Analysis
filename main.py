import pandas as pd
from stats import *

df = pd.read_excel('pcw.xlsx')


all24LNAPL = fourStats(df, "24-Hr LNAPL")
zone1LNAPL = fourStats(df, "Z-1 LNAPL")
zone2LNAPL = fourStats(df, "Z-2 LNAPL")
zone3LNAPL = fourStats(df, "Z-3 LNAPL")

print("{}{}" .format("24_HR LNAPL Stats: ", all24LNAPL))
print("{}{}" .format("Zone-1 LNAPL Stats: ", zone1LNAPL))
print("{}{}" .format("Zone-2 LNAPL Stats: ", zone2LNAPL))
print("{}{}" .format("Zone-3 LNAPL Stats: ", zone3LNAPL))
print(round(all24LNAPL["mean"] * 7, 2) * 4)