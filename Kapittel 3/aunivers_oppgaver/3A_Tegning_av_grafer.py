import matplotlib.pyplot as plt
import numpy as np

#Oppgave 1
"""
def f(x):
    return x**2

xverdier = np.linspace(0, 10, 21)
yverdier = f(xverdier)

plt.plot(xverdier, yverdier)
plt.show()
"""

#Oppgave 2
"""
def f(x):
    return 4*(x**3)-x**5

antall_punkter = [5, 10, 20, 50]

for n in antall_punkter:
    xverdier = np.linspace(-2, 2, n)
    yverdier = f(xverdier)
    plt.plot(xverdier, yverdier)
plt.show()
"""

#Oppgave 3
"""
def f(x):
    return 2*x - 3
    
xverdier = np.array([x for x in range(11)])
yverdier = f(xverdier)

plt.axhline(0, color="black", zorder=0)
plt.axvline(0, color="black", zorder=0)
plt.plot(xverdier, yverdier, color="coral", linestyle="dashed", zorder=1)
plt.scatter(xverdier, yverdier, color="skyblue", marker="D", zorder=2)
plt.grid()

plt.xlabel("$x$")
plt.ylabel("$y$")
plt.show()
"""
#Oppgave 4
"""
xverdier = np.linspace(0, 20, 50)

# Graf 1
yverdier = 0.5*xverdier**2 

plt.subplot(2, 1, 1)
plt.plot(xverdier, yverdier)
plt.grid()

# Graf 2
yverdier = -0.3*xverdier**3 

plt.subplot(2, 2, 1)
plt.plot(xverdier, yverdier)
plt.grid()

plt.show()"""

#Oppgave 5
"""
xverdier = np.linspace(0, 20, 50)

yverdier = 2*xverdier + 1
plt.subplot(2, 2, 1)
plt.plot(xverdier, yverdier)
plt.grid()

yverdier = (xverdier)**2 - 3
plt.subplot(2, 2, 2)
plt.plot(xverdier, yverdier)
plt.grid()

yverdier = 2**(xverdier)
plt.subplot(2, 2, 3)
plt.plot(xverdier, yverdier)
plt.grid()

yverdier = xverdier/3
plt.subplot(2, 2, 4)
plt.plot(xverdier, yverdier)
plt.grid()

plt.show()
#plt.savefig("min_figur.png", dpi=300) #Kan lagre figuren"""

#Oppgave 6
"""
aarstall = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022]
antall = [4478497, 4503436, 4524066, 4552252, 4577457, 4606363, 4640219, 4681134, 4737171, 4799252, 4858199, 4920305, 4985870, 5051275, 5109056, 5165802, 5213985, 5258317, 5295619, 5328212, 5367580, 5391369, 5425270]

plt.plot(aarstall, antall)
plt.show()  
"""

