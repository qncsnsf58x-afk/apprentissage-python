def learningtogreet(name, age, city):
    return f"Je m'appelle {name}, j'ai {age} ans et je vis à {city}."
print(learningtogreet("Stanley", 38,"Paris"))
print(learningtogreet("Marie",25,"Lyon"))
print(learningtogreet("Ahmed",42,"Marseille"))


def calculer_salaire_annuel(salaire_mensuel):
    return f"Salaire annuel : {salaire_mensuel*12}€"

print(calculer_salaire_annuel(4000))