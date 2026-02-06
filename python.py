# Source - https://codereview.stackexchange.com/q
# Posted by PythonConnaseur, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-12, License - CC BY-SA 4.0

from tkinter import *
click_times = 0
def click():
    global click_times
    click_times += 1
    clicks.set("Clicks: " + str(click_times))
root = Tk()
clicks = StringVar()
numClicks = Label(root, textvariable=clicks)
clicks.set("You clicked 0 times")

clicker = Button(root, text="Click me", command=click)
clicker.pack()
numClicks.pack()
mainloop()



         

    
