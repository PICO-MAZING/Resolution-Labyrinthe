import random
from time import sleep
from os import system
import keyboard as kb


##### INITIATION LABYRINTHE #####

def labInit(dim,pil,murH,murV):

    # Dimensions du tableau labyrinthe :
    larg = 4*dim+1
    haut = 2*dim+1

    # Toutes les cases sont vides au début
    lab = [[" " for j in range(0,larg)] for i in range(0,haut)]

    # On parcours toute les cases
    for i in range(0,haut):
        for j in range(0,larg):
            if(i % 2 == 0):              # Si la ligne est paire
                if(j % 4 == 0):             # Et que la colonne est un multiple de 4
                    lab[i][j]=pil               # On met un pilier
                else:                       # Si la colonne n'est pas un multiple de 4
                    lab[i][j]=murH              # On met un mur horizontale
            else:                       # Si la ligne est imparire
                if(j % 4 == 0) :             # Si la colonne est un multiple de 4
                    lab[i][j]=murV              # On met un mur vertical "|"
    return lab                          # On retourne le tableau


##### AFFICHAGE TABLEAU #####

def afficheTab(tab):                       
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            print(tab[i][j], end="")
        print()
    print()


##### CASE EST COINCEE? #####

def estCoince(tab,i,j):

    # Un booléen par direction
    droite = False
    gauche = False
    bas = False
    haut = False

    # droite
    if(j+1 < len(tab)) :                 # Si la case existe
        if(tab[i][j+1] == 1):               # Si la case est parcouru (=1)
            droite = True                       # Le booléen associé est vrai (ici "droite")
    else: droite = True    

    # gauche
    if(j-1 >= 0):
        if(tab[i][j-1] == 1):
            gauche = True
    else: gauche = True    

    # bas
    if(i+1 < len(tab)):
        if(tab[i+1][j] == 1):
            bas = True
    else: bas = True    
    
    # haut
    if(i-1 >= 0):
        if(tab[i-1][j] == 1):
            haut = True
    else: haut = True    

    # 4 directions
    if(droite & bas & gauche & haut):          # Si les 4 cases voisines sont parcourues (si elles existent)
        return True                                 # La case est "coincée"
    else:
        return False


##### TAILLAGE 'Hunt & kill' #####

def taillage(lab,dim,affiche):

    # On créé un tableau de même dimension que le labyrinthe représenté par des 0
    # 0 = pas encore parcourue
    # 1 = parcourue
    parcours = [[0 for j in range(0,dim)] for i in range(0,dim)]

    # On marque le point de départ
    y = random.randint(0,dim-1)
    x = random.randint(0,dim-1)
    depart = [y,x]

    # "On parcours la case"
    parcours[y][x]=1

    if(affiche) :
        afficheTab(lab)
    count = 1
    system('cls')
    while(count < dim**2):

        # Si on est coincé
        if (estCoince(parcours,y,x)):
            nouv = True
            if nouv :
                for j in range(0,dim):
                    if nouv :
                        for i in range(0,dim):                                                          # On cherche parmis toutes les cases
                            if parcours[j][i] == 1 and not estCoince(parcours,j,i) and nouv:                # La première qui n'est pas coincée
                                y=j                                                                             # On la prend comme nouveau point de départ
                                x=i
                                nouv = False
        
        # Si on peut avancer
        else:
            # On génère une direction avec un randint
            dir = random.randint(1,4)
            match dir:

                # Droite
                case 1:
                    if (x+1 < dim) :                            # On vérifie que la case existe
                        if (parcours[y][x+1] == 0):                   # On vérifie que la case n'est pas encore parcouru
                            lab[1+2*y][4+4*x] = " "                     # On casse le mur
                            x+=1                                        # On se "déplace"
                            parcours[y][x] = 1                          # On marque la case
                            if (affiche) :
                                system('cls')
                                afficheTab(lab)
                                sleep(0.2)
                            count+=1                            # On incrémente le nombre de case parcourues
                
                # Haut
                case 2:
                    if (y-1 >= 0):
                        if(parcours[y-1][x] == 0):
                            lab[2*y][1+(4*x)] = " "
                            lab[2*y][2+(4*x)] = " "
                            lab[2*y][3+(4*x)] = " "
                            y-=1
                            parcours[y][x] = 1
                            if (affiche) :
                                system('cls')
                                afficheTab(lab)
                                sleep(0.2)
                            count+=1
                
                # Gauche
                case 3:
                    if (x-1 >= 0):
                        if (parcours[y][x-1] == 0):
                            lab[1+2*y][4*x] = " "
                            x-=1
                            parcours[y][x] = 1
                            if (affiche) :
                                system('cls')
                                afficheTab(lab)
                                sleep(0.2)
                            count+=1
                
                # Bas
                case 4:
                    if (y+1 < dim):
                        if (parcours[y+1][x] == 0):
                            lab[2+2*y][1+(4*x)] = " "
                            lab[2+2*y][2+(4*x)] = " "
                            lab[2+2*y][3+(4*x)] = " "
                            y+=1
                            parcours[y][x] = 1    
                            if (affiche) :
                                system('cls')
                                afficheTab(lab)
                                sleep(0.2)
                            count+=1
    
    # On définit un départ et une arrivée au labyrinthe taillé
    depart = [random.randint(0,dim-1),random.randint(0,dim-1)]
    ya = random.randint(0,dim-1)
    xa = random.randint(0,dim-1)
    while(ya == depart[0] and xa == depart[1]):
        ya = random.randint(0,dim-1)
        xa = random.randint(0,dim-1)
    arrivee = [ya,xa]
    lab[1+2*depart[1]][2+4*depart[0]] = "D"
    lab[1+2*arrivee[1]][2+4*arrivee[0]] = "A"

    # On fait une pause d'1s pour l'affichage
    sleep(1)    

    # On renvoie le labyrinthe et la case de départ
    return [lab,depart,arrivee]  


