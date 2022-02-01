# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G0Xg3Sz9jabLE7Lem0t2tk3mgXc_WQOt

Q1
"""

def Polynome(x):
  y=x**3-1.5*x**2-x*6+5
  print(y)

Polynome(5)

"""Q2"""

def factorielle(x):
  fact1=1
  for i in range(1,x+1):
    if x==1:
      return 1
    else:
      fact1 *=i
  return fact1

factorielle(5)

a=[0,1]

def Fibonnaci(x): 
  count=0
  n1=0
  n2=1 
  while count < (x-2):
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
    a.append(nth)
  return a

Fibonnaci(6)

def Polynome(x):
  y=x**3-1.5*x**2-x*6+5
  print(y)

"""Q3"""

def Polynome_withexceptions(x):
  if(type(x) == int):
    if x>=0:
      if x>5000000:
        print("Saisie d'un très grand nombre, veuillez réessayer")
      elif x<3 & x>=0: 
        print("Saisie d'un très petit nombre, veuillez réessayer")
      else:
        y=x**3-1.5*x**2-x*6+5
        print(y)
    else:
      print("Saisie d'un nombre négatif, veuillez réessayer")
  elif(type(x) == float):
    if x>=0:
      if x>5000000:
        print("Saisie d'un très grand nombre, veuillez réessayer")
      elif x<3 & x>=0: 
        print("Saisie d'un très petit nombre, veuillez réessayer")
      else:
        y=x**3-1.5*x**2-x*6+5
        print(y)
    else:
      print("Saisie d'un nombre négatif, veuillez réessayer")
  elif (type(x) == complex):
    print("Saisie d'un nombre complexe, veuillez réessayer")
  elif(type(x) == str):
    print("Saisie d'une chaine de caractère, veuillez utiliser des chiffres")

Polynome_withexceptions(-1)

Polynome_withexceptions("fsfsdf")

Polynome_withexceptions(1j)

type(1.45)

"""Q4"""

import numpy as np
import scipy.stats as si
import sympy as sy
from sympy.stats import Normal, cdf
from sympy import init_printing
init_printing()

def euro_vanilla_call(S, K, T, r, sigma):
    
    #S = Prix actuel de l’action 
    #X = Prix d’exercice de l’option 
    #T = Temps restant avant l’expiration de l’option, en pourcentage d’une année r = Taux d’intérêt sans risque 
    #σ = volatilité implicite du prix de l’action, mesurée par un décimal 
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    call = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    
    return call

euro_vanilla_call(100, 120, 10, 3, 0.4)