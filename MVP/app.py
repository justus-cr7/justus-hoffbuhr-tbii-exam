# This code can be executed without any special instructions on how to run it.
# It is built to work on any type of operating system.
# It eschews the use of images to preserve simplicity and minimalism,
# as well as to make the code easy to execute for everybody.

# Importing all the libraries that I'm going to use.
import tkinter as tk
import random
import webbrowser

# Creating the GUI and setting the title, the geometry and the background colour.
root = tk.Tk()
root.title('ROLF.')
root.geometry('650x650')

# Creating variables for the two colours I am going to use, new colour scheme for the new version.
colour1 = '#aaaaaa'
colour2 = '#555357'

# Setting the background colour.
root.configure(background=colour2)

# Creating and placing the first two labels for the homepage.
title1 = tk.Label(root, text='HELLO.', font='Didot 30 bold', fg=colour1, bg=colour2)
title2 = tk.Label(root, text='WELCOME TO ROLF.', font='Didot 30 bold', fg=colour1, bg=colour2)
title1.place(x=255, y=210)
title2.place(x=155, y=260)

# Creating variables to store the users email address and name.
email_input = tk.StringVar()
name_input = tk.StringVar()


# This is the Log-In window, including an entry Box which will store the name of the user.
def login_window():
    overlay = tk.Label(width=650, height=650, bg=colour2)
    name_entry = tk.Entry(root, font='Didot 20 bold', bg=colour2, fg=colour1, highlightbackground='#cdc5bf',
                          justify='center', textvariable=name_input, width=35)
    next_button = tk.Button(text='NEXT.', font='Didot 25 bold', activeforeground='white', fg=colour2,
                            highlightbackground=colour2, command=pre_window)
    title = tk.Label(root, text='PLEASE ENTER YOUR NAME HERE.', font='Didot 30 bold', fg=colour1, bg=colour2)
    overlay.place(x=0, y=0)
    name_entry.place(x=110, y=280)
    next_button.place(x=265, y=380)
    title.place(x=50, y=180)


# This window works as a transition to the main menu, picturing the name of the user.
def pre_window():
    overlay1 = tk.Label(width=650, height=650, bg=colour2)
    text1 = tk.Label(root, text=f'HELLO {name_input.get().upper()}.', font='Didot 30 bold', fg=colour1, bg=colour2)
    text2 = tk.Label(root, text='NICE TO MEET YOU.', font='Didot 30 bold', fg=colour1, bg=colour2)
    menu_button = tk.Button(text='MENU.', font='Didot 25 bold', activeforeground='white', fg=colour2,
                            highlightbackground=colour2, command=main_window)
    overlay1.place(x=0, y=0)
    text1.place(x=195, y=200)
    text2.place(x=170, y=260)
    menu_button.place(x=265, y=380)


# This function defines the main menu of my application, including all the important buttons and some labels.
def main_window():
    # Creating an overlay to have a blank space for our window at first.
    overlay = tk.Label(width=650, height=650, bg=colour2)
    head_title = tk.Label(text='ROLF.', font='Didot 100 bold', fg=colour1, bg=colour2)
    title_text = tk.Label(text='GENTLEMAN TEACHING ASSOCIATION.', font='Didot 20 bold', fg=colour1,
                          bg=colour2)
    modules_button = tk.Button(text='MODULES.', font='Didot 40 bold', height='2', width='11', activeforeground='white',
                               fg=colour2, highlightbackground=colour2, command=age_window)
    random_module_button = tk.Button(text='RANDOM MODULE.', font='Didot 25 bold', height='2', width='21',
                                     activeforeground='white', fg=colour2, highlightbackground=colour2,
                                     command=module_chooser)
    explanation_button = tk.Button(text='WHAT IS ROLF?', font='Didot 20 bold', height='1', width='41',
                                   activeforeground='white', fg=colour2, highlightbackground=colour2,
                                   command=explanation_window)
    help_button = tk.Button(text='HELP.', font='Didot 20 bold', height='1', width='8', activeforeground='white',
                            fg=colour2, highlightbackground=colour2, command=help_window)
    credits_button = tk.Button(text='CREDITS.', font='Didot 20 bold', height='1', width='10', activeforeground='white',
                               fg=colour2, highlightbackground=colour2, command=credits_window)
    quit_button = tk.Button(text='QUIT.', font='Didot 20 bold', height='1', width='8', activeforeground='white',
                            fg=colour2, highlightbackground=colour2, command=root.destroy)

    # Placing everything I created.
    overlay.place(x=0, y=0)
    head_title.place(x=165, y=25)
    title_text.place(x=115, y=150)
    modules_button.place(x=180, y=245)
    random_module_button.place(x=160, y=395)
    explanation_button.place(x=62, y=540)
    help_button.place(x=60, y=590)
    credits_button.place(x=245, y=590)
    quit_button.place(x=460, y=590)


