import urllib.request
from urllib.request import *
from bs4 import BeautifulSoup
import io
import socket
red='\33[31m'
print(red+"""



 , ,  ,  ,__  ,_   ___, ,_  
 |_|, \_/'|_) |_) ' |   | \,
'| | , /`_|_)'| \  _|_,_|_/ 
 ' `(_/ '     '  `'   '     
          BY AMEER
                                                              
[https://github.com/ameer911]                                   
                                        
                                         """)
#color------------
red='\33[31m'
white='\33[26m'
yellow='\33[43m'
green='\33[92m'
burple='\33[90m'
blink='\33[5m'
blue='\33[34m'
#color------------


print(green+'''
1- admin page       
2- all sites are on the server              
3- all links are in-site 
4- scan server from vulnerability
5- port scan
6- get robots.txt from website''')

chose = input(white+'>>>:')
if chose == '1':
    url = input(green+'url:')
    if url == "":
        print('red+plz url')
    else:
        lista = ['admin.php', 'admin', 'login.php', 'login', 'user', 'user.php', 'admin/', 'administrator/', 'admin1/',
                 'admin2/', 'admin3/', 'admin4/', 'admin5/', 'usuarios/', 'usuario/', 'administrator/', 'moderator/',
                 'webadmin/', 'adminarea/', 'bb-admin/', 'adminLogin/', 'admin_area/', 'panel-administracion/',
                 'instadmin/',
                 'memberadmin/', 'administratorlogin/', 'adm/', 'admin/account.php', 'admin/index.php',
                 'admin/login.php', 'admin/admin.php', 'admin/account.php',
                 'admin_area/admin.php', 'admin_area/login.php', 'siteadmin/login.php', 'siteadmin/index.php',
                 'siteadmin/login.html', 'admin/account.html', 'admin/index.html', 'admin/login.html',
                 'admin/admin.html',
                 'admin_area/index.php', 'bb-admin/index.php', 'bb-admin/login.php', 'bb-admin/admin.php',
                 'admin/home.php', 'admin_area/login.html', 'admin_area/index.html',
                 'admin/controlpanel.php', 'admin.php', 'admincp/index.asp', 'admincp/login.asp', 'admincp/index.html',
                 'admin/account.html', 'adminpanel.html', 'webadmin.html',
                 'webadmin/index.html', 'webadmin/admin.html', 'webadmin/login.html', 'admin/admin_login.html',
                 'admin_login.html', 'panel-administracion/login.html',
                 'admin/cp.php', 'cp.php', 'administrator/index.php', 'administrator/login.php', 'nsw/admin/login.php',
                 'webadmin/login.php', 'admin/admin_login.php', 'admin_login.php',
                 'administrator/account.php', 'administrator.php', 'admin_area/admin.html',
                 'pages/admin/admin-login.php', 'admin/admin-login.php', 'admin-login.php',
                 'bb-admin/index.html', 'bb-admin/login.html', 'acceso.php', 'bb-admin/admin.html', 'admin/home.html',
                 'login.php', 'modelsearch/login.php', 'moderator.php', 'moderator/login.php',
                 'moderator/admin.php', 'account.php', 'pages/admin/admin-login.html', 'admin/admin-login.html',
                 'admin-login.html', 'controlpanel.php', 'admincontrol.php',
                 'admin/adminLogin.html', 'adminLogin.html', 'admin/adminLogin.html', 'home.html',
                 'rcjakar/admin/login.php', 'adminarea/index.html', 'adminarea/admin.html',
                 'webadmin.php', 'webadmin/index.php', 'webadmin/admin.php', 'admin/controlpanel.html', 'admin.html',
                 'admin/cp.html', 'cp.html', 'adminpanel.php', 'moderator.html',
                 'administrator/index.html', 'administrator/login.html', 'user.html', 'administrator/account.html',
                 'administrator.html', 'login.html', 'modelsearch/login.html',
                 'moderator/login.html', 'adminarea/login.html', 'panel-administracion/index.html',
                 'panel-administracion/admin.html', 'modelsearch/index.html', 'modelsearch/admin.html',
                 'admincontrol/login.html', 'adm/index.html', 'adm.html', 'moderator/admin.html', 'user.php',
                 'account.html', 'controlpanel.html', 'admincontrol.html',
                 'panel-administracion/login.php', 'wp-login.php', 'adminLogin.php', 'admin/adminLogin.php', 'home.php',
                 'admin.php', 'adminarea/index.php',
                 'adminarea/admin.php', 'adminarea/login.php', 'panel-administracion/index.php',
                 'panel-administracion/admin.php', 'modelsearch/index.php',
                 'modelsearch/admin.php', 'admincontrol/login.php', 'adm/admloginuser.php', 'admloginuser.php',
                 'admin2.php', 'admin2/login.php', 'admin2/index.php', 'usuarios/login.php',
                 'adm/index.php', 'adm.php', 'affiliate.php', 'adm_auth.php', 'memberadmin.php',
                 'administratorlogin.php', 'account.php', 'me.php', 'im.php', 'privet.php', 'god.php', 'phone.php',
                 'plus.php', 'home.php']
        for i in lista:
            if "/" not in url[-1]:
                s = url + "/"
                plus = s + i
                try:
                    opurl = urllib.request.urlopen(plus)
                    print(green+'[+] Found URL >>>  ', plus + '    <--- ')
                except urllib.request.URLError as msg:
                    print(red+'[-] Not Found >>>  ', plus)
            else:
                try:
                    plus = (url + i)
                    opurl = urllib.request.urlopen(plus)
                    print(green+'[+] Found URL >>>  ', plus + '    <--- ')
                except urllib.request.URLError as msg:
                    print(red+'[-] Not Found >>>  ', plus)

