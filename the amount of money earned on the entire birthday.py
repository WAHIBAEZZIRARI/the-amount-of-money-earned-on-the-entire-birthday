age = int(input("Veuillez saisir l'age d'Amal : "))
S=0
for i in range(1 ,age+1):
     S = S + ( 500 + (i * 3) )
print("Le compte d'Amal au ",age, "ième anniversaire est: ", S,"DH")