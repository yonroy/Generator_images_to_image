import os


def image_path(root_path):
   # list files in img directory
   files = os.listdir(root_path)
   img_paths = []
   for file in files:
       # make sure file is an image
       if file.endswith(('.jpg', '.png', 'jpeg')):
           img_path = root_path + file
           img_paths.append(img_path)
   return img_paths

if __name__ == '__main__':
   root_path = "./image/"
   img_paths = image_path(root_path)
   for i in img_paths:
      print(i)