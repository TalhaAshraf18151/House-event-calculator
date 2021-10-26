import tkinter
from tkinter import *
from tkinter import messagebox

tk = tkinter
main = Tk()  # Name of main window
main.title("House event calculator")  # Title
main.geometry("455x280")  # Size of the window in pixels
main.configure(bg="#D2D4DA")  # Background colour
main.resizable(False, False) #Makes window unable to resize in x and y direction just to keep the user from interfering with the structure in the window

All_events = [] #list in which I will hold my HouseEvent object
names_list = ["Lampada Games", "House Trivia"] #list for holding Event names to be used in drop down   
ph_list = [75, 66] #List for holding points of teams for use in Leader board
ku_list = [60, 68] #                   ''
kw_list = [72, 74] #                   ''
ru_list = [68, 73] #                   ''

#------Menu bar--------#
#This is for a help menu at the top of the screen
def entry_instructions():
    messagebox.showinfo('Entry Help', "To use the entry details section click on the box next to 'Name of event' and enter the name of the event. \n\nNext you can click on the yes button if the event was as sport and no if the event wasn't.\n\nThen You can click the arrows to increase or decrease the points of the corresponding house.\n\nFinally you can click the save event button to save the event")
def det_help():
    messagebox.showinfo("Details Help",'Click on the drop down menu that says select an event and click on the event you want\n\nThen click the show details button and a box with the details will appear ')
menubar = Menu(main, background='#C7C9D1')  
help = Menu(menubar, tearoff=0)  
help.add_command(label="Entry Instructions", command=entry_instructions) 
help.add_command(label="Details Instructions", command=det_help)
menubar.add_cascade(label="Entry Help", menu=help)  
main.config(menu=menubar)

#----------------------Frames----------------------#
#These frames keep things organized
#frame for entry box
entry_frame = LabelFrame(main, text= "Details Entry", background="#D2D4DA", font=("Fixedsys"))
entry_frame.grid(row=0, column=0, padx=10, pady=10, sticky=W)
#frame for details box
det_frame = LabelFrame(main, background="#D2D4DA", width='100')
det_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=N)
#frame for leader board
lead_frame = LabelFrame(main, background="#D2D4DA")
lead_frame.grid(row=0, column=1, padx=10, pady=10, sticky=E)

#----------------------Widgets----------------------#
    #-entry_frame labels-#
tk.Label(entry_frame, text="Name of Event", font=("Fixedsys", 12), background="#D2D4DA").grid(column=0, row=0, sticky=W)
tk.Label(entry_frame, text="Is it a sport", font=("Fixedsys", 10), background="#D2D4DA").grid(column=0, row=1, sticky=W)
tk.Label(entry_frame, text="Pohutukawa", font=("Fixedsys", 12), background="#FA6C38").grid(column=0, row=2, sticky=W)
tk.Label(entry_frame, text="Kauri", font=("Fixedsys", 12), background="#62A8F9").grid(column=0, row=3, sticky=W)
tk.Label(entry_frame, text="Kowhai", font=("Fixedsys", 12), background="#FFBC1F").grid(column=0, row=4, sticky=W)
tk.Label(entry_frame, text="Rimu", font=("Fixedsys", 12), background="#01F472").grid(column=0, row=5, sticky=W)
    #-det_frame labels-#
tk.Label(det_frame, text="Event Name", font=("Fixedsys", 12), background="#D2D4DA").grid(column=0, row=0, sticky=W)
    #-entry_frame inputs
name_entry = tk.Entry(entry_frame, font=("Fixedsys", 15), background="#E9E9ED")
# Is sport is a StringVar for the radio button so that the StringVar can be accessed to find the current state of the button in the program
is_sport = tk.StringVar()
is_sport.set("Yes")
Radiobutton(entry_frame, text="Yes", variable=is_sport, value="Yes", font=("Fixedsys", 12), background="#D2D4DA").grid(column=1, row=1,)
Radiobutton(entry_frame, text="No", variable=is_sport, value="No", font=("Fixedsys", 12), background="#D2D4DA").grid(column=2, row=1,)

red_points = Spinbox(entry_frame, from_=0, to=100, increment=1, wrap=YES, state="readonly", font=("Fixedsys"), readonlybackground="#E9E9ED", foreground="#FA6C38")
blue_points = Spinbox(entry_frame, from_=0, to=100, increment=1, wrap=YES, state="readonly", font=("Fixedsys"), readonlybackground="#E9E9ED", foreground="#0656B1")
yellow_points = Spinbox(entry_frame, from_=0, to=100, increment=1, wrap=YES, state="readonly", font=("Fixedsys"), readonlybackground="#E9E9ED", foreground="#E09D00")
green_points = Spinbox(entry_frame, from_=0, to=100, increment=1, wrap=YES, state="readonly", font=("Fixedsys"), readonlybackground="#E9E9ED", foreground="#1C9C76")

