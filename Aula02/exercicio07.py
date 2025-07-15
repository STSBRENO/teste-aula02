# 1=Branco
# 2=Verde
# 3=Vermelho

print('vote em um time (1-branco), (2-verde), (3-vermelho):')
voto = int(input('digite em qual time voce quer votar:'))
if(voto==1):
    print('voce votou no time branco')
elif(voto==2):
    print('voce votou no time verde')
elif(voto==3):
    print('voce votou no time vermelho')
else:
    print('voto errado')
print('obrigado pelo seu voto')