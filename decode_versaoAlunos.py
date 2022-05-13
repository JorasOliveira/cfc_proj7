#!/usr/bin/env python3
"""Show a text-mode spectrogram using live microphone data."""

#Importe todas as bibliotecas
from suaBibSignal import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time
import peakutils




#funcao para transformas intensidade acustica em dB
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)


def main():
 
    #declare um objeto da classe da sua biblioteca de apoio (cedida)    
    signal = signalMeu()
    #declare uma variavel com a frequencia de amostragem, sendo 44100
    freqDeAmostragem = 44100

    
    #voce importou a bilioteca sounddevice como, por exemplo, sd. entao
    # os seguintes parametros devem ser setados:
    
    sd.default.samplerate = freqDeAmostragem #taxa de amostragem
    sd.default.channels = 2  #voce pode ter que alterar isso dependendo da sua placa
    duration = 1 #tempo em segundos que ira aquisitar o sinal acustico captado pelo mic
    rec_time = 5 #tempo que vamos ficar gravadno


    # faca um print na tela dizendo que a captacao comecará em n segundos. e entao 
    #use um time.sleep para a espera
    print(f"Will start recording audio in {duration} seconds")
    print(f"gravaremos o som por {rec_time} segundos")
    time.sleep(duration)
   
    #faca um print informando que a gravacao foi inicializada
    print("recording now")
   
    #declare uma variavel "duracao" com a duracao em segundos da gravacao. poucos segundos ... 
    #calcule o numero de amostras "numAmostras" que serao feitas (numero de aquisicoes)

    numAmostras = rec_time * freqDeAmostragem
   
    audio = sd.rec(int(numAmostras), freqDeAmostragem, channels=1)
    print(len(audio))
    sd.wait()
    print("...     FIM")
    
    #analise sua variavel "audio". pode ser um vetor com 1 ou 2 colunas, lista ...
    #grave uma variavel com apenas a parte que interessa (dados)

   
    print(f"tamando da variavel audio: {len(audio)}")
    

    # use a funcao linspace e crie o vetor tempo. Um instante correspondente a cada amostra!
    t = np.linspace(0,duration,numAmostras)

    # plot do gravico  áudio vs tempo!
   
    
    ## Calcula e exibe o Fourier do sinal audio. como saida tem-se a amplitude e as frequencias
    xf, yf = signal.calcFFT(audio[:,0], freqDeAmostragem)
    plt.figure("F(y)")
    plt.plot(xf,yf)
    plt.grid()
    plt.title('Fourier audio')

    #esta funcao analisa o fourier e encontra os picos
    #voce deve aprender a usa-la. ha como ajustar a sensibilidade, ou seja, o que é um pico?
    #voce deve tambem evitar que dois picos proximos sejam identificados, pois pequenas variacoes na
    #frequencia do sinal podem gerar mais de um pico, e na verdade tempos apenas 1.
   
    index = peakutils.indexes(yf, thres=0.25, min_dist=200)
    picos = []
    for i in index:
        # print(i)
        picos.append(int(xf[i]))
        # print(f'pico : {xf[i]}')

    picos.sort(reverse=True)
    print(picos)

    if (1339 in picos) and (941 in picos):
        print("Numero 0")

    if (1206 in picos) and (697 in picos):
        print("Numero 1")

    if (1339 in picos) and (697 in picos):
        print("Numero 2")

    if (1477 in picos) and (697 in picos):
        print("Numero 3")

    if (1206 in picos) and (770 in picos):
        print("Numero 4")

    if (1339 in picos) and (770 in picos):
        print("Numero 5")

    if (1477 in picos) and (770 in picos):
        print("Numero 6")

    if (1206 in picos) and (852 in picos):
        print("Numero 7")

    if (1339 in picos) and (852 in picos):
        print("Numero 8")

    if (1477 in picos) and (852 in picos):
        print("Numero 9")

    
    #printe os picos encontrados! 
    
    #encontre na tabela duas frequencias proximas às frequencias de pico encontradas e descubra qual foi a tecla
    #print a tecla.
    
  
    ## Exibe gráficos
    plt.show()

if __name__ == "__main__":
    main()
