#!/usr/bin/env python
# coding: utf-8
# FINAL YEAR PROJECT
# FUZZY EXPERT SYSTEM FOR DIABETES DIAGNOSIS
# MOHAMAD HANIS BIN MOHD YUSOFF
# 2018299202
# UNIVERSITI TEKNOLOGI MARA PERLIS

#import library
import numpy as np
import skfuzzy as fuzz
import tkinter.messagebox as MessageBox
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import mysql.connector as mysql

#============================================== WINDOW & FRAME ====================================================
root = Tk()# Window Name
root.geometry("1180x860")# Window Size
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.title("Diabetes Diagnosis System")# Window Title

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)

for frame in (f1, f2, f3):
    frame.grid(row=0,column=0,sticky='nsew')

#============================================== FRAME 1 ============================================================
welcome = Label(f1, text='DIABETES DIAGNOSIS SYSTEM', font=('bold', 24))#IC
welcome.place(x=340, y=313);

f1_btn = Button(f1, text='Start', font=("bold", 12), bg="white",command=lambda:show_frame(f2))
f1_btn.place(x=520, y=600,width = 150, height = 45)

#============================================== FRAME 2 ============================================================
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#============================================== ENTRY FIELD ========================================================
eid = Entry(f2)# IC
eid.place(x=180, y=10, width = 250, height = 25)

enama = Entry(f2)# Nama
enama.place(x=180, y=40, width = 250, height = 25)

eumur = Entry(f2)# Umur
eumur.place(x= 180, y=70, width = 250, height = 25)

erbg = Entry(f2)# Random blodd glucose
erbg.place(x=180, y=100, width = 250, height = 25)

efbg = Entry(f2)# Fasting blood glucose
efbg.place(x=180, y=130, width = 250, height = 25)

#============================================== LABEL FOR ENTRY FIELD ==============================================
rangerbg = Label(f2, text='0>7.8><11<19', font=('bold', 12))# range rbg
rangerbg.place(x=430, y=100);

rangefbg = Label(f2, text='0>6><7<13', font=('bold', 12))# range fbg
rangefbg.place(x=430, y=130);

lblid = Label(f2, text='Masukkan IC :', font=('bold', 12))# IC
lblid.place(x=20, y=10);

lblnama = Label(f2, text='Masukkan Nama :', font=('bold', 12))# Nama
lblnama.place(x=20, y=40);

lblumur = Label(f2, text='Masukkan Umur :', font=('bold', 12))# Umur
lblumur.place(x=20, y=70);

lblrbg = Label(f2, text='Bacaan gula biasa :', font=('bold', 12))# Random blood glucose
lblrbg.place(x=20, y=100);

lblfbg = Label(f2, text='Bacaan gula puasa :', font=('bold', 12))# Fasting blood glucose
lblfbg.place(x=20, y=130);

lblswl = Label(f2, text='Berat badan turun :',font=('bold', 12))# Weigth loss
lblswl.place(x=20, y=160);

lblpoly = Label(f2, text='Kerap rasa lapar :',font=('bold', 12))# Polyphagia
lblpoly.place(x=20, y=190);

lbldiz = Label(f2, text='Kerap pening kepala :',font=('bold', 12))# Dizziness
lbldiz.place(x=20, y=220);

lblfat = Label(f2, text='Kerap berasa letih :',font=('bold', 12))# Fatigue
lblfat.place(x=20, y=250);

lblblu = Label(f2, text='Penglihatan kabur :',font=('bold', 12))# Blurry vision
lblblu.place(x=20, y=280);

#============================================== GRAPH FRAME ========================================================
lblgp = LabelFrame(f2, text = "Graph")  
lblgp.place(x = 540,y = 5, height = 840, width = 620)

#============================================== OUTPUT FRAME =======================================================
lblfm = LabelFrame(f2, text="Output")  
lblfm.place(x=8,y=390,height=390,width=450)

#============================================== OUTPUT LABEL & ENTRY ===============================================
lblIC = Label(f2, text='Nombor IC Pesakit  : ',font=('bold', 12))# Output IC
lblIC.place (x=20, y=420);

eeid = Entry(f2)
eeid.config(state="readonly")
eeid.place (x=190, y=420, width = 250, height = 25);

lblnama = Label(f2, text='Nama Pesakit : ',font=('bold', 12))# Output Nama
lblnama.place (x=20, y=450);

