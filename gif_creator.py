import imageio, os, time
import matplotlib.pyplot as plt
from pygifsicle import optimize

path = os.getcwd()
frames_path = path + "\\gif_pics"

def gif_generator(gif_path):
    global path, frames_path
    writer = imageio.get_writer(gif_path, mode= 'I')
    for folder, sub_folder, files in os.walk(frames_path):
        for f in files:
            pic_path = frames_path + "\\" + f
            print(pic_path)
            writer.append_data(imageio.imread(pic_path))

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