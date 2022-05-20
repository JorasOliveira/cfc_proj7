#!/usr/bin/env python3
"""Show a text-mode spectrogram using live microphone data."""

#Importe todas as bibliotecas
from suaBibSignal import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time
import peakutils
from funcoes_LPF import *




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
    rec_time = 6 #tempo que vamos ficar gravadno


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
   
    pergunta = input('aperte enter para comecar a ouvir')
    
    print("recording now")
    audio = sd.rec(int(numAmostras), freqDeAmostragem, channels=1)
    # print(len(audio))
    sd.wait()
    print("...     FIM")
    sd.play(audio, freqDeAmostragem)
    
    #analise sua variavel "audio". pode ser um vetor com 1 ou 2 colunas, lista ...
    #grave uma variavel com apenas a parte que interessa (dados)

   
    print(f"tamando da variavel audio: {len(audio)}")
    

    # use a funcao linspace e crie o vetor tempo. Um instante correspondente a cada amostra!
    t = np.linspace(0,duration,numAmostras)

    # plot do gravico  áudio vs tempo!
    ## Calcula e exibe o Fourier do sinal audio. como saida tem-se a amplitude e as frequencias
    xf, yf = signal.calcFFT(audio[:,0], freqDeAmostragem)
    plt.figure("Sinal modulado, dominio da frquencia")
    plt.plot(xf,yf)
    plt.grid()
    plt.title('Modulado - Fourier ')

    #calcula e exibe o grafico do sinal modulado, no dominio do tempo
    plt.figure("Sinal modulado, dominio do tempo")
    plt.plot(audio,t)
    plt.grid()
    plt.title('Modulado')

    #TODO: plotar os graficos, e testar
    

    #demodulando
    print("demodulando")
    t0, tone = signal.generateSin(13000, 1, 6, freqDeAmostragem)
    som = audio[:,0] * tone

    #filtrando
    print("filtrando")
    som_filtrado = LPF(som, 2500, freqDeAmostragem)
    sd.play(som_filtrado, freqDeAmostragem)

    #calcula e plota o grafico do sinal demodulado
    #dominio da frquencia
    xf, yf = signal.calcFFT(som_filtrado, freqDeAmostragem)
    plt.figure("Sinal Desmodulado, dominio da frquencia")
    plt.plot(xf,yf)
    plt.grid()
    plt.title('Desmodulado - Fourier')

    #dominio do tempo:
    plt.figure("Sinal Desmodulado, dominio do tempo")
    plt.plot(som_filtrado,t)
    plt.grid()
    plt.title('Desmodulado')
    
    # plt.show()


    #tocando
    # sd.play(som_filtrado, freqDeAmostragem)
  
    ## Exibe gráficos
    plt.show()

if __name__ == "__main__":
    main()
