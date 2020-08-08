from fonctions import sigmoide, tangente

class Reseau:
    
    def __init__(self,name='Reseau_Simple',learn='sigmoide',error=0.001):
        
        """
            # On init le réseau, avec pour paramètres :
              - on met un nom à notre reseau
              - on choisis la fonction d'activation qu'on vat utiliser
              - et on choisis un taux assez bas pour minimiser les erreurs 
        """
        
        self.name = Reseau_Simple #Le nom du réseau
        if 'tangente' == str.lower(learn):
            self.fun_learn = tangente
            self.name_fun_learn = 'tangente'
        else:
            self.fun_learn = sigmoide
            self.name_fun_learn = 'sigmoide'
        self.error = error #Erreur d'apprentissage
        self.couche = [] #Table de couches, nombre de neuronnes
        self.link = [] #Le table des poids
        self.values = [] #Le table avec les differentes valeurs des neuronnes

        self.control = 0 #Controleur pour empêcher l'ajout de couche/neurone après l'initialisation

    """
        # L ensemble des getter et setter pour les variables de l objet
    """

    
    def set_name(self, Reseau_Simple):
        self.name =  Reseau_Simple


    def get_name(self):
        return self.name

    
    def set_erreur(self, nbr):
        if (nbr >0):
            self.error = nbr


    def get_erreur(self):
        return self.error


    def set_fun_learn(self,name):
        if (str.lower(name) == 'tangente'):
            self.fun_learn = tangente
            self.name_fun_learn = 'tangente'
        else :
            self.fun_learn = sigmoide
            self.name_fun_learn = 'sigmoide'


    def get_name_fun_learn(self):
        return self.name_fun_learn


    def get_data(self):
        return [self.get_name(),self.get_name_fun_learn(),self.get_erreur(),self.get_nbr_couche()]


    def get_nbr_couche(self):
        return len(self.couche)


    def get_last_couche(self):
        return self.values[-1]

    def set_couche(self,value=2):
        
        """
            # On init les differentes couches du reseau
            # On a au minimum 2 couches (entrée + sortie)(self,value=2)
        """
        
        if (self.control == 0):
            if (value>=2):
                for i in range(0,value):
                    self.couche.append(0)
            else:
                print("Il doit y avoir au moins 2 couches")
        else:
            print("Le reseau est déjà créé, on ne peut plus le modif")
    
    
    def add_couche(self,pos):

        """
            # Fonction pour ajouter une couche
        """
        
        if (self.control == 0):
            if (pos>=0 and pos<len(self.couche)):
                self.couche.insert(pos,0)
            else:
                print("Vous pouvez ajouter une couche dans l'intervalle [0,",len(self.couche)-1,"]")
        else :
            print("Le réseau est déjà créé, on ne peut plus le modif")


    def add_neurone(self,couche,nbr=1):

        """
            # Ajouter au minimum un neurone sur la couche désirée
        """
            
        if (self.control == 0):
            if (couche>=0 and couche<len(self.couche) and nbr>0):
                self.couche[couche] += nbr
        else :
            print("Le réseau est déjà créé,  on ne peut plus le modif")

    
    def add_all_neurone(self,tab):

        """
            # Si on veut ajouter tout les différents neurones aux differentes couches
        """
        
        if (self.control == 0):
            if(len(tab) == len(self.couche)):
                for i in range(0,len(tab)):
                    self.add_neurone(i,tab[i])
            else:
                print("Le tableau doit avoir une taille concequante ",len(self.couche))
        else :
            print("Le réseau est déjà créé,  on ne peut plus le modif")


    def creer_reseau(self):

        """
            # On init toutes les connexion entre les neurones
            # Les poids sont mis à 0.5 par défaut
            # On initialise aussi le tableau des valeurs des neurones à 0
        """
        test = 0
        for j in range(0,len(self.couche)):
            if (self.couche[j] <= 0):
                print("La couche ",j," doit contenir au moins 1 neuronne")
                test = 1
        if (test != 1):
            if (self.control == 0):
                self.control = 1
                for i in range(0,len(self.couche)):
                    add = []
                    add1 = []
                    add_values = []
                    for j in range(0,self.couche[i]):
                        if (i!=len(self.couche)-1):
                            for k in range(0,self.couche[i+1]):
                                add1.append(0.5)
                            add.append(add1)
                            add1 = []
                        add_values.append(0)
                    if (i!=len(self.couche)-1):
                        self.link.append(add)
                    self.values.append(add_values)
            else:
                print("Reseau deja init")
        else :
            print("On ne pouvez pas lancer l'init")


    def parcourir(self, tab):
        
        """
            # Fonction pour le parcour du reseau
            # Les données à tester
        """
        if (self.control == 1):
            if (len(tab) == self.couche[0]):
                for i in range(0,len(tab)):
                    
                    # On stock dans la première couche les données d'entrées :
                    self.values[0][i] = tab[i]
                for i in range(1,len(self.values)):
                    for j in range(0,len(self.values[i])):
                        var = 0
                        for k in range(0,len(self.values[i-1])):

                            # On stock la somme pondéré pour le prochain neurone :
                            var += self.values[i-1][k] * self.link[i-1][k][j]
                        self.values[i][j] = self.fun_learn(var)
            else:
                print("La couche d'entree doit contenir ",self.couche[0],"valeurs")
        else:
            print("Reseau non init")


    def retropropagation(self, tab):

        """
            # Fonction de retropropagation par le gradient
            # Prend en paramètre les données attendu
            # La retropropagation ne marche qu'apres avoir effectué le parcour
        """

        if (len(tab) == len(self.values[len(self.values)-1])):
            for i in range(0,len(tab)):

                # On stock dans la dernière couche la soustraction (valeur_voulus - valeur_trouvée) :
                self.values[len(self.values)-1][i] = tab[i] - self.values[len(self.values)-1][i]
            for i in range(len(self.values)-1,0,-1):
                for j in range(0,len(self.values[i-1])):
                    for k in range(0,len(self.link[i-1][j])):
                        somme = 0
                        for l in range(0,len(self.values[i-1])):

                            # On effectue la somme ponderee du neurone vers lequel pointe la connexion :
                            somme += self.values[i-1][l] * self.link[i-1][l][k]
                        somme = self.fun_learn(somme)

                        # On met a jour le poids de la connexion 
                        self.link[i-1][j][k] -= self.get_erreur() * (-1 * self.values[i][k] * somme * (1 - somme) * self.values[i-1][j])
                for j in range(0,len(self.values[i-1])):
                    somme = 0
                    for k in range(0,len(self.values[i])):

                        # On met a jour les neurones de la prochaine couche en fonction de l'erreur qui se retropropage :
                        somme += self.values[i][k] * self.link[i-1][j][k]
                    self.values[i-1][j] = somme


    def learn(self, entree, sortie):
        
        """
            # Fonction d'apprentissage du reseau
            # Le premier paramètre est l'ensemble de valeurs à tester
            # Le second est le résultat attendu
        """
        if (self.control == 1):
            if(len(entree)==self.couche[0] and len(sortie)==self.couche[len(self.couche)-1]):
                self.parcourir(entree)
                self.retropropagation(sortie)
            else:
                print("La couche d'entrée doit contenir ",self.couche[0],"valeurs",
                      "La couche de sortie soit contenir ",self.couche[len(self.couche)-1],"valeurs")
        else:
            print("Reseau non init")




    def print_last_couche(self):
        print(self.values[len(self.values)-1])
                        

    def print_data(self):
        tab = self.get_data()
        print("Table 1 pour le nom du reseau :", tab[0],
              "\nFonction d'apprentissage :", tab[1],
              "\nValeur d'erreur d'apprentissage :", tab[2],
              "\nNombre de couche dans le reseau :", tab[3])


    def print_all(self):
        print('Values :')
        self.print_values()
        print('\nLink :')
        self.print_link()

    
    def print_values(self):
        i = 1
        for each in self.values:
            print("Couche ",i,":")
            i+=1
            print(each)

            
    def print_link(self):
        i = 1
        for each in self.link:
            print("Liens ",i,":")
            i+=1
            for k in each:
                print (k)
            print()

            
    def print_couche(self):
        print (self.couche)
