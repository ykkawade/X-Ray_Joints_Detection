import os

source_folder = r'D:\CV\Data\Main\images\Original X-ray 48 month' + '\\'
target_folder = r'D:\CV\Change_txt_labels\Images' + '\\'

for path, dir, files in os.walk(source_folder):
    if files:
        for file in files:
            print(path)
            split = path.split("\\")
            print(split[6]+"_"+split[7])
            if not os.path.isfile(target_folder + file):
                os.rename(path + '\\' + file, target_folder + split[6]+"_"+split[7])