eenama = Entry(f2)
eenama.config(state="readonly")
eenama.place (x=190, y=450, width = 250, height = 25);

lblumur = Label(f2, text='Umur Pesakit : ',font=('bold', 12))# Output Umur
lblumur.place (x=20, y=480);

eeumur = Entry(f2)
eeumur.config(state="readonly")
eeumur.place (x=190, y=480, width = 250, height = 25);

lblRBG = Label(f2, text='Bacaan Gula Biasa : ',font=('bold', 12))# Output RBG
lblRBG.place (x=20, y=510);

eerbg = Entry(f2)
eerbg.config(state="readonly")
eerbg.place (x=190, y=510, width = 250, height = 25);

lblFBG = Label(f2, text='Bacaan Gula Puasa : ',font=('bold', 12))# Output FBG
lblFBG.place (x=20, y=540);

eefbg = Entry(f2)
eefbg.config(state="readonly")
eefbg.place (x=190, y=540, width = 250, height = 25);

lblWL = Label(f2, text='Berat Badan Turun : ',font=('bold', 12))# Output Weight loss
lblWL.place (x=20, y=570);

etwl = Entry(f2)
etwl.config(state="readonly")
etwl.place (x=190, y=570, width = 250, height = 25);

lblOH = Label(f2, text='Kerap Rasa Lapar : ',font=('bold', 12))# Output Polyphagia
lblOH.place (x=20, y=600);

etoh = Entry(f2)
etoh.config(state="readonly")
etoh.place (x=190, y=600, width = 250, height = 25);

lblDZ = Label(f2, text='Kerap Pening Kepala : ',font=('bold', 12))# Output Dizziness
lblDZ.place (x=20, y=630);

etdz = Entry(f2)
etdz.config(state="readonly")
etdz.place (x=190, y=630, width = 250, height = 25);

lblTR = Label(f2, text='Kerap Berasa Letih : ',font=('bold', 12))# Output Fatigue
lblTR.place (x=20, y=660);

ettr = Entry(f2)
ettr.config(state="readonly")
ettr.place (x=190, y=660, width = 250, height = 25);

lblBV = Label(f2, text='Penglihatan Kabur : ',font=('bold', 12))# Output Blurry vision
lblBV.place (x=20, y=690);

etbv = Entry(f2)
etbv.config(state="readonly")
etbv.place (x=190, y=690, width = 250, height = 25);

lbldia = Label(f2, text='Anda Di Tahap : ',font=('bold', 12))# Output Result
lbldia.place (x=20, y=720);

eres = Entry(f2)
eres.config(state="readonly")
eres.place(x=190, y=720, width = 250, height = 25);

#============================================== RADIO BUTTON =======================================================
wl_chk = StringVar()
wl_chk.set('No') # Set radiobutton to No
rdwl = Radiobutton(f2, text="No", variable = wl_chk, value="No")# Weight Loss
rdwl.place(x=190, y=160)

rdwl1 = Radiobutton(f2, text="Yes", variable = wl_chk, value="Yes")
rdwl1.place(x=250, y=160)

oh_chk = StringVar()
oh_chk.set('No') #Set radiobutton to No
rdoh = Radiobutton(f2, text="No", variable = oh_chk, value="No")# Polyphagia
rdoh.place(x=190, y=190)

rdoh1 = Radiobutton(f2, text="Yes", variable = oh_chk, value="Yes")
rdoh1.place(x=250, y=190)

dz_chk = StringVar()
dz_chk.set('No') #Set radiobutton to No
rddz = Radiobutton(f2, text="No", variable = dz_chk, value="No")# Dizziness
rddz.place(x=190, y=220)

rddz1 = Radiobutton(f2, text="Yes", variable = dz_chk, value="Yes")
rddz1.place(x=250, y=220)

tr_chk = StringVar()
tr_chk.set('No') #Set radiobutton to No
rdtr = Radiobutton(f2, text="No", variable = tr_chk, value="No")# Fatigue
rdtr.place(x=190, y=250)

rdtr1 = Radiobutton(f2, text="Yes", variable = tr_chk, value="Yes")
rdtr1.place(x=250, y=250)

bv_chk = StringVar()
bv_chk.set('No') #Set radiobutton to No
rdbv = Radiobutton(f2, text="No", variable = bv_chk, value="No")# Blurry Vision
rdbv.place(x=190, y=280)

