idade = int(input("Qual a sua idade? "))

if idade < 18:
    print(f"{idade} anos. Você é menor de idade.")
elif idade == 18:  # similar ao "if else{}" do java
    print(f"Você tem {idade}.")
else:
    print(f"{idade} anos. Você é maior de idade")
