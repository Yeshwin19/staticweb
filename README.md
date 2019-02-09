
# Bienvenue dans le convertisseur gratuit Markdown-HTML.
 
 Ce petit convertisseur vous aidera à convertir tous vos fichiers écrits avec démarquage en HTML pur et générera un site Web sur lequel vous pourrez voir le résultat final. (Votre fichier écrit en balises).
 
 Tout le monde peut simplement construire un convertisseur simple comme je l’ai fait.
 Tout d’abord, vous devez télécharger 2 packages de la communauté Python pour pouvoir créer votre outil de conversion Markdown-HTML:
 - Installer Markdown
 - Installez Pygments.
 
 **Vous pouvez obtenir les deux en utilisant la commande (PIP) ou vous pouvez simplement le télécharger dans votre code Pycharm ou Visual Studio.**
 

## Que fait le package markdown?

 Le package markdown est un excellent paquet pour convertir chaque document écrit en markdown qui sera ensuite généré au format HTML.
 
## Que fait le package pygment?

 Le package pygment vous permettra d’insérer du code CSS dans votre fichier de Markdown final qui sera ensuite généré au format HTML et utilisera également pour la coloration syntaxique.
 
 Vous pouvez créer votre fichier de Markdown en ligne gratuitement **[ici](https://stackedit.io).**
 
 Une fois que vous avez créé votre fichier de Markdown, il vous suffit de le télécharger et il est prêt à être utilisé.
 
## Explorons maintenant la partie codage et l'algorithme.

 Maintenant que vous avez déjà installé Markdown et Pygments, nous sommes prêts à commencer.
 
**Faisons cela étape par étape.**

1) ``Import markdown``

- Nous devons importer markdown car Python-Markdown fournit une API permettant aux tiers d'écrire des extensions dans l'analyseur en ajoutant leurs propres ajouts ou modifications à la syntaxe. ... Les chaînes ne doivent être utilisées que lorsqu'il est impossible d'importer directement la classe d'extension (à partir de la ligne de commande ou dans un modèle).


2) ``Import OS``

- Le module OS en Python permet d’utiliser les fonctionnalités dépendantes du système d’exploitation. Les fonctions fournies par le module de système d’exploitation vous permettent d’interfacer avec le système d’exploitation sous-jacent sur lequel Python s’exécute - que ce soit Windows, Mac ou Linux.

3) ``Import subprocess``

- Le module de sous-processus vous permet de générer de nouveaux processus, de vous connecter à leurs canaux d'entrée / sortie / d'erreur et d'obtenir leurs codes de retour. Ce module vise à remplacer plusieurs modules et fonctions plus anciens. La méthode est définie comme suit: subprocess.check_output (args, *, stdin = None, stderr = None, shell = False, universal_newlines = False) # Exécute une commande avec des arguments et renvoie sa sortie sous forme d'octet. ** Exemple d'utilisation: #! / Usr / bin / env sous-processus d'importation python s = sous-processus. **

__REMARQUE: SI VOUS N'AVEZ PAS LES MODULES MENTIONNÉS CI-DESSUS, ASSUREZ-VOUS DE LE TÉLÉCHARGER SUR VOTRE CODE PYCHARM OU VISUAL STUDIO ET CONTINUEZ À SUIVRE LES ÉTAPES___.

4) Examinons attentivement notre programme pendant son exécution et essayons également de guider nos utilisateurs sur ce qu’ils devront faire une fois l’outil de conversion lancé. Faisons cela avec un peu de `PRINT`.

```
 print ('---------- Bienvenue dans le convertisseur Markdown-HTML ----------')
 print ('---------------------------------------------- ------------ ')
 print ('1 - Outil de conversion') [l'utilisateur doit faire son choix. Nous devons nous assurer que lorsqu’il appuiera sur «1», l’outil de conversion sera lancé.]
 print ('2 - Installer d'autres packages (utiliser <PIP>)' '] [l'utilisateur doit faire ce choix. Nous devons nous assurer que quand il / elle appuie sur 2, les packages nécessaires sont installés.]
 print ('3 - help') [l'utilisateur doit choisir s'il souhaite obtenir de l'aide s'il a des difficultés à utiliser l'outil de conversion]
 print ('Appuyez sur 1 pour utiliser l'outil de conversion librement')
 print ('Appuyez sur 2 si vous souhaitez télécharger d'autres packages.')
 print ('Appuyez sur 3 si vous voulez obtenir de l'aide')
 choice = int (input ()) [c’est la commande qui tiendra compte des choix de l’utilisateur]
```  
5) Appelons maintenant la boucle dependant sur la touche dur laquelle l'utilisateur appuiera.
```
 if choice == 1:

    fichier = input ("Merci de bien vouloir insérer le fichier de démarquage à convertir (markdown.md):")
    
    os.system ("python -m markdown -x codehilite" + file_to_be_converted + "> index.html")
```    
__NOTE: la commande * python -m markdown * est utilisée pour convertir le fichier de démarquage en html et si vous souhaitez que le CSS soit appliqué, vous devez utiliser la commande complète * python -m markdown -x codehilite + "file_to_be_converted +"> index.html *. Rappelez-vous que le signe '+' est utilisé pour la concaténation de chaînes .__

*Maintenant, si l'utilisateur choisit 1 et que le choix est exactement égal à 1, il pourra utiliser l'outil Markdwon-HTML.*
```
 elif choice == 2:

    os.system("pip install markdown")
```    
*Maintenant, si l'utilisateur appuie sur 2 et que le choix est exactement égal à 2, le Markdown package commencera automatiquement à télécharger.*
```    
 elif choice == 3:

    print("--Pour utiliser l'outil de conversion, relancez le programme en appuyant sur la touche F5..")
  
    print("--Une fois le programme lancé, appuyez sur 1 pour commencer à utiliser l'outil de conversion..")
  
    print("--Insérez le fichier Markdown à convertir en HTML.")
  
    print("--Vous pouvez cliquer sur le fichier index.html généré et situé sur votre bureau.")
  
    print("--Pour télécharger le package Markdown, appuyez sur 2 lorsque le programme est exécuté.")
  
    print("--Votre téléchargement va démarrer automatiquement.")
  
    print("--Pour obtenir de l'aide, appuyez sur 3 pendant l'exécution du programme.")
  
    print("--Appuyez à nouveau sur F5 pour relancer le programme dans l'ordre.")
```    
6) Et c'est la dernière étape.

- Exécutez le programme à l'aide de la touche F5 si vous utilisez le code Visual Studio. Le fichier index.html sera généré sur votre bureau. Assurez-vous de l'ouvrir et savourez le succès de votre travail acharné.

**Ça y est, vous êtes prêt à utiliser votre convertisseur gratuit _Markdown-HTML Convertor_**
    


 
 