rdbv1 = Radiobutton(f2, text="Yes", variable = bv_chk, value="Yes")
rdbv1.place(x=250, y=280)

#============================================== BUTTON =============================================================

resetbtn = Button(f2, text='Reset', font=("bold", 12), bg="white",command=lambda:reset())# Back to menu
resetbtn.place(x=170, y=340)

submit = Button(f2, text='Submit', font=("bold", 12), bg="white", command=lambda:[fuzzy(), insert()])
submit.place(x=230, y=340)

pesakit = Button(f2, text='Senarai Pesakit', font=("bold", 12), bg="white",command=lambda:show_frame(f3))
pesakit.place(x=300, y=340)

#============================================== FRAME 3 ============================================================
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#============================================== MAKLUMAT PESAKIT ===================================================

group2 = LabelFrame(f3, text="MAKLUMAT PESAKIT", font=('bold', 15), padx=5, pady=5)# Frame for entry
group2.place(x=18,y=10,height=230,width=1140)

lblidf3 = Label(f3, text='ID : ',font=('bold', 12))# Label IC
lblidf3.place(x=40, y=50);

f3id = Entry(f3)# IC
f3id.config(state="readonly")
f3id.place(x=130, y=50, width = 250, height = 25)

lblnamaf3 = Label(f3, text='Nama : ',font=('bold', 12))# Label nama
lblnamaf3.place(x=40, y=80);

f3nama = Entry(f3)# nama
f3nama.config(state="readonly")
f3nama.place(x=130, y=80, width = 250, height = 25)

lblumurf3 = Label(f3, text='Umur : ',font=('bold', 12))# Label umur
lblumurf3.place(x=40, y=110);

f3umur = Entry(f3)# Umur
f3umur.config(state="readonly")
f3umur.place(x=130, y=110, width = 250, height = 25)

lblrbgf3 = Label(f3, text='Gula Biasa : ',font=('bold', 12))# Label RBG
lblrbgf3.place(x=40, y=140);

f3rbg = Entry(f3)# RBG
f3rbg.config(state="readonly")
f3rbg.place(x=130, y=140, width = 250, height = 25)

lblfbgf3 = Label(f3, text='Gula Puasa : ',font=('bold', 12))# Label FBG
lblfbgf3.place(x=400, y=50);

f3fbg = Entry(f3)# FBG
f3fbg.config(state="readonly")
f3fbg.place(x=520, y=50, width = 250, height = 25)

lbl2wlf3 = Label(f3, text='Berat Turun : ',font=('bold', 12))# Label WL
lbl2wlf3.place(x=400, y=80);

f3wl = Entry(f3)# WL
f3wl.config(state="readonly")
f3wl.place(x=520, y=80, width = 250, height = 25)

lblohf3 = Label(f3, text='Kerap Lapar : ',font=('bold', 12))# Label OH
lblohf3.place(x=400, y=110);

f3oh = Entry(f3)# OH
f3oh.config(state="readonly")
f3oh.place(x=520, y=110, width = 250, height = 25)

lbldzf3 = Label(f3, text='Pening Kepala : ',font=('bold', 12))# Label DZ
lbldzf3.place(x=400, y=110);

f3dz = Entry(f3)# DZ
f3dz.config(state="readonly")
f3dz.place(x=520, y=110, width = 250, height = 25)

lbltrf3 = Label(f3, text='Kerap Letih : ',font=('bold', 12))# Label TR
lbltrf3.place(x=780, y=50);

f3tr = Entry(f3)# TR
f3tr.config(state="readonly")
f3tr.place(x=880, y=50, width = 250, height = 25)

lblbvf3 = Label(f3, text='Rabun : ',font=('bold', 12))# Label BV
lblbvf3.place(x=780, y=80);

f3bv = Entry(f3)# BV
f3bv.config(state="readonly")
f3bv.place(x=880, y=80, width = 250, height = 25)

lblresf3 = Label(f3, text='Result : ',font=('bold', 12))# Label RESULT
lblresf3.place(x=780, y=110);

f3res = Entry(f3)# RESULT
f3res.config(state="readonly")
f3res.place(x=880, y=110, width = 250, height = 25)

deletebtn = Button(f3, text='Padam', font=("bold", 12), bg="white",command=lambda:delete())# Delete data pesakit
deletebtn.place(x=200, y=180)