#Oppgave 7
"""
xverdier = np.arange(1, 11)
print(xverdier)
for i in range(1, 6):
    yverdier = xverdier * i
    plt.plot(xverdier, yverdier)

plt.title("De 5 gangetabellene")
plt.xticks(np.arange(1, 11))
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()
"""
"""
utdanningsprogram = [
  "Bygg- og anleggsteknikk", 
  "Elektro og datateknologi",
  "Helse- og oppvekstfag",
  "Naturbruk",
  "Restaurant- og matfag",
  "Teknologi- og industrifag",
  "Håndverk, design og produktutvikling",
  "Frisør, blomster, interiør og eksponeringsdesign",
  "Informasjonsteknologi og medieproduksjon",
  "Salg, service og reiseliv"
]

antall = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]

plt.figure(figsize = (10, 5))
plt.barh(utdanningsprogram, antall, color = "pink")
plt.grid(axis = "x")
plt.subplots_adjust(left = 0.4)
plt.title("Søkertall for yrkesfag i 2021")
plt.show()
""""""
import matplotlib.pyplot as plt
import numpy as np

utdanningsprogram = [
  "Bygg- og anleggsteknikk", 
  "Elektro og datateknologi",
  "Helse- og oppvekstfag",
  "Naturbruk",
  "Restaurant- og matfag",
  "Teknologi- og industrifag",
  "Håndverk, design og produktutvikling",
  "Frisør, blomster, interiør og eksponeringsdesign",
  "Informasjonsteknologi og medieproduksjon",
  "Salg, service og reiseliv"
]

antallGutter = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]
antallJenter = [352, 268, 7286, 1028, 709, 851, 243, 826, 200, 895]

fig, ax = plt.subplots(figsize=(10, 5))    # Angir dimensjoner for figure-objektet

y = np.arange(10)

ax.barh(y+0.2, antallJenter, height= 0.4, label="Jenter")  # Lager stolpediagram jenter
ax.barh(y-0.2, antallGutter, height = 0.4, label="Gutter")  # Lager stolpediagram gutter
ax.set_yticks(y, utdanningsprogram)                       # Legger til akseverdier
ax.legend()                                               # Legger til beskrivelse

fig.subplots_adjust(left=0.4)  # Øker plassen på venstre side av diagrammet

ax.grid(axis="x")  # Legger til rutenett (bare vertikale linjer)
plt.show()         # Viser diagrammet
"""
#Oppgave 12
"""
år = [1985, 1989, 1993, 1997, 2001, 2005, 2009, 2013, 2017, 2021]
arbeiderpartiet = [71, 63, 67, 65, 43, 61, 64, 55, 49, 48]
høyre = [50, 37, 28, 23, 38, 38, 41, 48, 45, 36]

fig, ax = plt.subplots(figsize =(10, 5))
x = np.arange(len(år))

ax.bar(x + 0.2, arbeiderpartiet, width= 0.4, label = "AP")
ax.bar(x - 0.2, høyre, width= 0.4, label = "H")
ax.set_xticks(x, år)
ax.legend()
ax.grid(axis = "x")
plt.show()
"""

