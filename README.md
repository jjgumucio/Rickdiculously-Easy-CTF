# Rickdiculously Easy CTF
### This repo covers my walkthrough of the [Rickdiculously Easy 1](https://www.vulnhub.com/entry/rickdiculouslyeasy-1,207/) CTF game.

First difficulty I had to tackle was not related with the game per se. After opening the box in Virtualbox and running it,
it wasn't visible on my network. I tryed using nmap with several host discovery options. Finally I realized that I had to
configure the VMs network adapter to be "Bridged Adapter" (It was set as "NAT").

The file pass_gen.py is a python script I wrote in order to generate passwords following instructions found during the game.
The file passwords.txt is the result of running this script.

## Flags:
| Flag Text | Points | Comments |
| --------- |:------:|----------|
| There is no zeus, in your face! | 10 | Visiting _http://machine-ip:9090_
| Whoa this is unexpected | 10 | Visiting _ftp://machine-ip_
| Yeah d- just don't do it. | 10 | Visiting _http://machine-ip/passwords/password.html_ (path discovered using nikto)
| Get off the high road Summer! | 10 | ssh into the machine with user "Summer" and password "winter". Username found visiting _http://machine-ip/cgi-bin/tracertool.cgi_ (command line injection). The tool was revealed after checking robots.txt
| TheyFoundMyBackDoorMorty | 10 | Obtained from one of the services running on the machine (part of the banner, using nmap -sV an all ports)
| Flip the pickle Morty! | 10 | Obtained connecting to _machine-ip_ on port 60000 using netcat
| 131333 | 20 | Used as a argument while executing "safe" file. (scp from RickSanchez home folder)
| And Awwwaaaaayyyy we Go! | 20 | Obtained running the "safe" file with 131333 cmd arg
| Ionic Defibrillator | 30 | Obtained loging in as RickSanchez and running "sudo -i" (RickSanchez was in sudoers)

## Notes:
- Account name "Summer" uses password "winter" (obtained from /passwords/passwords.html source)
- After running "safe" with 131333 as a cmd arg, I found some "instructions" to generate RickSanchez user password?
- "Also, sudo is wheely good." Quote from this flag. There is a user group named wheel (user RickSanchez belogs to)
 1 uppercase character
 1 digit
 One of the words in my old bands name
- Password for user RickSanchez: P7Curtains