resetf3btn = Button(f3, text='Reset', font=("bold", 12), bg="white",command=lambda:resetf3())# Reset entry
resetf3btn.place(x=130, y=180)

backmain = Button(f3, text='Laman Utama', font=("bold", 12), bg="white",command=lambda:show_frame(f2))# Back to menu
backmain.place(x=280, y=180)

#============================================== SENARAI PESAKIT ====================================================

group3 = LabelFrame(f3, text="SENARAI PESAKIT", font=('bold', 15), padx=5, pady=5)# Frame for Treeview
group3.place(x=18,y=300)
group3.rowconfigure(0, weight=1)
group3.columnconfigure(0, weight=1)

listBox = ttk.Treeview(group3, height=22, columns=("pesakitID","nama","umur","rbg","fbg","wl","oh","dz","tr","bv","result"),selectmode='browse')# Treeview
listBox.heading("pesakitID", text="ID Pesakit")
listBox.heading("nama", text="Nama Pesakit")
listBox.heading("umur", text="Umur Pesakit")
listBox.heading("rbg", text="Gula Biasa")
listBox.heading("fbg", text="Gula Puasa")
listBox.heading("wl", text="Berat Turun")
listBox.heading("oh", text="Kerap Lapar")
listBox.heading("dz", text="Pening")
listBox.heading("tr", text="Kerap Letih")
listBox.heading("bv", text="Kabur")
listBox.heading("result", text="Status")

listBox['show']='headings'

listBox.column("pesakitID", width=100, anchor='c')
listBox.column("nama", width=200, anchor='c')
listBox.column("umur", width=90, anchor='c')
listBox.column("rbg", width=90, anchor='c')
listBox.column("fbg", width=90, anchor='c')
listBox.column("wl", width=90, anchor='c')
listBox.column("oh", width=90, anchor='c')
listBox.column("dz", width=90, anchor='c')
listBox.column("tr", width=90, anchor='c')
listBox.column("bv", width=90, anchor='c')
listBox.column("result", width=90, anchor='c')
listBox.grid(row=0, column=0,   sticky=E+W+N+S)

vsb = ttk.Scrollbar(group3, orient="vertical", command=listBox.yview)# Scrollbar
vsb.grid(row=0, column=1,   sticky=E+W+N+S)

listBox.configure(yscrollcommand=vsb.set)

#============================================== FUNCTION ===========================================================
def show_frame(frame):
    frame.tkraise()

def exitProgram(root):
    exit()

def callback(input):# Validata entry as int only
	
	if input.isdigit():
		print(input)
		return True
						
	elif input is "":
		print(input)
		return True
        
	else:
		print(input)
		return False

reg = root.register(callback)
eid.config(validate ="key", validatecommand =(reg, '%P'))
eumur.config(validate ="key", validatecommand =(reg, '%P'))
erbg.config(validate ="key", validatecommand =(reg, '%P'))
efbg.config(validate ="key", validatecommand =(reg, '%P'))

def callbackString(input):# Validata entry as string only
	
	if input.isalpha():#isalpha
		print(input)
		return True
						
	elif input is "":
		print(input)
		return True

	else:
		print(input)
		return False

regstr = root.register(callbackString)
enama.config(validate ="key", validatecommand =(regstr, '%P'))

