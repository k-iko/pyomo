"""
Problem
min f(x1,x2) = 75*x1 + 125*x2
sub.to
    6*x1 + 3*x2 >= 38
    5*x1 + 21*x2 >= 29
"""
from pyomo.environ import *

# モデルのインスタンス作成
model = ConcreteModel(name="LP sample", )

# 変数の定義
## 制約なし
# model.x1 = Var()
# model.x2 = Var()
## 非負制約
# model.x1 = Var(domain=NonNegativeReals)
# model.x2 = Var(domain=NonNegativeReals)
## 範囲制約
# model.x1 = Var(bounds=(-5,5))
# model.x2 = Var(bounds=(0,10))
## 整数制約と範囲制約
model.x1 = Var(domain=Integers, bounds=(-5,5))
model.x2 = Var(domain=Integers, bounds=(0,10))


# 目的関数の定義
model.obj = Objective(expr=75*model.x1+125*model.x2, sense=minimize)

# 制約条件の定義
model.Con1 = Constraint(expr=6*model.x1+3*model.x2>=38)
model.Con2 = Constraint(expr=5*model.x1+21*model.x2>=29)

# 最適化
## ソルバーの設定
opt = SolverFactory('glpk')

## 最適化の実施
res = opt.solve(model)

# 結果出力
print(model.display())
print('\n')
print('opt = ', model.obj())
print('x1 = ',model.x1())
print('x2 = ',model.x2())