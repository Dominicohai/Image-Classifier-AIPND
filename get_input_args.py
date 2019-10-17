# PROGRAMMER: Ohaedoghasi Olisanonso
# DATE CREATED: October 7, 2019                                  
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse

def get_input_args():
    
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()
    
    # Create 3 command line arguments as mentioned above using add_argument() from ArguementParser method
    parser.add_argument('--dir', type = str, default = 'pet_images/',
                      help = 'Path to the folder of pet images')
    parser.add_argument('--arch', type = str, default = 'vgg',
                      help = 'Path to CNN Model Architecture')
    parser.add_argument('--dogfile', type = str, default = 'dognames.txt',
                      help = 'Path to the text file with dog names')
    
    return parser.parse_args()
