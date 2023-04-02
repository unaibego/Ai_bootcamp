import tensorflow_probability as tfp
import tensorflow as tf

"""
Oraingoan egunero egin ahal duen eguraldia kalkulatuko dugu, aurreko eguneko eguraldia ezagututa:
-Lehenengo egunean %80ko aukera dago egun hotza izateko. 
-Egun hotza izanda beroa izateko aukerak %30 dira eta beroa izanda hotza izateko aukerak %20koak. 
-Egun hotza denean tenperaturak distribuzio normala jarraitzen du, 0ºCko madiarekin eta 5ºCko desbiderazio tipikoarekin
-Ordez, egun beroetan media 15ºCkoa da eta dezbiderazio tipikoa 10ºCkoa.
"""
tfd = tfp.distributions 
initial_distribution = tfd.Categorical(probs = [0.2, 0.8]) #hemen lehenengo eguneko probabilitatea (egun hotza izatekoa) sartzen gabiz
transition_distribution = tfd.Categorical(probs = [[0.7, 0.3], [0.2, 0.8]]) #hemen trantsizioan izan ahal ditugun aukeretatik (hotza ala beroa) bakoitzaren probabilitateak
observation_distribution = tfd.Normal(loc=[0.,15.], scale=[5.,10.]) #bertan nolakoa izango den gure probabilitatearen grafikoa azalduko diogu: Normala, mediak eta desbiderazio tipikoak.
"""
goialdeko kodean ikus daiteke nola ez den inon hotz edo bero agertzen. Programarentzat 0 hotz izango da eta 1 bero, horregaitik lista guztietan
0. aldagaia hotzarentzat erabiltzen da eta 1. aldagaia beroarentzat. 
"""

model = tfd.HiddenMarkovModel(initial_distribution=initial_distribution, 
                              transition_distribution=transition_distribution,
                              observation_distribution=observation_distribution,
                              num_steps=7) #zenbat egun asmatu nahi ditugun

mean = model.mean()
print(mean.numpy()) #honek array bat itzuliko digu esaten egun bakoitzeko batazbezteko tenperatura