# using geometry manager to arange input widgets because we cant use .grid() on them directly because they are needed as variables
name_entry.grid(column=1, row=0, columnspan=2, padx=2)
red_points.grid(column=1, row=2,columnspan=2)
blue_points.grid(column=1, row=3,columnspan=2)
yellow_points.grid(column=1, row=4,columnspan=2)
green_points.grid(column=1, row=5,columnspan=2)

#--Leader board--##
Label(lead_frame, text="Leaderboard", font=("Fixedsys", 15), background="#D2D4DA").grid(column=0, row=0, columnspan=2, pady=10)
Label(lead_frame, text="Pohutukawa ", font=("Fixedsys", 11), background="#FA6C38").grid(column=0, row=1, sticky=W, pady=5)
Label(lead_frame, text="Kauri      ", font=("Fixedsys", 11), background="#62A8F9").grid(column=0, row=2, sticky=W, pady=5)
Label(lead_frame, text="Kowhai     ", font=("Fixedsys", 11), background="#FFBC1F").grid(column=0, row=3, sticky=W, pady=5)
Label(lead_frame, text="Rimu       ", font=("Fixedsys", 11), background="#01F472").grid(column=0, row=4, sticky=W, pady=5)
Label(lead_frame, text= sum(ph_list), font=("Fixedsys", 12), background="#FA6C38").grid(column=1, row=1, sticky=W, pady=5, padx= 3)
Label(lead_frame, text= sum(ku_list), font=("Fixedsys", 12), background="#62A8F9").grid(column=1, row=2, sticky=W, pady=5, padx= 3)
Label(lead_frame, text= sum(kw_list), font=("Fixedsys", 12), background="#FFBC1F").grid(column=1, row=3, sticky=W, pady=5, padx= 3)
Label(lead_frame, text= sum(ru_list), font=("Fixedsys", 12), background="#01F472").grid(column=1, row=4, sticky=W, pady=5, padx= 3)

#-----------Class using which I will create my house event objects-----------#
class HouseEvent:
    def __init__(self, name, eventtype, ph_points, ku_points, kw_points, ru_points, who_won):
        self.name = name
        self.eventtype = eventtype
        self.ph_points = ph_points
        self.ku_points = ku_points
        self.kw_points = kw_points
        self.ru_points = ru_points
        self.who_won = who_won
        
    def get_info(self):
        return(["Name : " + self.name, "Is a sport : " + self.eventtype, "Pohutukawa Points : " + str(self.ph_points), "Kauri Points : " + str(self.ku_points), "Kowhai Points : " + str(self.kw_points), "Rimu Points : " + str(self.ru_points), "Winner : " + self.who_won])

#--Pre made house events--#
All_events.append(HouseEvent("Lampada Games", "Yes", 75, 60, 72, 68, "Pohutukawa"))
All_events.append(HouseEvent("House Trivia", "No", 66, 68, 74, 73, "Kowhai"))
#----------------Drop down to select which events details need to be accessed----------------#
selected_event = tkinter.StringVar()
# Set the default value of the variable
selected_event.set("Select an event")
# Create the option menu widget and passing 
# the options_list and selected_event to it.
event_name_list_dropdown = tkinter.OptionMenu(det_frame, selected_event, *names_list)
event_name_list_dropdown.config(font=("Fixedsys", 12) , background="#D2D2DA", activebackground="#E9E9ED")
event_name_list_dropdown.grid(row=0, column=1)
#Updates leader board by packing latest  scores into leader board
def leaderboard_update():
    Label(lead_frame, text= sum(ph_list), font=("Fixedsys", 12), background="#FA6C38").grid(column=1, row=1, sticky=W)
    Label(lead_frame, text= sum(ku_list), font=("Fixedsys", 12), background="#62A8F9").grid(column=1, row=2, sticky=W)
    Label(lead_frame, text= sum(kw_list), font=("Fixedsys", 12), background="#FFBC1F").grid(column=1, row=3, sticky=W)
    Label(lead_frame, text= sum(ru_list), font=("Fixedsys", 12), background="#01F472").grid(column=1, row=4, sticky=W)