# This function defines the basic GUI for every other window except of the main menu and the module windows,
# including a simple instruction for colour and geometry and two buttons, the 'back button' and the 'quit button'.
def basic_gui():
    overlay = tk.Label(width=650, height=650, bg=colour2)
    back_button = tk.Button(text='BACK.', font='Didot 20 bold', height='1', width='8',
                            activeforeground='white', fg=colour2, highlightbackground=colour2,
                            command=main_window)
    quit_button = tk.Button(text='QUIT.', font='Didot 20 bold', height='1', width='8',
                            activeforeground='white', fg=colour2, highlightbackground=colour2,
                            command=root.destroy)

    overlay.place(x=0, y=0)
    back_button.place(x=60, y=590)
    quit_button.place(x=460, y=590)
    
    
# This function defines the GUI for the first 9 different module windows.
def basic_gui2():
    overlay = tk.Label(width=650, height=650, bg=colour2)
    back_button2 = tk.Button(text='BACK.', font='Didot 20 bold', height='1', width='8',
                             activeforeground='white', fg=colour2,
                             highlightbackground=colour2, command=modules_window1)
    quit_button = tk.Button(text='QUIT.', font='Didot 20 bold', height='1', width='8',
                            activeforeground='white', fg=colour2,
                            highlightbackground=colour2, command=root.destroy)
    title = tk.Label(text="BASIC TIPS:", font='Didot 30 bold', fg="white", bg=colour2)

    overlay.place(x=0, y=0)
    back_button2.place(x=60, y=590)
    quit_button.place(x=460, y=590)
    title.place(x=230, y=120)


# This function defines the GUI for the last 9 different module windows.
def basic_gui3():
    overlay = tk.Label(width=650, height=650, bg=colour2)
    back_button2 = tk.Button(text='BACK.', font='Didot 20 bold', height='1', width='8',
                             activeforeground='white', fg=colour2,
                             highlightbackground=colour2, command=modules_window2)
    quit_button = tk.Button(text='QUIT.', font='Didot 20 bold', height='1', width='8',
                            activeforeground='white', fg=colour2,
                            highlightbackground=colour2, command=root.destroy)
    title = tk.Label(text="BASIC TIPS:", font='Didot 30 bold', fg="white", bg=colour2)

    overlay.place(x=0, y=0)
    back_button2.place(x=60, y=590)
    quit_button.place(x=460, y=590)
    title.place(x=230, y=120)


# This function defines the explanation window and is called by the 'What is ROLF.?' button from the main menu.
def explanation_window():
    # Here I am using the first GUI function I just created, just to simplify the code.
    basic_gui()
    head_title = tk.Label(text='THE IDEA.', font='Didot 80 bold', fg=colour1, bg=colour2)
    title_text = tk.Label(text='ROLF. is a guide app for boys or young men \n who have had to grow up without a father '
                               'figure. \n The app aims to teach simple things that a father \n usually teaches his '
                               'son, such as how to shave, \n how to tie a tie, etc. The purpose of this app is '
                               'firstly \n to answer questions that a fatherless boy might want \n to ask his father '
                               'and secondly, possibly provide assistance \n with some practical matters.',
                          font='Didot 20 bold', fg=colour1, bg=colour2)

    head_title.place(x=100, y=30)
    title_text.place(x=50, y=215)


