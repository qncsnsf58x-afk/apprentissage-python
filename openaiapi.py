import os
import anthropic

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

historique = []  # on stocke la conversation ici

while True:
    question = input("Toi : ")
    
    if question == "exit":
        break
    
    historique.append({"role": "user", "content": question})
    
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system="Tu es un assistant dédié aux questions dermatologiques. Tu recherches les meilleures sources d'information concernant les problèmes de peau que les utilisateurs peuvent avoir. Mais il faut aussi que tu préviennes les utilisateurs que tu n'es pas un médecin et qu'un avis médical est toujours recommandé.",
        messages=historique
    )
    
    reponse = response.content[0].text
    historique.append({"role": "assistant", "content": reponse})
    
    print(f"Assistant : {reponse}\n")