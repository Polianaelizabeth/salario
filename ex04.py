salarioB = float(input("Qual o salário bruto? "))

if salarioB <= 350:
    gratific = 100
elif 351 <= salarioB <= 600:
    gratific = 75
elif 601 <= salarioB <= 900:
    gratific = 50
else:
    gratific = 35

imposto = float = 0.07 * salarioB

salarioF = float = salarioB + gratific + imposto

print("salário bruto: ", salarioB, "gratificação: ", gratific,
      " imposto: ", imposto, "salário final: ", salarioF)