# This function defines the help window and is called by the 'HELP.' button from the main menu.
def help_window():
    basic_gui()

    head_title = tk.Label(text='HELP.', font='Didot 80 bold', fg=colour1, bg=colour2)
    title_text = tk.Label(text='FOR QUESTIONS, SUGGESTIONS ETC.', font='Didot 20 bold', fg=colour1,
                          bg=colour2)
    title_text2 = tk.Label(text='ENTER YOUR EMAIL HERE.', font='Didot 20 bold', fg=colour1, bg=colour2)
    title_text3 = tk.Label(text='WE WILL CONTACT YOU.', font='Didot 20 bold', fg=colour1, bg=colour2)
    # Creating an entry to put in the users email address, then storing the input as the email_input variable I created
    # in the beginning.
    help_input = tk.Entry(root, font='Didot 20 bold', bg=colour2, fg=colour1, highlightbackground=colour1,
                          justify='center', textvariable=email_input, width=35)
    submit_button = tk.Button(text='SUBMIT.', font='Didot 25 bold', height='1', width='8',
                              activeforeground='white', fg=colour2, highlightbackground=colour2,
                              command=help_window2)

    head_title.place(x=200, y=30)
    title_text.place(x=130, y=220)
    title_text2.place(x=185, y=260)
    title_text3.place(x=195, y=470)
    help_input.place(x=110, y=330)
    submit_button.place(x=250, y=400)


# Second part of the help window that gets called by pushing the 'SUBMIT.' button from help_window()
# This window displays the input and stored email address of the user.
def help_window2():
    basic_gui()

    head_title = tk.Label(text='THANK YOU.', font='Didot 80 bold', fg=colour1, bg=colour2)
    # Accessing the email address stored in the email_input variable.
    title_text = tk.Label(text=f'WE HAVE SEND AN EMAIL TO \n {email_input.get().lower()}.', font='Didot 30 bold',
                          fg=colour1, bg=colour2)

    head_title.place(x=60, y=60)
    title_text.place(x=80, y=300)


# This function defines the credits window and is called by the 'CREDITS.' button from the main menu.
# It displays who created the application.
def credits_window():
    basic_gui()

    head_title = tk.Label(text='CREDITS.', font='Didot 80 bold', fg=colour1, bg=colour2)
    title_text1 = tk.Label(text='CREATED BY JUSTUS HOFFBUHR.', font='Didot 20 bold', fg=colour1,
                           bg=colour2)
    title_text2 = tk.Label(text='LEUPHANA UNIVERSITY LÜNEBURG.', font='Didot 20 bold', fg=colour1,
                           bg=colour2)
    title_text3 = tk.Label(text='MAJOR DIGITAL MEDIA.', font='Didot 20 bold', fg=colour1, bg=colour2)
    title_text4 = tk.Label(text='TECH BASICS II.', font='Didot 20 bold', fg=colour1, bg=colour2)
    title_text5 = tk.Label(text='FW 23/24.', font='Didot 20 bold', fg=colour1, bg=colour2)

    head_title.place(x=125, y=30)
    title_text1.place(x=140, y=275)
    title_text2.place(x=125, y=300)
    title_text3.place(x=190, y=325)
    title_text4.place(x=235, y=350)
    title_text5.place(x=270, y=375)


# This window will ask the user for his age to give him a better selection for the modules.
def age_window():
    overlay1 = tk.Label(width=650, height=650, bg=colour2)
    text = tk.Label(root, text='PLEASE SELECT YOUR AGE.', font='Didot 30 bold', fg=colour1, bg=colour2)
    button1 = tk.Button(root, text='< 18', font='Didot 25 bold', fg=colour2, highlightbackground=colour2,
                        command=modules_window1)
    button2 = tk.Button(root, text='18 +', font='Didot 25 bold', fg=colour2, highlightbackground=colour2,
                        command=modules_window2)
    overlay1.place(x=0, y=0)
    text.place(x=95, y=230)
    button1.place(x=180, y=350)
    button2.place(x=370, y=350)


