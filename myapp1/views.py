import requests
import bs4
import lxml
from django.shortcuts import render
from django.http import HttpResponse
def temperature(request):
    temp={"temp":{"t1":" ","t2":" ","s1":"selected"}}
    if request.method =='POST':
        typ=str(request.POST.get('type'))
        t1=float(request.POST.get('t1'))
        if typ=="ctf":
            t2=(t1*1.8)+32
            temp={"temp":{"t1":t1,"t2":t2,"s1":"selected"}}
        elif typ=="ftc":
            t2=(t1/1.8)-32
            temp={"temp":{"t1":t1,"t2":t2,"s2":"selected"}}
        elif typ=="ctk":
            t2=t1+273.15
            temp={"temp":{"t1":t1,"t2":t2,"s3":"selected"}}
        else:
            t2=t1-273.15
            temp={"temp":{"t1":t1,"t2":t2,"s4":"selected"}}
    return render(request, 'temperature.html',temp)
def calculator(request):
    temp=dict()
    temp["val"]=""
    if request.method =='POST':
        s=str(request.POST.get('res'))
        temp["val"]=eval(s)
    return render(request, 'calculator.html',temp)
'''return render(request,'scrap.html',{'content':ans}) 
'''
def hi(request):
    res=requests.get("https://www.ndtv.com/coronavirus/india-covid-19-tracker")
    soup=bs4.BeautifulSoup(res.text,'lxml')
    s=soup.select('.ind-mp_num')
    a=s[4]
    b=s[5]
    c=s[6]
    d=s[7]
    a1=a.text.split(" ")
    b1=b.text.split(" ")
    c1=c.text.split(" ")
    d1=d.text.split(" ")
    
    return render(request,'scrap.html',{'content1':a1[0],'content2':b1[0],'content3':c1[0],'content4':d1[0]}) 
