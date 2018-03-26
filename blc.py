#!/usr/bin/env python3
import os
a,b,c,d,e,f,g,h,j,k,l,m,n,o,p,q, = 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
os.system("clear")
print("\n\n--------------WELCOME----------------\n\twritten by parth patel\n")
i = int(input("select command by pressing number : \n\n press 99 to quit the program\n\n1)--To display available shells\n2)--To display current working shell\n3)--To open calender\n4)--To display date\n5)--To open calculator\n6)--To display a message\n7)--To change password\n8)--To display path of home directory\n9)--To display path of present working directory\n10)--To create a directory\n11)--To change directory\n12)--To remove a directory\n13)--To remove a file\n14)--To copy file\n15)--To rename a file\n16)--To compare two files\n"))

z = 99
if i == z:
    print("-----------THANKS FOR USING MY PROGRAM---------\n\t Parth Patel")
elif i == a:
    os.system("cat /etc/shells")
elif i == b:
    os.system("echo $SHELL")
elif i == c:
    m = int(input("enter the month number"))
    y = int(input("enter the year number"))
    os.system("cal {0} {1}".format(m,y))
elif i == d:
    os.system("date")
elif i == e:
    os.system("bc -l")
elif i == f:
    mess = input("enter the message")
    os.system("echo {0}".format(mess))
elif i == g:
    os.system("passwd")
elif i == h:
    os.system("echo $HOME")
elif i == j:
    os.system("pwd")
elif i == k:
    dire = input("enter the directory name")
    os.system("mkdir {0}".format(dire))
    
elif i == l:
    cha = input("enter the directory name you want to change")
    os.system("cd {0}".format(cha))
elif i == m:
    rmd = input("enter the file name you want to remove")
    os.system("rmdir {0}".format(rmd))
elif i == n:
    rf = input("enter file name that you want to remove")
    os.system("rm {0}".format(rf))
elif i == o:
    c1 = input("enter original file name")
    c2 = input("enter new file name where you want to copy original file")
    os.system("cp {0} {1}".format(c1,c2))
elif i == p:
    c12 = input("enter original file name")
    c22 = input("enter new file name ")
    os.system("mv {0} {1}".format(c12, c22))
elif i == q:
    cmp1 = input("enter first file name to compare ")
    cmp2 = input("enter second  file name to compare")
    os.system("cmp {0} {1}".format(cmp1, cmp2))
else:
    print("invalid input")


print("DONE")












