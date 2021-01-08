import os
import glob
import random
import shutil


def make_folders(img_list, dir_name):

    test_split = 0.9
    dir_ = path + dir_name
    if not os.path.isdir(dir_):
        os.mkdir(dir_)

    for i, img in enumerate(img_list):
        current_pos = float(i) / len(img_list)

        if current_pos < test_split:
            pass
        else:
            shutil.move(img, dir_ + "/" + img.split("/")[-1])


if __name__ == "__main__":
    imglist = glob.glob("./data/japanese2indian/indian_face" + "/*.jpg")
    random.shuffle(imglist)
    make_folders(imglist, "testB")