#Function that takes the users input and uses the class constructor the make an object and then append it to the list we created above
def save_event_function(): 
    #Using global here because I need the option menu and stringVar to be accessible by other functions like the the show_event_details function which needs to destroy  these elements to prevent stacking.
    global selected_event
    global event_name_list_dropdown
    name = name_entry.get()
    event_type = is_sport.get()
    points_ph = int(red_points.get())
    points_ku = int(blue_points.get())
    points_kw = int(yellow_points.get())
    points_ru = int(green_points.get())
    #validating name input
    if name.strip() != "" and name not in names_list and len(name) <= 15:
        #Sorting Scores
        points_list = [('Pohutukawa', points_ph), ('Kauri', points_ku),("Kowhai", points_kw), ('Rimu', points_ru)]
        points_list.sort(reverse=YES, key = lambda x: x[1])
        #Validating Points input
        if points_ph == 0 and points_ku == 0 and points_kw == 0 and points_ru == 0:
            messagebox.showerror("Points Error", "Please enter points")
        else:
            names_list.append(str(name))  
            #These checks are used in the function to compare adjacent values in the sorted list to see if they are the same for the purpose of finding winners that are tied since we can have upto 4 tied teams we have to check upto 3 times to find all the possible tied winners  
            first_check = None
            second_check = None
            third_check = None
            
            if points_list[0][1] == points_list[1][1]:
                first_check = True
                if points_list[1][1] == points_list[2][1]:
                    second_check = True
                    if points_list[2][1] == points_list[3][1]:
                        third_check = True
                    else:
                        third_check = False
                else:
                    second_check = False   
            else:
                first_check = False
                second_check = False
                third_check = False
            #Setting the winner variable by first finding out if there are multiple winners and then setting the winner as the singular or multiple winners found
            if points_list[0][1] != 0:
                    
                if first_check == True:
                    if second_check == True:
                        if third_check == True:
                            winners = "All teams tied"
                        else:
                            winners = points_list[0][0] +", "+ points_list[1][0] + ", " + points_list[2][0]
                    else:
                        winners = points_list[0][0]+", "+ points_list[1][0]
                else:
                    winners = points_list[0][0]
            else:
                winners = 0

            #Creating the House event object and appending it to a list for it to be stored in memory
            All_events.append(HouseEvent(name, event_type, points_ph, points_ku, points_kw, points_ru, winners))

            #Adding scores to house points list for leader board
            ph_list.append(points_ph)
            ku_list.append(points_ku)
            kw_list.append(points_kw)
            ru_list.append(points_ru)
            #Running the function that puts updated scores on the leader board
            leaderboard_update()

            #Destroying previous option menu so that when we add a new one with the updated list there is no overlap
            event_name_list_dropdown.destroy() 
            #selected_event is a StringVar for event_name_list_dropdown so that whatever option is selected can be pulled by other functions
            selected_event = tkinter.StringVar()
            selected_event.set("Select an event")
            #This option menu has to be put in because the one that is there previously will now be missing an event
            event_name_list_dropdown = tkinter.OptionMenu(det_frame, selected_event, *names_list)
            event_name_list_dropdown.config(font=("Fixedsys", 12), background="#D2D2DA", activebackground="#E9E9ED")
            event_name_list_dropdown.grid(row=0, column=1)
    #Error messages if the data is not valid
    elif name in names_list:
        messagebox.showwarning("Name Error", "An event with this name already exists please chose another name")
    elif name.strip() == "":    
       messagebox.showwarning("Name Error", "You must enter a name for the event")
    elif len(name) > 15:
       messagebox.showwarning("Name Error", "Your name is too long it must be 15 characters only")

#Function for showing event details. It takes the string var from the option menu then uses a class function get_info() to pull information from the desired object and show it in an infobox 
def show_details_function():
    entry = selected_event.get()
    for info in All_events:
        if entry == info.name:
            global event_name_list_dropdown
            event_name_list_dropdown.destroy()
            event_name_list_dropdown = tkinter.OptionMenu(det_frame, selected_event, *names_list)
            event_name_list_dropdown.grid(row=0, column=1)
            event_name_list_dropdown.config(font=("Fixedsys", 12), background="#D2D2DA", activebackground="#E9E9ED")
            tkinter.messagebox.showinfo("Event Details", "\n".join(info.get_info()))

#button for saving event it calls the save_event_function function and creates each event as an object
tk.Button(entry_frame, text="Save Event", command=save_event_function, font=("Fixedsys", 12), background="#C7C7D1", activebackground="#E9E9ED").grid(row=7, column=0,columnspan=3, pady=5)
#Button for showing details it calls the show_details_function which shows a info box with information. Refer to the comments for the show_details_function() for more details on how that works
tk.Button(det_frame, text="Show Details", command=show_details_function, font=("Fixedsys", 12), background="#C7C7D1", activebackground="#E9E9ED").grid(column=0, row=1, columnspan=2)

main.mainloop()