##### INITIALISATION CARTE #####

def carteInit(carte):
    larg = len(carte[0])
    haut = len(carte)
    for j in range(1,haut-1):
        for i in range(1,larg-1):
            if carte[j][i]  != "D" or carte[j][i] != "A" or carte[i][j] != "X":
                carte[j][i] = " "


##### DEPLACEMENTS CLAVIERS #####

def deplacement(lab,carte,dir,depart,pos,arrivee,pas):
    
    texte = "D = Départ ; A = Arrivée ; X = position initiale ;\nAppuyer sur z/q/s/d ou les flèches pour vous déplacer, echap pour quitter :"
    
    # Coordonnées du départ et arrivée du labyrinthe
    yd = 2*depart[0]+1
    xd = 4*depart[1]+2
    ya = 2*arrivee[0]+1
    xa = 4*arrivee[1]+2

    # Coordonnées initiales de position
    y = 2*pos[0]+1
    x = 4*pos[1]+2
    run = True
    
    # Paramètres utiles aux calculs de déplacement
    murH = lab[0][1]
    murV = lab[1][0]
    carte[y][x] = dir

    if(dir == 'X'):
        cartographiage(lab,carte,x,y,xd,yd,xa,ya,dir,texte)

    # On regarde quelle touche est appuyé
    event = kb.read_event()
    if (event.event_type == kb.KEY_DOWN):
        match event.name:
            
            # Droite
            case 'd' | 'droite':
                if (dir == '→'):
                    if (lab[y][x+2] == murV):
                        print("Mur rencontré")
                        sleep(0.2)
                    else:
                        carte[y][x] = " "
                        x+=4
                        pos[1]+=1
                        carte[y][x] = dir
                        pas+=1
                else: dir = '→'                    

            # Gauche
            case 'q' | 'gauche':
                if(dir == '←'):
                    if(lab[y][x-2] == murV):
                        print("Mur rencontré")
                        sleep(0.2)
                    else:
                        carte[y][x] = " "
                        x-=4
                        pos[1]-=1
                        carte[y][x] = dir
                        pas+=1
                else: dir = '←'    

            # Haut
            case 'z' | 'haut':
                if(dir == '↑'):
                    if(lab[y-1][x] == murH):
                        print("Mur rencontré")
                        sleep(0.2)
                    else:
                        carte[y][x] = " "
                        y-=2
                        pos[0]-=1
                        carte[y][x] = dir
                        pas+=1
                else: dir = '↑'
            
            # Bas
            case 's' | 'bas':
                if(dir == '↓'):
                    if(lab[y+1][x] == murH):
                        print("Mur rencontré")
                        sleep(0.2)
                    else:
                        carte[y][x] = " "
                        y+=2
                        pos[0]+=1
                        carte[y][x] = dir
                        pas+=1
                else: dir = '↓'
            case 'esc':
                run = False

        
        # On cartographie et affiche la carte
        cartographiage(lab,carte,x,y,xd,yd,xa,ya,dir,texte)
        if(y == ya and x == xa):
            run = False
            print("Gagné en", pas, "pas !")
    
    return [run,carte,pos,dir,pas]


##### DEPLACEMENTS ALGORITHMES #####

