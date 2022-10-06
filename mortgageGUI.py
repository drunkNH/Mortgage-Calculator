"""
Program Name: mortgageGUI
Program Description: The purpose of this program is to utilize Python tkinter to write
                     a GUI based mortgage calculation program. There is exception handling
                     so that the user does not enter invalid inputs. The user will enter
                     a loan amount, interest rate, and loan term in years, and these values
                     will calculate the monthly payment of the mortgage, and the total paid.
                     The user will not be able to change the fields of monthly payment and
                     total paid. There is a calculate button to calculate based on user input
                     in the fields, a chart button which will print out a 30 year
                     historical mortgage data line chart, and a quit button to exit the program.
"""
from print_me_first import print_me_first
from makeChart import chart
import tkinter as tk
from tkinter import *
from tkinter import messagebox as msg

#Create fields list to be used in order to make a GUI form
fields = ('Loan Amount', 'Interest Rate %', 'Loan Term (Years)',"Monthly Payment", "Total Paid")

"""
Function name: calculateMortgage
Function description: this function calculate monthly payment and total paid on a mortgage
                      based on user's loan amount, interest rate, and loan term in years,
                      and place the result on the GUI form.
@param entries - contains the form field on the GUI forms
@return none
"""
def calculateMortgage(entries):

   try:  # catch exception if inputs are invalid (value is not a positive number)
      loanAmount = float(entries['Loan Amount'].get())  
      interestRate = float(entries['Interest Rate %'].get())
      loanTerm = float(entries['Loan Term (Years)'].get())

      #If any user input is lower than 0
      if loanAmount < 0 or interestRate < 0 or loanTerm < 0:
         msg.showwarning('Error: Invalid Input', "Must be positive number > 0") #Show user error message
      else:
         #Calculations for monthly payment and total paid on a mortgage
         monthlyRate = (interestRate / 100) / 12
         numPayments = loanTerm * 12
         monthlyPayment = loanAmount * monthlyRate \
                         * pow((1 + monthlyRate), numPayments) \
                         / (pow((1+monthlyRate),numPayments) - 1)
         totalPayment = monthlyPayment * (loanTerm * 12)
         
         #make fields monthly payment and total paid normal again
         #so we can insert calculated monthly payment and total paid into field,
         #then disable it so user can't change it for both Monthly payment entry and Total paid entry
         entries['Monthly Payment'].configure(state='normal')
         entries['Monthly Payment'].delete(0,END)
         entries['Monthly Payment'].insert(0, "${:,.2f}".format(monthlyPayment))
         entries['Monthly Payment'].configure(state='disabled')
         
         entries['Total Paid'].configure(state='normal')
         entries['Total Paid'].delete(0,END)
         entries['Total Paid'].insert(0, "${:,.2f}".format(totalPayment))
         entries['Total Paid'].configure(state='disabled')
         
   except: #Exception handling to catch any invalid input (user inputs a string)
      msg.showwarning('Error: Invalid Input', 'Must be positive number > 0') #Show user error message

#Main driver code
if __name__ == '__main__':
   root = Tk() # create a Tk window
   root.title("Mortgage Calculator")
   root.configure(background="light blue")

   #create GUI form with all the necessary fields based on the fields list
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0,"0")
      row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
      lab.pack(side = LEFT)
      ent.pack(side = RIGHT, expand = YES, fill = X)
      entries[field] = ent

   #Using lambda to recontruct a new function with same function name with different paramters
   
   #Create calculate button that calls the calculateMortgage function with user input
   #to calculate mortgage data
   b1 = Button(root, text = 'Calculate', bg = 'light blue',
               command=(lambda e = entries: calculateMortgage(e)))
   b1.pack(side = LEFT, padx = 5, pady = 5)

   #Create chart button that calls chart function to create historical mortgage data line chart
   b2 = Button(root, text = 'Chart', command = chart)
   b2.pack(side = LEFT, padx = 5, pady = 5)

   #Create quit button that destroys the window, quitting the porgram
   b3 = Button(root, text = 'Quit', command = root.destroy)
   b3.pack(side = LEFT, padx = 5, pady = 5)

   # make Monthly Payment field readonly with specified font, fontsize, etc
   entries['Monthly Payment'].configure(state='readonly', \
                            font=("Arial", 14, "bold", "italic"))

   # make Total Paid with field readonly with specified font, fontsize, etc
   entries['Total Paid'].configure(state='readonly', \
                            font=("Arial", 14, "bold", "italic"))


   #Create a small textbox next to the quit button that contains print_me_first info, disabled so user can't change it
   tbox = tk.Text(root, height=2, width=30)
   tbox.pack()
   tbox.insert(tk.END, print_me_first("Jeffrey Gu"))
   tbox.configure(state='disabled')
   
   root.mainloop()
