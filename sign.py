a = int(input("Donnez le premier nombre a : "))
b = int(input("Donnez le deuxième nombre b : "))

if (a < 0 and b < 0) or (a > 0 and b > 0):
      print("Les deux nombres ont le même signe.")
else:
    print("Les deux nombres ont des signes différents.")