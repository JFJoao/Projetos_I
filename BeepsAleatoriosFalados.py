import gtts
from playsound import playsound
import random

b1=open('beeps.txt','r')
b1=b1.read()
b2=open('novosbeeps.txt','r')
b2=b2.read()
b3=open('maisbeeps.txt','r')
b3=b3.read()
lista=[b1,b2,b3]
# Strlista="".join(lista)
escolhido=random.choice(lista)

# with open('lista','r') as arquivo:
for linha in lista:
        voice=gtts.gTTS(linha,lang='pt-br')
        voice.save('voice.mp3')
        playsound('voice.mp3')