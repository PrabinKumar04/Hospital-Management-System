from tkinter import *
from tkinter import ttk
import random
import datetime
import time
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root = root 
        self.root.title("Hospital Management System")
        self.root.geometry("1366x768+0+0") 
        
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.PatientAddress=StringVar()     
        self.DailyDose=StringVar()
        self.sideEfect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
        
        lb_title = Label(self.root, bd=10, relief=RIDGE, text="Hospital Management System", fg="red", bg="white", font=("times new roman", 28, "bold"))  # Reduced font size
        lb_title.pack(side=TOP, fill=X)
        
        # --------------------------Data_frame-----------------
        
        Dataframe = Frame(self.root, bd=10, relief=RIDGE)
        Dataframe.place(x=0, y=70, width=1280, height=340)
        
        Dataframe_left = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                  font=("arial", 10, "bold"), text="Patient Information")
        Dataframe_left.place(x=5, y=5, width=800, height=310)
   
        Dataframe_right = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,
                  font=("arial", 10, "bold"), text="Prescription")
        Dataframe_right.place(x=820, y=5, width=435, height=310) 
        
        # -------------------------Button_frame----------------
        
        Button_frame = Frame(self.root, bd=10, relief=RIDGE)
        Button_frame.place(x=0, y=405, width=1280, height=50)
        
        #--------------------------Details_frame---------------
        
        Details_frame = Frame(self.root, bd=10, relief=RIDGE)
        Details_frame.place(x=0, y=460, width=1280, height=230)
        
        #--------------------------Data_frame_left-------------
        
        lb_name_Tablet = Label(Dataframe_left,text="Name of Tablet",font=("arial",8,"bold"),padx=2,pady=6)
        lb_name_Tablet.grid(row=0,column=0)
        
        com_name_tablet=ttk.Combobox(Dataframe_left,textvariable=self.Nameoftablets,state="readonly",font=("arial",8,"bold"),width=43)
        
        com_name_tablet["values"]=("Paracetamol","Ibuprofen","Amoxicillin","Omeprazole","Metformin","Atorvastatin","Salbutamol","Cetirizine","Warfarin","Prednisone")
        com_name_tablet.grid(row=0,column=1)
        
        #--------_rows_and _1stcolumn-------
        
        lb_name_Ref = Label(Dataframe_left,text="Reference No:",font=("arial",8,"bold"),padx=2,pady=6)
        lb_name_Ref.grid(row=1,column=0,sticky=W)
        lb_name_Tablet = Entry(Dataframe_left,font=("arial",8,"bold"),textvariable=self.ref,width=45)
        lb_name_Tablet.grid(row=1,column=1)
        
        lb_Dose = Label(Dataframe_left,text="Dose:",font=("arial",8,"bold"),padx=2,pady=6)
        lb_Dose.grid(row=2,column=0,sticky=W)
        lb_Dose = Entry(Dataframe_left,font=("arial",8,"bold"),textvariable=self.Dose,width=45)
        lb_Dose.grid(row=2,column=1)
        
        lb_No_of_Tablets = Label(Dataframe_left,text="No of Tablets:",font=("arial",8,"bold"),padx=2,pady=6)
        lb_No_of_Tablets.grid(row=3,column=0,sticky=W)
        lb_No_of_Tablets = Entry(Dataframe_left,font=("arial",8,"bold"),textvariable=self.NumberofTablets,width=45)
        lb_No_of_Tablets.grid(row=3,column=1)
        
        lb_Lot = Label(Dataframe_left,text="Lot:",font=("arial",8,"bold"),padx=2,pady=6)
        lb_Lot.grid(row=4,column=0,sticky=W)
        lb_Lot = Entry(Dataframe_left,font=("arial",8,"bold"),textvariable=self.Lot,width=45)
        lb_Lot.grid(row=4,column=1)
        
        lb_Issue_Date = Label(Dataframe_left,text="Issue Date:",font=("arial",8,"bold"),padx=2,pady=6)
        lb_Issue_Date.grid(row=5,column=0,sticky=W)
        lb_Issue_Date = Entry(Dataframe_left,font=("arial",8,"bold"),textvariable=self.Issuedate,width=45)
        lb_Issue_Date.grid(row=5,column=1)
        
        lb_Exp_Date = Label(Dataframe_left,text="Exp Date:",font=("arial",8,"bold"),padx=2,pady=6)
        lb_Exp_Date.grid(row=6,column=0,sticky=W)
        lb_Exp_Date = Entry(Dataframe_left,font=("arial",8,"bold"),textvariable=self.ExpDate,width=45)
        lb_Exp_Date.grid(row=6,column=1)
        
        lb_Daily_Dose = Label(Dataframe_left,text="Daily Dose:",font=("arial",8,"bold"),padx=2,pady=6)
        lb_Daily_Dose.grid(row=7,column=0,sticky=W)
        lb_Daily_Dose = Entry(Dataframe_left,font=("arial",8,"bold"),textvariable=self.DailyDose,width=45)
        lb_Daily_Dose.grid(row=7,column=1)
        
        lb_Side_Effect = Label(Dataframe_left,text="Side Effect:",font=("arial",8,"bold"),padx=2,pady=6)
        lb_Side_Effect.grid(row=8,column=0,sticky=W)
        lb_Side_Effect = Entry(Dataframe_left,font=("arial",8,"bold"),textvariable=self.sideEfect,width=45)
        lb_Side_Effect.grid(row=8,column=1)
        
        #--------_rows_and _3rdcolumn-------
        
        lb_Further_Info = Label(Dataframe_left,text="Further Information:",font=("arial",8,"bold"),padx=2)
        lb_Further_Info.grid(row=0,column=2,sticky=W)
        lb_Further_Info = Entry(Dataframe_left,font=("arial",8,"bold"),textvariable=self.FurtherInformation,width=45)
        lb_Further_Info.grid(row=0,column=3)
        
        
        lb_Blood_Pressure = Label(Dataframe_left,text="Blood Pressure:",font=("arial",8,"bold"),padx=2,pady=6)
        lb_Blood_Pressure.grid(row=1,column=2,sticky=W)
        lb_Blood_Pressure = Entry(Dataframe_left,font=("arial",8,"bold"),textvariable=self.DrivingUsingMachine,width=45)
        lb_Blood_Pressure.grid(row=1,column=3)
         
        lb_Storage = Label(Dataframe_left,text="Storage Advice:",font=("arial",8,"bold"),padx=2,pady=6)
        lb_Storage.grid(row=2,column=2,sticky=W)
        lb_Storage = Entry(Dataframe_left,font=("arial",8,"bold"),textvariable=self.StorageAdvice,width=45)
        lb_Storage.grid(row=2,column=3)
        
        lb_Medicine = Label(Dataframe_left,text="Medicine:",font=("arial",8,"bold"),padx=2,pady=6)
        lb_Medicine.grid(row=3,column=2,sticky=W)
        lb_Medicine = Entry(Dataframe_left,font=("arial",8,"bold"),textvariable=self.HowToUseMedication,width=45)
        lb_Medicine.grid(row=3,column=3)
        
        lb_Patient_Id = Label(Dataframe_left,text="Patient Id:",font=("arial",8,"bold"),padx=2,pady=6)
        lb_Patient_Id.grid(row=4,column=2,sticky=W)
        lb_Patient_Id = Entry(Dataframe_left,font=("arial",8,"bold"),textvariable=self.PatientId,width=45)
        lb_Patient_Id.grid(row=4,column=3)
        
        lb_Nhs_Number = Label(Dataframe_left,text="NHS Number:",font=("arial",8,"bold"),padx=2,pady=6)
        lb_Nhs_Number.grid(row=5,column=2,sticky=W)
        lb_Nhs_Number = Entry(Dataframe_left,font=("arial",8,"bold"),textvariable=self.nhsNumber,width=45)
        lb_Nhs_Number.grid(row=5,column=3)
        
        lb_Patient_Name = Label(Dataframe_left,text="Patient Name:",font=("arial",8,"bold"),padx=2,pady=6)
        lb_Patient_Name.grid(row=6,column=2,sticky=W)
        lb_Patient_Name = Entry(Dataframe_left,font=("arial",8,"bold"),textvariable=self.PatientName,width=45)
        lb_Patient_Name.grid(row=6,column=3)
        
        lb_Date_of_Birth = Label(Dataframe_left,text="Date of Birth:",font=("arial",8,"bold"),padx=2,pady=6)
        lb_Date_of_Birth.grid(row=7,column=2,sticky=W)
        lb_Date_of_Birth = Entry(Dataframe_left,font=("arial",8,"bold"),textvariable=self.DateOfBirth,width=45)
        lb_Date_of_Birth.grid(row=7,column=3)
        
        lb_Patient_Address = Label(Dataframe_left,text="Patient Address:",font=("arial",8,"bold"),padx=2,pady=6)
        lb_Patient_Address.grid(row=8,column=2,sticky=W)
        lb_Patient_Address = Entry(Dataframe_left,font=("arial",8,"bold"),textvariable=self.PatientAddress,width=45)
        lb_Patient_Address.grid(row=8,column=3)
        
        #--------------------------Data_frame_Right--------------
        self.txtPrescription=Text(Dataframe_right,font=("arial",8,"bold"),width=66,height=19,padx=1,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        
    
        #-------------------------Buttons-----------------------
        #---------------prescription_data----------------
        def prescription_data():
            messagebox.showinfo("Information", "Prescription Data Inserted Successfully")
            
        #---------function_declaration-----------  
          
        def i_Prescription_data(self):
            if self.Nameoftablets.get()=="" or self.ref.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="prabin",database="my_data")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                    self.Nameoftablets.get(),
                                    self.ref.get(),
                                    self.Dose.get(),
                                    self.NumberofTablets.get(),
                                    self.Lot.get(),
                                    self.Issuedate.get(),
                                    self.ExpDate.get(),
                                    self.DailyDose.get(),
                                    self.StorageAdvice.get(),
                                    self.nhsNumber.get(),
                                    self.PatientName.get(),
                                    self.DateOfBirth.get(),
                                    self.PatientAddress.get()
                                    ))
                
                prescription_data()
                conn.commit()
                self.fetch_data()
                conn.close()
        
        But_PrescriptionData=Button(Button_frame,text="Prescription Data",bg="green",fg="white",font=("arial",8,"bold"),command=lambda:i_Prescription_data(self),width=28,height=1,padx=3,pady=6)
        But_PrescriptionData.grid(row=0,column=1)

        #-----------------prescription-------------
        def prescription():
            messagebox.showinfo("Information", "Prescription Displayed Successfully")
            
        #----------------function_declaration------
        def iPrescription(self):
            self.txtPrescription.insert(END, "Reference No:\t\t\t" + self.ref.get() + "\n") 
            self.txtPrescription.insert(END, "Name of Tablets:\t\t\t" + self.Nameoftablets.get() + "\n")
            self.txtPrescription.insert(END, "Dose:\t\t\t" + self.Dose.get() + "\n")
            self.txtPrescription.insert(END, "Number Of Tablets:\t\t\t" + self.NumberofTablets.get() + "\n")
            self.txtPrescription.insert(END, "Lot:\t\t\t" + self.Lot.get() + "\n")
            self.txtPrescription.insert(END, "Issue Date: \t\t\t" + self.Issuedate.get() + "\n")
            self.txtPrescription.insert(END, "Exp date: \t\t\t" + self.ExpDate.get() + "\n")
            self.txtPrescription.insert(END, "daily Dose:\t\t\t" + self.DailyDose.get() + "\n")
            self.txtPrescription.insert(END, "Side Effect:\t\t\t" + self.sideEfect.get() + "\n")
            self.txtPrescription.insert(END, "Further Information:\t\t\t" + self. FurtherInformation.get() + "\n")
            self.txtPrescription.insert(END, "StorageAdvice:\t\t\t" + self. StorageAdvice.get() + "\n")
            self.txtPrescription.insert(END, "DrivingUsing Machine:\t\t\t" + self.DrivingUsingMachine.get() + "\n")
            self.txtPrescription.insert(END, "PatientId:\t\t\t" + self.PatientId.get() + "\n")
            self.txtPrescription.insert(END, "NHSNumber:\t\t\t" + self.nhsNumber.get() + "\n") 
            self.txtPrescription.insert(END, "PatientName:\t\t\t" + self.PatientName.get() + "\n")
            self.txtPrescription.insert(END, "DateOfBirth:\t\t\t" + self.DateOfBirth.get() + "\n")
            self.txtPrescription.insert(END, "PatientAddress: \t\t\t" + self.PatientAddress.get() + "\n")
            
            prescription()
        
        But_Prescription = Button(Button_frame, text="Prescription", bg="green", fg="white", font=("arial", 8, "bold"), command=lambda: iPrescription(self), width=28, height=1, padx=3, pady=6)
        But_Prescription.grid(row=0, column=0)

        #---------------------Update---------------
        def update():
            messagebox.showinfo("Information", "Prescription Data Updated Successfully")
            
        #----------------function_declaration------
        def i_update(self):
            if self.Nameoftablets.get()=="" or self.ref.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="prabin",database="my_data")
                my_cursor=conn.cursor()
                my_cursor.execute(("UPDATE hospital SET Nameoftablets=%s, dose=%s, Numbersoftablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, storage=%s, nhsnumber=%s, patientname=%s, DOB=%s, patientaddress=%s WHERE Reference_No=%s"),(
                                    self.Nameoftablets.get(),
                                    self.Dose.get(),
                                    self.NumberofTablets.get(),
                                    self.Lot.get(),
                                    self.Issuedate.get(),
                                    self.ExpDate.get(),
                                    self.DailyDose.get(),
                                    self.StorageAdvice.get(),
                                    self.nhsNumber.get(),
                                    self.PatientName.get(),
                                    self.DateOfBirth.get(),
                                    self.PatientAddress.get(),
                                    self.ref.get()))
                update()
                conn.commit()
                self.fetch_data()
                conn.close()
        
        But_Update=Button(Button_frame,text="Update",bg="green",fg="white",font=("arial",8,"bold"),command=lambda:i_update(self),width=28,height=1,padx=3,pady=6)
        But_Update.grid(row=0,column=2)
        
        #---------------------Delete--------------
        def delete():
            messagebox.showinfo("Information", "Data Deleted Successfully")
        
        #----------------function_declaration------
        def idelete(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="prabin",database="my_data")
            my_cursor=conn.cursor()
            query=("delete from hospital where Reference_No=%s")
            value=(self.ref.get(),)
            my_cursor.execute(query, value)
            
            
            delete()
            conn.commit()
            self.fetch_data()
            conn.close()
            
                    
        But_Delete=Button(Button_frame,text="Delete",bg="green",fg="white",font=("arial",8,"bold"),command=lambda:idelete(self),width=28,height=1,padx=3,pady=6)
        But_Delete.grid(row=0,column=3)
        
        
        #---------------------Clear----------------
        def clear():
            messagebox.showinfo("Information", "Data Cleared successfully")
        
        #----------------function_declaration------
        def iclear(self):
            self.Nameoftablets.set("")
            self.ref.set("")
            self.Dose.set("")
            self.NumberofTablets.set("")
            self.Lot.set("")
            self. Issuedate.set("")
            self.ExpDate.set("")
            self.DailyDose.set("")
            self.sideEfect.set("")
            self. FurtherInformation.set("")
            self.StorageAdvice.set("")
            self.DrivingUsingMachine.set("")
            self.HowToUseMedication.set("")
            self.PatientId.set("")
            self.nhsNumber.set("")
            self.PatientName.set("")
            self.DateOfBirth.set("")
            self.PatientAddress.set("")
            self.txtPrescription.delete("1.0", END)
            
            clear()
            self.fetch_data()
            
        But_Clear=Button(Button_frame,text="Clear",bg="green",fg="white",font=("arial",8,"bold"),command=lambda:iclear(self),width=28,height=1,padx=3,pady=6)
        But_Clear.grid(row=0,column=4)
        
        #---------------------Exit---------------------        
        #----------------function_declaration------
        def iExit(self):
            iExit=messagebox.askyesno("Hospital Management System","Do you want to exit")
            if iExit>0:
                root.destroy()
                return
        
        
        But_Exit=Button(Button_frame,text="Exit",bg="green",fg="white",font=("arial",8,"bold"),command=lambda:iExit(self),width=28,height=1,padx=3,pady=6)
        But_Exit.grid(row=0,column=5)
        
        #--------------------------Table-------------------------
        #----------------Scroll_bar--------------
        Scroll_x=ttk.Scrollbar(Details_frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Details_frame,orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Details_frame, column=("name_of_tablets", "ref", "dose", "no_of_tablets", "lot", "issue_date", "exp_date",
                               "daily_dose", "storage", "NHS_number", "p_name", "dob", "address"), xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        
        Scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        Scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading("name_of_tablets", text="Name of Tablets")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("no_of_tablets", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issue_date", text="Issue Date")
        self.hospital_table.heading("exp_date", text="Exp Date")
        self.hospital_table.heading("daily_dose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("NHS_number", text="NHS Number")
        self.hospital_table.heading("p_name", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")
        
        self.hospital_table["show"]="headings"
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        self.hospital_table.column("name_of_tablets",width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("dose", width=70)
        self.hospital_table.column("no_of_tablets", width=100)
        self.hospital_table.column("lot", width=70)
        self.hospital_table.column("issue_date", width=100)
        self.hospital_table.column("exp_date", width=100)
        self.hospital_table.column("daily_dose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("NHS_number", width=100)
        self.hospital_table.column("p_name", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)
        self.fetch_data()
        
        
    
              
    #---------------fetching_data-------------
       
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="prabin",database="my_data")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from hospital")
         rows=my_cursor.fetchall()
         if len(rows)>0:
             self.hospital_table.delete(*self.hospital_table.get_children())
             for i in rows:
                 self.hospital_table.insert("",END,values=i)
         else:
             self.hospital_table.delete(*self.hospital_table.get_children())
         conn.commit()                
         conn.close()
         
         
         
    #-------------------fetching_data_Back-------------
    def get_cursor(self,ev=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])
        
      
        
        
         
root = Tk()
ob = Hospital(root)
root.mainloop()
