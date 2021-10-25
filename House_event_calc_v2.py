
import tkinter
from tkinter import *

tk = tkinter
main = Tk()  # Name of window in my code
main.title("House event calculator")  # Title
main.geometry("600x300")  # How big the window opens
main.minsize(100, 400)  # How small the window can be made
main.configure(bg="grey")  # Background colour


# anchor the .packs     

All_events = [] #list in which I will hold my HouseEvent object


is_sport_list= ["sport", "other"]

all_events_name = []
 
#----all visual elements that will be on the tkinter----#

heading = tk.Label(main, text="Name of Event")
entry_1 = tk.Entry(main)


lable_1 = tk.Label(main, text="Is it a sport")

is_sport = tk.StringVar()
is_sport.set(is_sport_list[0])
entry_2 = OptionMenu(main, is_sport, *is_sport_list)


lable_2 = tk.Label(main, text="Pohutukawa")

spin_1 = Spinbox(main ,from_=0, to=100, increment=1, wrap=YES, state="readonly")


lable_3 = tk.Label(main, text="Kauri")

spin_2 = Spinbox(main ,from_=0, to=100, increment=1, wrap=YES, state="readonly")


lable_4 = tk.Label(main, text="Kowhai")

spin_3 = Spinbox(main ,from_=0, to=100, increment=1, wrap=YES, state="readonly")


lable_5 = tk.Label(main, text="Rimu")

spin_4 = Spinbox(main ,from_=0, to=100, increment=1, wrap=YES, state="readonly")


lable_6 = tk.Label(main, text="Enter house event name for details")

random_var=tk.StringVar()
entry_7 = tk.Entry(main, textvariable=random_var)

#using geometry manager to arange all the widgets

heading.grid(column=0, row=0)
lable_1.grid(column=0, row=1)
lable_2.grid(column=0, row=2)
lable_3.grid(column=0, row=3)
lable_4.grid(column=0, row=4)
lable_5.grid(column=0, row=5)
lable_6.grid(column=0, row=6)

entry_1.grid(column=1, row=0,)
entry_2.grid(column=1, row=1,)
spin_1.grid(column=1, row=2,)
spin_2.grid(column=1, row=3,)
spin_3.grid(column=1, row=4,)
spin_4.grid(column=1, row=5,)
entry_7.grid(column=1, row=6,)



#defining the class using which I will create my house event objects


class HouseEvent:
    def __init__(self, name, eventtype, ph_points, ku_points, kw_points, ru_points):
        self.name = name
        self.eventtype = eventtype
        self.ph_points = ph_points
        self.ku_points = ku_points
        self.kw_points = kw_points
        self.ru_points = ru_points
        
    def PrintObj(self):
        return(self.name, self.eventtype, self.ph_points, self.ku_points, self.kw_points, self.ru_points)




#Function that takes the users input and uses the class constructor the make an object and then append it to the list we created above

def MakeObj():
    #getting all the entries and asigning them as variable to use as attributes in the constructor
    name = entry_1.get()
    event_type = is_sport.get()
    points_ph = spin_1.get()
    points_ku = spin_2.get()
    points_kw = spin_3.get()
    points_ru = spin_4.get()
    #getting all points and sorting them for setting the winner attribute
    points_list = [('Pohutukawa', points_ph), ('Kauri', points_ku),("Kowhai", points_kw), ('Rimu', points_ru)]
    print(points_list)
    points_list.sort(key = lambda x: x[1])
    print(points_list)
    
    #using the variables from above and using them as a 
    All_events.append(HouseEvent(name, event_type, points_ph, points_ku, points_kw, points_ru))
    all_events_name.append(name)
    # print(all_events_name)


#Function I used as a diagnostics tool 
# to test if my objects are being saved correctly and if I can access them 
def ShowObjects():
    for i in All_events:
        print (i.name)
        print(i.eventtype, i.ph_points, i.ku_points, i.kw_points, i.ru_points)    


def print_my_name():
    entry = random_var.get()
    for variable in All_events:
        if entry == variable.name:
            print(variable.PrintObj())


def pack_func():
    entry = random_var.get()
    for variable in All_events:
        if entry == variable.name:
            tk.Label(main, text=variable.PrintObj()).grid(column=3, row=0)
            print(variable.PrintObj())

tk.Button(main, text="Make Obj", command=MakeObj).grid(column=3, row=1)

# tk.Button(main, text="Show Object", command=ShowObjects).pack()

# tk.Button(main, text="Print object attributes", command=print_my_name).pack()

tk.Button(main, text="Show Details", command=pack_func).grid(column=3, row=2)

main.mainloop()



# #code for deciding who won for this event 
# points_list = []
# points_list.append(points_ph)
# points_list.append(points_ku)
# points_list.append(points_kw)
# points_list.append(points_ru)
# print(points_list)

# max_points = max(points_list)
# print(max_points)
# winner_indecies = [i for i,j in enumerate(max_points) if j == max_points]
# print(winner_indecies)