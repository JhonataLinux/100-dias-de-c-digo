

texte = "Existe uma janela de atendimento de 24 horas quando o usuário inicia a conversa — se você responder dentro dessa janela, você pode usar mensagens “livres” (free-form) sem taxas de template."

def contador_frequencia(texto):
    texto_min = texto.lower()
    texto_sem_pontiacao = texto_min.replace('.', '').replace(',', '').replace('!','').replace('?','').replace('—','').replace('()','')
    dividi_palavras = texto_sem_pontiacao.split()
    frequencia = {}
    for palavra in dividi_palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1
    return frequencia

resultado = contador_frequencia(texte)
print(resultado)
