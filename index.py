from io import open
import tkinter as tk  # this is the preferred import for tkinter
from tkinter import filedialog


class Practica1:
    def __init__(self):
        root = tk.Tk()  # esto se hace solo para eliminar la ventanita de Tkinter
        root.withdraw()  # ahora se cierra
        file_path = filedialog.askopenfilename()
        self.archive = open(file_path)

    def save(self):

        try:
            arc = self.archive.readlines()
            for i in arc:
                hexa, other = self.separateHexa(i)
                name = other[1]
                ipv4 = self.separeteIpv4(other[5])
                hexaToDec = self.converter(hexa, 16)
                decToHex = self.converter(ipv4, 10)
                aux = ':'.join(map(str, hexaToDec))
                aux2 = '.'.join(map(str, decToHex))
                string = "{}:{}:{}".format(name, aux, aux2)
                res = open('res.txt', 'a')
                res.write(string + '\n')
            self.archive.close()

        except print(0):
            self.archive.close()

    def separateHexa(self, arc):
        hexaNum1 = arc.split(':')
        hexaNum2 = hexaNum1[7].split('/')
        hexaNum1 = hexaNum1[:7]
        hexaNum1.append(hexaNum2[0])
        otherText = hexaNum2[1].split(',')
        return hexaNum1, otherText

    def separeteIpv4(self, ipv4):
        aux = ipv4.split('.')
        return aux

    def converter(self, num, base):
        if(base != 10):
            for i in range(len(num)):
                num[i] = int(num[i], base)
                # print(num[i])
        else:
            for i in range(len(num)):
                num[i] = hex(int(num[i])).split('x')[-1]
                # print(num[i])
        return num


archivo = Practica1()
archivo.save()
