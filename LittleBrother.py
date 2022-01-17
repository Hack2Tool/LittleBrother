#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, time, random, threading
from colorama import init, Fore,  Back,  Style
from lib.menu import checkVersion, clear, menu
from lib.loading import thread_loading
#Lookup Menu
from core.searchEmail import SearchEmail
from core.searchPersonne import searchPersonne
from core.searchAdresse import searchAdresse
from core.searchUserName import searchUserName
from core.ipFinder import ipFinder
from core.bssidFinder import bssidFinder
from core.mailToIP import mailToIP
from core.employee_lookup import employee_lookup
from core.google import google
from core.facebookStalk import facebookStalk
from core.searchTwitter import searchTwitter
from core.searchInstagram import searchInstagram
from core.profilerFunc import profilerFunc
from core.searchNumber import searchNumber
#Other tool menu
from core.hashDecrypt import hashdecrypt


#Help & settings
from txt.help import *
import settings

init()
settings.init()

warning = "["+Fore.RED+"!"+Fore.RESET+"]"
question = "["+Fore.YELLOW+"?"+Fore.RESET+"]"
information = "["+Fore.BLUE+"I"+Fore.RESET+"]"
wait = "["+Fore.MAGENTA+"*"+Fore.RESET+"]"
found = "["+Fore.GREEN+"+"+Fore.RESET+"]"
tiret = "["+Fore.CYAN+"-"+Fore.RESET+"]"


checkVersion()
thread_loading()



mainOption = """
 [1] Пробивы
 [2] Другие утилиты
 [3] Профилер

 [e] Выйти из скрипта    [h] Помощь    [c] Очистить экран"""


lookupOption = """
 [1] Пробив человека          [8] Пробить письмо
 [2] Пробив по нику           [9] Пробив работников
 [3] Пробив по адресу         [10] Поиск в Google
 [4] Пробив по телефону       [11] Facebook GraphSearch
 [5] Пробив по IP             [12] Пробив Твиттера
 [6] SSID локатор             [13] Пробив Инстаграма
 [7] Пробив по эмейлу

 [b] вернуться в меню   [e] выйти из скрипта    [h] помощь    [c] очистить экран"""

otherToolOption = """
 [1] Hash декодер

 [b] вернуться в меню    [e] выйти из скрипта    [h] помощь    [c] очистить экран
"""

profilerOption = """
 [1] Профилер
 [2] Показать профили
 [3] Создать профиль

 [b] вернуться в меню    [c] очистить экран   [h] помощь
"""

countryMenu = """

 [b] вернуться в меню    [c] очистить экран   [h] помощь
"""

clear()
menu()
print(mainOption)

