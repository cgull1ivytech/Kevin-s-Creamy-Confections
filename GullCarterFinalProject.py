#Created by Carter Gull
#This program will utilitize tkinter GUIs to create an ordering kiosk for customers at Kevins Creamy Confections

#import tkinter
from tkinter import *

#create gui window
gui = Tk()
gui.title('Kevins Creamy Confections')

#create labels for pickup/dinein option
label1 = Label(gui, text='We Offer Pickup Orders ', fg='blue', bg='yellow')
label2 = Label(gui, text='And Dine In Orders ', fg='blue', bg='yellow')

label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=0, column=2, padx=10, pady=10)

label3 = Label(gui, text='How would you like to receive your order? ', fg='blue', bg='yellow')

label3.grid(row=1, column=1, padx=10, pady=10)

#define pickup/dinein options
def pickup():
    print('You ordered pick up!')
def dine():
    print('You ordered to dine in!')

#create buttons for pickup/dinein option
btn_pickup = Button(gui, text='Order Pick up', command=pickup)
btn_dine = Button(gui, text='Order Dine In', command=dine)

                  
btn_pickup.grid(row=2, column=0, padx=10, pady=10)
btn_dine.grid(row=2, column=2, padx=10, pady=10)

#function to create new gui window for cone/sundae option
def openCone():
    Cone = Toplevel(gui)
    Cone.title = ('Kevins Creamy Confections')

    #create label for cone/sundae option
    ConeLabel = Label(Cone, text= 'We Offer Ice Cream Cones and Ice Cream Sundaes, which would you like? ', fg='blue', bg='yellow')
    ConeLabel.grid(row=0,column=1, padx=10, pady=10)

    #define cone/sundae options
    def chooseCone():
        print('Your order will be in a Cone!')
    def chooseSundae():
        print('Your order will be a Sundae!')

    #create buttons for cone/sundae option    
    Conebtn_chooseCone = Button(Cone, text='Cone', command=chooseCone)
    Conebtn_chooseSundae = Button(Cone, text='Sundae', command=chooseSundae)
    
    Conebtn_chooseCone.grid(row=1, column=0, padx=10, pady=10)
    Conebtn_chooseSundae.grid(row=1, column=2, padx=10, pady=10)

    #function to create new gui for size selection
    def openSize():
        Size = Toplevel(gui)
        Size.title = ('Kevins Creamy Confections')

        #create label for size selection
        SizeLabel = Label(Size, text='We offer 3 sizes, 1 Scoop, 2 Scoops, or 3 Scoops. Which would you like? ', fg='blue', bg='yellow')
        SizeLabel.grid(row=0, column=1, padx=10, pady=10)

        #define size options
        def choose1():
            print('Your order will have 1 Scoop of Icecream!')
        def choose2():
            print('Your order will have 2 Scoops of Icecream!')
        def choose3():
            print('Your order will have 3 Scoops of Icecream!')

        #create buttons for size selections
        Sizebtn_choose1 = Button(Size, text='1 Scoop', command=choose1)
        Sizebtn_choose2 = Button(Size, text='2 Scoops', command=choose2)
        Sizebtn_choose3 = Button(Size, text='3 Scoops', command=choose3)

        Sizebtn_choose1.grid(row=1, column=0, padx=10, pady=10)
        Sizebtn_choose2.grid(row=1, column=1, padx=10, pady=10)
        Sizebtn_choose3.grid(row=1, column=2, padx=10, pady=10)

        #function to create new gui window for toppings
        def openToppings():
            Toppings = Toplevel(gui)
            Toppings.title = ('Kevins Creamy Confections')

            #create label for toppings selection
            ToppingsLabel = Label(Toppings, text='We offer many toppings, which are listed below. Choose as many as you like! ', fg='blue', bg='yellow')
            ToppingsLabel.grid(row=0, column=1, padx=10, pady=10)

            #define toppings options
            def chooseNuts():
                print('You have added Nuts to your order!')
            def chooseChocolate():
                print('You have added Chocolate to your order!')
            def chooseStrawberrySyrup():
                print('You have added Strawberry Syrup to your order!')
            def choosePineappleSyrup():
                print('You have added Pineapple Syrup to your order!')
            def chooseWhipCream():
                print('You have added Whipped Cream to your order!')
            def chooseSprinkles():
                print('You have added Sprinkles to your order!')
            def chooseSugarCookies():
                print('You have added Sugar Cookies to your order!')
            def chooseBananas():
                print('You have added Bananas to your order!')
            def chooseCherryOnTop():
                print('You have added a Cherry on Top to your order!')

            #buttons for toppings options
            Toppingsbtn_chooseNuts = Button(Toppings, text='Nuts', command=chooseNuts)
            Toppingsbtn_chooseChocolate = Button(Toppings, text='Chocolate', command=chooseChocolate)
            Toppingsbtn_chooseStrawberrySyrup = Button(Toppings, text='Strawberry Syrup', command=chooseStrawberrySyrup)
            Toppingsbtn_choosePineappleSyrup = Button(Toppings, text='Pineapple Syrup', command=choosePineappleSyrup)
            Toppingsbtn_chooseWhipCream = Button(Toppings, text='Whipped Cream', command=chooseWhipCream)
            Toppingsbtn_chooseSprinkles = Button(Toppings, text='Sprinkles', command=chooseSprinkles)
            Toppingsbtn_chooseSugarCookies = Button(Toppings, text='Sugar Cookies', command=chooseSugarCookies)
            Toppingsbtn_chooseBananas = Button(Toppings, text='Bananas', command=chooseBananas)
            Toppingsbtn_chooseCherryOnTop = Button(Toppings, text='Cherry on Top', command=chooseCherryOnTop)

            Toppingsbtn_chooseNuts.grid(row=1, column=0, padx=10, pady=10)
            Toppingsbtn_chooseChocolate.grid(row=1, column=1, padx=10, pady=10)
            Toppingsbtn_chooseStrawberrySyrup.grid(row=1, column=2, padx=10, pady=10)
            Toppingsbtn_choosePineappleSyrup.grid(row=2, column=0, padx=10, pady=10)
            Toppingsbtn_chooseWhipCream.grid(row=2, column=1, padx=10, pady=10)
            Toppingsbtn_chooseSprinkles.grid(row=2, column=2, padx=10, pady=10)
            Toppingsbtn_chooseSugarCookies.grid(row=3, column=0, padx=10, pady=10)
            Toppingsbtn_chooseBananas.grid(row=3, column=1, padx=10, pady=10)
            Toppingsbtn_chooseCherryOnTop.grid(row=3, column=2, padx=10, pady=10)

            #function to create new gui window for end screen
            def openFinalize():
                Finalize = Toplevel(gui)
                Finalize.title = ('Kevin Creamy Confections')
                
                FinalizeLabel = Label(Finalize, text='Thank you for ordering with us, your order will be done shortly. Have a great day! ', fg='blue', bg='yellow')
                FinalizeLabel.grid(row=0, column=0, padx=10, pady=10)
                                
            #button that opens new gui window for end screen                   
            btn_openFinalize = Button(Toppings, text='Click to Finalize your order', command = openFinalize)
            btn_openFinalize.grid(row=5, column=1, padx=10, pady=10)
            

    
        #button that opens a new gui window for toppings selection 
        btn_openToppings = Button(Size, text='Click to continue with your order', command = openToppings)
        btn_openToppings.grid(row=2, column=1, padx=10, pady=10)
        
    #button that opens a new gui window for size selection
    btn_openSize = Button(Cone, text='Click to continue with your order', command = openSize)
    btn_openSize.grid(row=2, column=1, padx=10, pady=10)
    
#button that opens a new gui window for cone/sundae selection    
btn_openCone = Button(gui, text='Click to continue with your order', command = openCone)
btn_openCone.grid(row=3, column=1, padx=10, pady=10)


gui.mainloop()