def fuzzy():

    #For symptom radio button
    nilaiwl = wl_chk.get();
    nilaioh = oh_chk.get();
    nilaidz = dz_chk.get();
    nilaitr = tr_chk.get();
    nilaibv = bv_chk.get();
    
    if nilaiwl == "No":
        wl = 0
    else:
        wl = 2
        
    if nilaioh == "No":
        oh = 0
    else:
        oh = 2

    if nilaidz == "No":
        dz = 0
    else:
        dz = 2

    if nilaitr == "No":
        tr = 0
    else:
        tr = 2

    if nilaibv == "No":
        bv = 0
    else:
        bv = 2
    
    # Generate universe variables
    x_rbg = np.arange(0, 20, 0.5)
    x_fbg = np.arange(0, 14, 0.5)
    x_wl = np.arange(0, 2.1, 0.5)
    x_oh = np.arange(0, 2.1, 0.5)
    x_dz = np.arange(0, 2.1, 0.5)
    x_tr = np.arange(0, 2.1, 0.5)
    x_bv = np.arange(0, 2.1, 0.5)
    x_res  = np.arange(0, 3.1, 0.5)
    
    # Generate fuzzy triangular membership functions
    rbg_lo = fuzz.trimf(x_rbg, [0, 4, 8]) # random blood glucose
    rbg_md = fuzz.trimf(x_rbg, [7.8, 9.4, 11])
    rbg_hi = fuzz.trimf(x_rbg, [10.8, 14.9, 19])
    fbg_lo = fuzz.trimf(x_fbg, [0, 3.1, 6.2]) # fasting blood glucose
    fbg_md = fuzz.trimf(x_fbg, [6, 6.5, 7])
    fbg_hi = fuzz.trimf(x_fbg, [6.8, 9.9, 13])
    wl_no = fuzz.trimf(x_wl, [0, 0.6, 1.2]) # weight loss
    wl_yes = fuzz.trimf(x_wl, [0.8, 1.4, 2])
    oh_no = fuzz.trimf(x_oh, [0, 0.6, 1.2]) # often hunger
    oh_yes = fuzz.trimf(x_oh, [0.8, 1.4, 2])
    dz_no = fuzz.trimf(x_dz, [0, 0.6, 1.2]) # often dizzy
    dz_yes = fuzz.trimf(x_dz, [0.8, 1.4, 2])
    tr_no = fuzz.trimf(x_tr, [0, 0.6, 1.2]) # often tired
    tr_yes = fuzz.trimf(x_tr, [0.8, 1.4, 2])
    bv_no = fuzz.trimf(x_bv, [0, 0.6, 1.2]) # blurry vision
    bv_yes = fuzz.trimf(x_bv, [0.8, 1.4, 2])
    res_lo = fuzz.trimf(x_res, [0, 0.6, 1.2]) # Result
    res_md = fuzz.trimf(x_res, [1, 1.5, 2])
    res_hi = fuzz.trimf(x_res, [1.8, 2.4, 3])
    
    # We need the activation of our fuzzy membership functions based on user input.
    # User input random blood glucose
    rbglo = fuzz.interp_membership(x_rbg, rbg_lo, erbg.get())
    rbgmd = fuzz.interp_membership(x_rbg, rbg_md, erbg.get())
    rbghi = fuzz.interp_membership(x_rbg, rbg_hi, erbg.get())

    # User input fasting blood glucose
    fbglo = fuzz.interp_membership(x_fbg, fbg_lo, efbg.get())
    fbgmd = fuzz.interp_membership(x_fbg, fbg_md, efbg.get())
    fbghi = fuzz.interp_membership(x_fbg, fbg_hi, efbg.get())
    
    # User input weight loss
    wlno = fuzz.interp_membership(x_wl, wl_no, wl)
    wlyes = fuzz.interp_membership(x_wl, wl_yes, wl)

    # User input often hunger
    ohno = fuzz.interp_membership(x_oh, oh_no, oh)
    ohyes = fuzz.interp_membership(x_oh, oh_yes, oh)

    # User input often dizzy
    dzno = fuzz.interp_membership(x_dz, dz_no, dz)
    dzyes = fuzz.interp_membership(x_dz, dz_yes, dz)

    # User input often tired
    trno = fuzz.interp_membership(x_tr, tr_no, tr)
    tryes = fuzz.interp_membership(x_tr, tr_yes, tr)

    # User input blurry vision
    bvno = fuzz.interp_membership(x_bv, bv_no, bv)
    bvyes = fuzz.interp_membership(x_bv, bv_yes, bv)
    
    # Rules /IF part
    # Now we take our rules and apply them.
    # The OR operator, take the maximum of any value.
    r1 = np.fmax(wlno, np.fmax(ohno, np.fmax(dzno, np.fmax(trno, np.fmax(bvno, np.fmax(rbglo, fbglo))))))
    r2 = np.fmax(wlno, np.fmax(ohno, np.fmax(dzno, np.fmax(trno, np.fmax(bvno, np.fmax(rbgmd, fbglo))))))
    r3 = np.fmax(wlno, np.fmax(ohno, np.fmax(dzno, np.fmax(trno, np.fmax(bvno, np.fmax(rbgmd, fbgmd))))))
    r4 = np.fmax(wlno, np.fmax(ohno, np.fmax(dzno, np.fmax(trno, np.fmax(bvno, np.fmax(rbghi, fbgmd))))))
    r5 = np.fmax(wlno, np.fmax(ohno, np.fmax(dzno, np.fmax(trno, np.fmax(bvno, np.fmax(rbghi, fbghi))))))
    r6 = np.fmax(wlyes, np.fmax(ohyes, np.fmax(dzyes, np.fmax(tryes, np.fmax(bvyes, np.fmax(rbglo, fbglo))))))
    r7 = np.fmax(wlyes, np.fmax(ohyes, np.fmax(dzyes, np.fmax(tryes, np.fmax(bvyes, np.fmax(rbgmd, fbglo))))))
    r8 = np.fmax(wlyes, np.fmax(ohyes, np.fmax(dzyes, np.fmax(tryes, np.fmax(bvyes, np.fmax(rbgmd, fbgmd))))))
    r9 = np.fmax(wlyes, np.fmax(ohyes, np.fmax(dzyes, np.fmax(tryes, np.fmax(bvyes, np.fmax(rbghi, fbgmd))))))
    r10 = np.fmax(wlyes, np.fmax(ohyes, np.fmax(dzyes, np.fmax(tryes, np.fmax(bvyes, np.fmax(rbghi, fbghi))))))
    
    # Untuk potong bahagian atas output dari rules /THEN part
    # Now we apply this by clipping the top off the corresponding output
    reslo = np.fmin(r7, np.fmin(r6, np.fmin(r2, np.fmin(r1, res_lo))))
    resmd = np.fmin(r9, np.fmin(r8, np.fmin(r4, np.fmin(r3, res_md))))
    reshi = np.fmin(r10, np.fmin(r5, res_hi))
    res0 = np.zeros_like(x_res)
    
    # Aggregate(combine) all three output membership functions together / Aggregate all output - max
    aggregated = np.fmax(reslo, np.fmax(resmd, reshi))

    # Calculate defuzzified result / Defuzzify using centroid
    res = fuzz.defuzz(x_res, aggregated, 'centroid')
    res_activation = fuzz.interp_membership(x_res, aggregated, res)  # for plot

    if res < 1:
        status="Selamat"
    elif 1 < res < 2:
        status="Pre-Diabetes"
    elif res > 2:
        status="Diabetes"
    
    # the figure that will contain the plot
    # Graph RBG
    fig = Figure(figsize=(6, 2.5), dpi=100)
    ax0 = fig.add_subplot(1,1,1)
    ax0.plot(x_rbg, rbg_lo, 'g', linewidth=1.5, linestyle='--', label='Low')
    ax0.plot(x_rbg, rbg_md, 'y', linewidth=1.5, linestyle='--', label='Medium')
    ax0.plot(x_rbg, rbg_hi, 'r', linewidth=1.5, linestyle='--', label='High')
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.get_tk_widget().place(x=550, y=30);
    ax0.set_title('Random Blood Glucose')
    ax0.legend()

    # Graph FBG
    fig = Figure(figsize=(6, 2.5), dpi=100)
    ax1 = fig.add_subplot(1,1,1)
    ax1.plot(x_fbg, fbg_lo, 'g', linewidth=1.5, label='Low')
    ax1.plot(x_fbg, fbg_md, 'y', linewidth=1.5, label='Medium')
    ax1.plot(x_fbg, fbg_hi, 'r', linewidth=1.5, label='High')
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.draw()
    canvas.get_tk_widget().place(x=550, y=300);
    ax1.set_title('Fasting Blood Glucose')
    ax1.legend()

    # Graph Aggregated
    fig = Figure(figsize=(6, 2.5), dpi=100)
    ax2 = fig.add_subplot(1,1,1)
    ax2.fill_between(x_res, res0, reslo, facecolor='g', alpha=0.7)
    ax2.plot(x_res, res_lo, 'g', linewidth=0.5, linestyle='--', label='Selamat')
    ax2.fill_between(x_res, res0, resmd, facecolor='orange', alpha=0.7)
    ax2.plot(x_res, res_md, 'orange', linewidth=0.5, linestyle='--', label='Pre-Diabetes')
    ax2.fill_between(x_res, res0, reshi, facecolor='r', alpha=0.7)
    ax2.plot(x_res, res_hi, 'r', linewidth=0.5, linestyle='--', label='Diabetes')
    ax2.plot([res, res], [0, res_activation], 'k', linewidth=1.5, alpha=0.9)
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.get_tk_widget().place(x=550, y=570);
    ax2.set_title('Aggregated membership and diabetes result (line)')
    ax2.legend()

    eeid.config(state="normal")# Output IC
    eeid.delete(0,"end")
    eeid.insert(0, eid.get())
    eeid.config(state="readonly")
    eenama.config(state="normal")# Output Nama
    eenama.delete(0,"end")
    eenama.insert(0, enama.get())
    eenama.config(state="readonly")
    eeumur.config(state="normal")# Output Umur
    eeumur.delete(0,"end")
    eeumur.insert(0, eumur.get())
    eeumur.config(state="readonly")
    eerbg.config(state="normal")# Output RBG
    eerbg.delete(0,"end")
    eerbg.insert(0, erbg.get())
    eerbg.config(state="readonly")
    eefbg.config(state="normal")# Output FBG
    eefbg.delete(0,"end")
    eefbg.insert(0, efbg.get())
    eefbg.config(state="readonly")
    etwl.config(state="normal")# Output WL
    etwl.delete(0,"end")
    etwl.insert(0, wl_chk.get())
    etwl.config(state="readonly")
    etoh.config(state="normal")# Output OH
    etoh.delete(0,"end")
    etoh.insert(0, oh_chk.get())
    etoh.config(state="readonly")
    etdz.config(state="normal")# Output DZ
    etdz.delete(0,"end")
    etdz.insert(0, dz_chk.get())
    etdz.config(state="readonly")
    ettr.config(state="normal")# Output TR
    ettr.delete(0,"end")
    ettr.insert(0, tr_chk.get())
    ettr.config(state="readonly")
    etbv.config(state="normal")# Output BV
    etbv.delete(0,"end")
    etbv.insert(0, bv_chk.get())
    etbv.config(state="readonly")
    eres.config(state="normal")# Output Result
    eres.delete(0,"end")
    eres.insert(0, status)
    eres.config(state="readonly")

