#tkinter meghívása
from tkinter import *
import math

#változó létrehozása és dekralálás
kifejez = "" 
elozoeredmeny=""



# frisíti a beírt müveletett
# beviteli mező
def press(num): 
	#változó meghívása
	global kifejez 

	# szöveg lesz a szám
	kifejez = kifejez + str(num) 

	# frisíti a beírt müveletett
	egyenloseg.set(kifejez) 


# kiszámolás 
def equalpress(): 
	#próba
	try: 

		global kifejez 
		global elozoeredmeny

		#kiszámolja, eval átalakítja műveleté 
		total = str(eval(kifejez)) 

		egyenloseg.set(total)
		
        #előző eredmény elmentése
		elozoeredmeny=str(total)
		

		#újra üres lesz a müvelet
		kifejez = ""

	#ha valami nem münködne vagy rossz müveletett írt be
	except: 

		egyenloseg.set(" error ") 
		kifejez = "" 


#eltünteti az eddig beírt számokat
def clear(): 
	global kifejez 
	kifejez = "" 
	egyenloseg.set("") 

def delete():
	global egyenloseg
	global kifejez
	kifejez = kifejez[:-1]
	egyenloseg.set(kifejez)

#fő kód

	#létrehozza az ablakot 
root = Tk() 

	#szöveg méret és szín
font = ('Arial', 16)

	# háttérszín 
root.configure(background="white") 

	# title/felirat
root.title("Számoló gép") 

	# ablak mérete 
root.geometry("250x380") 

	#egy változó lesz amit beírunk, bármikor le lehet kérni
egyenloseg = StringVar() 

	#ide lehet beírni a számokat
kifejez_field = Entry(root, textvariable=egyenloseg,bg='white',fg='green',font=font) 

	#hol legyen a beviteli mező 
kifejez_field.grid(columnspan=4,pady=8 )

	#gombok és helyzetük
	#Mindegyik egy külön szám
	# jelek is itt vannak 
button1 = Button(root, text=' 1 ', fg='white', bg='gray', 
					command=lambda: press(1), height=3, width=7) 
button1.grid(row=2, column=0) 

button2 = Button(root, text=' 2 ', fg='white', bg='gray', 
					command=lambda: press(2), height=3, width=7) 
button2.grid(row=2, column=1) 

button3 = Button(root, text=' 3 ', fg='white', bg='gray', 
					command=lambda: press(3), height=3, width=7) 
button3.grid(row=2, column=2) 

button4 = Button(root, text=' 4 ', fg='white', bg='gray', 
					command=lambda: press(4), height=3, width=7) 
button4.grid(row=3, column=0) 

button5 = Button(root, text=' 5 ', fg='white', bg='gray', 
					command=lambda: press(5), height=3, width=7) 
button5.grid(row=3, column=1) 

button6 = Button(root, text=' 6 ', fg='white', bg='gray', 
					command=lambda: press(6), height=3, width=7) 
button6.grid(row=3, column=2) 

button7 = Button(root, text=' 7 ', fg='white', bg='gray', 
					command=lambda: press(7), height=3, width=7) 
button7.grid(row=4, column=0) 

button8 = Button(root, text=' 8 ', fg='white', bg='gray', 
					command=lambda: press(8), height=3, width=7) 
button8.grid(row=4, column=1) 

button9 = Button(root, text=' 9 ', fg='white', bg='gray', 
					command=lambda: press(9), height=3, width=7) 
button9.grid(row=4, column=2) 

button0 = Button(root, text=' 0 ', fg='white', bg='gray', 
					command=lambda: press(0), height=3, width=7) 
button0.grid(row=5, column=0) 

plus = Button(root, text=' + ', fg='white', bg='gray', 
				command=lambda: press("+"), height=3, width=7) 
plus.grid(row=2, column=3) 

minus = Button(root, text=' - ', fg='white', bg='gray', 
				command=lambda: press("-"), height=3, width=7) 
minus.grid(row=3, column=3) 

multiply = Button(root, text=' * ', fg='white', bg='gray', 
					command=lambda: press("*"), height=3, width=7) 
multiply.grid(row=4, column=3) 

divide = Button(root, text=' / ', fg='white', bg='gray', 
					command=lambda: press("/"), height=3, width=7) 
divide.grid(row=5, column=3) 

equal = Button(root, text=' = ', fg='white', bg='gray', 
				command=equalpress, height=3, width=7) 
equal.grid(row=6, column=3) 

clear = Button(root, text='Clear', fg='white', bg='gray', 
				command=clear, height=3, width=7) 
clear.grid(row=5, column='1') 

Decimal= Button(root, text='.', fg='white', bg='gray', 
					command=lambda: press('.'), height=3, width=7) 
Decimal.grid(row=6, column=0) 

ans= Button(root, text='Ans', fg='white', bg='gray', 
					command=lambda: press(elozoeredmeny), height=3, width=7) 
ans.grid(row=5, column=2) 
	#loop/folyamatos ismétlődés

log= Button(root, text='log', fg='white', bg='gray', 
					command=lambda: press('math.log('), height=3, width=7) 
log.grid(row=6, column=1) 
rod= Button(root, text=',', fg='white', bg='gray', 
					command=lambda: press(','), height=3, width=7) 
rod.grid(row=6, column=2) 
close= Button(root, text=')', fg='white', bg='gray', 
					command=lambda: press(')'), height=3, width=7) 
close.grid(row=7, column=2) 
delet= Button(root, text='Del', fg='white', bg='gray', 
					command=delete, height=3, width=7) 
delet.grid(row=7, column=1) 
	#loop/folyamatos ismétlődés

root.mainloop() 
