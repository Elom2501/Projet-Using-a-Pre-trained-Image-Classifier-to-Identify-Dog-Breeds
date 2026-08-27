#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Yao Elom Jean-Paul KAPOU
# DATE CREATED:  27/08/2026                               
# REVISED DATE: 27/08/2026  
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files.
    Returns:
           None - results_dic is mutable data type so no return needed.
    """

    # Créer un dictionnaire vide pour les noms des chiens
    dognames_dic = dict()

    # Lire tous les noms de chiens dans le fichier
    with open(dogfile, "r") as infile:
        for line in infile:
            dog_name = line.rstrip()

            if dog_name in dognames_dic:
                print("Warning: Duplicate dog name found:", dog_name)
            else:
                dognames_dic[dog_name] = 1

    # Parcourir chaque image dans le dictionnaire des résultats
    for key in results_dic:

        # Label provenant du nom de l'image
        pet_label = results_dic[key][0]

        # Label prédit par le classifier
        classifier_label = results_dic[key][1]

        # Vérifier si l'animal réel est un chien
        if pet_label in dognames_dic:
            pet_is_dog = 1
        else:
            pet_is_dog = 0

        # Vérifier si la prédiction du classifier est un chien
        classifier_is_dog = 0

        # Le classifier peut retourner plusieurs alias séparés par des virgules
        classifier_labels = classifier_label.split(",")

        for label in classifier_labels:
            label = label.strip()

            if label in dognames_dic:
                classifier_is_dog = 1
                break

        # Ajouter les deux nouveaux résultats
        results_dic[key].extend([pet_is_dog, classifier_is_dog])