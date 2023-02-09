from PySimpleGUI import PySimpleGUI as sg
import os

n1 = []
n2 = []
o = ''


class Tela:
    def __init__(self):
        
        #Layout#
        sg.theme('Reddit')


        layout = [
            [sg.Output(size = (100,3))],
            [sg.Button('7', size = (4,2), key = 'n7'), sg.Button('8', size = (4,2), key = 'n8'),sg.Button('9', size = (4,2), key = 'n9'),sg.Button('/', size = (10,2), key = 'od') ],
            [sg.Button('4', size = (4,2), key = 'n4'), sg.Button('5', size = (4,2), key = 'n5'),sg.Button('6', size = (4,2), key = 'n6'),sg.Button('X', size = (10,2), key = 'om') ],
            [sg.Button('1', size = (4,2), key = 'n1'), sg.Button('2', size = (4,2), key = 'n2'),sg.Button('3', size = (4,2), key = 'n3'),sg.Button('+', size = (10,2), key = 'oa')],
            [sg.Button('CE', size = (4,2), key = 'ce'), sg.Button('0', size = (4,2), key = 'n0'),sg.Button(',', size = (4,2), key = 'v'),sg.Button('=', size = (10,2), key = 'fn') ]
        ]


        self.window = sg.Window('Calculadora', size =(230,290)).layout(layout)

        
    def Iniciar(self):
        while True:
            self.button, self.values = self.window.Read() 
            if self.button == sg.WIN_CLOSED :
                break

            if self.button == 'n0' :
                n1.append('0')
            if self.button == 'n1' :
                n1.append('1')
            if self.button == 'n2' :
                n1.append('2')
            if self.button == 'n3' :
                n1.append('3')
            if self.button == 'n4' :
                n1.append('4')
            if self.button == 'n5' :
                n1.append('5')
            if self.button == 'n6' :
                n1.append('6')
            if self.button == 'n7' :
                n1.append('7')
            if self.button == 'n8' :
                n1.append('8')
            if self.button == 'n9' :
                n1.append('9')


            while True: 
                self.button, self.values = self.window.Read() 
                if self.button == sg.WIN_CLOSED :
                    break

                ### Primeiro numero###
                
                if self.button == 'n0' :
                    n1.append('0')
                if self.button == 'n1' :
                    n1.append('1')
                if self.button == 'n2' :
                    n1.append('2')
                if self.button == 'n3' :
                    n1.append('3')
                if self.button == 'n4' :
                    n1.append('4')
                if self.button == 'n5' :
                    n1.append('5')
                if self.button == 'n6' :
                    n1.append('6')
                if self.button == 'n7' :
                    n1.append('7')
                if self.button == 'n8' :
                    n1.append('8')
                if self.button == 'n9' :
                    n1.append('9')

                if self.button == 'v' :
                    n1.append('.')
                
                if self.button == 'oa' :
                    o = 'ad'
                    strn1 = "".join(n1)   
                    nn1 = float(strn1)
                    print(nn1)
                    print('+')
                    break

                if self.button == 'om' :
                    o = 'mul'
                    strn1 = "".join(n1)   
                    nn1 = float(strn1)
                    print(nn1)
                    print('X')
                    break

                if self.button == 'od' :
                    o = 'div'
                    strn1 = "".join(n1)   
                    nn1 = float(strn1)
                    print(nn1)
                    print('/')
                    break


                if self.button == 'fn' :
                    strn1 = "".join(n1)   
                    nn1 = float(strn1)
                    print(nn1)



            while True :
                self.button, self.values = self.window.Read() 
                if self.button == sg.WIN_CLOSED :
                    break

                if self.button == 'n0' :
                    n2.append('0')
                if self.button == 'n1' :
                    n2.append('1')
                if self.button == 'n2' :
                    n2.append('2')
                if self.button == 'n3' :
                    n2.append('3')
                if self.button == 'n4' :
                    n2.append('4')
                if self.button == 'n5' :
                    n2.append('5')
                if self.button == 'n6' :
                    n2.append('6')
                if self.button == 'n7' :
                    n2.append('7')
                if self.button == 'n8' :
                    n2.append('8')
                if self.button == 'n9' :
                    n2.append('9')

                if self.button == 'v' :
                    n2.append('.')


                if self.button == 'fn' :
                    if o == 'ad' :
                        strn1 = "".join(n1)   
                        nn1 = float(strn1)

                        strn2 = "".join(n2) 
                        nn2 = float(strn2)
                        print(nn2 ,' = ', nn1 + nn2)

                    elif o == 'mul' :
                        strn1 = "".join(n1)   
                        nn1 = float(strn1)

                        strn2 = "".join(n2) 
                        nn2 = float(strn2)
                        print(nn2 ,' = ', nn1 * nn2)

                    elif o == 'div' :
                        strn1 = "".join(n1)   
                        nn1 = float(strn1)

                        strn2 = "".join(n2) 
                        nn2 = float(strn2)
                        print(nn2 ,' = ', nn1 / nn2)




janela = Tela()
janela.Iniciar()
