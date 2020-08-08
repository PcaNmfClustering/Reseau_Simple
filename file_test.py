from reseau import Reseau

res = Reseau()

res.set_erreur(0.5)#on précise le taux d'erreur [qui est bas] pour minimiser les fautes

res.print_data()#data vat dire qu'il y a 0 couche
res.set_couche(3)#pour regler ça on précise qu'il y a trois couches
res.add_all_neurone([4,4,2])#ici c'est la valeur des couche 
res.creer_reseau()#creation du reseau
res.print_all()

res.learn([1,0,1,0],[1,0])


res.print_last_couche()
