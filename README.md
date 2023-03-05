# Into the Breach Color Palette Editor 
Welcome to the Into the Breach Color Palette Editor! Here's some quick instructions on how to use this tool. \

*Author:* NamesAreHard 

*Version:* 1.0.1

## Booting the Editor:

1. The first step is downloading python 3 if you don't currently own it. Visit https://www.python.org/downloads/ and download either a. The latest python version, or b. Python 3.9, the version this was made in. It should work in newer versions, but if it doesn't you can always fall back. If you've worked with python before, this should be done already. 
2. The next step is to install dependencies. This does have a few things you need to install (actually only one!). So open the command line, and type this command:
    `pip install Pillow`
  That should install the only required dependency, allowing me to open images, which is kinda important, and the rest should have been downloaded with python
3. The third step is initializing your "settings" so to speak. You'll need to open 'ItB_Color_Palette_Editor.py' in the text editor of you choice. Everything is located at the top, here is what you should note. 
  - IMAGE_FILE_NAME is the file name. Change this to what your file is called, and make sure it is located in the same folder. Or name your file "Example.png" if you want.
  - PIXEL_SIZE is the scale of the image. Bigger number = bigger pixels. Feel free to have a bigger or smaller image depending on your liking. 
  - IDENTIFY_COLOR is the hex color that is used when using an identify color. It's set to pink, but if you're making a pink palette, or just want a different color, feel free to change it. 
  - SAVE_FILE_NAME is the file name you wannt it to save as. It can be the same as IMAGE_FILE_NAME. You can also set it to False, with no quotes, to not save the image, and just save the palette. DON'T FORGET THE FILE EXTENSION
  - Finally, your_palette is your starting palette. Inside, you'll see the 8 different colors, with rgb values. You can leave them as the defualt and edit from there (Nuclear Nightmares Yellow) or put it a starting palette you already have. You can also always reset to rift walkers in the editor if you wish. 
DON'T FORGET TO SAVE THESE CHANGES
5. Once you've changed these to your liking, open up a command line and navigate (using `cd`) to the folder containing the python script, and type:
python3 ItB_Color_Palette_Editor.py
This will open up the editor for you! And there you go, edit away. The window is resizable, so if things are cut off, resize the window to fit. If it won't fit, you'll need to shut it down and go edit PIXEL_SIZE.

## Using the Editor:

The Editor is pretty simple to use, but let's walk through all the buttons and boxes. You can also just try things if you're done reading. 

At the top is your image. It's not actually the image, but a recreation of it with a bunch of rectangles. It can't do opacity, sorry. 

On the left are identify buttons. They are colored as the color of the corresponding palette item, and clicking one will turn all of that palette item to pink (default) so you can see what they are. Pressing any other identify button, reset identify, or making a change to the palette will turn off that identify. 

In the middle are all the input boxes with the corresponding key label to its left. You can use arrow keys while focused on one of these boxes to increment/decrement. You can also just type in them. Any change to these boxes will automatically update the image. If a box turns red, it means there is an invalid number. It could have a letter, be greater than 255, or be empty. If a box is red, the image will no longer update, so you need to fix it before it will. 

On the right are color picker buttons. Clicking a color picker button will open a color picker that, once closed, will change the color of the corresponding row to that color, and update the image. The image will not update as you change the color picker, it will only update once it closes. 

At the bottom are the final three buttons. One resets to the originial palette you had when the program first booted up. The other resets to the rift walkers default. Both of these button will lose you all of your progress, so don't press these buttons unless you're sure you don't like what you have, or haven't saved what you do like. 

Finally, the save button will print out your palette in Python and Lua code out to the command line and in a file named output.txt in the same directory as the python script, as well as save an image of the mech. (more below)


## Shutting Down the Editor:

Once you've finished, close the window, but don't close the command line. Closing the window will autosave once, and Lua code and Python code will be output in the command line and saved in output.txt, so you can copy and paste to save your work, just like how it would work if you clicked the save button. Either copy and paste the python code back in to save for later, copy and paste the lua code into your init.lua, or just copy either one and save it somewhere safe, it outlines each color with their RGB values. The output.txt will have time stamps, but it can get big fast, since it always appends, so you might want to delete occasionally, as long as there's nothing important. The code will recreate the file. If you are saving images as well (SAVE_FILE_NAME is set to True), they will go into the saved folder. It's suggested to delete these too when you're done with them, because it also might get big fast.

Note: A picture/screenshot before shutting things down will guarantee you don't lose anything (in case there is some bizare error) if you'd like to really make sure. 


If you have any questions (which you might, I don't write README's like this) about how to use this, ping me @NamesAreHard#2501 on the ItB discord! I'd love to make improvements and help you out. I hope this helps! And good luck "palette"ing. 

#### TO DO LIST:
This is a list (for me) of things that could still be done to make this an easier process. 
Change your_palette to be read from a file so that it's easier to edit
Left and right up and down 10?
