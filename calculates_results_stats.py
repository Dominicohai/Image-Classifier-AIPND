                                      
# PROGRAMMER: Ohaedoghasi Olisanonso
# DATE CREATED: October 9, 2019                                 

# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images.   
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value. 


def calculates_results_stats(results_dic):
    
    results_stats_dic = {}
    
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    
    for key in results_dic:
        #Label Match Check
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1
        
        #Image is a Dog
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
            
            if results_dic[key][2] == 1:
                results_stats_dic['n_correct_breed'] += 1
        
        #Image is not a Dog
        else:
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1
    
    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_notdogs_img'] = results_stats_dic['n_images'] - results_stats_dic['n_dogs_img']
    
    #Percentage calculations
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images'])*100.0
    
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] /  
                                             results_stats_dic['n_dogs_img'])*100.0
    
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] /                                                                                   results_stats_dic['n_dogs_img'])*100.0
    
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs']/        
                                                    results_stats_dic['n_notdogs_img'])*100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0
        
        

    return results_stats_dic