def deplacementAlgo(action,lab,carte,dir,depart,pos,arrivee,pas):
    
    texte = "D = Départ ; A = Arrivée ; X = position initiale"
    
    # Coordonnées du départ et arrivée du labyrinthe
    yd = 2*depart[0]+1
    xd = 4*depart[1]+2
    ya = 2*arrivee[0]+1
    xa = 4*arrivee[1]+2

    # Coordonnées initiales de position
    y = 2*pos[0]+1
    x = 4*pos[1]+2
    run = True
    
    # Paramètres utiles aux calculs de déplacement
    murH = lab[0][1]
    murV = lab[1][0]
    carte[y][x] = dir
    
    if(dir == 'X'):
        cartographiage(lab,carte,x,y,xd,yd,xa,ya,dir,texte)
    
    # Tourner à Droite
    if(action == 'droite'):
        match dir:
            case '→' | 'X':
                dir = '↓'
            case '↓':
                dir = '←'
            case '←':
                dir = '↑'
            case '↑':
                dir = '→'
        action = 'avancer'

    # Tourner à Gauche
    if(action == 'gauche'):
        match dir:
            case '→' | 'X':
                dir = '↑'
            case '↑':
                dir = '←'
            case '←':
                dir = '↓'
            case '↓':
                dir = '→'
        action = 'avancer'
                
    # Demi-tour
    if(action =='demitour'):
        match dir:
            case '→' | 'X':
                dir = '←'
            case '↑':
                dir = '↓'
            case '←':
                dir = '→'
            case '↓':
                dir = '↑'
        action = 'avancer'
    
    # Avancer
    if(action == 'avancer'):
        match dir:
            case'→':                              # Orientation Est
                if(lab[y][x+2] == murV):
                    print("Mur rencontré")
                    sleep(0.2)
                else:
                    carte[y][x] = " "
                    x+=4
                    pos[1]+=1
                    carte[y][x] = dir
                    pas+=1   
            case '←':                              # Orientation Ouest
                if(lab[y][x-2] == murV):
                    print("Mur rencontré")
                    sleep(0.2)
                else:
                    carte[y][x] = " "
                    x-=4
                    pos[1]-=1
                    carte[y][x] = dir
                    pas+=1 
            case '↑':                              # Orientation Nord
                if(lab[y-1][x] == murH):
                    print("Mur rencontré")
                    sleep(0.2)
                else:
                    carte[y][x] = " "
                    y-=2
                    pos[0]-=1
                    carte[y][x] = dir
                    pas+=1 
            case '↓':                              # Orientation Sud
                if(lab[y+1][x] == murH):
                    print("Mur rencontré")
                    sleep(0.2)
                else:
                    carte[y][x] = " "
                    y+=2
                    pos[0]+=1
                    carte[y][x] = dir
                    pas+=1
        
    # On efface, réaffiche les commandes, cartographie et affiche la carte
    
    cartographiage(lab,carte,x,y,xd,yd,xa,ya,dir,texte)
    if(y == ya and x == xa):
        run = False
        print("Gagné en", pas, "pas !")
    
    return [run,carte,pos,dir,pas]


##### CARTOGRAPHIE #####

def cartographiage(lab,carte,x,y,xd,yd,xa,ya,dir,texte):

    # On récupère la position initiale
    carte[y][x] = dir

    # On récupère le murs de Droite
    if not(dir == '←'):
        carte[y][2+x] = lab[y][2+x]

    # On récupère le murs de Gauche
    if not(dir == '→'):
        carte[y][x-2] = lab[y][x-2]

    # On récupère les murs du Haut
    if not(dir == '↓'):
        carte[y-1][x-1] = lab[y-1][x-1]
        carte[y-1][x] = lab[y-1][x] 
        carte[y-1][x+1] = lab[y-1][x+1] 
    
    # On récupère les murs du Bas
    if not(dir == '↑'):
        carte[y+1][x-1] = lab[y+1][x-1]
        carte[y+1][x] = lab[y+1][x] 
        carte[y+1][x+1] = lab[y+1][x+1] 

    # On récupère les piliers
    carte[y-1][x-2] = lab[y-1][x-2]
    carte[y-1][x+2] = lab[y-1][x+2]
    carte[y+1][x-2] = lab[y+1][x-2]
    carte[y+1][x+2] = lab[y+1][x+2]      

    # AFFICHAGE
    system('cls')
    print(texte)    
    if(y != yd or x != xd):
        carte[yd][xd] = "D"
    if(y != ya or x != xa):
        carte[ya][xa] = "A"
    afficheTab(carte)
    sleep(0.1)