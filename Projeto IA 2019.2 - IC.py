import requests, sys

# Obtém o conteúdo de uma imagem na Internet para
# enviando ao modelo de aprendizado de máquina 
def getImageUrlData(wwwLocationOfImage):
    data = requests.get(wwwLocationOfImage).content
    if sys.version_info[0] < 3:
        
        return data.encode("base64")
    else:
        
        import base64
        return base64.b64encode(data).decode()



# Esta função passa a imagem para o modelo de aprendizado de máquina
# e retorna o resultado com maior confiança
def classify(imageurl):
    key = "f26f40a0-f4eb-11e9-baa6-3f33709df9e6f20f5a1f-72b1-49ae-96b8-7a21a0d6b357"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.post(url, json={ "data" : getImageUrlData(imageurl) })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# Mude isto para URL da imagem que você deseja classificar
print("Coloca as URL's que vou descobrir se é um pato ou ganso!\n")
for i in range(100):
    try:      
        demo = classify(input("Digite a URL: "))

        label = demo["class_name"]
        confidence = demo["confidence"]
# Podemos mudar isso para fazer algo diferente com o resultado    
    except:
         print ('Coloca uma URL ai jogador')
    else:     
         print ("Eu acho que é um %s, minha confiança é de %d%%, sei la mano os bixo é tudo igual pô \n" % (label, confidence))
 