def insert():
    
    simptomID = ''
    resultID = ''
    pesakitID = eid.get()
    nama = enama.get()
    umur = eumur.get()
    rbg = erbg.get()
    fbg = efbg.get()
    wl = wl_chk.get()
    oh = oh_chk.get()
    dz = dz_chk.get()
    tr = tr_chk.get()
    bv = bv_chk.get()
    result = eres.get()

    if(id=="" or nama=="" or umur=="" or rbg=="" or fbg==""):
        MessageBox.showinfo("Insert status", "Isi tempat kosong")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="diabetes")
        cursor = con.cursor()
        cursor.execute("BEGIN")
        cursor.execute("INSERT INTO pesakit VALUES('"+ pesakitID +"','"+ nama +"','"+ umur +"')")
        cursor.execute("INSERT INTO simptom VALUES('"+ simptomID +"','"+ pesakitID +"','"+ rbg +"','"+ fbg +"','"+ wl +"','"+ oh +"','"+ dz +"','"+ tr +"','"+ bv +"')")
        cursor.execute("INSERT INTO result VALUES('"+ resultID +"','"+ pesakitID +"','"+ result +"')")
        cursor.execute("COMMIT")
        
        eid.delete(0, 'end')
        enama.delete(0, 'end')
        eumur.delete(0, 'end')
        erbg.delete(0, 'end')
        efbg.delete(0, 'end')
        MessageBox.showinfo("Insert status", "Data berjaya dimasukkan")
        con.close();
        fetch()

