# 403Bytepass
Python tool for forbidden urls bypassing

Prerequisites:

- python3
- curl

install:

$ git clone https://github.com/mathis2001/403Bytepass.git

Check installation:

$ cd 403Bytepass

$ python3 403bytepass.py

or
 
$ chmod u+x 403bytepass.py
$ ./403bytepass.py

![image](https://user-images.githubusercontent.com/40497633/160373432-f9b141e3-5a1a-4344-a691-0b1055bf1c7a.png)


Usage:

$ python3 403bytepass.py "target"

$ ./403bytepass.py "target"

Exemples:
 
$ python3 403bytepass.py http://target.xxx

or
 
$ python3 403bytepass.py http://target.xxx/XXX
 
or
 
$ python3 403bytepass.py https://target.xxx
 
or
 
$ python3 403bytepass.py https://target.xxx/XXX

![tempsnip](https://user-images.githubusercontent.com/40497633/160359511-3c80c4ab-6eb7-45e4-9833-6a0b19c5a929.png)
 
![image](https://user-images.githubusercontent.com/40497633/160358945-dec9b05d-6573-477d-8856-283a69b4d4d1.png)

![image](https://user-images.githubusercontent.com/40497633/160359035-ea029ded-25c6-4630-b19c-af61edb9619d.png)

![image](https://user-images.githubusercontent.com/40497633/160359133-d68b3068-c478-4c60-a117-98afdfa3ee2e.png)

Wanted improvement:
- grep Location header when redirecting (You can use curl -k -s -I -L "option" "target" to follow redirection)
- add args parser to make it more user friendly !
