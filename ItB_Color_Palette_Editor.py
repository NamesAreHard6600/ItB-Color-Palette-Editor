import _tkinter
from tkinter import *
from tkinter.colorchooser import askcolor
from functools import partial # Required for a replacement to lambda, to pass functions with parameters in buttons
import copy
import time
from os.path import exists
from PIL import Image #Requires Install

true = True
false = False
#Read the README for detail
#Constants you can change
IMAGE_FILE_NAME = "Example.png" # The file name of your image. Make sure it's in the same folder
PIXEL_SIZE = 4 # This is the scale: One pixel equals a 4x4 pixel, you can change this and note that
# The window CAN be resized
IDENTIFY_COLOR = "#fc03e3" # Pink Default, but if you want a different identify color, set it here

SAVE_FILE_NAME = "Example.png" # False

# Starting/Your Palette, is currently my mod, Nuclear Nightmares, palette
your_palette = {
  "PlateHighlight": ( 35, 248, 255),
	"PlateLight":     (221, 188,  65),
	"PlateMid":       (159, 128,  62),
	"PlateDark":      ( 74,  64,  53),
	"PlateOutline":   ( 15,  22,  16),
	"PlateShadow":    ( 69,  74,  57),
	"BodyColor":      (109, 109,  94),
  "BodyHighlight":  (152, 153, 131),
}

# EVERYTHING BELOW THIS SHOULDN'T NEED ANY CHANGES. But you can if you want to.

# Don't Edit, this is Rift Walkers. If you edit it this, a proper mech image with the proper
# palette will not properly initialize. I hope that makes sense. Just best to not edit this
base_palette = {
  "PlateHighlight": (221, 141, 140),
  "PlateLight":     (136, 126,  68),
  "PlateMid":       ( 63,  75,  50),
  "PlateDark":      ( 29,  40,  31),
  "PlateOutline":   ( 15,  22,  16),
  "PlateShadow":    ( 34,  36,  34),
  "BodyColor":      ( 67,  72,  68),
  "BodyHighlight":  (134, 146, 120),
}

new_palette = copy.copy(your_palette)

def calculateBrightness(rgb):
  # print(rgb, (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]))
  return (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2])

def save(dict):
  """Saves, by printing the given palette dictionary as a copy paste version of what the code would look lik
  Python and Lua, despite the name

  :param dict: the palette to print
  :type dict: dictionary
  """
  # Saving Palette
  global key_array, new_palette, SAVE_FILE_NAME, IMAGE_FILE_NAME
  with open("output.txt", "a") as f:
    print(time.ctime() + "\n")
    f.write(time.ctime() + "\n\n")
    print("Lua Code:\n")
    f.write("Lua Code:\n\n")
    for key, value in dict.items():
      print(f'"{key}" = {{{value[0]}, {value[1]}, {value[2]}}},')
      f.write(f'"{key}" = {{{value[0]}, {value[1]}, {value[2]}}},\n')
    print("\nEnd Lua Code\nPython Code:\n")
    f.write("\nEnd Lua Code\nPython Code:\n\n")
    for key, value in dict.items():
      print(f'"{key}": ({value[0]}, {value[1]}, {value[2]}),')
      f.write(f'"{key}": ({value[0]}, {value[1]}, {value[2]}),\n')
    print("\nEnd Python Code")
    f.write("\nEnd Python Code\n")

    # Saving Image
    if SAVE_FILE_NAME: # If you want to save the image
      print("Saving Image...")
      f.write("Saving Image...\n")
      tempSaveName = SAVE_FILE_NAME.split(".") #This got messy fast...
      save_count = 0
      while exists("saved\\" + tempSaveName[0] + "_" + str(save_count) + "." + tempSaveName[1]):
        save_count += 1
      tempSaveName = "saved\\" + tempSaveName[0] + "_" + str(save_count) + "." + tempSaveName[1]

      im = Image.open(IMAGE_FILE_NAME, mode='r')
      size = im.size
      for x in range(size[0]):
        for y in range(size[1]):
          key = key_array[x][y]
          if key != None:
            im.putpixel((x,y),new_palette[key])
      im.save(tempSaveName)
      print(f"Image Saved Named: {tempSaveName}")
      f.write(f"Image Saved Named: {tempSaveName}\n")
    print("\n\n")
    f.write("\n\n")

