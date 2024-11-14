from tkinter import * 
root=Tk()
root.geometry("500x300")

def getvals():
    print("Your Form Saved Successfully")

#Heading
Label(root,text="Python Login Page",font="arial 16 bold").grid(row=0
                                                               ,column=3)

#Field-Names
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
email=Label(root,text="Email")


#Packing Fields
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
email.grid(row=4,column=2)


#Variables For Storing Data
namevalue=StringVar
phonevalue=IntVar
gendervalue=StringVar
emailvalue=StringVar

checkvalue=IntVar

#Creating Entry Fields  
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
emailentry=Entry(root,textvariable=emailvalue)

#Packing Entry Fields
nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emailentry.grid(row=4,column=3)

#Creating Checkbox

checkbtn=Checkbutton(text="Remember Me!" ,variable=checkvalue)
checkbtn.grid(row=6,column=3)

#Submit button

Button(text="Submit",command=getvals).grid(row=7,column=3)

root.mainloop()

