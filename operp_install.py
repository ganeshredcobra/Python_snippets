#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       operp_install.py
#       
#       Copyright 2011 Ganesh.H <ganesh@space-kerala.org>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import os
import commands


def main():
	os.system('apt-get install python python-dateutil python-egenix-mxdatetime python-psycopg2 python-pychart python-pydot python-reportlab python-tz python-lxml python-mako python-libxslt1 python-vobject python-yaml python-hippocanvas python-matplotlib python-setuptools python-cherrypy python-formencode python-pyparsing python-simplejson python-dev build-essential babel')
	os.system('apt-get install postgresql-8.4 postgresql-client-8.4 postgresql-client')
	postgres()
	editconf()
	print os.getuid()	
	#os.system('clear')
	print "ok"
	os.system('wget http://www.openerp.com/download/stable/deb/openerp-server-6.0.2-0_all.deb')
	os.system('dpkg -i openerp-server-6.0.2-0_all.deb')
	servconf()
	os.system('wget http://www.openerp.com/download/stable/deb/openerp-client-6.0.2-0_all.deb')
	os.system('dpkg -i openerp-client-6.0.2-0_all.deb')	
	return 0

def editconf():
	try:
		path='/etc/postgresql/8.4/main/pg_hba.conf'
		file=open('%s'%path,'r+')
		new=file.read()
		text=new.replace('local   all         all                               ident','local   all         all                               trust')
		text=text.replace('host    all         all         127.0.0.1/32          md5','host    all         all         127.0.0.1/32          trust')
		text=text.replace('host    all         all         ::1/128               md5','host    all         all         ::1/128               trust')
		file=open('%s'%path,'w+')
		file.write('%s'%text)
		return
	except:
		print "Postgres Configuration file editing error file not present or unable to edit...."
 
def postgres():
	try:
		#id=commands.getoutput('id -u postgres')
		#os.setuid(int(id))
		#print os.getuid()
		os.system('clear')
		name=raw_input("Enter a name for database and user : ")
		global name
		os.system('su - postgres -c "createuser --createdb --no-createrole --pwprompt %s"'%name)
		os.system('su - postgres -c "createdb -O %s %s"'%(name,name))
		os.system('su - postgres -c "/etc/init.d/postgresql restart"')
		return	
	except:
		print "Error while creating Postgres database and user......."

def servconf():
	try:		
		passwd=raw_input('Enter the postgres passowrd : ')
		path='/etc/openerp-server.conf'
		file=open('%s'%path,'r+')
		new=file.read()
		text=new.replace('; db_name = terp','; db_name = %s'%name)
		text=text.replace('db_user = openerp','db_user = %s'%name)
		text=text.replace('db_password = False','db_password = %s'%passwd)
		text=text.replace('db_host = False','db_host = localhost')
		text=text.replace('db_port = False','db_port = 5432')
		file=open('%s'%path,'w+')
		file.write('%s'%text)
		return
	except:
		print "Error while editing openerp-server.conf file ; File not present or unable to edit......"

def root():
	val=os.getuid()
	if val!=0:
		print "You are not root!!Pls run the script as root user :)"
	else:
		main()



if __name__ == '__main__':
	root()
