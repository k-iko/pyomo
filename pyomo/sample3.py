"""
Problem
min f(x1,x2) = 75*x1 + 125*x2
sub.to
    6*x1 + 3*x2 >= 38
    5*x1 + 21*x2 >= 29
"""
import numpy as np
from pyomo.environ import *

# 変数
I = 2

## 目的変数の係数
a_data =  np.array([75,125])
## 係数行列
t_data = np.array([[6, 3],
                   [5, 21]])
## ベクトル（各制約式の下限）
t0_data = np.array([38,29])
#
# 辞書(dictionary)へ変換
#
## 目的変数の係数
a = dict((i, a_data[i-1]) for i in range(1, I+1))
## 係数行列
t = dict(
    ((i, j), t_data[i-1][j-1])  
    for i in range(1, I+1) 
    for j in range(1, I+1)
)
## ベクトル（各制約式の下限）
t0 = dict((i, t0_data[i-1]) for i in range(1,I+1))

# モデルのインスタンス作成
model = ConcreteModel()

# 添え字(各変数に対してキーワードを割り当てる)
model.I = Set(initialize=range(1, I+1))

# 変数(上記のキーワードを最適化問題を行うときのインデックスとして定義するときには、以下のように設定する)
model.x = Var(model.I, within=Reals,  initialize=0)

def func(model):
    return sum(a[i]*model.x[i] for i in model.I)

model.obj = Objective(rule=func, sense=minimize)

def const(model, i):
    tmp = sum(t[i,j]*model.x[j] for j in model.I)
    return tmp >= t0[i]

model.Con = Constraint(model.I, rule=const)

opt = SolverFactory('glpk')

res = opt.solve(model)

print(model.display())
print('opt = ',model.obj())
print('x = ',model.x[:]())