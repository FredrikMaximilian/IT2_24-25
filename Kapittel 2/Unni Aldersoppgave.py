dag = int(input("Hvilen dag er det"))
måned = int(input("Hvilken måned er det"))
år = int(input("Hvilket år er det"))
dagfødt = int(input("Hvilken dag er du født"))
månedfødt = int(input("Hvilken måned er du født"))
årfødt = int(input("Hvilket år er du født"))

antallSkuddår = 0
for å in range(årfødt, år+1):
    if å % 4 == 0 and å % 100 != 0:
        antallSkuddår += 1
    elif å % 400 == 0:
        antallSkuddår += 1
    else:
        continue

antallDager = (år - årfødt) * 365 + antallSkuddår

if måned > månedfødt:
    for md in range(månedfødt, måned):
        if md == 1:
            antallDager += 30
        elif md == 2:
            antallDager += 28
        elif md == 3:
            antallDager += 31
        elif md == 4:
            antallDager += 30
        elif md == 5:
            antallDager += 31
        elif md == 6:
            antallDager += 30
        elif md == 7:
            antallDager += 31
        elif md == 8:
            antallDager += 31
        elif md == 9:
            antallDager += 30
        elif md == 10:
            antallDager += 31
        elif md == 11:
            antallDager += 30
        elif md == 12:
            antallDager += 31

else:
    for md in range(måned, månedfødt):
        if md == 1:
            antallDager -= 30
        elif md == 2:
            antallDager -= 28
        elif md == 3:
            antallDager -= 31
        elif md == 4:
            antallDager -= 30
        elif md == 5:
            antallDager -= 31
        elif md == 6:
            antallDager -= 30
        elif md == 7:
            antallDager -= 31
        elif md == 8:
            antallDager -= 31
        elif md == 9:
            antallDager -= 30
        elif md == 10:
            antallDager -= 31
        elif md == 11:
            antallDager -= 30
        elif md == 12:
            antallDager -= 31

antallDager += dag - dagfødt
print(f'Det er {antallDager} siden fødselsdagen din')