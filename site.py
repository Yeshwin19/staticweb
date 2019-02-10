import markdown
import os
import subprocess

print('----------Welcome to the Markdown-HTML convertor----------')
print('----------------------------------------------------------')
print('1 - Conversion Tool')
print('2 - Install other packages (make use of <PIP>)')
print('3 - help')
print('Press 1 to use the conversion tool freely')
print('Press 2 if you want to download other packages.')
print('Press 3 if you want to get help')
choice = int(input())


if choice == 1:
    fichier = input("Please kindly insert the markdown file to be converted (markdown.md) : ")
    os.system("python -m markdown -x codehilite " + fichier + " > index.html")

elif choice == 2:
    print("Your download will start in a few seconds...")
    os.system("pip install markdown")

elif choice == 3:
    print("--Pour utiliser l'outil de conversion, re-éxécute le programme en utilisant la touche F5")
    print("--Dès que le programme se lance, appuyer sur 1 pour utiliser l'outil de conversion")
    print("--Inserer le fichier markdown à convertir en html")
    print("--Votre fichier index.html se trouvera sur votre Bureau")
    print("--Pour telecharger le package Markdown, appuyer sur 2 dès que le programme se lance")
    print("--Votre téléchargement commencera automatiquement.")
    print("--Pour avoir de l'aide appuyer sur 3")
    print("--Appuyer encore sur F5 pour éxécuter le programme encore")











































































