# main Application to Enter the Details of the Flight

import ttk
from Tkinter import *
import sage_joinspan
import sqlite3
from PIL import *
from PIL import Image
import Tkinter as Tk
#from xlrd import open_workbook
import xlrd,xlwt, xlutils
import tkMessageBox
import subprocess,os
class Flight(object,ttk.Notebook):
    # function __init__ would start at the start of the program
    def __init__(self,unm,parent):
        self.root=parent
        self.root.title("Air Route Finder: Main Application")
        self.frame=Tk.Frame(parent)
        self.frame.pack()
        #app=Flight()
        self.aduser=unm
        self.menubar = Menu(self.frame)
        
        self.root.config(menu=self.menubar)
    
        self.filemenu = Menu(self.menubar,tearoff=0)
        
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Find Tour",command=self.find_tour)
        self.filemenu.add_command(label="Show City List",command=self.Get)
        self.filemenu.add_command(label="Open Previous Tour",command=self.prev_tour)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.quit)
    
        
        self.editmenu = Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)
        self.addcitymenu= Menu(self.editmenu,tearoff=0)
        self.editmenu.add_cascade(label="Update City List",menu=self.addcitymenu)
        self.addcitymenu.add_command(label= "Add a City",command=self.add_city)
        
        
        self.helpmenu = Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="Scope", )
        self.helpmenu.add_command(label="Objectives", )
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label="About",menu=self.aboutmenu)
        
        
    
    

    
        self.menubar.add_command(label="Quit!", command=self.frame.quit)

        self.canvas= Canvas(self.frame, width='1300', height='775' , bg='grey')
        self.canvas.pack()
        
        self.status = Label(self.root, text="Hello "+unm, bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)
        
        
    
        
        
        
    def find_tour(self):
        '''
        self.can=Canvas(self.root)
        self.can.pack() 
        labelFirst= Label(self.can,text="Welcome to Air Route Finder",font=('Times New Roman',30)).grid(row=0,columnspan=2)
        '''
        '''
        #self.frame=self.root()
        self.can= Canvas(self.canvas, width='1300', height='300' , bg='white')
        self.can.grid(row=0,column=0)
        #self.can.pack()

        pic=PhotoImage(file="city.gif")
        tem=can.create_image(5,5,image=pic)
        '''
        '''
        self.button=Button(self.canvas,text='Find', width=10, height=2, command=self.Get)
        self.button.pack()
        
        self.can= Canvas(self.canvas, width='1300', height='400' , bg='white')
        self.can.grid(row=0,column=0)

        '''
        self.frame=Tk.Tk()
        self.frame.title("Find Tour")
        self.frame.geometry('600x300+400+200')
        
        group = Label(self.frame, text="Find Best Tour", padx=5, pady=5,height=500,width=1300)
        group.pack(padx=10, pady=10)

        

        self.labelprime = Label(group , text="Find Tour",font=('Times New Roman',20)).grid(row=1,columnspan=2)

        self.label1 = Label(group , text="Enter the City : ")
        self.label1.grid(row=1,column=0)
        #self.label1.pack(anchor=W)
        
        self.ent1=Entry(group,bg='white')
        self.ent1.grid(row=1,column=1)
        #self.ent1.pack(anchor=E)
              
        self.hi_there= Button(group, text="Find Tour",command=self.finder)
        self.hi_there.grid(row=2,column=0)
        
        print "Everything's gonna be alright"
        

    def Get(self):
        '''
        wb = open_workbook('./city_info/city_distances.xls')
        nest=[]
        for s in wb.sheets():
            print 'Sheet:',s.name
            for row in range(s.nrows):
                values = []
                for col in range(s.ncols):
                    values.append(unicode(s.cell(row,col).value))
                    
                print ','.join(values)
                nest.append(values)
        a=len(nest[0])
        '''
        os.system('libreoffice ./city_info/city_distances.xls')
        
        #subprocess.call(['libreoffice ./city_info/city_distances.xls'])
        '''
        self.frame=Tk.Tk()
        self.frame.title("Show City List")
        self.frame.geometry('600x300+400+200')
        '''
        #for i in range(0,a):
            


        
        '''
        global pic
        global tem
        self.can= Canvas(self.canvas, width='1300', height='400' , bg='white')
        self.can.grid(row=0,column=0)
        
        inp="citylist.gif"
        if inp=='clear':
            self.can.delete(tem)
        else:
            pic=PhotoImage(file=inp)
            tem=self.can.create_image(500,200,image=pic)    
        '''

    def finder(self):
        start=self.ent1.get()
        sage_joinspan.main(start)

    def add_city(self):

        if self.aduser=="Chitrank":
            self.frame=Tk.Tk()
            self.frame.title("Add a City")
            self.frame.geometry('600x300+270+100')

            self.labelFirst= Label(self.frame,text="Add a City",font=('Times New Roman',30)).grid(row=0,columnspan=2)
            #self.labelFirst.pack()
    
   
        
            self.label1 = Label(self.frame , text="Enter the New City : ")
            self.label1.grid(row=1,column=0)
            #self.label1.pack(anchor=W)
        
            self.ent1=Entry(self.frame,bg='white')
            self.ent1.grid(row=1,column=1)
            #self.ent1.pack(anchor=E)

        
            self.label2 = Label(self.frame , text="Enter distances seperated by comma (City Sequence) ,:  ")
            self.label2.grid(row=2,column=0)
            #self.label1.pack(anchor=W)
        
            self.ent2=Entry(self.frame,bg='white')
            self.ent2.grid(row=2,column=1)
            #self.ent1.pack(anchor=E)
        
            self.hi_there= Button(self.frame, text="Add City",command=self.update_citylist)
            self.hi_there.grid(row=3,column=0)
        
            #print "Everything's gonna be alright"
        else:
            tkMessageBox.showinfo("Invalid Operation ", "You are not authorized to do this operation")
            
    
    def update_citylist(self):
        if self.ent1.get()==self.ent2.get()=='':
            tkMessageBox.showinfo("Error while Processing ", "Check username and Email")
        
        wb = xlrd.open_workbook('./city_info/city_distances.xls',formatting_info=True)
        nest=[]
        for s in wb.sheets():
            print 'Sheet:',s.name
            for row in range(s.nrows):
                values = []
                for col in range(s.ncols):
                    values.append(unicode(s.cell(row,col).value))
                    
                print ','.join(values)
                nest.append(values)
        
        #for i in range(1,len(nest)):
        #    for j in range(1,len(nest[i])):
        #        nest[i][j]=float(nest[i][j])

        
        
        pre=len(nest)
        print pre
        #split distances
        li=self.ent2.get()
        distance_list=li.split(',')
        print distance_list
        city=self.ent1.get()
        print nest
        
        if self.ent1 =='':
            tkMessageBox.showinfo("Duplicate Entry ", "City already in Citylist")
        else:
            nest[0].append(unicode(city))
            nest.append([unicode(city)])
              
            for k in range(0,len(distance_list)):
                nest[-1].append(unicode(distance_list[k]))

            print nest[-1]
                
            print nest
            for i in range(0,len(distance_list)):
                j=i+1
                nest[j].append(unicode(distance_list[i]))
            print "\n\n\n", nest
            print len(nest)

            #nest[0][row-1].append(city)
            #nest[row-1][0].append(city)
            wbk=xlwt.Workbook()
            sheet=wbk.add_sheet('Sheet1')

            for i in range(len(nest)-1):
                for j in range(len(nest)-1):
                    print i,j
                    sheet.write(i,j,unicode(nest[i][j]))
            off=len(nest)-1
            i=0
            while i<off:
                sheet.write(i,off,unicode(nest[i][off]))
                sheet.write(off,i,unicode(nest[off][i]))
                i=i+1

            sheet.write(off,off,unicode(nest[-1][-1]))
            wbk.save('./city_info/city_distances.xls')
            

    def show_tour(self):
        global tem
        global pic

        im = Image.open(r'Graph.png')
        bg = Image.new("RGB",im.size,(255,255,255))
        bg.paste(im,im)
        conv_file_name='G.gif'
        bg.save(r'G.gif')
        
        self.can= Canvas(self.canvas, width='1300', height='1000' , bg='white')
        self.can.pack()# grid(row=0,column=0)
        
        #inp="citylist.gif"
        if conv_file_name=='clear':
            self.can.delete(tem)
        else:
            pic=PhotoImage(file=conv_file_name)
            tem=self.can.create_image(600,200,image=pic)
        #transparency = im.info['transparency'] 
        #im.save('GraphT.gif', transparency=transparency)
    
    def prev_tour(self):
        '''
        self.iframe=Tk.Tk()
        self.iframe.title("Previous Tour")
        self.iframe.geometry('1000x775+220+70')

        self.show=Button(self.iframe,text='Show Tour',command=self.show_tour)
        self.show.pack()
        #transparency = im.info['transparency'] 
        #im.save('GraphT.gif', transparency=transparency)
        '''
        os.system('display Graph.png')
        

        
        
        

       
    
    def change_canv(self):
        self.sho=Label(frame,text="")
        self.sho.pack()

    def connect_us(self):
        conn=sqlite3.connect("AirRoute.db")
        cursor=conn.cursor()
        return cursor,conn

    
        

    def insert_indb(self):
        n1=self.ent1.get()
        n2=self.ent2.get()
        cursor,conn=self.connect_us()
        #c=self.create_table(cursor)
        cursor.execute("INSERT INTO airroute values(?,?)",(n1,n2))
        conn.commit()
        self.ent1.delete(0,END)
        self.ent2.delete(0,END)
        print "Data Inserted"


    def login(self):
        n1=self.ent1.get()
        n2=self.ent2.get()
        cursor,conn=self.connect_us()
        #c=self.create_table(cursor)
        a=cursor.execute("select * from airroute where uname='n1' and pass='n2'")
        conn.commit()
        self.ent1.delete(0,END)
        self.ent2.delete(0,END)
        
        
        if a:
            print "Logged In"
    



        