# 2------------------
if chose == '2':
    print(burple+'get all server site')
    get = input(green+'site to get ip [with out https or http]:')
    server = socket.gethostbyname(get)
    print(burple+'copy this ip ', server)
    print(blink+'-'*20)
    IP = input(green+'ip:')
    print(blink+'-'*20)
    agent = ({'User-agent': 'Mozilla/5.0'})
    bing = Request('https://www.bing.com/search?q=ip%3A' + IP + '&go=Search&qs=ds&form=QBRE', headers=agent)
    bing2 = Request('https://www.bing.com/search?q=ip%3a' + IP + '&go=Search&qs=ds&first=11&FORM=PERE', headers=agent)
    opnurl = urllib.request.urlopen(bing).read()
    opnurl2 = urllib.request.urlopen(bing2).read()
    soup = BeautifulSoup(opnurl, 'html.parser')
    soup2 = BeautifulSoup(opnurl2, 'html.parser')
    for site in soup.findAll('div', {'class': 'b_attribution'}):
        print(white+site.span.text)
        for site2 in soup2.findAll('dev', {'class': 'b_attribution'}):
            print(white+site2.span.text)
            print(blink+'-'*20)

# 3-------------------
if chose == '3':
    print(burple+'ex:https://www.google.com')
    site = input(green+'site url:')
    agent = ({'User-agent': 'Mozilla/5.0'})
    url = Request(site, headers=agent)
    openurl = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(openurl, 'html.parser')
    for i in soup.findAll('a'):
        print(red+'-' * 35)
        print(green+i.get('href'))

# 4--------------------
if chose=='4':
    print(burple+'scan all website on server from sql and upload')
    ips=input('website to get ip:')
    print('copy this ip: ',socket.gethostbyname(ips))
    scan=input(green+'Enter ip server:')
    print('')
    print('scanning from sql injection....')
    page=['php?id=','phpcat?id=','php?buyid=','page?id=','mysql']
    for i in page:
        op=Request('https://www.bing.com/search?q=ip%3A'+scan+'+'+i,headers=({'User-agent':'Mozilla/5.0'}))
        urlr=urllib.request.urlopen(op).read()
        soup2 = BeautifulSoup(urlr, 'html.parser')
        for sop in soup2.findAll('li', {'class': 'b_algo'}):
            print(green+sop.a.get('href'))

    print('scaning website from upload file....')
    page2=['upload.php','up.php','ud.php','load.php','shell.php','up.asp','upload.asp','file_upload.php','file_up.php','file_upload.asp','uploads.php','fileupload.php','fileupload.asp','upload','image-upload-php','upload-file.php']
    for i2 in page2:
        op2=Request('https://www.bing.com/search?q=ip%3A'+scan+'+'+i2,headers=({'User-agent':'Mozilla/5.0'}))
        urlr2=urllib.request.urlopen(op2).read()
        soup3=BeautifulSoup(urlr2, 'html.parser')
        for sop2 in soup3.findAll('li',{'class':'b_algo'}):
            print(green+sop2.a.get('href'))


#5--------------------
if chose=="5":
    print('ex:www.google.com')
    sites = input('website or ip:')
    print('-' * 60)
    print('please wait scanneing ip :',socket.gethostbyname(sites),' [maybe take 2-3 minute]')
    print('-' * 60)
    port = (range(1,1024))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for i in port:

        scans = s.connect_ex((sites, i))
        if scans == 0:
            print(i, 'open')
            print('--------')
    print('_' * 30)
    print('done')

#6--------------------
if chose=='6':
    print('ex:https://www.google.com')
    urls = input(green+'URL::')
    if urls.endswith('/'):
        path = urls
    else:
        path = urls + '/'
    req = urllib.request.urlopen(path + 'robots.txt', data=None)
    data = io.TextIOWrapper(req, encoding='utf-8')
    reed = data.read()
    print(reed)

