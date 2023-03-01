#Importing the neccessary Libraries
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#For more information on Theorum Please Refere to
#https://link-springer-com.proxy.library.emory.edu/search?query=worm&facet-eisbn=978-3-642-16712-6&facet-content-type=ReferenceWorkEntry
#Defining the Neccessary Inputs For the WormLike Model
Z=int(input("What is the End to End extention value?"))
L=int(input("What is the contour length?"))
E=int(input("What is the canonical length of the persistence value?"))

#X=input("Are you using ssDNA/ssRNA or dsDNA?")
# For instance, the canonical value for the persistencelength of dsDNA near physiological ionic concentra-tions is 50 nm.
# While for ssDNA it is 1.3 nm, which is consistent since dsDNA should be much stiffer than ssDNA due to the hydro-gen bonding between base pairs.
K=1.380649 *10**(-23) #Boltsman Constant
T=int(input("What is the temperature in Kelvin?"))

#Defining the calculation according to the peer reviewed article above
#10.1007/978-3-642-16712-6
#Never use [] brackets since python thinks it's a string and not an integer value
F=(K*(T/E))*(((1/4)*((1-2/(L)**2)))-(1/4)+((Z)/(L)))

print(F)
