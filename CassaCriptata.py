from tkinter import *
from tkinter import ttk  
from math import gcd, isqrt, log
from tkinter import messagebox
from sympy import isprime, nextprime
from random import randint, seed
import time
from tkinter import simpledialog
import os
import hashlib

def hash_password(password):
    # Genera un salt casuale per aggiungere casualità all'hashing
    salt = os.urandom(32)

    # Combina la password con il salt e calcola l'hash
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    # Combina il salt e l'hash in un unico valore da memorizzare nel database
    hashed_password_hex = salt.hex() + hashed_password.hex()

    return hashed_password_hex

def verify_password(input_password, stored_password):
    # Estrae il salt dal valore memorizzato
    salt = bytes.fromhex(stored_password[:64])

    # Calcola l'hash della password di input con lo stesso salt
    hashed_input_password = hashlib.pbkdf2_hmac('sha256', input_password.encode('utf-8'), salt, 100000)

    # Confronta il salt e l'hash con il valore memorizzato
    return stored_password[64:] == hashed_input_password.hex()

def get_password_from_user():
    password = simpledialog.askstring("Password", "Inserisci la password:", show="*")
    return password

# Esempio di utilizzo
password = "Dicembre2023"
hashed_password = hash_password(password)

# Verifica della password
input_password = get_password_from_user()

if verify_password(input_password, hashed_password):
    pass
else:
    messagebox.showerror("Errore", "La password inserita è errata.")
    exit()


fondo_finestra1 = '#007FFF'
fondo_finestra2 = '#3D9140'
fondo_finestra3 = '#CD950C'


#****************************************************************
#   carica la lista txt contenuti nella cartella DCP
#****************************************************************
def popola_combobox_con_file():
    if os.path.exists(cartella) and os.path.isdir(cartella):
        file_txt = [file for file in os.listdir(cartella) if file.endswith(".txt")]
        combobox['values'] = file_txt
        combobox.update()
    else:
        messagebox.showerror('Attenzione', 'La cartella non esiste')

#****************************************************************
#   Apre il file codificato e lo decodifica
#****************************************************************
def apri_file_selezionato(event):
    nome_file = cartella+'/'+ combobox.get()
    
    try:
        # Tentativo di aprire il file in modalità lettura ('r')
        with open(nome_file, 'r') as leggi:
            data_inserito=leggi.readline()
            n_semiprimo=leggi.readline()
            testo_criptato=leggi.readline()
            leggi.close()
            n_semiprimo=n_semiprimo.strip()
            testo_criptato=testo_criptato.strip()
            chiave = 797623877234873371056847296053**18
            n_semiprimo=int(n_semiprimo)
            a = n_semiprimo%chiave
            b=n_semiprimo-a
            for i in range(10):
                r = gcd(b, a)
                if r != 1:
                    break
                a=a+chiave
                b=b-chiave    
            if r==1:
                messagebox.showerror('Attenzione', 'Codice Non Trovato')
                return
            start1 = str(r)
            start2 = len(start1)
            start = int(start1[start2-5]+start1[start2-4])

            ln = list(str(r))
            if len(ln) % 2 == 0:
                pass
            else:
                ln.append('0')
            
            divln = []

            for i in range(0, len(ln), 2):
                c1 = int(ln[i])
                c2 = int(ln[i+1])
                c3 = c1*10+c2
                divln.append(c3)

           #**********************************************
            m1 = 101
            m2 = 213
            m3 = 157
            m4 = 255
            m5 = 341
          # **********************************************
            te=[]    
            d0=list(testo_criptato)
            for i in range(0,len(d0),3):
                d1=d0[i]
                d2=d0[i+1]
                d3=d0[i+2]
                te.append(d1+d2+d3)
            cont = start
            tdecript=''
            for i in range(len(te)):
                if cont >= len(divln):
                    cont = 0
                x=int(divln[cont])
                if x>=0 and x<25:
                    y=int(te[i])
                    tdecript=tdecript+(chr(y-x-m1))
                if x>=25 and x<40:
                    y=int(te[i])
                    tdecript=tdecript+(chr(y-x-m2))
                if x>=40 and x<50:
                    y=int(te[i])
                    tdecript=tdecript+(chr(y-x-m3))
                if x>=50 and x<75:
                    y=int(te[i])
                    tdecript=tdecript+(chr(y-x-m4))
                if x>=75 and x<100:
                    y=int(te[i])
                    tdecript=tdecript+(chr(y-x-m5))
                cont=cont+1        
            ae1.delete(0,END)    
            ae1.insert(0,data_inserito)
            tw1.delete('1.0',END)    
            tw1.insert('1.0',str(tdecript))
            return

    except FileNotFoundError:
            # Il file non esiste
            messagebox.showerror('Attenzione', 'Nome file inesistente')
            return

#****************************************************************
#   Codifica il testo e lo salva in DCP
#****************************************************************
def salva_documento():
    testo=tw2.get('1.0',END)
    testo=testo.strip()
    nome_file=be1.get()
    nome_file=nome_file.strip()
    if testo=='' or nome_file=='': 
        messagebox.showerror('Attenzione', 'Testo o nome file Assenti')
        return
    T = int(time.time())
    seed(T)
    p = (797623877234873371056847296053**16+3**50)
    q = (797623877234873371056847296053**21+2**50)
    nd=nextprime(p+randint(1,3**100))
    nd2=nextprime(q+randint(1,3**100))
    n = nd*nd2
    start1=str(nd)
    start2=len(start1)
    start=int(start1[start2-5]+start1[start2-4])
    ln=list(str(nd))
    if len(ln) % 2 == 0:
        pass
    else:
        ln.append('0')
    divln = []
    for i in range(0, len(ln), 2):
        c1 = int(ln[i])
        c2 = int(ln[i+1])
        c3 = c1*10+c2
        divln.append(c3)