def resetToOriginal():
  """Resets the image to the original color palette
  """
  global new_palette, your_palette, c
  x = 0
  y = 0
  for rect in c.find_all():  # It always finds them in the order made, but I have to make a fake nested for loop
    key = key_array[x][y]
    if key != None:
      try:
        c.itemconfig(rect, fill=rgbToHex(your_palette[key]), outline=rgbToHex(your_palette[key]))
      except _tkinter.TclError:  # Supress Improper Color Error
        pass
    y = (y + 1) % (size[1])
    if y == 0:
      x += 1

  new_palette = copy.copy(your_palette)
  count = 0
  for key, value in your_palette.items():
    e1 = entryArray[count * 3]
    e2 = entryArray[count * 3 + 1]
    e3 = entryArray[count * 3 + 2]
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e1.insert(0, f"{value[0]}")
    e2.insert(0, f"{value[1]}")
    e3.insert(0, f"{value[2]}")
    count += 1

def resetToDefault():
  """Resets the image to the defualt/base color palette
  """
  global c, base_palette, new_palette
  x = 0
  y = 0
  for rect in c.find_all():  # It always finds them in the order made, but I have to make a fake nested for loop
    key = key_array[x][y]
    if key != None:
      try:
        c.itemconfig(rect, fill=rgbToHex(base_palette[key]), outline=rgbToHex(base_palette[key]))
      except _tkinter.TclError:  # Supress Improper Color Error
        pass
    y = (y + 1) % (size[1])
    if y == 0:
      x += 1
  new_palette = copy.copy(base_palette)
  count = 0
  for key, value in base_palette.items():
    e1 = entryArray[count * 3]
    e2 = entryArray[count * 3 + 1]
    e3 = entryArray[count * 3 + 2]
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e1.insert(0, f"{value[0]}")
    e2.insert(0, f"{value[1]}")
    e3.insert(0, f"{value[2]}")
    count += 1

def callback(sv):
  """ Just a helper function for input changes
  """

  if len(entryArray) < 24: #When you add a fucntion call to an input, it runs it when it is created
    return
  changeCanvas()

def changeCanvas():
  """Changes the canvas to the new palette
  """
  global new_palette, c, size
  ret = False
  for e in entryArray:
    try:
      value = int(e.get())
      if value < 0 or value > 255:
        raise ValueError
      e.config({"background": "White"})
    except ValueError:
      e.config({"background": "Red"})
      ret = True
  if ret:
    return
  try:
    new_palette = {
      "PlateHighlight": (int(entryArray[0].get()), int(entryArray[1].get()), int(entryArray[2].get())),
      "PlateLight":     (int(entryArray[3].get()), int(entryArray[4].get()), int(entryArray[5].get())),
      "PlateMid":       (int(entryArray[6].get()), int(entryArray[7].get()), int(entryArray[8].get())),
      "PlateDark":      (int(entryArray[9].get()), int(entryArray[10].get()), int(entryArray[11].get())),
      "PlateOutline":   (int(entryArray[12].get()), int(entryArray[13].get()), int(entryArray[14].get())),
      "PlateShadow":    (int(entryArray[15].get()), int(entryArray[16].get()), int(entryArray[17].get())),
      "BodyColor":      (int(entryArray[18].get()), int(entryArray[19].get()), int(entryArray[20].get())),
      "BodyHighlight":  (int(entryArray[21].get()), int(entryArray[22].get()), int(entryArray[23].get())),
    }
  except ValueError: #Supress Improper Value Error
    pass
  x=0
  y=0
  for rect in c.find_all(): #It always finds them in the order made, but I have to make a fake nested for loop
    key = key_array[x][y]
    if key != None:
      try:
        c.itemconfig(rect, fill=rgbToHex(new_palette[key]), outline=rgbToHex(new_palette[key]))
      except _tkinter.TclError: #Supress Improper Color Error
        pass
    '''
    for key, value in your_palette.items():
      # print(value,color)
      if value == color:
        c.itemconfig(rect, fill=rgbToHex(new_palette[key]), outline=rgbToHex(new_palette[key]))
    '''
    y = (y + 1) % (size[1])
    if y == 0:
      x += 1

  #Change Identify Button Colors
  for key, value in identifyButtonDict.items():
    try:
      color = new_palette[key]

      brightness = calculateBrightness(color)
      if brightness < 255*.4:
        value.configure(bg=rgbToHex(color), fg="White")
      else:
        value.configure(bg=rgbToHex(color), fg="Black")
    except _tkinter.TclError: #Supress Improper Color Error
      pass