def fetch():
    con = mysql.connect(host="localhost", user="root", password="", database="diabetes")
    cursor = con.cursor()
    cursor.execute("SELECT p.pesakitID, p.nama, p.umur, s.rbg, s.fbg, s.wl, s.oh, s.dz, s.tr, s.bv, r.result FROM pesakit p, simptom s, result r WHERE p.pesakitID = s.pesakitID AND p.pesakitID = r.pesakitID")
    records = cursor.fetchall()
    
    if len(records)!=0:
        listBox.delete(*listBox.get_children())
        for row in records:
            listBox.insert('',END,values=row)
        con.commit
    con.close()

def delete():
    
    pesakitID = f3id.get()

    con = mysql.connect(host="localhost", user="root", password="", database="diabetes")
    cursor = con.cursor()
    msgbox = messagebox.askyesno("Confirmation", "Anda pasti untuk padam maklumat pesakit ini?")
    if msgbox==True:
        cursor.execute("BEGIN")
        cursor.execute("DELETE FROM pesakit WHERE pesakitID = '"+ f3id.get() +"'")
        cursor.execute("DELETE FROM simptom WHERE pesakitID = '"+ f3id.get() +"'")
        cursor.execute("DELETE FROM result WHERE pesakitID = '"+ f3id.get() +"'")
        cursor.execute("COMMIT")
        fetch()
        con.close()
        resetf3()
        MessageBox.showinfo("Status Padam", "Data berjaya dipadamkan")
    else:
        con.close()

