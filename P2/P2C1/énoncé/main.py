# Calculatrice
nb1=input()
nb2=input()
if nb1.isnumeric() and nb2.isnumeric() :
    print(f"les nombres entrés {nb1}  & {nb2} sont des chiffres")
    nb1=int(nb1)
    nb2=int(nb2)


else :
    raise SystemExit("Fin du programme")

operation=input()
if operation=='+' or operation=='-' or operation=='*'or operation=='/':
    print("....")
else :
    raise SystemError("Entrez une opération valide +,/,-,* ou,")

match operation:
    case '+':
        resultat=nb1+nb2
    case '-':
        resultat=nb1-nb2
    case '*':
        resultat=nb1*nb2
    case '/':
        if nb2!=0:
         resultat=round(nb1/nb2, 2)
        else:
            raise SystemExit("On ne peut diviser un nombre par 0")
    case _:
        print("L'opération n'est pas possible")
resultat

