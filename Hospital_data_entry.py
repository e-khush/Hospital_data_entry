from tkinter import *

import mysql.connector;

con=mysql.connector.connect(host='localhost',database='MinPro',user='root',password='khushi12@')

if con.is_connected():
    print('Database connected!')
cur=con.cursor()

s1=1
s2=1
s3=2017
r=''
d=''
g=''

def Search():
        r3=Tk()
        r3.title('Search Data')
        w3=Frame(r3,height=500,width=800,bg='pink')
        l1=Label(r3,text='Patient ID',width=12,height=2,font=('Times New Roman',-20),bg='pink')
        E1=Entry(w3,width=30)
        l2=Label(r3,text='Doctor ID',width=12,height=2,font=('Times New Roman',-20),bg='pink')
        E2=Entry(w3,width=30)
        l1.place(x=100,y=100)
        E1.place(x=250,y=115)
        l2.place(x=100,y=150)
        E2.place(x=250,y=165)
        r3.resizable(False,False)
        w3.pack()
        r3.mainloop()
        cur.execute('Select * from regpat_checks where patient_id=\':pid\'',{'pid':E1.get()})
        print(cur.fetchall())
        cur.execute('Select * from admpat_checks where patient_id=\':pid\'',{'pid':E1.get()})
        print(cur.fetchall())
        cur.execute('Select * from doc_reg where doctor_id=\':did\'',{'did':E2.get()})
        print(cur.fetchall())
        
