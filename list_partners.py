#!/usr/bin/python

import sys
import xmlrpclib
import ssl

username = 'admin' #the user
pwd = 'demo_ar' #the user
dbname = 'demo_ar'    #the database

gcontext = ssl._create_unverified_context()

# Get the uid
sock_common = xmlrpclib.ServerProxy ('http://capacitacion:8069/xmlrpc/common',context=gcontext)
uid = sock_common.login(dbname, username, pwd)

#replace localhost with the address of the server
sock = xmlrpclib.ServerProxy('http://capacitacion:8069/xmlrpc/object',context=gcontext)

partner_ids = sock.execute(dbname,uid,pwd,'res.partner','search',[('customer_rank','>',0)])
for partner_id in partner_ids:
	partner_data = sock.execute(dbname,uid,pwd,'res.partner','read',partner_id,['name','email','city'])
	print partner_id,partner_data[0]