def identify(sKey):
  """Identifies the given key by changing it to the IDENTIFY_COLOR. If an invalid key is given,
  identify is reset.
  :param sKey: The key to _s_earch and identify
  :type sKey: String
  """
  global new_palette, IDENTIFY_COLOR
  x = 0
  y = 0
  # print(key_array)
  for rect in c.find_all():  # It always finds them in the order made, but I have to make a fake nested for loop
    # print(x, y)
    aKey = key_array[x][y] #akey stands for actual key

    if aKey == sKey:
      try:
        c.itemconfig(rect, fill=IDENTIFY_COLOR, outline=IDENTIFY_COLOR)
      except _tkinter.TclError:  # Supress Improper Color Error
        pass
    else:
      if aKey != None:
        try:
          c.itemconfig(rect, fill=rgbToHex(new_palette[aKey]), outline=rgbToHex(new_palette[aKey]))
        except _tkinter.TclError:  # Supress Improper Color Error
          pass
    '''
    for key, value in your_palette.items():
      # print(value,color)
      if value == color:
        c.itemconfig(rect, fill=rgbToHex(new_palette[key]), outline=rgbToHex(new_palette[key]))
    '''
    y = (y + 1) % (size[1])
    if y == 0:
      x += 1

def colorPicker(row):
  """Fills in a row to match the color of a color picker
  :param row: What row the color picker is for
  :type row: int
  """
  e1 = entryArray[row*3]
  e2 = entryArray[row * 3 + 1]
  e3 = entryArray[row * 3 + 2]
  colors = askcolor()
  if colors[0] != None:
    # print(colors)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e1.insert(0, f"{colors[0][0]}")
    e2.insert(0, f"{colors[0][1]}")
    e3.insert(0, f"{colors[0][2]}")
    changeCanvas()

def rgbToHex(rgb):
  """Converts a rgb color value to its hex equivalent

  :param rgb: the rgb value
  :type: tuple (r, g, b)
  :rtype: String
  :return: the hex value
  """
  return '#%02x%02x%02x' % rgb

