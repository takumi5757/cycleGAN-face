import numpy as np
import cv2
import os
import glob
import shutil
import argparse


def set_images(in_dir):
    """collect_image.pyで集めたデータをひとつ上のディレクトリにまとめて展開する
    Args:
    :
    Return:
    :
    """
    folders = os.listdir(in_dir)
    for i, dir_ in enumerate(folders):
        img_list = glob.glob(in_dir + dir_ + "/*.jpg")
        for ind, img in enumerate(img_list):
            shutil.move(img, in_dir + f"{i}_{ind}.jpg")

    img_list = glob.glob(in_dir + "*.jpg")

    return img_list


def crop_face(img_list, out_dir):
    for img in img_list:
        image = cv2.imread(img)
        if image is None:
            print("Not open:")
            continue
        image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_alt.xml")
        face_list = cascade.detectMultiScale(
            image_gs, scaleFactor=1.1, minNeighbors=2, minSize=(128, 128)
        )

        count = 0
        if len(face_list) > 0:
            for rect in face_list:
                count += 1
                x, y, width, height = rect
                print(x, y, width, height)
                image_face = image[y : y + height, x : x + width]
                if image_face.shape[0] < 64:
                    print("face.shape < 64")
                image_face = cv2.resize(image_face, (128, 128))
                fileName = os.path.join(
                    out_dir
                    + str(img.split("/")[-1].split(".")[0])
                    + "_"
                    + str(count)
                    + ".jpg"
                )
                print(fileName)
                cv2.imwrite(str(fileName), image_face)
        else:
            print("no face")
            continue


if __name__ == "__main__":
    """
    in_dir = "./data/input/"
    out_dir = "./data/face/"
    """
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    parser.add_argument("-i", "--in_dir", help="input_dir", type=str, required=True)
    parser.add_argument("-o", "--out_dir", help="output_dir", type=str, required=True)

    args = parser.parse_args()

    in_dir = args.in_dir
    out_dir = args.out_dir

    os.makedirs(out_dir, exist_ok=True)

    img_list = set_images(in_dir)

    crop_face(img_list, out_dir)
