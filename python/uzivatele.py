#!/usr/bin/env python3

class Uzivatel:

  def __init__(self, poradi):
    self.jmeno = input("Zadej jmeno {0}. uzivatele:".format(poradi))
    self.prijmeni = input("Zadej prijmeni {0}. uzivatele:".format(poradi))

if(__name__=="__main__"):

  uzivatele = []

  pocet = int(input("Kolik bude uzivatelu:"))

  for a in range(pocet):
    u = Uzivatel(a+1)
    uzivatele.append(u)

  f = open("uzivatele.csv", "w")
  f.write("Jmeno;Prijmeni\n")

  for a in range(len(uzivatele)):
    print(uzivatele[a].jmeno, uzivatele[a].prijmeni)
    f.write(uzivatele[a].jmeno + ";" + uzivatele[a].prijmeni + "\n")

  f.close()