def hexToRgb(hex):
  """Converts a hex color value to its rgb equivalent

    :param hex: the hex value
    :type: String
    :rtype: tuple (r, g, b)
    :return: the rgb value
    """
  hex = hex.lstrip('#')
  lv = len(hex)
  return tuple(int(hex[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def upPress(event):
  """Increments the focused entry by one when up is pressed
  """
  global win
  try:
    focus = win.focus_get()
    focus = win.nametowidget(focus)
    old = focus.get()
    focus.delete(0, END)
    focus.insert(0, str(int(old) + 1))
    changeCanvas()
  except AttributeError: #Supress "no focus" error
    pass

def downPress(event):
  """Decrements the focused entry by one when down is pressed
  """
  global win
  try:
    focus = win.focus_get()
    focus = win.nametowidget(focus)
    old = focus.get()
    focus.delete(0, END)
    focus.insert(0, str(int(old) - 1))
    changeCanvas()
  except AttributeError: #Supress "no focus" error
    pass


# Setting up the main window
win = Tk()
win.bind("<Up>",upPress)
win.bind("<Down>",downPress)
win.geometry("1028x456")


#Setting up the image
im = Image.open(IMAGE_FILE_NAME,mode='r')
size = im.size
# (size)
c = Canvas(win, width=im.size[0]*PIXEL_SIZE, height=im.size[1]*PIXEL_SIZE)
c.grid(row=0,column=4)

key_array=[[] for _ in range(size[0])] #key array is an array with the keys of all the pixels
# (len(key_array))
#Draw "pixels" (rectangles) on the canvas, so we can edit them
for x in range(size[0]):
  for y in range(size[1]):
    curr_pixel = im.getpixel((x,y))
    edited = False
    if curr_pixel[3] == 0:
      rect = c.create_rectangle(x * PIXEL_SIZE, y * PIXEL_SIZE, x * PIXEL_SIZE + PIXEL_SIZE,
                         y * PIXEL_SIZE + PIXEL_SIZE,
                         outline='#FFFFFF', fill='#FFFFFF'
                         )
      key_array[x].append(None)
      edited = True
    else:
      curr_pixel = curr_pixel[0: 3]
      for key, value in base_palette.items():
        if value == curr_pixel:
          color = your_palette[key]
          rect = c.create_rectangle(x * PIXEL_SIZE, y * PIXEL_SIZE, x * PIXEL_SIZE + PIXEL_SIZE, y * PIXEL_SIZE + PIXEL_SIZE,
                             outline=rgbToHex(color), fill=rgbToHex(color)
                             )
          key_array[x].append(key)
          edited = True
      if not edited:
        rect = c.create_rectangle(x * PIXEL_SIZE, y * PIXEL_SIZE, x * PIXEL_SIZE + PIXEL_SIZE,
                           y * PIXEL_SIZE + PIXEL_SIZE,
                           outline=rgbToHex(curr_pixel), fill=rgbToHex(curr_pixel)
                           )
        key_array[x].append(None)
# print(key_array)
# print(len(key_array[0]))
# print(key_array[0][32])

count = 1
entryArray = [] # A soon-to-be list of every entry (input box)
identifyButtonDict = {} #A dictionary of the identify buttons so I can change their colors
for key, value in your_palette.items(): #Creating lots of entries now
  Label(win, text=f"{key} Red: ").grid(row=count,column=1) #Labels
  Label(win, text=f"{key} Green: ").grid(row=count,column=3)
  Label(win, text=f"{key} Blue: ").grid(row=count,column=5)

  sv1 = StringVar() #This is what allows for the auto update
  sv1.trace("w", lambda name, index, mode, sv1=sv1: callback(sv1))
  e1 = Entry(win, textvariable=sv1)
  e1.insert(0,f"{value[0]}")
  e1.grid(row=count, column=2)

  sv2 = StringVar()
  sv2.trace("w", lambda name, index, mode, sv2=sv2: callback(sv2))
  e2 = Entry(win, textvariable=sv2)
  e2.insert(0,f"{value[1]}")
  e2.grid(row=count, column=4)

  sv3 = StringVar()
  sv3.trace("w", lambda name, index, mode, sv3=sv3: callback(sv3))
  e3 = Entry(win, textvariable=sv3)
  e3.insert(0,f"{value[2]}")
  e3.grid(row=count, column=6)

  entryArray.append(e1)
  entryArray.append(e2)
  entryArray.append(e3)

  b = Button(win, text="Color Picker", command=partial(colorPicker,count-1)) #Color picker button
  b.grid(row=count,column=7)

  # Identify Button
  color = your_palette[key]
  brightness = calculateBrightness(color)
  if brightness < 255 * .4:
    b = Button(win, text=f"Identify {key}", command=partial(identify, key), bg=rgbToHex(color), fg="White")
  else:
    b = Button(win, text=f"Identify {key}", command=partial(identify, key), bg=rgbToHex(color), fg="Black")
  b.grid(row=count, column=0)
  identifyButtonDict[key] = b
  count += 1
# print(entryArray)
# Straggling buttons
b = Button(win, text="Reset Identify", command = partial(identify, "Reset"))
b.grid(row=9,column=0)
b = Button(win, text="Reset to Original", command = resetToOriginal)
b.grid(row=9,column=3)
b = Button(win, text="Reset to Rift Walkers", command = resetToDefault)
b.grid(row=9,column=4)
b = Button(win, text="Save", command = partial(save, new_palette))
b.grid(row=9,column=6)
'''
b = Button(win, text="Change", command = changeCanvas)
b.grid(row=9,column=4)
'''

#Main loop
win.mainloop()
#Print when main loop closes
save(new_palette)