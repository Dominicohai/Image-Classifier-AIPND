# PROGRAMMER: Ohaedoghasi Olisanonso
# DATE CREATED: October 9, 2019                                 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file.
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 


from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classifier import classifier 
from classify_images import classify_images

def adjust_results4_isadog(results_dic, dogfile): 
    dognames_dic = {}
    
    with open(dogfile, 'r') as f:
        for line in f:       
                dognames_dic[line.rstrip()] = 1
    
    for key in results_dic:
        if results_dic[key][0] in dognames_dic:
            
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((1,1))
            
            else:
                results_dic[key].extend((1,0))
        
        else:
            
            if results_dic[key][1] in dognames_dic:
                results_dic[key].extend((0,1))
            
            else:
                results_dic[key].extend((0,0))
        
   