def insp():

    def dbinsp():
        D1=str(s3)+'-'+str(s2)+'-'+str(s1)
        D2=str(Sp3)+'-'+str(Sp2)+'-'+str(S1)
        if r=='Regular':
            cur.execute('Insert into regpat_checks values(:id,:dia,:st,:trt,:nm,:s,:add,:pno,:med,:vd,:pm)',{'id':e2.get(),'dia':e4.get(),'st':e5.get(),'trt':e7.get(),'nm':e3.get(),'s':g,'add':e8.get(),'pno':e6.get(),'med':e9.get(),'vd':D1,'pm':e10.get()})
            con.commit()
        elif r=='Admitted':
            cur.execute('Insert into admpat_checks values(:id,:dia,:st,:trt,:nm,:s,:add,:pno,:bno,:pm,:adate,:rno)',{'id':e2.get(),'dia':e4.get(),'st':e5.get(),'trt':e7.get(),'nm':e3.get(),'s':g,'add':e8.get(),'pno':e6.get(),'bno':E1.get(),'pm':e10.get(),'adate':D2,'rno':E2.get()})
            con.commit()
    
    def adm():
        r3=Tk()
        r3.title('Admitted Patient Data')
        w3=Frame(r3,height=400,width=600,bg='pink')
        l1=Label(r3,text='Room No',width=12,height=2,font=('Times New Roman',-20),bg='pink')
        E1=Entry(w3,width=30)
        l2=Label(r3,text='Bed No',width=12,height=2,font=('Times New Roman',-20),bg='pink')
        E2=Entry(w3,width=30)
        l1.place(x=100,y=100)
        E1.place(x=250,y=115)
        l2.place(x=100,y=200)
        E2.place(x=250,y=215)
        l3=Label(r1,text='Visit Date',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
        Sp1=Spinbox(w1,from_=1,to=31,command=getval1)
        Sp2=Spinbox(w1,from_=1,to=12,command=getval2)
        Sp3=Spinbox(w1,from_=2017,to=2022,command=getval3)
        l3.place(x=100,y=200)
        Sp1.place(x=250,y=200)
        Sp2.place(x=250,y=230)
        Sp3.place(x=250,y=260)
        w3.pack()
        r3.mainloop()
    
    def submit():
        dbinsp()
        root2=Tk()
        root2.title('Success')
        w1=Frame(root2,height=150,width=300,bg='snow')
        m=Message(root2,text='Insertion Successful',width=100,font=('Times New Roman',-15),bg='snow',fg='black')
        m.place(x=100,y=50)
        w1.pack()
        root2.resizable(False,False)
        display()
        mainloop()
        
    def clear():
        x=int(S1.get())
        while x>1:
            S1.invoke("buttondown")
            x=x-1
        y=int(S2.get())
        while y>1:
            S2.invoke("buttondown")
            y=y-1
        z=int(S3.get())
        while z>1:
            S3.invoke("buttondown")
            z=z-1
        R1.deselect()
        R2.deselect()
        R3.deselect()
        R4.deselect()
        R5.deselect()
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        
    def getval1():
        global s1
        s1=S1.get()
        
    def getval2():
        global s2
        s2=S2.get()

    def getval3():
        global s2
        s3=S3.get()

    def getval4():
        global r
        R1=v1.get()
        if R1==1:
            r='Regular'
        elif R1==2:
            r='Admitted'
            adm()
        else:
            pass

    def getval5():
        global g
        R2=v2.get()
        if R2==1:
            g='M'
        elif R2==2:
            g='F'
        elif R2==3:
            g='O'
        else:
            pass

    r1=Tk()
    r1.title('Patient\'s Data')
    v1=IntVar(r1)
    v2=IntVar(r1)
    w1=Frame(r1,height=768,width=1600,bg='mintcream')
    l1=Message(r1,text='Insert patient\'s data',width=500,font=('Tahoma',-20),fg='Black',bg='mintcream')
    l1.place(x=570,y=20)
    l2=Label(r1,text='Patient ID',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e2=Entry(w1,width=30)
    l3=Label(r1,text='Name',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e3=Entry(w1,width=30)
    l4=Label(r1,text='Diagnosis',width=10,height=2,font=('Times New Roman',-20),bg='mintcream')
    e4=Entry(w1,width=30)
    l5=Label(r1,text='Status',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e5=Entry(w1,width=30)
    l6=Label(r1,text='Phone No.',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e6=Entry(w1,width=30)
    l7=Label(r1,text='Treatment',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e7=Entry(w1,width=30)
    l8=Label(r1,text='Address',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e8=Entry(w1,width=105)
    l9=Label(r1,text='Medicine',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e9=Entry(w1,width=30)
    l10=Label(r1,text='Payment Mode',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e10=Entry(w1,width=30)
    l11=Label(r1,text='Visit Date',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    S1=Spinbox(w1,from_=1,to=31,command=getval1)
    S2=Spinbox(w1,from_=1,to=12,command=getval2)
    S3=Spinbox(w1,from_=2017,to=2022,command=getval3)
    l12=Label(r1,text='Type',width=10,height=2,font=('Times New Roman',-20),bg='mintcream')
    R1=Radiobutton(r1,text="Regular",variable=v1,value=1,bg='mintcream',command=getval4)
    R2=Radiobutton(r1,text="Admitted",variable=v1,value=2,bg='mintcream',command=getval4)
    l13=Label(r1,text='Sex',width=10,height=2,font=('Times New Roman',-20),bg='mintcream')
    R3=Radiobutton(r1,text="M",variable=v2,value=1,bg='mintcream',command=getval5)
    R4=Radiobutton(r1,text="F",variable=v2,value=2,bg='mintcream',command=getval5)
    R5=Radiobutton(r1,text="O",variable=v2,value=3,bg='mintcream',command=getval5)
    b1=Button(w1,text="Submit",width=15,height=2,bg="green",command=submit)
    b2=Button(w1,text="Clear All",width=15,height=2,bg="yellow",command=clear)
    b3=Button(w1,text="Close",width=15,height=2,bg="red",command=quit)
    l2.place(x=240,y=80)
    e2.place(x=400,y=95)
    l3.place(x=645,y=80)
    e3.place(x=850,y=95)
    l4.place(x=250,y=150)
    e4.place(x=400,y=165)
    l5.place(x=645,y=150)
    e5.place(x=850,y=165)
    l6.place(x=240,y=220)
    e6.place(x=400,y=235)
    l7.place(x=660,y=220)
    e7.place(x=850,y=235)
    l8.place(x=230,y=290)
    e8.place(x=400,y=305)
    l9.place(x=235,y=360)
    e9.place(x=400,y=375)
    l10.place(x=680,y=360)
    e10.place(x=850,y=375)
    l11.place(x=235,y=430)
    S1.place(x=400,y=447)
    S2.place(x=550,y=447)
    S3.place(x=700,y=447)
    l12.place(x=228,y=500)
    R1.place(x=400,y=515)
    R2.place(x=400,y=535)
    l13.place(x=695,y=500)
    R3.place(x=800,y=515)
    R4.place(x=800,y=535)
    R5.place(x=800,y=555)
    b1.place(x=480,y=650)
    b2.place(x=600,y=650)
    b3.place(x=720,y=650)
    w1.pack()
    r1.mainloop()
    
def insd():

    def dbinsd():
        cur.execute('Insert into doc_reg Values(:id,:pno,:ex,:nm,:qf,:odd,:sal,:dnm)',{'id':e2.get(),'pno':e6.get(),'ex':e4.get(),'nm':e3.get(),'qf':e5.get(),'odd':d,'sal':e7.get(),'dnm':e8.get()})
        con.commit()
        cur.execute('Insert into department Values(:did,:dnm,:dhd)',{'did':e10.get(),'dnm':e8.get(),'dhd':e9.get()})
        con.commit()

    def submit():
        dbinsd()
        root2=Tk()
        root2.title('Success')
        w1=Frame(root2,height=150,width=300,bg='snow')
        m=Message(root2,text='Insertion Successful',width=100,font=('Times New Roman',-15),bg='snow',fg='black')
        m.place(x=100,y=50)
        w1.pack()
        root2.resizable(False,False)
        display()
        
    def clear():
        R1.deselect()
        R2.deselect()
        R3.deselect()
        R4.deselect()
        R5.deselect()
        R6.deselect()
        R7.deselect()
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)

    def getval1():
        global d
        R=v2.get()
        if R==1:
            d='Sunday'
        elif R==2:
            d='Monday'
        elif R==3:
            d='Tuesday'
        elif R==4:
            d='Wednesday'
        elif R==5:
            d='Thursday'
        elif R==6:
            d='Friday'
        elif R==7:
            d='Saturday'
        else:
            pass
        
    r1=Tk()
    r1.title('Doctor\'s Data')
    v2=IntVar(r1)
    w1=Frame(r1,height=768,width=1600,bg='mintcream')
    l1=Message(r1,text='Insert doctor\'s data',width=500,font=('Tahoma',-20),fg='Black',bg='mintcream')
    l1.place(x=570,y=20)
    l2=Label(r1,text='Doctor ID',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e2=Entry(w1,width=30)
    l3=Label(r1,text='Name',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e3=Entry(w1,width=30)
    l4=Label(r1,text='Experience',width=10,height=2,font=('Times New Roman',-20),bg='mintcream')
    e4=Entry(w1,width=30)
    l5=Label(r1,text='Qualification',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e5=Entry(w1,width=30)
    l6=Label(r1,text='Phone No.',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e6=Entry(w1,width=30)
    l7=Label(r1,text='Salary',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e7=Entry(w1,width=30)
    l8=Label(r1,text='Department',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e8=Entry(w1,width=30)
    l9=Label(r1,text='Department Head',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e9=Entry(w1,width=30)
    l10=Label(r1,text='Department Id',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e10=Entry(w1,width=30)
    l11=Label(r1,text='Off Duty Day',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    R1=Radiobutton(r1,text="Sunday",variable=v2,value=1,bg='mintcream',command=getval1)
    R2=Radiobutton(r1,text="Monday",variable=v2,value=2,bg='mintcream',command=getval1)
    R3=Radiobutton(r1,text="Tuesday",variable=v2,value=3,bg='mintcream',command=getval1)
    R4=Radiobutton(r1,text="Wednesday",variable=v2,value=4,bg='mintcream',command=getval1)
    R5=Radiobutton(r1,text="Thursday",variable=v2,value=5,bg='mintcream',command=getval1)
    R6=Radiobutton(r1,text="Friday",variable=v2,value=6,bg='mintcream',command=getval1)
    R7=Radiobutton(r1,text="Saturday",variable=v2,value=7,bg='mintcream',command=getval1)
    b1=Button(w1,text="Submit",width=15,height=2,bg="green",command=submit)
    b2=Button(w1,text="Clear All",width=15,height=2,bg="yellow",command=clear)
    b3=Button(w1,text="Close",width=15,height=2,bg="red",command=quit)
    l2.place(x=240,y=80)
    e2.place(x=400,y=95)
    l3.place(x=710,y=80)
    e3.place(x=850,y=95)
    l4.place(x=250,y=150)
    e4.place(x=400,y=165)
    l5.place(x=690,y=150)
    e5.place(x=850,y=165)
    l6.place(x=240,y=220)
    e6.place(x=400,y=235)
    l7.place(x=710,y=220)
    e7.place(x=850,y=235)
    l8.place(x=235,y=290)
    e8.place(x=400,y=305)
    l9.place(x=670,y=290)
    e9.place(x=850,y=305)
    l10.place(x=240,y=360)
    e10.place(x=400,y=375)
    l11.place(x=700,y=360)
    R1.place(x=850,y=375)
    R2.place(x=850,y=400)
    R3.place(x=850,y=425)
    R4.place(x=850,y=450)
    R5.place(x=850,y=475)
    R6.place(x=850,y=500)
    R7.place(x=850,y=525)
    b1.place(x=480,y=650)
    b2.place(x=600,y=650)
    b3.place(x=720,y=650)
    w1.pack()
    r1.mainloop()
    
def updd():

    def dbupdd():
        cur.execute('Update table doc_reg set phone_no=:pno,experience=:ex,name=:nm,qualification=:qf,off_duty_day=:odd,salary=:sal,dept_name=:dnm where doctor_id=:id',{'pno':e6.get(),'ex':e4.get(),'nm':e3.get(),'qf':e5.get(),'odd':d,'sal':e7.get(),'dnm':e8.get(),'id':e2.get()})
        con.commit()
        cur.execute('Update table department set dept_name=:dnm,dept_head=:dhd where dept_id=:did',{'dnm':e8.get(),'dhd':e9.get(),'did':e10.get()})
        con.commit()

    def submit():
        dbupdd()
        root2=Tk()
        root2.title('Success')
        w1=Frame(root2,height=150,width=300,bg='snow')
        m=Message(root2,text='Updation Successful',width=100,font=('Times New Roman',-15),bg='snow',fg='black')
        m.place(x=100,y=50)
        w1.pack()
        root2.resizable(False,False)
        display()
        mainloop()
        
    def clear():
        R1.deselect()
        R2.deselect()
        R3.deselect()
        R4.deselect()
        R5.deselect()
        R6.deselect()
        R7.deselect()
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)

    def getval1():
        global d
        R=v2.get()
        print(R)
        if R==1:
            d='Sunday'
        elif R==2:
            d='Monday'
        elif R==3:
            d='Tuesday'
        elif R==4:
            d='Wednesday'
        elif R==5:
            d='Thursday'
        elif R==6:
            d='Friday'
        elif R==7:
            d='Saturday'
        else:
            pass
        
    r1=Tk()
    r1.title('Doctor\'s Data')
    v2=IntVar(r1)
    w1=Frame(r1,height=768,width=1600,bg='mintcream')
    l1=Message(r1,text='Update doctor\'s data',width=500,font=('Tahoma',-20),fg='Black',bg='mintcream')
    l1.place(x=570,y=20)
    l2=Label(r1,text='Doctor ID',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e2=Entry(w1,width=30)
    l3=Label(r1,text='Name',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e3=Entry(w1,width=30)
    l4=Label(r1,text='Experience',width=10,height=2,font=('Times New Roman',-20),bg='mintcream')
    e4=Entry(w1,width=30)
    l5=Label(r1,text='Qualification',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e5=Entry(w1,width=30)
    l6=Label(r1,text='Phone No.',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e6=Entry(w1,width=30)
    l7=Label(r1,text='Salary',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e7=Entry(w1,width=30)
    l8=Label(r1,text='Department',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e8=Entry(w1,width=30)
    l9=Label(r1,text='Department Head',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e9=Entry(w1,width=30)
    l10=Label(r1,text='Department Id',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e10=Entry(w1,width=30)
    l11=Label(r1,text='Off Duty Day',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    R1=Radiobutton(r1,text="Sunday",variable=v2,value=1,bg='mintcream',command=getval1)
    R2=Radiobutton(r1,text="Monday",variable=v2,value=2,bg='mintcream',command=getval1)
    R3=Radiobutton(r1,text="Tuesday",variable=v2,value=3,bg='mintcream',command=getval1)
    R4=Radiobutton(r1,text="Wednesday",variable=v2,value=4,bg='mintcream',command=getval1)
    R5=Radiobutton(r1,text="Thursday",variable=v2,value=5,bg='mintcream',command=getval1)
    R6=Radiobutton(r1,text="Friday",variable=v2,value=6,bg='mintcream',command=getval1)
    R7=Radiobutton(r1,text="Saturday",variable=v2,value=7,bg='mintcream',command=getval1)
    b1=Button(w1,text="Submit",width=15,height=2,bg="green",command=submit)
    b2=Button(w1,text="Clear All",width=15,height=2,bg="yellow",command=clear)
    b3=Button(w1,text="Close",width=15,height=2,bg="red",command=quit)
    l2.place(x=240,y=80)
    e2.place(x=400,y=95)
    l3.place(x=710,y=80)
    e3.place(x=850,y=95)
    l4.place(x=250,y=150)
    e4.place(x=400,y=165)
    l5.place(x=690,y=150)
    e5.place(x=850,y=165)
    l6.place(x=240,y=220)
    e6.place(x=400,y=235)
    l7.place(x=710,y=220)
    e7.place(x=850,y=235)
    l8.place(x=235,y=290)
    e8.place(x=400,y=305)
    l9.place(x=670,y=290)
    e9.place(x=850,y=305)
    l10.place(x=250,y=360)
    e10.place(x=400,y=375)
    l11.place(x=700,y=360)
    R1.place(x=850,y=375)
    R2.place(x=850,y=400)
    R3.place(x=850,y=425)
    R4.place(x=850,y=450)
    R5.place(x=850,y=475)
    R6.place(x=850,y=500)
    R7.place(x=850,y=525)
    b1.place(x=480,y=650)
    b2.place(x=600,y=650)
    b3.place(x=720,y=650)
    w1.pack()
    r1.mainloop()
    
def updp():

    def dbupdp():
        D1=str(s3)+'-'+str(s2)+'-'+str(s1)
        D2=str(Sp3)+'-'+str(Sp2)+'-'+str(S1)
        if r=='Regular':
            cur.execute('Update table regpat_checks set diagnosis=:dia,status=:st,treatment=:trt,name=:nm,sex=:s,address=:add,phone_no=:pno,medicine=:med,date_of_visit=:vd,payment_mode=:pm where patient_id=:id)',{'dia':e4.get(),'st':e5.get(),'trt':e7.get(),'nm':e3.get(),'s':g,'add':e8.get(),'pno':e6.get(),'med':e9.get(),'vd':D1,'pm':e10.get(),'id':e2.get()})
            con.commit()
        elif r=='Admitted':
            cur.execute('Update table admpat_checks set diagnosis=:dia,status=:st,treatment=:trt,name=:nm,sex=:s,address=:add,phone_no=:pno,bed_no=:bno,payment_mode=:pm,admit_date=:adate,room_no=:rno where patient_id=:id',{'dia':e4.get(),'st':e5.get(),'trt':e7.get(),'nm':e3.get(),'s':g,'add':e8.get(),'pno':e6.get(),'bno':E1.get(),'pm':e10.get(),'adate':D2,'rno':E2.get(),'id':e2.get()})
            con.commit()
            
    def adm():
        r3=Tk()
        r3.title('Admitted Patient Data')
        r3.resizable(False,False)
        w3=Frame(r3,height=400,width=600,bg='pink')
        l1=Label(r3,text='Room No',width=12,height=2,font=('Times New Roman',-20),bg='pink')
        e1=Entry(w3,width=30)
        l2=Label(r3,text='Bed No',width=12,height=2,font=('Times New Roman',-20),bg='pink')
        e2=Entry(w3,width=30)
        l1.place(x=150,y=100)
        e1.place(x=300,y=100)
        l2.place(x=150,y=300)
        e2.place(x=300,y=300)
        l3=Label(r1,text='Visit Date',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
        Sp1=Spinbox(w1,from_=1,to=31,command=getval1)
        Sp2=Spinbox(w1,from_=1,to=12,command=getval2)
        Sp3=Spinbox(w1,from_=2017,to=2022,command=getval3)
        l3.place(x=100,y=200)
        Sp1.place(x=250,y=200)
        Sp2.place(x=250,y=230)
        Sp3.place(x=250,y=260)
        w3.pack()
        r3.mainloop()
    
    def submit():
        dbupdp()
        root2=Tk()
        root2.title('Success')
        w1=Frame(root2,height=150,width=300,bg='snow')
        m=Message(root2,text='Updation Successful',width=100,font=('Times New Roman',-15),bg='snow',fg='black')
        m.place(x=100,y=50)
        w1.pack()
        root2.resizable(False,False)
        display()
        mainloop()

    def clear():
        x=int(S1.get())
        while x>1:
            S1.invoke("buttondown")
            x=x-1
        y=int(S2.get())
        while y>1:
            S2.invoke("buttondown")
            y=y-1
        z=int(S3.get())
        while z>1:
            S3.invoke("buttondown")
            z=z-1
        R1.deselect()
        R2.deselect()
        R3.deselect()
        R4.deselect()
        R5.deselect()
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)

    def getval1():
        global s1
        s1=S1.get()

    def getval2():
        global s2
        s2=S2.get()

    def getval3():
        global s2
        s3=S3.get()

    def getval4():
        global r
        R=v1.get()
        if R==1:
            r='Regular'
        elif R==2:
            r='Admitted'
            adm()
        else:
            pass

    def getval5():
        global g
        R2=v2.get()
        if R2==1:
            g='M'
        elif R2==2:
            g='F'
        elif R2==3:
            g='O'
        else:
            pass
        
    r1=Tk()
    r1.title('Patient\'s Data')
    v1=IntVar(r1)
    v2=IntVar(r1)
    w1=Frame(r1,height=768,width=1600,bg='mintcream')
    l1=Message(r1,text='Update patient data',width=500,font=('Tahoma',-20),fg='Black',bg='mintcream')
    l1.place(x=570,y=20)
    l2=Label(r1,text='Patient ID',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e2=Entry(w1,width=30)
    l3=Label(r1,text='Name',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e3=Entry(w1,width=30)
    l4=Label(r1,text='Diagnosis',width=10,height=2,font=('Times New Roman',-20),bg='mintcream')
    e4=Entry(w1,width=30)
    l5=Label(r1,text='Status',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e5=Entry(w1,width=30)
    l6=Label(r1,text='Phone No.',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e6=Entry(w1,width=30)
    l7=Label(r1,text='Treatment',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e7=Entry(w1,width=30)
    l8=Label(r1,text='Address',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e8=Entry(w1,width=105)
    l9=Label(r1,text='Medicine',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e9=Entry(w1,width=30)
    l10=Label(r1,text='Payment Mode',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e10=Entry(w1,width=30)
    l11=Label(r1,text='Visit Date',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    S1=Spinbox(w1,from_=1,to=31,command=getval1)
    S2=Spinbox(w1,from_=1,to=12,command=getval2)
    S3=Spinbox(w1,from_=2017,to=2022,command=getval3)
    l12=Label(r1,text='Type',width=10,height=2,font=('Times New Roman',-20),bg='mintcream')
    R1=Radiobutton(r1,text="Regular",variable=v1,value=1,bg='mintcream',command=getval4)
    R2=Radiobutton(r1,text="Admitted",variable=v1,value=2,bg='mintcream',command=getval4)
    l13=Label(r1,text='Sex',width=10,height=2,font=('Times New Roman',-20),bg='mintcream')
    R3=Radiobutton(r1,text="M",variable=v2,value=1,bg='mintcream',command=getval5)
    R4=Radiobutton(r1,text="F",variable=v2,value=2,bg='mintcream',command=getval5)
    R5=Radiobutton(r1,text="O",variable=v2,value=3,bg='mintcream',command=getval5)
    b1=Button(w1,text="Submit",width=15,height=2,bg="green",command=submit)
    b2=Button(w1,text="Clear All",width=15,height=2,bg="yellow",command=clear)
    b3=Button(w1,text="Close",width=15,height=2,bg="red",command=quit)
    l2.place(x=240,y=80)
    e2.place(x=400,y=95)
    l3.place(x=645,y=80)
    e3.place(x=850,y=95)
    l4.place(x=250,y=150)
    e4.place(x=400,y=165)
    l5.place(x=645,y=150)
    e5.place(x=850,y=165)
    l6.place(x=240,y=220)
    e6.place(x=400,y=235)
    l7.place(x=660,y=220)
    e7.place(x=850,y=235)
    l8.place(x=230,y=290)
    e8.place(x=400,y=305)
    l9.place(x=235,y=360)
    e9.place(x=400,y=375)
    l10.place(x=680,y=360)
    e10.place(x=850,y=375)
    l11.place(x=235,y=430)
    S1.place(x=400,y=447)
    S2.place(x=550,y=447)
    S3.place(x=700,y=447)
    l12.place(x=228,y=500)
    R1.place(x=400,y=515)
    R2.place(x=400,y=535)
    l13.place(x=695,y=500)
    R3.place(x=800,y=515)
    R4.place(x=800,y=535)
    R5.place(x=800,y=555)
    b1.place(x=480,y=650)
    b2.place(x=600,y=650)
    b3.place(x=720,y=650)
    w1.pack()
    r1.mainloop()
    
def deld():

    def delt():
        cur.execute('Delete from doc_reg where doctor_id=:did',{'did':e2.get()})
        con.commit()
        root2=Tk()
        root2.title('Record Delted')
        w1=Frame(root2,height=150,width=300,bg='snow')
        m=Message(root2,text='Record Deleted',width=100,font=('Times New Roman',-15),bg='snow',fg='black')
        m.place(x=100,y=50)
        w1.pack()
        root2.resizable(False,False)
        display()
        quit
        mainloop()
  
    def cleard():
        e2.delete(0,END)

    r1=Tk()
    r1.title('Doctor\'s Data')
    r1.resizable(False,False)
    w1=Frame(r1,height=500,width=800,bg='mintcream')
    l1=Message(r1,text='Delete doctor\'s data',width=500,font=('Tahoma',-20),fg='Black',bg='mintcream')
    l1.place(x=300,y=20)
    l2=Label(r1,text='Doctor\'s Id',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e2=Entry(w1,width=30)
    b1=Button(w1,text="Delete",width=15,height=2,bg="light green",command=delt)
    b2=Button(w1,text="Clear",width=15,height=2,bg="yellow",command=cleard)
    b3=Button(w1,text="Close",width=15,height=2,bg="red",command=quit)
    l2.place(x=200,y=170)
    e2.place(x=400,y=185)
    b1.place(x=200,y=350)
    b2.place(x=350,y=350)
    b3.place(x=500,y=350)
    r1.resizable(False,False)
    w1.pack()
    r1.mainloop()

def delp():
    
    def delt():
        if r=='Regular':
            cur.execute('Delete from regpat_checks where patient_id=:pid',{'pid':e2.get()})
            con.commit()
        elif r=='Admitted':
            cur.execute('Delete from admpat_checks where patient_id=:pid',{'pid':e2.get()})
            con.commit()
        root2=Tk()
        root2.title('Record Delted')
        w1=Frame(root2,height=150,width=300,bg='snow')
        m=Message(root2,text='Record Deleted',width=100,font=('Times New Roman',-15),bg='snow',fg='black')
        m.place(x=100,y=50)
        w1.pack()
        root2.resizable(False,False)
        display()
        quit
        mainloop()
  
    def cleard():
        e2.delete(0,END)

    r1=Tk()
    r1.title('Patient\'s Data')
    r1.resizable(False,False)
    w1=Frame(r1,height=500,width=800,bg='mintcream')
    l1=Message(r1,text='Delete patient\'s data',width=500,font=('Tahoma',-20),fg='Black',bg='mintcream')
    l1.place(x=300,y=20)
    l2=Label(r1,text='Patient\'s Id',width=12,height=2,font=('Times New Roman',-20),bg='mintcream')
    e2=Entry(w1,width=30)
    b1=Button(w1,text="Delete",width=15,height=2,bg="light green",command=delt)
    b2=Button(w1,text="Clear",width=15,height=2,bg="yellow",command=cleard)
    b3=Button(w1,text="Close",width=15,height=2,bg="red",command=quit)
    l2.place(x=200,y=170)
    e2.place(x=400,y=185)
    b1.place(x=200,y=350)
    b2.place(x=350,y=350)
    b3.place(x=500,y=350)
    r1.resizable(False,False)
    w1.pack()
    r1.mainloop()

def display():
    cur.execute('Select * from doc_reg')
    print(cur.fetchall(),'\n')
    cur.execute('Select * from department')
    print(cur.fetchall(),'\n')
    cur.execute('Select * from regpat_checks')
    print(cur.fetchall(),'\n')
    cur.execute('Select * from admpat_checks')
    print(cur.fetchall(),'\n')
      
root=Tk()
root.title('Mini Project')
w=Frame(root,height=768,width=1600,bg='wheat')
m1=Message(root,text='Hospital Data Entry',width=800,font=('Castellar',-50),fg='black',bg='wheat')
m2=Message(root,text='To enter/update desired data, click the button below!',width=500,font=('Tahoma',-15),fg='Blue',bg='wheat')
l1=Label(root,text='Doctor',width=12,height=2,font=('Times New Roman',-20,'bold'),bg='wheat')
l2=Label(root,text='Patient',width=12,height=2,font=('Times New Roman',-20,'bold'),bg='wheat')
B1=Button(w,text="Insert",width=30,height=2,bg='light green',fg='black',command=insd)
B2=Button(w,text="Update",width=30,height=2,bg='light green',fg='black',command=updd)
B3=Button(w,text="Delete",width=30,height=2,bg='light green',fg='black',command=deld)
B4=Button(w,text="Insert",width=30,height=2,bg='light green',fg='black',command=insp)
B5=Button(w,text="Update",width=30,height=2,bg='light green',fg='black',command=updp)
B6=Button(w,text="Delete",width=30,height=2,bg='light green',fg='black',command=delp)
B7=Button(w,text="Search",width=50,height=2,command=Search)
B8=Button(w,text="Exit",width=50,height=2,bg='Red',command=quit)
m1.place(x=380,y=20)
m2.place(x=500,y=120)
l1.place(x=480,y=190)
B1.place(x=650,y=200)
B2.place(x=650,y=250)
B3.place(x=650,y=300)
l2.place(x=480,y=370)
B4.place(x=650,y=380)
B5.place(x=650,y=430)
B6.place(x=650,y=480)
B7.place(x=500,y=550)
B8.place(x=500,y=600)
w.pack()
root.mainloop()
con.close()
