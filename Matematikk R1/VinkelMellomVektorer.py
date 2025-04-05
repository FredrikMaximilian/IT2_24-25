import math
 
def vinkel_mellom_vektorer():
    vektor_1 = []
    vektor_2 = []
   
    x = float(input('Skriv inn x-koordinaten til vektor 1: '))
    y = float(input('Skriv inn y-koordinaten til vektor 1: '))
    vektor_1 = [x, y]
   
    x = float(input('Skriv inn x-koordinaten til vektor 2: '))
    y = float(input('Skriv inn y-koordinaten til vektor 2: '))
    vektor_2 = [x, y]
   
    abs_vektor_1 = math.sqrt(vektor_1[0]**2 + vektor_1[1]**2)
    abs_vektor_2 = math.sqrt(vektor_2[0]**2 + vektor_2[1]**2)
    prikk_produkt = vektor_1[0]*vektor_2[0] + vektor_1[1]*vektor_2[1]
    cos_vinkel = prikk_produkt / (abs_vektor_1 * abs_vektor_2)
    vinkel_radianer = math.acos(cos_vinkel)
    vinkel_grader = math.degrees(vinkel_radianer)
 
    if vektor_1[0] * vektor_2[1] == vektor_1[1] * vektor_2[0]:
            print('Vektorene er parallelle, det er dermed 0° mellom dem.')
    elif prikk_produkt > 0:
        print(f'Vinkelen mellom vektorene er {vinkel_grader:.2f}°, og den er spiss.')
    elif prikk_produkt < 0:
        print(f'Vinkelen mellom vektorene er {vinkel_grader:.2f}°, og den er stump.')
    elif prikk_produkt == 0:
        print(f'Vinkelen mellom vektorene er {vinkel_grader:.2f}°, og de er ortogonale.')
   
vinkel_mellom_vektorer()