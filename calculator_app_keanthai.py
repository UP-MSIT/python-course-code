from tkinter import *
from functools import partial
from decimal import Decimal
main =Tk()
main.geometry('320x540+200+200')
main.title("Calculator")
main.resizable(0,0)

firstText=""
secondText=""
operator=""
result=0

lblWidget=Label(main,text='0',fg='Black',bg='White',width=35,height=4)
lblWidget.place(x=0,y=0)

def clearCache():
    global firstText
    global operator
    global secondText
    global result
    firstText=""
    secondText=""
    operator=""
    result=0

def remove_exponent(d):
    return (
        d.quantize(Decimal(1))
        if d == d.to_integral()
        else d.normalize()
    )

def customButton(value,x,y,click,w=6,h=6):
    btn=Button(main,text=f"{value}",bd=1,bg='White',width=w,height=h,command=click)
    btn.place(x=x,y=y)
    return btn

def onNumBtnClick(value):
    global firstText
    global secondText
    global result
    if result != 0:
        clearCache()
    if firstText == '0':
        firstText = ""
    if secondText == '0':
        secondText = ""
    if operator=='':
        firstText+=value
        lblWidget.configure(text=firstText)
    elif operator!='':
        secondText+=value
        lblWidget.configure(text=secondText)

def onEdqualClick():
    global operator
    global firstText
    global secondText
    global result
    num1=float(firstText)
    num2=float(secondText)
    if operator=='+':
        result=num1+num2

    elif operator=='-':
        result=num1-num2

    elif operator=='*':
        result=num1*num2

    elif operator=='/':
        if num2==0.0:
            clearCache()
            lblWidget.configure(text='Error operant!')
            return
        else:
            result=num1/num2
    result=remove_exponent(Decimal(result))
    lblWidget.configure(text=result)
    #firstText=""
    #secondText=""
    #operator=""

def onDotClick():
    global firstText
    global secondText
    if firstText == '':
        firstText = "0"
    if secondText == '':
        secondText = "0"
    
    if operator=='':
        if '.' not in firstText:
            firstText+='.'
            lblWidget.configure(text=firstText)
    elif operator!='':
        if '.' not in secondText:
            secondText+='.'
            lblWidget.configure(text=secondText)

def onCBtnClick():
    global firstText
    global operator
    global secondText
    firstText="0"
    secondText="0"
    operator=""
    lblWidget.configure(text=firstText)

def onOperatorClick(value):
    global operator
    global result
    global firstText
    global secondText
    if firstText!="0" and firstText!="" and secondText!="0" and secondText != "":
        onEdqualClick()
    if result != 0:
        firstText=result
        result=0
        secondText=""
    operator=value

cBtn=customButton("C",0,70,w=24,h=6,click=onCBtnClick)
plusBtn=customButton("+",240,70,click=partial(onOperatorClick,"+"))

oneBtn=customButton("1",0,155,click=partial(onNumBtnClick,"1"))
twoBtn=customButton("2",80,155,click=partial(onNumBtnClick,"2"))
threeBtn=customButton("3",160,155,click=partial(onNumBtnClick,"3"))
minusBtn=customButton("-",240,155,click=partial(onOperatorClick,"-"))

fourBtn=customButton("4",0,250,click=partial(onNumBtnClick,"4"))
fiveBtn=customButton("5",80,250,click=partial(onNumBtnClick,"5"))
sixBtn=customButton("6",160,250,click=partial(onNumBtnClick,"6"))
multiplyBtn=customButton("x",240,250,click=partial(onOperatorClick,"*"))

sevenBtn=customButton("7",0,345,click=partial(onNumBtnClick,"7"))
eightBtn=customButton("8",80,345,click=partial(onNumBtnClick,"8"))
nineBtn=customButton("9",160,345,click=partial(onNumBtnClick,"9"))
divideBtn=customButton("/",240,345,click=partial(onOperatorClick,"/"))

zeroBtn=customButton("0",0,440,w=16,h=6,click=partial(onNumBtnClick,"0"))
dotBtn=customButton(".",160,440,click=onDotClick)
equalBtn=customButton("=",240,440,click=onEdqualClick)

main.mainloop()
