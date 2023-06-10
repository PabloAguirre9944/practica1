
from traitlets.config.application import catch_config_error
import matplotlib as ptl
import numpy as np

def calculo(x,vf,vo,t,a):
  if t == "?":
    try:
      t = str((np.double(vf)-np.double(vo))/np.double(a))
    except:
      t = str(np.sqrt((np.double(x))/(0.5*np.double(a))))
  if vf == "?":
    vf = str(np.double(vo)+np.double(a)*np.double(t))
  if vo == "?":
    vo = str(np.double(t)+np.double(a)*np.double(t))
  if a == "?":
    a = str((np.double(vf)-np.double(vo))/np.double(t))
  if x == "?":
    x = str(np.double(vo)*np.double(t)+(1/2)*np.double(a)*np.square(np.double(t)))
  print("x = " + x + ", vf = " + vf + ", vo = " + vo +", t = " + t  + ", a = " + a)

print("Ingrese x: ")
x = input()
print("Ingrese vf: ")
vf = input()
print("Ingrese vo: ")
vo = input()
print("Ingrese t: ")
t = input()
print("Ingrese a: ")
a = input()

calculo(x,vf,vo,t,a)