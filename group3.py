#Group 3 Spotify News
#Put Names/ Student Numbers here

#Import modules

import tkinter as tk

##Create window

root = tk.Tk()
root.title("Spotify News Suggestor")

#Create Frame for widgets
rootFrame = tk.Frame(root)
rootFrame.pack()

#Title Frame
titleFrame = tk.Frame(rootFrame)
titleFrame.pack()

#Banner Text
banner = tk.Label(titleFrame, text="Spotify News Suggestor", font = "Tahoma")
banner.pack()



#Call tk windoew mainloop
root.mainloop()
