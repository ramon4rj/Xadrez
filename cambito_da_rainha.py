#import termcolor
#from termcolor import colored

class Xadrez:

#    def __init__(self):
#        self.matriz = []

    def cria_tabuleiro(self):
        self.matriz = []
        for i in range(8):
            linha = []
            for j in range(8):
                linha.append(" x ")
            self.matriz.append(linha)
        ### PRETAS ###
        for l in range(8):
            linha[0] = "B-T1"
            linha[1] = "B-C1"
            linha[2] = "B-B1"
            linha[3] = "B-Q"
            linha[4] = "B-K"
            linha[5] = "B-B2"
            linha[6] = "B-C2"
            linha[7] = "B-T2"
            self.matriz[0][l] = linha[l]

        for c in range(8):
            linha[0] = "B-P1"
            linha[1] = "B-P2"
            linha[2] = "B-P3"
            linha[3] = "B-P4"
            linha[4] = "B-P5"
            linha[5] = "B-P6"
            linha[6] = "B-P7"
            linha[7] = "B-P8"
            self.matriz[1][c] = linha[c]
        
        ### Brancas ###
        for ll in range(8):
            linha[0] = "W-T1"
            linha[1] = "W-C1"
            linha[2] = "W-B1"
            linha[3] = "W-Q"
            linha[4] = "W-K"
            linha[5] = "W-B2"
            linha[6] = "W-C2"
            linha[7] = "W-T2"
            self.matriz[6][ll] = linha[ll]

        for cc in range(8):
            linha[0] = "W-P1"
            linha[1] = "W-P2"
            linha[2] = "W-P3"
            linha[3] = "W-P4"
            linha[4] = "W-P5"
            linha[5] = "W-P6"
            linha[6] = "W-P7"
            linha[7] = "W-P8"
            self.matriz[7][cc] = linha[cc]        

#    def calculo_pos(self):


    def movimento(self, inst):
        #inst = intrução. Ex: W-R/H3   ~/~   rei branco vai p/ h3
        #receber uma string e a partir dessa string fazer o movimento
        if inst[0] == "W":
            if inst[2] == "R":
                print("sim")
            else:
                print("não")

            #posi = calculo_pos
            #matriz[i][j] = pos

    def imprime_tabuleiro(self):
        for i in range(8):
            print(self.matriz[i])

x = Xadrez()
b = x.cria_tabuleiro()
x.imprime_tabuleiro()
a = x.movimento("W-TH3")