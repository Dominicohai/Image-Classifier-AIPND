# PROGRAMMER:   Ohaedoghasi Olisanonso
# DATE CREATED: October 7, 2019                                  
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. 

# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    start_time = time()
    
    in_arg = get_input_args()

    results = get_pet_labels(in_arg.dir)

    classify_images(in_arg.dir, results, in_arg.arch)

    adjust_results4_isadog(results, in_arg.dogfile)

    results_stats = calculates_results_stats(results)

    print_results(results, results_stats, in_arg.arch, True, True)
    
    end_time = time()

    tot_time = end_time - start_time
    #calculate difference between end time and start time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )
    

if __name__ == "__main__":
    main()
