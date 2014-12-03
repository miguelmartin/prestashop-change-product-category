#!/usr/bin/python
# -*- encoding: utf-8 -*-
import MySQLdb
import getpass

server = raw_input('Nombre de del host o dirección ip del servidor de BBDD :')
host = (server)
base = raw_input('Nombre de la base de datos de Prestashop :')
database = (base)
nombreu = raw_input('Nombre de del usuario para la base de datos :')
user = (nombreu)
contra = getpass.getpass("Contraseña del usuario para la base de datos :")
passwd = (contra)

try:
	db=MySQLdb.connect(host=host,user=user,passwd=passwd,db=database)
except:
	print "Conexion a la base de datos fallida, revise los datos"
	exit()
print "Esto AÑADIRA a todos los articulos a una categoria, la cuál especificara por su id_category"
print "¡Asegurese de que el id de la categoria que va a facilitar existe y tiene algun producto asociado!"
categoria = raw_input('ID de la categoria a la que quiere añadir los productos :')
category = (categoria)

cursor = db.cursor()
cursor2 = db.cursor()
mi_query = 'select distinct(id_product) from ps_category_product where id_product not in (select distinct(id_product) from ps_category_product where id_category=%s);' % (category)
mi_query2 = 'select max(position) from ps_category_product where id_category=%s;' % (category)
cursor.execute(mi_query)
cursor2.execute(mi_query2)
productos = cursor.fetchall()
posicion = cursor2.fetchall()
posicion =  posicion[0][0]
for producto in productos:
        try:
		posicion = posicion+1
	except:
		print "El id de la categoria facilitado no existe"
		exit()
        producto = producto[0]
        insert = "insert into ps_category_product values ('%s','%s','%s');" % (category,producto,posicion)
	cursor.execute(insert)
        db.commit()
db.close()
