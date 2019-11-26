import numpy as np
import math as m
class world:
  size=3
  serie=1
  number=size**2
  matrix = np.zeros((size, size))
  #1:Fib, 2: X^2, 3: Primes, 4: 2^n, 5: Even, 6: Odd
  def __init__(self, size, serie):
    self.size = size
    self.serie = serie
    self.number=size**2
    self.matrix = np.zeros((size, size))

  def fib(self, lim):
      arr=np.zeros(lim)
      cont=0
      while cont<lim:
        if cont<=1:
          arr[cont]=1
        else:
          arr[cont]= arr[cont-1]+arr[cont-2]
        cont+=1
      return arr

  def square(self, lim):
      arr=np.zeros(lim)
      cont=0
      while cont<lim:
        arr[cont]=cont**2
        cont+=1
      return arr


  def p3(self, num):
    i = 2
    primo = True
    # Reviso y si el modulo del número con algún otro número es 0, es porque no es primo.
    while primo and i < num:
      if m.fmod(num, i) == 0:
        primo = False
      i = i + 1
    return primo
  def primes(self,lim):
    arr=np.zeros(lim)
    cont=0
    i=0
    while cont<lim:
      if self.p3(i) and i!=0 and i!=1:
        arr[cont]=i
        cont+=1
      i+=1

    return arr

  def quadratic(self,lim):
    arr = np.zeros(lim)
    cont = 0
    while cont < lim:
      arr[cont] = 2**cont
      cont+=1
    return arr

  def even(self, lim):
    arr = np.zeros(lim)
    cont = 0
    i = 0
    while cont < lim:
      if i==0:
        arr[cont]=i
        cont+=1
      elif m.fmod(i,2)==0:
        arr[cont] = i
        cont += 1
      i += 1

    return arr

  def odd(self, lim):
    arr = np.zeros(lim)
    cont = 0
    i = 0
    while cont < lim:
      if m.fmod(i,2)==1:
        arr[cont] = i
        cont += 1
      i += 1

    return arr
  def initialize(self):
    if self.serie==1:
      arr=self.fib(self.number)
      cont=0
      for i in range(0,np.size(self.matrix,axis=1)):
        for j in range(0,np.size(self.matrix,axis=1)):
          self.matrix[i,j]=int(arr[cont])
          cont+=1
    elif self.serie==2:
      arr=self.square(self.number)
      cont = 0
      for i in range(0, np.size(self.matrix, axis=1)):
        for j in range(0, np.size(self.matrix, axis=1)):
          self.matrix[i, j] = int(arr[cont])
          cont += 1
    elif self.serie==3:
      arr=self.primes(self.number)
      cont = 0
      for i in range(0, np.size(self.matrix, axis=1)):
        for j in range(0, np.size(self.matrix, axis=1)):
          self.matrix[i, j] = int(arr[cont])
          cont += 1
    elif self.serie==4:
      arr=self.quadratic(self.number)
      cont = 0
      for i in range(0, np.size(self.matrix, axis=1)):
        for j in range(0, np.size(self.matrix, axis=1)):
          self.matrix[i, j] = int(arr[cont])
          cont += 1
    elif self.serie==5:
      arr = self.even( self.number)
      cont = 0
      for i in range(0, np.size(self.matrix, axis=1)):
        for j in range(0, np.size(self.matrix, axis=1)):
          self.matrix[i, j] = int(arr[cont])
          cont += 1
    elif self.serie==6:
      arr = self.odd( self.number)
      cont = 0
      for i in range(0, np.size(self.matrix, axis=1)):
        for j in range(0, np.size(self.matrix, axis=1)):
          self.matrix[i, j] = int(arr[cont])
          cont += 1
