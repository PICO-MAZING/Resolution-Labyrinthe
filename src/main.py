import labyrinthe as lb
import algos
from time import sleep
from os import system


def main():
    
    system('cls')

    # Paramètres de créatio ns du labyrinthe
    pil ="o"
    murH = "-"
    murV = "|"


    # Interactions utilisateurs pour initialiser les paramètres
    print("Bienvenue dans le Simulateur de Résolution de Labyrinthe! \n ")

    ok = False
    while(not(ok)):
        dim = input("Dimension du labyrinthe souhaité? (nombre entier supérieur à 1) ")
        try:
            dim = int(dim)
            if(dim > 1):
                ok = True
        except:
            print("Choix invalide : choisir un nombre entier \n" )

    ok = False
    while(not(ok)):
        affiche = input('Voulez-vous afficher la génération du Labyrinthe? ("o" ou "n") ')
        if(affiche == 'o'):
            affiche = True
            ok = True
        elif(affiche == 'n'):
            affiche = False
            ok = True
        else:
            print('Choix invalide: répondre par "oui" ou "non" \n')

    ok = False
    while(not(ok)):
        nbreRobot = input("Combien de robots pour la résolution? (nombre entier positif) ")
        try:
            nbreRobot = int(nbreRobot)
            if(nbreRobot >= 1):
                ok = True
        except:
            print("Choix invalide: choisir un nombre entier positif \n")

    system('cls')
    

    # Création du Labyrinthe, Départ(s), Arrivée, Carte
    lab = lb.labInit(dim,pil,murH,murV)
    [lab,depart,arrivee] = lb.taillage(lab,dim,nbreRobot,affiche)
    carte = lb.labInit(dim,pil,murH,murV)
    lb.carteInit(carte)
    

    # Affichage menu approprié
    # SOLO
    if(nbreRobot == 1):
        ok = False
        while(not(ok)):
            option = input("Mode de résolution : \n ¤ manuel \n ¤ droite \n ¤ aléatoire \n ¤ poids \n \n")
            if(option == 'manuel' or option == 'droite' or option == 'aléatoire' or option == 'poids'):
                ok = True
            else:
                print("Choix invalide: choisir une option dans la liste \n")

    # COOPERATION
    else:
        ok = False
        while(not(ok)):
            option = input("Mode de résolution : \n ¤ droite \n ¤ aléatoire \n ¤ poids \n \n")
            if(option == 'manuel' or option == 'droite' or option == 'aléatoire' or option == 'poids'):
                ok = True
            else:
                print("Choix invalide: choisir une option dans la liste \n")

    system('cls')

    # On démarre la phase de déplacement avec l'algo choisi / mode manuel
    dir = []
    run = True
    pos = []
    pas = 0
    for i in range(0,nbreRobot):
        dir.append('X')
        pos.append([depart[i][0],depart[i][1]])

    # Mode manuel
    if(option == 'manuel' and nbreRobot == 1):
        while(run):
            [run,carte,pos[0],dir[i],pas] = lb.deplacement(lab,carte,dir[i],depart,pos[0],arrivee,pas)

    # Toujours à droite
    elif(option == 'droite'):
        while(run):
            for i in range(0,nbreRobot):
                if(run):
                    action = algos.toujoursDroite(carte,dir[i],pos[i])
                    algos.communication(action)
                    [run,carte,pos[i],dir[i],pas] = lb.deplacementAlgo(action,lab,carte,dir[i],depart,pos[i],arrivee,pas)
                else: break
    
    elif(option == 'aléatoire'):
        while(run):
            for i in range(0,nbreRobot):
                if(run):
                    action = algos.leDestin()
                    algos.communication(action)
                    [run,carte,pos[i],dir[i],pas] = lb.deplacementAlgo(action,lab,carte,dir[i],depart,pos[i],arrivee,pas)
                else: break
    
    elif(option ==  'poids'):
        premierPassage = True
        while(run):
            if(premierPassage):
                # Données initiales utiles pour l'algorithme
                for i in range(0,nbreRobot):
                    dir[i] = "↑"
                poids = algos.initPoids(dim,arrivee)
                premierPassage = False

            for i in range(0,nbreRobot):
                if(run):
                    [action,poids] = algos.poids(carte,dim,dir[i],pos[i],poids)
                    [run,carte,pos[i],dir[i],pas] = lb.deplacementAlgo(action,lab,carte,dir[i],depart,pos[i],arrivee,pas)
                    poids = algos.actuPoids(poids,carte,arrivee)
                    algos.affichePoids(poids)
                    algos.communication(action)
                    sleep(0.2)
                else: break

    else: print("Choix invalide: choisir une option de la liste")


main()

# Autre programme pour la résolution
# Séparer les méthodes