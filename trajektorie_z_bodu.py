import pandas as pd
import numpy as np

OpenFile = open("EO_2024_04_02_Cervene_Pecky.txt", 'r')
Lines = OpenFile.readlines()
OpenFile.close()
WriteFile = open("test_data" + ".txt", 'w')
WriteFile.write("number x y z \n")
for Line in Lines:
    if "." in Line:
        Line2 = Line.replace("\t", " ")
        while "  " in Line2:
            Line2 = Line2.replace("  ", " ")
            Line2 = Line2.lstrip()
        WriteFile.write(Line2)
WriteFile.close()
OpenFile = open("test_data.txt", 'r')
Lines = OpenFile.readlines()
OpenFile.close()
WriteFile = open("test_data_" + ".txt", 'w')
WriteFile.write("number_ x_ y_ z_ \n")
WriteFile.writelines(Lines[2:])


vstup1 = pd.read_csv("test_data.txt", sep=" ")
vstup2 = pd.read_csv("test_data_.txt", sep=" ")
df=pd.DataFrame(vstup1)
df2 = pd.DataFrame((df.loc[:,["number","x","y","z"]]))
df3=pd.DataFrame(vstup2)


result = df2.join(df3)

result['vzdalenost'] = result.apply(lambda row: pow(pow((row.x-row.x_),2) + pow((row.y-row.y_),2),1/2), axis = 1)

#result.to_csv("test_data_CSV.txt", index=False)
#print(result)

vystup= pd.DataFrame(result)

for x in range()
vystup.loc[1, "vzdalenost"] = result.loc[2, "vzdalenost"]

print(vystup)

#for _ in range(len(vystup)):
#    if result.loc[_,['vzdalenost']] < 8:


#while vystup.loc ['vzdalenost']
#print(result.loc[3,['vzdalenost']])