# **********************************************
    m1 = 101
    m2 = 213
    m3 = 157
    m4 = 255
    m5 = 341
# **********************************************


    text=(testo)
    te = list(text)
    cont = start
    tcript=''

    for i in range(len(text)):
        if cont>=len(divln):
            cont=0
        if ord(te[i])>700:
            pass
        else:
            x=int(divln[cont])
            if x>=0 and x<25:
                x=x+m1+ord(te[i])
            if x>=25 and x<40:
                x=x+m2+ord(te[i])
            if x>=40 and x<50:
                x=x+m3+ord(te[i])
            if x>=50 and x<75:
                x=x+m4+ord(te[i])
            if x>=75 and x<100:
                x=x+m5+ord(te[i])
            tcript=tcript+str(x)    
            cont=cont+1        
    try:
        # Tentativo di aprire il file in modalità lettura ('r')
        with open(cartella+'/'+nome_file, 'r') as file:
            file.close()
            # Il file esiste, puoi eseguire le azioni necessarie
            messagebox.showerror('Attenzione', 'File esistente Non posso Sovrascriverlo\n Per motivi di sicurezza')
            return

    except FileNotFoundError:
        # Gestisci l'eccezione se il file non viene trovato
        ora = time.strftime('%a, %d %b %y %H:%M:%S', time.localtime())
        scrivi = open(cartella+'/'+nome_file, 'w')
        scrivi.write('File creato '+str(ora)+' S3675'+'\n')
        scrivi.write(str(n)+'\n')
        scrivi.write(tcript+'\n')
        scrivi.close()
        messagebox.showinfo('OK', 'File memorizzato correttamente')
        return
        


#****************************************************************
#   Finestra Principale
#****************************************************************
class Finestra1(Tk):  # Cambiato da tk.Tk a Tk
    def __init__(self):
        super().__init__()
        self.title("Finestra 1")
        self.title("Archivio Cassaforte Criptata")
        self.geometry('500x300')
        self.configure(bg=fondo_finestra1)
        global cartella
        cartella = 'C:\DCP'

        l1 = Label(self, text='CASSAFORTE 3675b', bg=fondo_finestra1, fg='black', font='arial 22 bold')
        l1.place(x=90, y=200)
        b1 = Button(self, text="Inserisci Documento", command=self.apri_finestra2)
        b1.place(x=100, y=100)
        b1 = Button(self, text="Apri Documento", command=self.apri_finestra3)
        b1.place(x=300, y=100)

    def apri_finestra2(self):
        finestra2 = Finestra2(self)
        finestra2.grab_set()

    def apri_finestra3(self):
        finestra3 = Finestra3(self)
        finestra3.grab_set()

#****************************************************************
#   Finestra2 crea e salva documento
#****************************************************************
class Finestra2(Toplevel):  # Cambiato da tk.Toplevel a Toplevel
    def __init__(self, master):
        super().__init__(master)
        self.geometry('600x620')
        self.configure(bg=fondo_finestra2)
        self.title("Crea e Salva Documento")
        global tw2
        global be1
        bl2 = Label(self,text='Salva Documento Con "nome.txt" ', bg=fondo_finestra2,font='arial 14')
        bl2.place(x=10, y=50)
        bb1=Button(self,width=5,text='Salva',bg='#CAFF70',command=salva_documento)
        bb1.place(x=330,y=73)
        be1=Entry(self,width=50,bg='yellow',justify='center')
        be1.place(x=10,y=79)
        tw2 = Text(self, height=30, width=72, wrap=WORD,bg='beige', fg='black', cursor='arrow')
        tw2.place(x=10, y=100)

    def apri_finestra3(self):
        finestra3 = Finestra3(self)
        finestra3.grab_set()

#****************************************************************
#   Finestra3 carica un documento da DCP e lo traduce
#****************************************************************
class Finestra3(Toplevel):  # Cambiato da tk.Toplevel a Toplevel
    def __init__(self, master):
        super().__init__(master)
        self.geometry('600x670')
        self.configure(bg=fondo_finestra3)
        self.title("Carica Documento")
        global combobox
        global ae1
        global tw1
        combobox_value = StringVar()  # Aggiunta di una variabile di testo per il Combobox
        combobox = ttk.Combobox(self, textvariable=combobox_value, state="readonly",width=40)  # Utilizzo di ttk.Combobox
        combobox.place(x=10, y=50)
        popola_combobox_con_file()
        combobox.bind("<<ComboboxSelected>>", apri_file_selezionato)
        al1 = Label(self,text='Carica il file', bg=fondo_finestra3,font='arial 14')
        al1.place(x=10, y=5)
        al2 = Label(self,text='Data Inserimento File', bg=fondo_finestra3,font='arial 14')
        al2.place(x=10, y=110)
        ae1=Entry(self,width=50,bg='yellow',justify='center')
        ae1.place(x=10,y=140)
        tw1 = Text(self, height=25, width=72, wrap=WORD,bg='beige', fg='black', cursor='arrow')
        tw1.place(x=10, y=190)
        

if __name__ == "__main__":
    finestra_principale = Finestra1()
    finestra_principale.mainloop()
