#Kalkulator materiałowy arkuszy , płytek , formatek.
#Przelicza ile potrzeba sztuk materiału o podanych wymiarach.

odp="T"
szer=80

while odp.upper()=="T":
    print()
    metry=float(input("Ile potrzebujesz materiału w metrach kwadratowych ?: "))
    print()
    szerokosc=float(input("Wprowadź szerokość formatu materiału w mm: "))
    print()
    wysokosc=float(input("Wprowadź wysokość formatu materiału w mm: "))
    print()
    if metry<=0 or szerokosc<=0 or wysokosc<=0:       
        print("Źle wprowadzone dane")
        print("-"*20)
        print()
        odp=input("Czy chcesz ponownie wprowadzić dane ?: (T/N)")
        print("-"*szer)
        print()
        
    elif szerokosc<150 or wysokosc<150:
        szerokosc=szerokosc/10
        wysokosc=wysokosc/10
        rozmiar=szerokosc*wysokosc
        print("Jedna sztuka ma: %.2f"%rozmiar,"cm2.","jest to: %6.4f"%(rozmiar/10000),"m2")
        ilosc_sztuk=metry/(rozmiar/10000)
        print()
        print("Potrzebujesz: %.1f"%ilosc_sztuk,"sztuk.")
        print()
        odp=input("Czy chcesz wprowadzić nowe dane ? (T/N)")
        print("-"*szer)
        print()
        
    else:
        szerokosc=szerokosc/1000
        wysokosc=wysokosc/1000
        rozmiar=szerokosc*wysokosc

        print("Jedna sztuka ma: %.2f"%rozmiar,"m2.")
        ilosc_sztuk=metry/rozmiar
        print()
        print("Potrzebujesz: %.1f"%ilosc_sztuk,"sztuk.")
        print()
        odp=input("Czy chcesz wprowadzić nowe dane ? (T/N)")
        print("-"*szer)
                
print("Program zakończył pracę.")
print()
        
