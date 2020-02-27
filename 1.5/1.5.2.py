from tkinter import * # Don't import like this except for Tkinter


root = Tk() # Create main window
# Make and place a Canvas widget for events and drawing
canvas = Canvas(root, height=600, width=600, relief=RAISED, bg='#3d3d3d')
canvas.grid() # Puts the canvas in the main Tk window

canopy = canvas.create_arc(0, 50, 600, 650, start=30, extent=120, width=50, style=ARC, outline='#c814ff')

canopySecondary = canvas.create_arc(
    30,  100, 
    570, 720,
    start=30,extent=120, width=25, style=ARC, 
    outline='#c814ff')
face = canvas.create_oval(150, 300, 450, 600, fill='gray')

checkbox = canvas.create_rectangle(60, 270, 160, 370, dash=[1,4], outline='#f0f0f0')
# check = canvas.create_line(100, 250, 150, 300, 220, 150, fill='red', width=20)
crossA = canvas.create_line(60, 270, 160, 370, fill='red', width=20)
crossB = canvas.create_line(160, 270, 60, 370, fill='red', width=20)

message = canvas.create_text(380, 295, text='This is not a meme', font=('Impact', -50), fill='#f0f0f0')
message2 = canvas.create_text(380, 345, text='Give me your money', font=('Impact', -50), fill='#f0f0f0')
# shadow = canvas.create_oval(100,490,500,590, fill='#888888', outline='#888888')
# Make an array of objects on the canvas
circles=[]
for r in range(10, 50, 10): 
    circles.append(canvas.create_oval(375-r, 440-r, 375+r, 440+r, outline='red'))
    circles.append(canvas.create_oval(225-r, 440-r, 225+r, 440+r, outline='red'))


canopy = canvas.create_arc(
    215, 400, 
    385, 550, 
    start=210, extent=120, width=10, style=ARC, 
    outline='red')

# Make one more object on the canvas

# Enter event loop. This displays the GUI and starts listening for events.
# The program ends when you close the window.
root.mainloop()
