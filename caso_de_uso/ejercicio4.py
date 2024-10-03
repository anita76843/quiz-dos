Nombre=input(" digite su nombre: ")
Días= int(input("digite los dias laborados:"))
Salario= 785000

prima = (Días * Salario)/360
cesantias = (Días * Salario)/360
Intereses_cesantías= (cesantias * 0.12)/Días
vacaciones = (Días*Salario)/720
liquidacion = (prima+cesantias+Intereses_cesantías+vacaciones)

print(f"Señor {Nombre}"
      f" para los {Días} días laborados y salario ${Salario},"
      f" su liquidación se compone así:")
print(f"prima: {prima} ")
print(f"Cesantías: {cesantias}")
print(f"intereses cesantias: {Intereses_cesantías}")
print(f"Vacaciones: {vacaciones}")
print(f"liquidacion: {liquidacion}")


