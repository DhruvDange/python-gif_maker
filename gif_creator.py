import imageio, os, time
import matplotlib.pyplot as plt
from pygifsicle import optimize

path = os.getcwd()
frames_path = path + "\\gif_pics"
frames = []
duration = 0.2

def gif_generator(gif_path):
    global path, frames_path, frames
    for folder, sub_folder, files in os.walk(frames_path):
        for f in files:
            pic_path = frames_path + "\\" + f
            print(pic_path)
            frames.append(imageio.imread(pic_path))
    dur = float(input("Enter duration for each frame (seconds): "))
    print("Processing...please wait")
    imageio.mimsave(gif_path, frames, 'GIF', duration = dur)
    print("Success!")

def welcome_page():
    global name
    print("Welcome to gif maker!")
    time.sleep(0.5)
    print("Please place your pictures in a folder titled \"gif_pics\" \n and place it in the same folder with this file.")
    input("Press any key to continue...")
    print("Please make sure your pictures are in the same order as you'd like to see in the gif.")
    time.sleep(1)
    name = input("Please enter the name for gif file (exclude .gif): ")
    input("Press any key to create gif...")
    name = name + ".gif"
    gif_generator(name)

welcome_page()
optimize(name)