def reset():

    eid.delete(0,"end")
    enama.delete(0,"end")
    eumur.delete(0,"end")
    erbg.delete(0,"end")
    efbg.delete(0,"end")
    wl_chk.set('No')
    oh_chk.set('No')
    dz_chk.set('No')
    tr_chk.set('No')
    bv_chk.set('No')

def resetf3():

    f3id.config(state="normal")
    f3id.delete(0,"end")
    f3id.config(state="readonly")
    
    f3nama.config(state="normal")
    f3nama.delete(0,"end")
    f3nama.config(state="readonly")
    
    f3umur.config(state="normal")
    f3umur.delete(0,"end")
    f3umur.config(state="readonly")
    
    f3rbg.config(state="normal")
    f3rbg.delete(0,"end")
    f3rbg.config(state="readonly")

    f3fbg.config(state="normal")
    f3fbg.delete(0,"end")
    f3fbg.config(state="readonly")

    f3wl.config(state="normal")
    f3wl.delete(0,"end")
    f3wl.config(state="readonly")

    f3oh.config(state="normal")
    f3oh.delete(0,"end")
    f3oh.config(state="readonly")

    f3dz.config(state="normal")
    f3dz.delete(0,"end")
    f3dz.config(state="readonly")

    f3tr.config(state="normal")
    f3tr.delete(0,"end")
    f3tr.config(state="readonly")

    f3bv.config(state="normal")
    f3bv.delete(0,"end")
    f3bv.config(state="readonly")

    f3res.config(state="normal")
    f3res.delete(0,"end")
    f3res.config(state="readonly")

def infoPesakit(event):
    
    viewInfo = listBox.focus()
    learnerData = listBox.item(viewInfo)
    row = learnerData ['values']

    f3id.config(state="normal")# Output IC
    f3id.delete(0,"end")
    f3id.insert(0,row[0])
    f3id.config(state="readonly")

    f3nama.config(state="normal")# Output IC
    f3nama.delete(0,"end")
    f3nama.insert(0,row[1])
    f3nama.config(state="readonly")

    f3umur.config(state="normal")# Output IC
    f3umur.delete(0,"end")
    f3umur.insert(0,row[2])
    f3umur.config(state="readonly")

    f3rbg.config(state="normal")# Output IC
    f3rbg.delete(0,"end")
    f3rbg.insert(0,row[3])
    f3rbg.config(state="readonly")

    f3fbg.config(state="normal")# Output IC
    f3fbg.delete(0,"end")
    f3fbg.insert(0,row[4])
    f3fbg.config(state="readonly")

    f3wl.config(state="normal")# Output IC
    f3wl.delete(0,"end")
    f3wl.insert(0,row[5])
    f3wl.config(state="readonly")

    f3oh.config(state="normal")# Output IC
    f3oh.delete(0,"end")
    f3oh.insert(0,row[6])
    f3oh.config(state="readonly")

    f3dz.config(state="normal")# Output IC
    f3dz.delete(0,"end")
    f3dz.insert(0,row[7])
    f3dz.config(state="readonly")

    f3tr.config(state="normal")# Output IC
    f3tr.delete(0,"end")
    f3tr.insert(0,row[8])
    f3tr.config(state="readonly")

    f3bv.config(state="normal")# Output IC
    f3bv.delete(0,"end")
    f3bv.insert(0,row[9])
    f3bv.config(state="readonly")

    f3res.config(state="normal")# Output IC
    f3res.delete(0,"end")
    f3res.insert(0,row[10])
    f3res.config(state="readonly")

listBox.bind("<ButtonRelease-1>", infoPesakit)

fetch()
show_frame(f1)
root.mainloop

