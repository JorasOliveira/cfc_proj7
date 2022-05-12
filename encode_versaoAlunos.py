
#importe as bibliotecas
from suaBibSignal import *
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import sys

#funções a serem utilizadas
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

#converte intensidade em Db, caso queiram ...
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)




def main():
    
   
    #********************************************instruções*********************************************** 
    # seu objetivo aqui é gerar duas senoides. Cada uma com frequencia corresposndente à tecla pressionada
    # então inicialmente peça ao usuário para digitar uma tecla do teclado numérico DTMF
    # agora, voce tem que gerar, por alguns segundos, suficiente para a outra aplicação gravar o audio, duas senoides com as frequencias corresposndentes à tecla pressionada, segundo a tabela DTMF
    # se voce quiser, pode usar a funcao de construção de senoides existente na biblioteca de apoio cedida. Para isso, você terá que entender como ela funciona e o que são os argumentos.
    # essas senoides tem que ter taxa de amostragem de 44100 amostras por segundo, entao voce tera que gerar uma lista de tempo correspondente a isso e entao gerar as senoides
    # lembre-se que a senoide pode ser construída com A*sin(2*pi*f*t)
    # o tamanho da lista tempo estará associada à duração do som. A intensidade é controlada pela constante A (amplitude da senoide). Seja razoável.
    # some as senoides. A soma será o sinal a ser emitido.
    # utilize a funcao da biblioteca sounddevice para reproduzir o som. Entenda seus argumento.
    # grave o som com seu celular ou qualquer outro microfone. Cuidado, algumas placas de som não gravam sons gerados por elas mesmas. (Isso evita microfonia).
    
    # construa o gráfico do sinal emitido e o gráfico da transformada de Fourier. Cuidado. Como as frequencias sao relativamente altas, voce deve plotar apenas alguns pontos (alguns periodos) para conseguirmos ver o sinal
    

    # Construção de senoide: A*sin(2*pi*f*t), tem função

    

    print("Inicializando encoder")

    signal = signalMeu()


    print("Aguardando usuário")


    pergunta = input('Entre 0 e 9, qual teclas você deseja apertar?')

    NUM = int(pergunta)

    print("Gerando Tons base")
    print("Executando as senoides (emitindo o som)")
    print("Gerando Tom referente ao símbolo : {}".format(NUM))

    fs = 44100
    
    if NUM == 0:
        sinal = [1339,941]
    if NUM == 1:
        sinal = [1206,697]
    if NUM == 2:
        sinal = [1339,697]
    if NUM == 3:
        sinal = [1477,697]
    if NUM == 4:
        sinal = [1206,770]
    if NUM == 5:
        sinal = [1339,770]
    if NUM == 6:
        sinal = [1477,770]
    if NUM == 7:
        sinal = [1206,852]
    if NUM == 8:
        sinal = [1339,852]
    if NUM == 9:
        sinal = [1477,852]
    
    #for i in range
    t0, tone0 = signal.generateSin(sinal[0], 1, 3, fs)

    t1, tone1 = signal.generateSin(sinal[1], 1, 3, fs)


    tone_a = tone0 + tone1

    sd.play(tone_a, fs)
    # Exibe gráficos
    plt.show()
    # aguarda fim do audio
    sd.wait()
    # plt.plotFFT(self, signal, fs)
    

if __name__ == "__main__":
    main()