def main(unm):
    root=Tk.Tk()
    root.geometry('1300x800+220+70')
    FD=Flight(unm,root)
    root.mainloop()
    '''
    root=Tkinter.Tk()
    root.title("Air Route Finder: Main Application")
    root.geometry('1300x550+200+100')
    #app=Flight()
    menubar = Menu(root)
    
    menubar.add_command(label="File",)
    menubar.add_command(label="Edit",)
    menubar.add_command(label="Help",)
    menubar.add_command(label="Quit!", command=root.quit)
    
    root.config(menu=menubar)

    filemenu = Menu(menubar,tearoff=0)
    
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Find Tour",)
    filemenu.add_command(label="Open Previous Tour", )
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)

    
    editmenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Edit", menu=editmenu)
    editmenu.add_command(label="Add a City", )
    editmenu.add_separator()
    editmenu.add_command(label="Cut", )
    editmenu.add_command(label="Copy", )
    editmenu.add_command(label="Paste", )
    editmenu.add_separator()
    editmenu.add_command(label="Undo", )
    editmenu.add_command(label="Redo", )

    helpmenu = Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="Scope", )
    helpmenu.add_command(label="Objectives", )
    helpmenu.add_separator()
    helpmenu.add_command(label="About", )
    
    

    
    menubar.add_command(label="Quit!", command=root.quit)
    
    status = Label(root, text="Hello ", bd=1, relief=SUNKEN, anchor=W)
    status.pack(side=BOTTOM, fill=X)
    
    root.mainloop()
    '''


if __name__=="__main__":
    unm='Chitrank'
    main(unm)
    
