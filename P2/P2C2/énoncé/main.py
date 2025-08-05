nombre=input("Entrez une liste de nombres séparés par des virgules: ")
liste=nombre.split(",")
l=[]
for i in liste:
    i=int(i)
    l.append(i)

s=0
for i in l:

    s+=i
m=round(s/len(l),3)
print(f"la somme des nombres {l} est {s}, et leur moyenne est {m}")

for i in l:
    if i>m:
        print(i,"\t")# Ecrivez votre code ici !
