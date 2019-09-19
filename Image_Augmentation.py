import os
import cv2
import shutil

'''
All augmentation type:
Horizontal Flip, Vertical Flip, Change Channel

# ** Do all augmentation.
DataAugmentation(original_path = 'D:\\data')

# ** Do Horizontal Flip.
DataAugmentation(original_path = 'D:\\data',
                 augmentation_type = 'hflip')

# ** Do Vertical Flip.
DataAugmentation(original_path = 'D:\\data',
                 augmentation_type = 'vflip')

# ** Change RGB from BGR to BRG, RGB, RBG, GRB, and GBR image.
# if only RGB and RBG:
DataAugmentation(original_path = 'D:\\data',
                 augmentation_type = 'changeRGB',
                 object_type = ['rgb', 'rbg'])
# if all:
DataAugmentation(original_path = 'D:\\data',
                 augmentation_type = 'changeRGB')
'''

class DataAugmentation(object):
    def __init__(self, original_path = '', augmentation_type = None, object_type = []):
        if original_path == '':
            print('Do not find the path!')
            os._exit(0)
        elif not os.path.isdir(original_path):
            print('Do not find the path!')
            os._exit(0)
    
        save_path = original_path + '_augmentation'
        try:
            os.mkdir(save_path)
        except:
            shutil.rmtree(save_path)
            os.mkdir(save_path)

        if augmentation_type == None:
            print('Do all augmentation!')
            self.horizontal_flip(original_path, save_path)
            self.vertical_flip(original_path, save_path)
            self.changeRGB(original_path, save_path, object_type)
        elif 'hflip' in augmentation_type:
            self.horizontal_flip(original_path, save_path)
        elif 'vflip' in augmentation_type:
            self.vertical_flip(original_path, save_path)
        elif 'changeRGB' in augmentation_type:
            self.changeRGB(original_path, save_path, object_type)
        else:
            print('**error type!')

    def horizontal_flip(self, original_path, save_path):
        for folder_name in os.listdir(original_path):
            flip_folder_path = os.path.join(save_path, folder_name + '_hflip')
            os.mkdir(flip_folder_path)

            for file_name in os.listdir(os.path.join(original_path, folder_name)):
                image = cv2.imread(os.path.join(original_path, folder_name, file_name))
                hflip_image = cv2.flip(image, 1)
                cv2.imwrite(os.path.join(flip_folder_path, file_name[:-4] + '_hflip.jpg'), hflip_image)
        print('Finish horizontal flip~')

    def vertical_flip(self, original_path, save_path):
        for folder_name in os.listdir(original_path):
            flip_folder_path = os.path.join(save_path, folder_name + '_vflip')
            os.mkdir(flip_folder_path)

            for file_name in os.listdir(os.path.join(original_path, folder_name)):
                image = cv2.imread(os.path.join(original_path, folder_name, file_name))
                vflip_image = cv2.flip(image, 0)
                cv2.imwrite(os.path.join(flip_folder_path, file_name[:-4] + '_vflip.jpg'), vflip_image)
        print('Finish vertical flip~')

    def changeRGB(self, original_path, save_path, object_type):
        if object_type:
            for obj in object_type:
                for folder_name in os.listdir(original_path):
                    os.mkdir(os.path.join(save_path, folder_name + '_' + obj))

            for folder_name in os.listdir(original_path):
                for file_name in os.listdir(os.path.join(original_path, folder_name)):
                    image = cv2.imread(os.path.join(original_path, folder_name, file_name))
                    b, g, r = cv2.split(image)

                    if 'BRG' in object_type:
                        changeRGB_image = cv2.merge([b, r, g])
                        cv2.imwrite(os.path.join(save_path, folder_name + '_BRG', file_name[:-4] + '_BRG.jpg'), changeRGB_image)
                    elif 'RGB' in object_type:
                        changeRGB_image = cv2.merge([r, g, b])
                        cv2.imwrite(os.path.join(save_path, folder_name + '_RGB', file_name[:-4] + '_RGB.jpg'), changeRGB_image)
                    elif 'RBG' in object_type:
                        changeRGB_image = cv2.merge([r, b, g])
                        cv2.imwrite(os.path.join(save_path, folder_name + '_RBG', file_name[:-4] + '_RBG.jpg'), changeRGB_image)
                    elif 'GRB' in object_type:
                        changeRGB_image = cv2.merge([g, r, b])
                        cv2.imwrite(os.path.join(save_path, folder_name + '_GRB', file_name[:-4] + '_GRB.jpg'), changeRGB_image)
                    elif 'GBR' in object_type:
                        changeRGB_image = cv2.merge([g, b, r])
                        cv2.imwrite(os.path.join(save_path, folder_name + '_GBR', file_name[:-4] + '_GBR.jpg'), changeRGB_image)
        else:
            for folder_name in os.listdir(original_path):
                os.mkdir(os.path.join(save_path, folder_name + '_BRG'))
                os.mkdir(os.path.join(save_path, folder_name + '_RGB')) 
                os.mkdir(os.path.join(save_path, folder_name + '_RBG')) 
                os.mkdir(os.path.join(save_path, folder_name + '_GRB')) 
                os.mkdir(os.path.join(save_path, folder_name + '_GBR'))
            
            for folder_name in os.listdir(original_path):
                for file_name in os.listdir(os.path.join(original_path, folder_name)):
                    image = cv2.imread(os.path.join(original_path, folder_name, file_name))
                    b, g, r = cv2.split(image)

                    BRG_image = cv2.merge([b, r, g])
                    cv2.imwrite(os.path.join(save_path, folder_name + '_BRG', file_name[:-4] + '_BRG.jpg'), BRG_image)
                    
                    RGB_image = cv2.merge([r, g, b])
                    cv2.imwrite(os.path.join(save_path, folder_name + '_RGB', file_name[:-4] + '_RGB.jpg'), RGB_image)
                
                    RBG_image = cv2.merge([r, b, g])
                    cv2.imwrite(os.path.join(save_path, folder_name + '_RBG', file_name[:-4] + '_RBG.jpg'), RBG_image)
                
                    GRB_image = cv2.merge([g, r, b])
                    cv2.imwrite(os.path.join(save_path, folder_name + '_GRB', file_name[:-4] + '_GRB.jpg'), GRB_image)
                
                    GBR_image = cv2.merge([g, b, r])
                    cv2.imwrite(os.path.join(save_path, folder_name + '_GBR', file_name[:-4] + '_GBR.jpg'), GBR_image)
        print('Finish change RGB~')
