# PROGRAMMER: Ohaedoghasi Olisanonso
# DATE CREATED: October 7, 2019                                 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    
    filename_list = listdir(image_dir)
    results_dic = dict()
    pet_names = []
    
    for i in range(len(filename_list)):
        if filename_list[i][0] != '.':
            pet_label1 = filename_list[i].strip('.jpg').lower().split('_')
            pet_name = ''

            for word in pet_label1:
                if word.isalpha():
                    pet_name += word + ' '
            pet_name = pet_name.strip()
            #pet_names.append(pet_name)


            if filename_list[i] not in results_dic:
                results_dic[filename_list[i]] = [pet_name]

    return results_dic
   
   