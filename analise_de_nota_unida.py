notas = {2,5,9,4,3,7,6,7,4,5,10}

def analisa_nota(notas):
   notas_unica = set(notas)
   print(f"quantidade de notas unica: {len(notas_unica)}")
   soma = sum(notas_unica)
   print(f"Notas unica: {soma}")
   qual = soma / len(notas_unica)
   ordem = sorted(notas_unica, reverse=True)
   lista = ordem[0:3]
   return {
   'quantidade_unica': len(notas_unica),
   'media_unica': soma / len(notas_unica),
   'top_3_notas' : lista
   }
print(analisa_nota(notas))