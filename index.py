import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
anoter = 'test'  

def check(email):   
    if(re.search(regex,email)):   
        return True  
    else:   
        return False

def return_emails(emails):
    for i in range(len(emails)):
        name, email = emails[i].split(' ')

        if check(email[1:-1]):
          print(name, email)

return_emails(['dheeraj <dheeraj-234@gmail.com>',
'crap <itsallcrap>',
'harsh <harsh_1234@rediff.in>',
'kumal <kunal_shin@iop.az>',
'mattp <matt23@@india.in>',
'harsh <.harsh_1234@rediff.in>',
'harsh <-harsh_1234@rediff.in>'])