# This function defines the modules window and is called by the 'MODULES.' button from the main menu.
# It shows all the different modules available for the <18 people.
def modules_window1():
    basic_gui()

    head_title = tk.Label(text='MODULES.', font='Didot 80 bold', fg=colour1, bg=colour2)
    module1_button = tk.Button(text='SHAVING.', width='10', height='5', font='Didot 14 bold',
                               activeforeground='white', fg=colour2, highlightbackground=colour2,
                               command=module1_window)
    module2_button = tk.Button(text='APPLYING A\n SCENT.', width='10', height='5', font='Didot 14 bold',
                               activeforeground='white', fg=colour2, highlightbackground=colour2,
                               command=module2_window)
    module3_button = tk.Button(text='BASIC\n HYGIENE.', width='10', height='5', font='Didot 14 bold',
                               activeforeground='white', fg=colour2, highlightbackground=colour2,
                               command=module3_window)
    module4_button = tk.Button(text='BUYING\n FLOWERS.', width='10', height='5', font='Didot 14 bold',
                               activeforeground='white', fg=colour2, highlightbackground=colour2,
                               command=module4_window)
    module5_button = tk.Button(text='SIMPLE\n DANCING.', width='10', height='5', font='Didot 14 bold',
                               activeforeground='white', fg=colour2, highlightbackground=colour2,
                               command=module5_window)
    module6_button = tk.Button(text='ASKING OUT\n A GIRL.', width='10', height='5', font='Didot 14 bold',
                               activeforeground='white', fg=colour2, highlightbackground=colour2,
                               command=module6_window)
    module7_button = tk.Button(text='PLAYING\n CHESS.', width='10', height='5', font='Didot 14 bold',
                               activeforeground='white', fg=colour2, highlightbackground=colour2,
                               command=module7_window)
    module8_button = tk.Button(text='DRESSING\n UP.', width='10', height='5', font='Didot 14 bold',
                               activeforeground='white', fg=colour2, highlightbackground=colour2,
                               command=module8_window)
    module9_button = tk.Button(text='CAMPING.', width='10', height='5', font='Didot 14 bold',
                               activeforeground='white', fg=colour2, highlightbackground=colour2,
                               command=module9_window)
    change_age = tk.Button(text='CHANGE AGE.', font='Didot 20 bold', height='1', width='12', activeforeground='white',
                           fg=colour2, highlightbackground=colour2, command=age_window)

    head_title.place(x=100, y=0)
    module1_button.place(x=120, y=130)
    module2_button.place(x=270, y=130)
    module3_button.place(x=420, y=130)
    module4_button.place(x=120, y=280)
    module5_button.place(x=270, y=280)
    module6_button.place(x=420, y=280)
    module7_button.place(x=120, y=430)
    module8_button.place(x=270, y=430)
    module9_button.place(x=420, y=430)
    change_age.place(x=235, y=590)


# Same window as before, but now with the modules for the 18+ people.
def modules_window2():
    basic_gui()

    head_title = tk.Label(text='MODULES.', font='Didot 80 bold', fg=colour1, bg=colour2)
    module10_button = tk.Button(text='TYING A\n TIE.', width='10', height='5', font='Didot 14 bold',
                                activeforeground='white', fg=colour2, highlightbackground=colour2,
                                command=module10_window)
    module11_button = tk.Button(text='WORKING\n OUT.', width='10', height='5', font='Didot 14 bold',
                                activeforeground='white', fg=colour2, highlightbackground=colour2,
                                command=module11_window)
    module12_button = tk.Button(text='DRIVING\n A CAR.', width='10', height='5', font='Didot 14 bold',
                                activeforeground='white', fg=colour2, highlightbackground=colour2,
                                command=module12_window)
    module13_button = tk.Button(text='PREPARING\n A DINNER.', width='10', height='5', font='Didot 14 bold',
                                activeforeground='white', fg=colour2, highlightbackground=colour2,
                                command=module13_window)
    module14_button = tk.Button(text='MAKING\n BARBECUE.', width='10', height='5', font='Didot 14 bold',
                                activeforeground='white', fg=colour2, highlightbackground=colour2,
                                command=module14_window)
    module15_button = tk.Button(text='MAKING\n COCKTAILS.', width='10', height='5', font='Didot 14 bold',
                                activeforeground='white', fg=colour2, highlightbackground=colour2,
                                command=module15_window)
    module16_button = tk.Button(text='HAVING\n SAFE SEX.', width='10', height='5', font='Didot 14 bold',
                                activeforeground='white', fg=colour2, highlightbackground=colour2,
                                command=module16_window)
    module17_button = tk.Button(text='PROPOSING.', width='10', height='5', font='Didot 14 bold',
                                activeforeground='white', fg=colour2, highlightbackground=colour2,
                                command=module17_window)
    module18_button = tk.Button(text='BREAKING\n UP.', width='10', height='5', font='Didot 14 bold',
                                activeforeground='white', fg=colour2, highlightbackground=colour2,
                                command=module18_window)
    change_age = tk.Button(text='CHANGE AGE.', font='Didot 20 bold', height='1', width='12', activeforeground='white',
                           fg=colour2, highlightbackground=colour2, command=age_window)

    head_title.place(x=100, y=0)
    module10_button.place(x=120, y=130)
    module11_button.place(x=270, y=130)
    module12_button.place(x=420, y=130)
    module13_button.place(x=120, y=280)
    module14_button.place(x=270, y=280)
    module15_button.place(x=420, y=280)
    module16_button.place(x=120, y=430)
    module17_button.place(x=270, y=430)
    module18_button.place(x=420, y=430)
    change_age.place(x=235, y=590)


