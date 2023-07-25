import os
from PIL import Image
import shutil

directory = "D:\CV\Change_txt_labels\labels"
imageDirectory = "D:\CV\Change_txt_labels\Images2" + "\\"
count = 1

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        print(str(count) + "\t" + filename)
        imageFilename = filename.split(".")
        img = Image.open(imageDirectory + imageFilename[0] + ".png")
        width = img.width
        height = img.height
        count = count + 1
        file = open(os.path.join(directory, filename), "r+")
        read = file.readlines()
        file.seek(0)
        modified = []
        splitVal = []
        for line in read:
            if line == "q\n" or line == "sq\n" or line == "fq\n" or line == "fsq\n" or line == "\n":
                continue
            modified.append(line.strip())
        print(modified)
        file.truncate()
        for element in modified:
            splitVal = element.split()
            splitVal[0] = 0
            splitVal[1] = str(int(splitVal[1])/width)
            splitVal[2] = str(int(splitVal[2])/height)
            splitVal.remove(splitVal[3])
            splitVal.append("0.06")
            splitVal.append("0.06")
            element = splitVal
            for i in element:
                file.write(str(i) + " ")
            file.write("\n")

