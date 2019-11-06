#Group 3 Spotify News
#Put Names/ Student Numbers here

#Import modules

import tkinter as tk

##Create window

root = tk.Tk()
root.title("Spotify News Suggestor")
root.geometry("700x500")

#Create Frame for widgets
rootFrame = tk.Frame(root)
rootFrame.pack()

#Title Frame
titleFrame = tk.Frame(rootFrame)
titleFrame.pack()

#Banner Text
banner = tk.Label(titleFrame, text="Spotify News Suggestor", font = "Tahoma")
banner.pack()

#Get Song Function

def getSong():
    print("Song Chosen!")




#Get song Button

songButton = tk.Button(rootFrame, text="Get Song!", font= "Tahoma", command= getSong)
songButton.pack()



#Call tk window mainloop
root.mainloop()
