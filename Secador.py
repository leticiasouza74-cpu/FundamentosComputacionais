from dataclasses import dataclass
import numpy as np
from scipy.integrate import solve_ivp

@dataclass

class ParametroCinetica:
  '''
  Xe: umidade de equilibrio (valor mínimo atingível no processo)
  Xt: umidade livre do material (kg de água/kg de sólido seco)
  kt: função crescente de Temperatura para T>= 50°C
  '''

  @staticmethod
  def constante(T):
    kt = 0.2*(1+0.02*(T - 60))
    return kt

  Xe: float = 0.05

def dXdt(t, X, T, ParametroCinetica):
  dXdt = -ParametroCinetica.constante(T)*(X - ParametroCinetica.Xe)
  return dXdt


def simulacao(t, X0=0.5, param = ParametroCinetica, T=50):
  sol = solve_ivp(dXdt, [t[0],t[-1]], [X0], t_eval = t, args=(T, param)) 
  return sol.t, sol.y[0]
