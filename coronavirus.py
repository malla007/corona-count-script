import smtplib
from lxml import html
import requests
from lxml.etree import tostring

array = []

def send_mail(result):
    url = 'http://coronavirus.lk/'
    page = requests.get(url)
    tree = html.fromstring(page.content)

    count = tree.xpath('/html/body/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[2]/label')[0]
    new_total_cases = tostring(count)
    new_total_cases = str(new_total_cases)
    new_total_cases = new_total_cases.replace("'","")
    new_total_cases = new_total_cases.replace('"',"")
    new_total_cases = new_total_cases.replace('b<label style=color: #bc1717;>',"")
    new_total_cases = new_total_cases.replace('</label>',"")

    count = tree.xpath('/html/body/div[3]/div[2]/div[2]/table/tbody/tr[2]/td[2]/label')[0]
    patients = tostring(count)
    patients = str(patients)
    patients = patients.replace("'","")
    patients = patients.replace('"',"")
    patients = patients.replace('b<label style=color: #6f22c5;>','')
    patients = patients.replace('</label>','')

    yhat = tree.xpath('/html/body/div[3]/div[2]/div[2]/table/tbody/tr[3]/td[2]/label')[0]
    recovered = tostring(yhat)
    recovered = str(recovered)
    recovered = recovered.replace("'","")
    recovered = recovered.replace('"',"")
    recovered = recovered.replace('b<label style=color: #13a20c;','')
    recovered = recovered.replace('</label>','')
    recovered = recovered.replace('>','')
   
    woo = tree.xpath('/html/body/div[3]/div[2]/div[2]/table/tbody/tr[4]/td[2]/label')[0]
    suspicious = tostring(woo)
    suspicious = str(suspicious)
    suspicious = suspicious.replace("'","")
    suspicious = suspicious.replace('"',"")
    suspicious = suspicious.replace('b<label style=color: #ea5300;>','')
    suspicious = suspicious.replace('</label>','')
    suspicious = suspicious.replace('>','')

    e = tree.xpath('/html/body/div[3]/div[2]/div[2]/table/tbody/tr[5]/td[2]/label')[0]
    dead = tostring(e)
    dead = str(dead)
    dead = dead.replace("'","")
    dead = dead.replace('"',"")
    dead = dead.replace('b<label style=color: #fba03e;>','')
    dead = dead.replace('</label>','')
    dead = dead.replace('>','')
    
    result = str(result)
    result_message = result+' people diagnosed with Corona!'

    data = 'Total Patients: '+new_total_cases+'\n'+'Current Patients: '+patients+'\n'+'Recovered Patients: '+recovered+'\n'+'Suspicious: '+suspicious+'\n'+'Dead: '+dead

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('email','pass')

    subject = result_message
    body = data
    print(subject)
    print(body)

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'mallasrilanka@gmail.com',
        'malindapath@gmail.com',
        msg
    )
    server.sendmail(
        'mallasrilanka@gmail.com',
        'mp0777840266@gmail.com',
        msg
    )
    server.quit()

while True:
    url = 'http://coronavirus.lk/'
    page = requests.get(url)
    tree = html.fromstring(page.content)
    count = tree.xpath('/html/body/div[3]/div[2]/div[2]/table/tbody/tr[1]/td[2]/label')[0]
    new_total_cases = tostring(count)
    new_total_cases = str(new_total_cases)
    new_total_cases = new_total_cases.replace("'","")
    new_total_cases = new_total_cases.replace('"',"")
    new_total_cases = new_total_cases.replace('b<label style=color: #bc1717;>',"")
    new_total_cases = new_total_cases.replace('</label>',"")
    new_total_cases = int(new_total_cases)
    array.append(new_total_cases)
    print(array)
    if len(array)>1:
        last_number = int(array[-1])
        before_number = int(array[-2])
        result = last_number-before_number
        if result>0:
            print(result)
            send_mail(result)             
        else:
            pass
    if len(array)>2:
        array.pop(0)
    else:
        pass







