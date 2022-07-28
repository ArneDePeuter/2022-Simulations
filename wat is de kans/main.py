from random import randint as randint
from matplotlib import pyplot as plt

testrange = 50

list = []
getal_list = []
zelfde_perc_list = []
som_perc_list = []
gevaar_list = []

for getal in range(3,testrange+1):
    zelfde = 0
    som = 0
    getest = 0
    for p1 in range(1,getal+1):
        for p2 in range(1,getal+1):
            if p1+p2 == getal:
                som += 1
            elif p1 == p2:
                zelfde += 1
            getest += 1

    zelfde_perc = (zelfde/getest)*100
    som_perc = (som/getest)*100

    print(round((getal/getest)*100), "%")

    gevaar_list.append(zelfde_perc+som_perc)
    getal_list.append(getal)
    zelfde_perc_list.append(zelfde_perc)
    som_perc_list.append(som_perc)
    list.append((getal, zelfde_perc, som_perc))

for i in list:
    print("getal:", i[0])
    print("zelfde_perc:", i[1])
    print("som_perc:", i[2])
    print()

plt.plot(getal_list, zelfde_perc_list)
plt.plot(getal_list, som_perc_list)
plt.plot(getal_list, gevaar_list)
plt.show()
