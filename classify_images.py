# PROGRAMMER: Ohaedoghasi Olisanonso    
# DATE CREATED: October 8, 2019                                 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
##

# Imports classifier function for using CNN to classify images 
from classifier import classifier 
from get_pet_labels import get_pet_labels

def classify_images(images_dir, results_dic, model):
    
    for key in results_dic.keys():
        model_label = classifier(images_dir + key, model).lower().strip()
        
        truth = results_dic[key][0]
        
        if truth in model_label:
           results_dic[key].extend((model_label, 1))
        else:
           results_dic[key].extend((model_label, 0))
        
    
        
        
    
    
    
    return results_dic 