# This function is a random number generator which is used for picking a random module among the 16 that I created.
# It picks a random number between 1 and 16 and then calls the paired module. Every number is paired with a one module.
def module_chooser():
    module_choice = random.choice(['1', '2', '3', '4', '5', '6', '7', '8', '9',
                                   '10', '11', '12', '13', '14', '15', '16', '17', '18'])
    if module_choice == '1':
        module1_window()
    elif module_choice == '2':
        module2_window()
    elif module_choice == '3':
        module3_window()
    elif module_choice == '4':
        module4_window()
    elif module_choice == '5':
        module5_window()
    elif module_choice == '6':
        module6_window()
    elif module_choice == '7':
        module7_window()
    elif module_choice == '8':
        module8_window()
    elif module_choice == '9':
        module9_window()
    elif module_choice == '10':
        module10_window()
    elif module_choice == '11':
        module11_window()
    elif module_choice == '12':
        module12_window()
    elif module_choice == '13':
        module13_window()
    elif module_choice == '14':
        module14_window()
    elif module_choice == '15':
        module15_window()
    elif module_choice == '15':
        module16_window()
    elif module_choice == '15':
        module17_window()
    else:
        module18_window()


# Now I'm creating every window for every single of the 16 modules. To simplify this progress, I am using the
# basic_gui2 function that I just created.
def module1_window():
    basic_gui2()
    head_title = tk.Label(text='SHAVING.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=190, y=20)

    text = tk.Label(text='1. BE GENTLE.\n\n2. USE A SINGLE-BLADE RAZOR.\n\n3. USE SHAVING FOAM.\n\n4. USE AFTER SHAVE.',
                    justify="left", font='Didot 20 bold', fg="white", bg=colour2)

    # This definition is used in every single module window. It provides access to the internet,
    # making it possible to watch a YouTube Video when clicking the button.
    def link():
        webbrowser.open_new(r"https://youtu.be/DzdT84upVNQ?si=SFniVg1rcRdrHyVc")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


def module2_window():
    basic_gui2()
    head_title = tk.Label(text='APPLYING A SCENT.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=60, y=20)

    text = tk.Label(text='1. I DO FIVE SPRAYS.\n\n2. TWO ON YOUR NECK.\n\n3. TWO BEHIND EACH EAR.\n'
                         '\n4. ONE AT THE BACK OF YOUR NECK.',
                    justify="left", font='Didot 20 bold', fg="white", bg=colour2)

    def link():
        webbrowser.open_new(r"https://youtu.be/-cnvorwYPOM?si=7X_j87C15BllN0Ht")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


def module3_window():
    basic_gui2()
    head_title = tk.Label(text='BASIC HYGIENE.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=105, y=20)

    text = tk.Label(text='1. GET A SKINCARE ROUTINE.\n\n2. SHOWER DAILY.\n\n3. USE DEODORANT.\n\n4. STYLE YOUR HAIR.',
                    justify="left", font='Didot 20 bold', fg="white", bg=colour2)

    def link():
        webbrowser.open_new(r"https://youtu.be/U-kKKZATK70?si=6kSrdeiv5OLwwGmp")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


def module4_window():
    basic_gui2()
    head_title = tk.Label(text='BUYING FLOWERS.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=80, y=20)

    text = tk.Label(text='1. DO NOT MIX FLOWERS.\n\n2. MIND THE OCCASION.\n\n3. NO SUPERMARKET FLOWERS.\n'
                         '\n4. SPEND AT LEAST 20€.',
                    justify="left", font='Didot 20 bold', fg="white", bg=colour2)

    def link():
        webbrowser.open_new(r"https://youtu.be/694B0AzwH94?si=FeRKmIg6VufSz7fG")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


def module5_window():
    basic_gui2()
    head_title = tk.Label(text='SIMPLE DANCING.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=90, y=20)

    text = tk.Label(text='1. DO NOT STEP ON HER FOOT.\n\n2. BE CONFIDENT.\n\n3. GET DANCING LESSONS.\n'
                         '\n4. GO WITH THE FLOW.',
                    justify="left", font='Didot 20 bold', fg="white", bg=colour2)

    def link():
        webbrowser.open_new(r"https://youtu.be/S1qp7r99DcE?si=tY5PafdYx2zryLvj")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


def module6_window():
    basic_gui2()
    head_title = tk.Label(text='ASKING OUT A GIRL.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=55, y=20)

    text = tk.Label(text='1. BE RESPECTFUL.\n\n2. BE CONFIDENT.\n\n3. ACCEPT A REJECTION.\n\n4. CHOOSE WISELY.',
                    justify="left", font='Didot 20 bold', fg="white", bg=colour2)

    def link():
        webbrowser.open_new(r"https://youtu.be/LCOSTpygvAk?si=bemEr0RBo-1LmrTw")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


def module7_window():
    basic_gui2()
    head_title = tk.Label(text='PLAYING CHESS.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=100, y=20)

    text = tk.Label(text='1. LEARN OPENING TACTICS.\n\n2. LEARN ENDGAME TACTICS.\n\n3. THINK THREE MOVES AHEAD.\n'
                         '\n4. STAY FOCUSSED.',
                    justify="left", font='Didot 20 bold', fg="white", bg=colour2)

    def link():
        webbrowser.open_new(r"https://youtu.be/OCSbzArwB10?si=rBVH7gAwPTGI5w9k")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


def module8_window():
    basic_gui2()
    head_title = tk.Label(text='DRESSING UP.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=130, y=20)

    text = tk.Label(text='1. MIND THE OCCASION.\n\n2. WEAR BLUE & BLACK IN WINTER.\n\n3. WEAR GREY & BEIGE IN SUMMER.\n'
                         '\n4. DO NOT WEAR SNEAKERS.',
                    justify="left", font='Didot 20 bold', fg="white", bg=colour2)

    def link():
        webbrowser.open_new(r"https://youtu.be/_1j-CcFCBRg?si=eynSJ8utHBguTCKM")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


def module9_window():
    basic_gui2()
    head_title = tk.Label(text='CAMPING.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=190, y=20)

    text = tk.Label(text='1. TRY NOT TO DIE.\n\n2. BE CAREFUL WITH FIRE.\n\n3. USE GOOD EQUIPMENT.\n\n4. STAY DRY.',
                    justify="left", font='Didot 20 bold', fg="white", bg=colour2)

    def link():
        webbrowser.open_new(r"https://youtu.be/xUqTgNJgWUs?si=G2WO-BjfytUJ6Qy1")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


def module10_window():
    basic_gui3()
    head_title = tk.Label(text='TYING A TIE.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=150, y=20)

    text = tk.Label(text='1. CHOOSE A TYING STYLE.\n\n2. I RECOMMEND THE WINDSOR KNOT.\n\n3. NO SLIM TIES.\n'
                         '\n4. JUST WATCH THE VIDEO.',
                    justify="left", font='Didot 20 bold', fg="white", bg=colour2)

    def link():
        webbrowser.open_new(r"https://youtu.be/0Pdg2gXx2t8?si=TuZTJUrbB3Jrefo-")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


def module11_window():
    basic_gui3()
    head_title = tk.Label(text='WORKING OUT.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=125, y=20)

    text = tk.Label(text='1. DAY ONE: BACK & BICEPS.\n\n2. DAY TWO: CHEST, SHOULDERS & TRICEPS.\n'
                         '\n3. DAY THREE: TRAIN LEGS.\n\n4. DAY 4: REST.',
                    justify="left", font='Didot 20 bold', fg="white", bg=colour2)

    def link():
        webbrowser.open_new(r"https://youtu.be/3sEeVJEXTfY?si=TshfTt88fcAPjZHf")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


def module12_window():
    basic_gui3()
    head_title = tk.Label(text='DRIVING A CAR.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=120, y=20)

    text = tk.Label(text='1. ASK SOMEONE WHO CAN DRIVE.\n\n2. PRACTICE SOMEWHERE SAFE.\n\n3. GET DRIVING LESSONS.\n'
                         '\n4. DO NOT FAIL THEORY.',
                    justify="left", font='Didot 20 bold', fg="white", bg=colour2)

    def link():
        webbrowser.open_new(r"https://youtu.be/VIVaqt4VhKc?si=En1QEqkljE8KVyaB")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


def module13_window():
    basic_gui3()
    head_title = tk.Label(text='PREPARING A DINNER.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=30, y=20)

    text = tk.Label(text='1. MIND THE OCCASION.\n\n2. STARTER, MAIN COURSE, DESSERT.\n\n3. TRY YOUR BEST.\n'
                         '\n4. BE ABLE TO COOK.',
                    justify="left", font='Didot 20 bold', fg="white", bg=colour2)

    def link():
        webbrowser.open_new(r"https://youtu.be/X_qo3lnRS1k?si=QqKhQSBK00dy1XMV")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


def module14_window():
    basic_gui3()
    head_title = tk.Label(text='MAKING BARBECUE.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=55, y=20)

    text = tk.Label(text='1. GET A BEER.\n\n2. USE A GAS GRILL.\n\n3. USE GOOD MEAT.\n'
                         '\n4. JUST WATCH THE VIDEO PLEASE.',
                    justify="left", font='Didot 20 bold', fg="white",  bg=colour2)

    def link():
        webbrowser.open_new(r"https://youtu.be/tB1UzkEqJJs?si=g4w7ViSgcqyCSJG4")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


def module15_window():
    basic_gui3()
    head_title = tk.Label(text='MAKING COCKTAILS.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=40, y=20)

    text = tk.Label(text='1. MIND THE OCCASION.\n\n2. USE GOOD INGREDIENTS.\n\n3. TOO STRONG > NOT STRONG ENOUGH.\n'
                         '\n4. DO NOT PROVIDE ALCOHOL TO CHILDREN.',
                    justify="left", font='Didot 20 bold', fg="white", bg=colour2)

    def link():
        webbrowser.open_new(r"https://youtu.be/b0IuTL3Z-kk?si=c-zlOpQEibzYw34O")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


def module16_window():
    basic_gui3()
    head_title = tk.Label(text='HAVING SAFE SEX.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=85, y=20)

    text = tk.Label(text='1. USE A CONDOM SOMETIMES.\n\n2. BE RESPECTFUL.\n\n3. COMMUNICATION IS KEY.\n'
                         '\n4. SHOW OFF YOUR PULL-OUT GAME.',
                    justify="left", font='Didot 20 bold', fg="white", bg=colour2)

    def link():
        webbrowser.open_new(r"https://youtu.be/EUxAevRbEnY?si=7zXNOwQKvoG2f4SQ")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


def module17_window():
    basic_gui3()
    head_title = tk.Label(text='PROPOSING.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=160, y=20)

    text = tk.Label(text='1. MAKE SURE SHE IS THE ONE.\n\n2. PREPARATION IS KEY.\n\n3. BUY A RING.\n'
                         '\n4. GET DOWN ON YOUR KNEE.',
                    justify="left", font='Didot 20 bold', fg="white", bg=colour2)

    def link():
        webbrowser.open_new(r"https://youtu.be/-P0vBx3uP-0?si=0Eo_h5EXR7-VtTst")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


def module18_window():
    basic_gui3()
    head_title = tk.Label(text='BREAKING UP.', font='Didot 50 bold', fg=colour1, bg=colour2)
    head_title.place(x=135, y=20)

    text = tk.Label(text='1. BE RESPECTFUL.\n\n2. IT IS OKAY TO CRY.\n\n3. TRY NOT TO HURT HER FEELINGS.\n'
                         '\n4. MAKE IT HAPPEN.',
                    justify="left", font='Didot 20 bold', fg="white", bg=colour2)

    def link():
        webbrowser.open_new(r"https://youtu.be/wSyTRCLlq2w?si=4W3drgFr9mGB6pir")

    video_button = tk.Button(root, text='VIDEO.', font='Didot 20 bold', height='2', width='6', activeforeground='white',
                             fg=colour2, highlightbackground=colour2, command=link)
    video_text = tk.Label(text="CLICK HERE TO WATCH THE VIDEO.", font='Didot 20 bold', fg=colour1, bg=colour2)
    video_text.place(x=125, y=430)
    video_button.place(x=275, y=480)
    text.place(x=125, y=190)


# Here I am creating the start button for the homepage, which will lead to my main window.
start_button = tk.Button(text='START.', font='Didot 25 bold', activeforeground='white', fg=colour2,
                         highlightbackground=colour2, command=login_window)

# Placing the start button.
start_button.place(x=255, y=340)

root.mainloop()