#Oppgave 13
"""
partiforkortelser = ["AP", "FrP", "H", "KrF", "MDG", "R", "Sp", "SV", "V", "PF"]
representanter = [48, 21, 36, 3, 3, 8, 28, 13, 8, 1]
farger = ["#f58c68", "#004281", "#3396d2", "#d2bc2a", "#25a23c", "#5d0008", "#90cc93", "#d34d2f", "#005245", "#f69465"]

plt.pie(representanter, labels = partiforkortelser, colors = farger, labeldistance=1.15, wedgeprops = { "linewidth": 0.5, "edgecolor": "white" })
plt.show()
"""
#Oppgave 14
"""
utdanningsprogram = [
  "Bygg- og anleggsteknikk", 
  "Elektro og datateknologi",
  "Helse- og oppvekstfag",
  "Naturbruk",
  "Restaurant- og matfag",
  "Teknologi- og industrifag",
  "Håndverk, design og produktutvikling",
  "Frisør, blomster, interiør og eksponeringsdesign",
  "Informasjonsteknologi og medieproduksjon",
  "Salg, service og reiseliv"
]
antallgutter = [3811, 4168, 8661, 2057, 1484, 5501, 313, 901, 1309, 2061]
antalljenter = [352, 268, 7286, 1028, 709, 851, 243, 826, 200, 895]

totalt = [g + j for g, j in zip(antallgutter, antalljenter)]

plt.pie(totalt, labels=utdanningsprogram)
plt.show()"""
#Oppgave 15
"""
dag = {"morgen": 2, "skole": 7, "chillern": 5, "sove": 10}
navn = list(dag.keys())
timer = list(dag.values())
plt.pie(timer, labels = navn)
plt.show()
"""
#Oppgave 16
"""
data = np.random.normal(3.5, 0.5, 100)
plt.hist(data, bins = [3, 3.2, 3.4, 3.6, 3.8, 4, 4.2, 4.4], color = "seagreen", edgecolor = "black")
plt.show()
"""
#Sluttoppgave 1
"""
karakterer = [5, 3, 6, 3, 5, 1, 2, 2, 2, 4, 2, 2, 5, 5, 6, 3, 5, 3, 5, 4, 2, 6, 1, 4, 2, 3, 3, 3, 5, 5]

plt.hist(karakterer, bins = range(1, 8), align = "left", rwidth= 0.8)
plt.xlabel("Karakterer")
plt.ylabel("Antall elever")
plt.title("Karakterfordeling")
plt.grid(axis = "y")
plt.show()


from collections import Counter
tall = Counter(karakterer)
karaktertyper = sorted(tall.keys())
antall = [tall[k] for k in karaktertyper]
plt.bar(karaktertyper, antall, width = 0.8, color = "pink", edgecolor = "black")
plt.xlabel("Karakterer")
plt.ylabel("Antall")
plt.title("Oversikt av klasse")
plt.grid(axis = "y")
plt.legend()
plt.show()
""""""
tider = [9.92, 8.46, 9.65, 7.74, 9.33, 8.58, 10.17, 8.03, 9.29, 9.55, 11.36, 9.77, 8.97, 9.68, 8.47, 8.29, 8.25, 9.12, 6.38, 7.94, 11.01, 8.34, 9.52, 7.75, 10.4, 9.9, 10.24, 7.94, 8.14, 9.05, 6.98, 9.08, 9.28, 6.89, 7.54, 8.86, 9.16, 8.32, 10.96, 10.43, 11.23, 10.21, 9.98, 9.96, 9.81, 10.12, 10.36, 9.41, 8.14, 7.91, 7.51, 10.28, 9.48, 9.62, 8.14, 10.49, 9.78, 9.39, 8.16, 8.07, 7.79, 7.39, 8.56, 9.15, 8.23, 9.36, 7.7, 8.21, 9.07, 8.5, 8.3, 9.9, 9.97, 8.82, 8.92, 9.13, 9.87, 9.88, 9.19, 9.45, 8.82, 9.49, 8.71, 9.16, 7.38, 7.05, 8.83, 9.63, 9.41, 9.0, 8.73, 9.13, 8.28, 10.64, 9.48, 8.95, 9.04, 8.81, 9.0, 8.86, 9.62, 8.98, 7.7, 9.32, 9.84, 7.29, 9.92, 10.89, 9.64, 9.74, 9.41, 10.83, 6.22, 9.71, 9.79, 9.75, 9.39, 7.78, 9.02, 9.09]
plt.hist(tider, bins=15, width = 0.33, color = "pink")
plt.xlabel("Tid i sekunder")
plt.ylabel("Antall elever")
plt.title("60 meter VGS")
plt.grid(axis = "y")
plt.show()"""
"""
aarstall = [1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]
eksportert = [325, 898, 1421, 2176, 907, 1859, 3174, 1569, 1644, 3373, 4767, 5259, 5607, 5703, 6877, 1570, 4250, 5493, 2501, 7154, 6704, 13847, 9130, 4627, 2180, 3320, 7355, 15166, 16241, 6049, 10109, 8486, 4968, 8962, 4236, 4874, 4412, 8776, 20529, 7162, 15002, 5587, 3842, 15695, 8947, 15320, 17291, 14633, 7123, 14329, 22006, 15140, 21932, 22038, 22151, 21276, 18489, 12309, 24968, 25819]
importert = [-34, -54, -116, -117, -631, -344, -179, -221, -808, -458, -120, -66, -63, -83, -240, -2653, -845, -842, -2039, -1925, -642, -431, -860, -4083, -4212, -2983, -1727, -314, -334, -3274, -1380, -587, -4836, -2300, -13212, -8692, -8046, -6857, -1474, -10760, -5329, -13472, -15334, -3653, -9802, -5284, -3414, -5650, -14673, -11255, -4190, -10135, -6347, -7411, -5741, -6112, -8340, -12353, -4496, -8235]

plt.figure(figsize=(12, 5))
plt.plot(aarstall, eksportert, label = "Eksport", marker = "o", color = "green")
plt.plot(aarstall, importert, label = "Import", marker = "o", color = "red")
plt.axhline(0, color="black", linewidth=1)

plt.xlabel("år")
plt.ylabel("GWh eksportert")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()"""

#Sluttoppgave 2
import random as rd
from collections import Counter
liste = []
for i in range(100000):
    kast = rd.randint(1, 6)
    liste.append(kast)

samlet = Counter(liste)
print(samlet)
tall = sorted(samlet.keys())
antall = [samlet[k] for k in tall]

plt.bar(tall, antall, color = "pink", edgecolor = "black")
plt.xlabel("Øyne")
plt.ylabel("Antall")
plt.grid(axis = "y")
plt.show()