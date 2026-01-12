# Converts the videos to mp3 
import os 
import subprocess

files = os.listdir("Videos")
# print("total video:" ,len(files))
# print(files)
for file in files: 
    tutorial_number = file.split(" [")[0].split(" #")[1]
    # print(tutorial_number)
    file_name = file.split(" ] ")[0]
    print("processing:",file)

    # print( tutorial_number,  file_name)
    subprocess.run(["ffmpeg", "-y", "-i",  f"Videos/{file}", f"audios/{tutorial_number}_{file_name}.mp3"], check = True)
     
     