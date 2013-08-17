#!/usr/bin/python

import md5
texto = md5.new()

with open("diccionario.txt") as infile:
    for line in infile:
        linea_leida = line.strip('\n')
        print linea_leida
        texto.update(linea_leida)
        letra_md5 = texto.hexdigest()
        print letra_md5
        if (letra_md5 == "4d6bfce7c3d01def4625e405087939ed"):
                print line
                print "Lo he encontrado!"
                break

#test = md5.new("a")
#print test.hexdigest()