try:
	while True:
		choix = input("\n LittleBrother("+Fore.BLUE + "~" + Fore.RESET + ")$ ")

		if choix.lower() == 'h':
			print(helpMain)
		elif choix.lower() == 'c':
			clear()
			menu()
			print(mainOption)
		elif choix == '3':
			clear()
			menu()
			print(profilerOption)

			while True:
				pr = settings.Profiler()
				pr.loadDatabase(settings.pathDatabase)
				database = pr.database

				choix = input("\n LittleBrother("+Fore.BLUE + "Профилер" + Fore.RESET + ")$ ")

				info = {"URL": {}}
				
				if choix.lower() == 'h':
					print(helpProfiler)
				elif choix.lower() == 'b':
					clear()
					menu()
					print(mainOption)
					break
				elif choix.lower() == 'c':
					clear()
					menu()
					print(profilerOption)
				elif choix.lower() == 'e' or choix.lower() == 'exit':
					sys.exit("\n"+information+" Пока ! :)")
				elif choix.lower() == "1":
					if pr.count >= 1:
						while True: 
							profile = input(" Профиль: ")
							if profile != '':
								break
						data = pr.searchDatabase(profile, database=database)
						profilerFunc(data, path=settings.pathDatabase)
					else:
						print(warning+" Профиль не найден. Пожалуйста, создайте его.")
				elif choix.lower() == "2":
					pr.showAllProfiles(database=database)

				elif choix.lower() == '3':
					print("\n"+Fore.YELLOW+"(Формат: Имя Фамилия)"+Fore.RESET)
					while True: 
						name = input(" Имя профиля: ")
						if name != '':
							break
					name = name.split(" ")
					name = [i.capitalize() for i in name]
					name = " ".join(name)
					while True:
						print(question+" Хотите зарегистрировать учетную запись Twitter для профиля?")
						choixPr = input(" [O/n]: " )
						if choixPr.upper() == 'N':
							break
						else:
							twitter = input("\n Твиттер: ")
							info['URL']['Twitter'] = twitter
							break
					# print(found+" %s" % (twitter))
					while True:
						print(question+" Хотите зарегистрировать учетную запись Instagram для профиля?")
						choixPr = input(" [O/n]: " )
						if choixPr.upper() == 'N':
							break
						else:
							instagram = input("\n Инстаграм: ")
							info['URL']['Instagram'] = instagram
							break
					while True:
						print(question+" Хотите зарегистрировать учетную запись Facebook для профиля?")
						choixPr = input(" [O/n]: " )
						if choixPr.upper() == 'N':
							break
						else:
							facebook = input("\n Facebook: ")
							info['URL']['Facebook'] = facebook
							break

					create = pr.writeProfile(fileName=name, path=settings.pathDatabase, info=info)

					if create:
						print("\n"+found+" Профиль '%s' был успешно создан" % (name))
					else:
						print("\n"+warning+" Произошла ошибка. Не удалось создать профиль '%s'." % (name))

		elif choix.lower() == 'e' or choix.lower() == 'exit':
			sys.exit("\n"+information+" Пока ! :)")
		elif choix == '1':
			clear()
			menu()
			print(lookupOption)
			while True:
				lookup = input("\n LittleBrother("+Fore.BLUE+"Lookup"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if lookup == 'h':
					print(helpLookup)
				elif lookup.lower() == '1':
					searchPersonne(settings.codemonpays)
				elif lookup.lower() == '2':
					searchUserName()
				elif lookup.lower() == '3':
					searchAdresse(settings.codemonpays)
				elif lookup.lower() == '4':
					searchNumber(settings.codemonpays)
				elif lookup.lower() == '5':
					ipFinder()
				elif lookup.lower() == '6':
					bssidFinder()
				elif lookup.lower() == '7':
					SearchEmail()
				elif lookup.lower() == '8':
					mailToIP()
				elif lookup.lower() == '9':
					employee_lookup()
				elif lookup.lower() == '10':
					google()
				elif lookup.lower() == "11":
					facebookStalk()
				elif lookup.lower() == "12":
					searchTwitter()
				elif lookup.lower() == "13":
					searchInstagram()
				elif lookup.lower() == "b":
					clear()
					menu()
					print(mainOption)
					break
				elif lookup.lower() == "c":
					clear()
					menu()
					print(lookupOption)
				elif lookup == '':
					pass
				elif lookup.lower() == "e":
					sys.exit("\n"+information+" Bye ! :)")
				else:
					pass
					# print("Команда не найдена")
		elif choix == '2':
			clear()
			menu()
			print(otherToolOption)
			while True:
				se = input("\n LittleBrother("+Fore.BLUE+"Другие утилиты"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if se == 'h':
					print(helpOtherTool)
				elif se == "1":
					hashdecrypt()
				elif se.lower() == "b":
					clear()
					menu()
					print(mainOption)
					break
				elif se.lower() == "c":
					clear()
					menu()
					print(otherToolOption)
				elif se == '':
					pass
				elif se.lower() == "e":
					sys.exit("\n"+information+" Bye ! :) ")
				else:
					pass
					# print("Commande introuvable")
		elif choix == "4":
			clear()
			menu()
			print(countryMenu)

			while True:
				newCode = input("\n LittleBrother("+Fore.BLUE+"Country"+Fore.BLUE + "" + Fore.RESET + ")$ ")
				if newCode == '1':
					settings.codemonpays = "FR"
					settings.monpays = "France"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == "2":
					settings.codemonpays = "BE"
					settings.monpays = "Belgique"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '3':
					settings.codemonpays = "CH"
					settings.monpays = 'Suisse'
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '4':
					settings.codemonpays = "LU"
					settings.monpays = "Luxembourg"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode == '5':
					settings.codemonpays = "XX"
					settings.monpays = "Europe"
					clear()
					menu()
					print(mainOption)
					break
				elif newCode.lower() == 'b':
					break
				elif newCode.lower() == 'c':
					clear()
					menu()
					print(countryMenu)
				elif newCode.lower() == 'h':
					print(helpMain)
		else:
			pass
			# print("Commande introuvable")

except KeyboardInterrupt:
	sys.exit("\n"+information+" Пока ! :)")
