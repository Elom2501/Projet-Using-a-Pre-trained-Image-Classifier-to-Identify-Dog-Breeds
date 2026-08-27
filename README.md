# Projet-Using-a-Pre-trained-Image-Classifier-to-Identify-Dog-Breeds
## Future AWS AI Programmer (AWS and Uacity) first project Pre-trained Model
🐶 Pre-trained Image Classifier to Identify Dog Breeds
📌 Project Overview

This project was completed as part of the AWS AI Programmer / Udacity AI Programming with Python curriculum.

The objective is to build a Python program capable of analyzing pet images using pre-trained Convolutional Neural Network (CNN) architectures and determining:

    Whether an image contains a dog or a non-dog.
    If the image contains a dog, which dog breed is most likely represented.
    Which pre-trained CNN architecture — ResNet, AlexNet, or VGG — provides the best overall performance.
    Whether the improvement in accuracy provided by a model justifies its computational runtime.

    The project uses pre-trained models trained on ImageNet rather than training a CNN from scratch. This demonstrates an important practical machine-learning concept: using an existing model to perform inference on a new classification task.

🎯 Project Objectives

The project has four principal objectives.
Objective 1 — Dog Detection

Determine whether each pet image represents:

    🐶 a dog
    🐱🐰🦎🐻 another animal / non-dog

    The breed does not need to be correct for this objective. If the classifier predicts any dog breed for a dog image, the image is considered correctly identified as a dog.

Objective 2 — Dog Breed Classification

For images that actually contain dogs, determine whether the classifier correctly identifies the dog's breed.

For example:

Real label:       golden retrieverClassifier:       golden retriever

is considered a correct breed classification.
Objective 3 — CNN Architecture Comparison

Compare three pre-trained CNN architectures:

     ResNet
     AlexNet
     VGG

The goal is to determine which architecture performs best across the two primary objectives.
Objective 4 — Accuracy vs Runtime

Accuracy is not the only consideration.

     

    A model that is slightly more accurate but takes significantly longer to execute may not always be the best practical solution.

Therefore, the project also considers the computational time required by each architecture.
🧠 Machine Learning Approach

The project does not train the CNN models from scratch. Instead, it uses pre-trained models available through torchvision.

The general workflow is:
text
 
  
 
 
Pet Images
     │
     ▼
Extract image labels
     │
     ▼
Load pre-trained CNN
     │
     ▼
Classify each image
     │
     ▼
Normalize classifier output
     │
     ▼
Determine Dog / Not Dog
     │
     ▼
Compare predicted breed
     │
     ▼
Calculate statistics
     │
     ▼
Compare CNN architectures
 
 

This approach is an example of transfer learning / reuse of pre-trained representations for inference.
🏗️ Project Architecture

The project is divided into several Python modules, each responsible for a specific part of the pipeline.
get_input_args.py

Handles command-line arguments:
Argument
	
Default
--dir	pet_images/
--arch	vgg
--dogfile	dognames.txt
  

This makes the program flexible instead of hard-coding paths and model architectures.
get_pet_labels.py

Reads the image directory and constructs a dictionary containing the expected labels extracted from the image filenames.

Example:
python
 
  
 
 
{
    "Poodle_07956.jpg": ["poodle"],
    "cat_02.jpg": ["cat"],
    "Great_dane_05320.jpg": ["great dane"]
}
 
 

The complete dataset contains 40 images.
classify_images.py

This module sends each image to the selected pre-trained CNN classifier.

The image path is constructed from the image directory and filename:
python
 
  
 
 
classifier(images_dir + users_key, model)
 
 

The classifier output is normalized using lowercase conversion and whitespace removal before comparison.
adjust_results4_isadog.py

This is one of the most important parts of the project.

The classifier predicts specific ImageNet classes such as:

     golden retriever
     border collie
     tabby cat
     polar bear

The program must transform these detailed predictions into a binary decision:
text
 
  
 
 
Dog     → 1
Not Dog → 0
 
 

This allows the project to evaluate Objective 1 independently from breed accuracy.

For example:
text
 
  
 
 
Real:       dog
Classifier: golden retriever

PetLabelDog:   1
ClassLabelDog: 1
 
 

     

    The breed is correct in this case, but even if the classifier had predicted another dog breed, Objective 1 would still be considered correct.

calculates_results_stats.py

Calculates the principal evaluation metrics:

     Number of images
     Number of dog images
     Number of non-dog images
     Percentage of correctly identified dogs
     Percentage of correctly identified non-dogs
     Percentage of correctly classified dog breeds

print_results.py

Produces the final human-readable summary of the experiment.
🧪 Dataset

The project evaluates the classifier on 40 pet images.
Category
	
Count
Total images	40
Dog images	30
Non-dog images	10
  

The non-dog images include animals such as cats, geckos, rabbits, squirrels, bears and birds.

This is important because the task is not simply:

     

    "Which breed is this dog?"

It is first:

     

    "Is this image actually a dog?"

and only then:

     

    "What breed is the dog?"

📊 Results

The three CNN architectures were evaluated using the same 40 images.
Overall Results
CNN Architecture
	
Correct Dogs
	
Correct Non-Dogs
	
Correct Dog Breeds
	
Overall Matches
ResNet	100.0%	90.0%	90.0%	82.5%
AlexNet	100.0%	100.0%	80.0%	75.0%
VGG	100.0%	100.0%	93.3%	87.5%
  
🔬 ResNet Results
text
 
  
 
 
Number of Images:       40
Dog Images:             30
Non-Dog Images:         10

Correct Dogs:           100.0%
Correct Non-Dogs:        90.0%
Correct Dog Breeds:      90.0%

Overall Match:           82.5%
 
 

ResNet correctly recognized all 30 dog images as dogs.

However, it incorrectly classified one of the 10 non-dog images as a dog:
text
 
  
 
 
Real:       cat
Classifier: norwegian elkhound
 
 

Therefore:

     Correct dogs = 100%
     Correct non-dogs = 90%
     Breed classification accuracy = 90%

🔬 AlexNet Results
text
 
  
 
 
Number of Images:       40
Dog Images:             30
Non-Dog Images:         10

Correct Dogs:           100.0%
Correct Non-Dogs:       100.0%
Correct Dog Breeds:      80.0%

Overall Match:           75.0%
 
 

AlexNet achieved perfect binary classification:

     Dogs = 100%
     Non-dogs = 100%

However, its breed classification performance was lower: 80%

Several dog breeds were incorrectly classified, including:
Real Breed
	
Predicted Breed
Boston terrier	Basenji
Great Pyrenees	Kuvasz
Golden retriever	Tibetan mastiff
Beagle	English foxhound
Golden retriever	Afghan hound
Beagle	Walker hound
  
🔬 VGG Results
text
 
  
 
 
Number of Images:       40
Dog Images:             30
Non-Dog Images:         10

Correct Dogs:           100.0%
Correct Non-Dogs:       100.0%
Correct Dog Breeds:      93.3%

Overall Match:           87.5%
 
 

VGG achieved:

     ✅ 100% dog identification
     ✅ 100% non-dog identification
     ✅ 93.3% dog breed classification

Only two dog breed classifications were incorrect:
Real Breed
	
Predicted Breed
Great Pyrenees	Kuvasz
Beagle	Walker hound
  

This gives VGG the highest breed classification accuracy of the three architectures.
🏆 Best Model

Based on the experimental results, VGG is the best-performing architecture for this project.
text
 
  
 
 
                 Dogs     Non-Dogs     Dog Breeds
---------------------------------------------------
ResNet           100%       90%          90%
AlexNet          100%      100%          80%
VGG              100%      100%         93.3%
 
 

VGG is the only model that simultaneously achieves:

     ✅ 100% dog classification
     ✅ 100% non-dog classification
     ✅ 93.3% breed classification

Therefore, VGG provides the strongest overall solution for the two primary objectives.
⏱️ Runtime Consideration

Accuracy must also be considered together with computational cost.

In the VGG experiment, the displayed runtime was approximately 18 seconds.

     

    💡 Key principle: The best model is not necessarily the model with the highest accuracy alone. Model selection should consider both predictive performance and computational cost.

For this particular dataset, however, VGG's improvement in breed classification makes it the strongest candidate.
📈 What the Results Tell Us

The experiment reveals an interesting distinction between object detection/classification and fine-grained classification.

All three models performed extremely well at determining whether an image contained a dog:
Model
	
Dog Detection
ResNet	100%
AlexNet	100%
VGG	100%
  

The more difficult problem was identifying the exact breed:
Model
	
Breed Classification
VGG	93.3%
ResNet	90.0%
AlexNet	80.0%
  

     

    This shows that a model can be excellent at recognizing the broad semantic category dog while being less accurate at distinguishing between visually similar breeds.

🧩 What I Learned From the Project
Python

     Command-line arguments
     Functions and modular programming
     Dictionaries
     String processing
     File and directory manipulation
     Data validation
     Timing program execution

Machine Learning

     CNN architectures
     Image classification
     Pre-trained models
     ImageNet
     Transfer learning concepts
     Model evaluation
     Classification accuracy
     Binary classification vs multi-class classification

Software Engineering

The project separates responsibilities into independent modules:
text
 
  
 
 
Input
 ↓
Labels
 ↓
Classification
 ↓
Dog/Not-Dog adjustment
 ↓
Statistics
 ↓
Results
 
 

This makes the program easier to understand, test and maintain.
📋 Udacity Project Requirements
1. Timing Code

The program must measure execution time around the main processing pipeline.
2. Command-Line Arguments

The program must support:

     --dir
     --arch
     --dogfile

with appropriate defaults.
3. Pet Image Labels

The program must correctly construct the pet-label dictionary.

For the provided dataset: 40 key-value pairs were successfully generated.
4. Image Classification

The program must:

     construct the correct image path;
     pass the image to the classifier;
     normalize classifier output;
     store classification results.

5. Dog / Non-Dog Classification

The program must independently determine whether:
text
 
  
 
 
Real image = dog         AND Classifier result = dog breed
Real image = non-dog     AND Classifier result = non-dog
 
 

This is separate from exact breed classification.
6. Statistics

The program must calculate:

     pct_correct_dogs
     pct_correct_notdogs
     pct_correct_breed

7. Model Comparison

Finally, the project requires running:
bash
 
  
 
 
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
 
 

and comparing the results.

The three runs produced the expected pattern:
text
 
  
 
 
ResNet   → 100 / 90 / 90
AlexNet  → 100 / 100 / 80
VGG      → 100 / 100 / 93.3
 
 
🏁 Conclusion

This project demonstrates how a pre-trained CNN can be used as an image classification system without training a neural network from scratch.

The evaluation separates the problem into two levels:

    Is the image a dog?
    If it is a dog, what breed is it?

The results show that all three architectures were highly effective at identifying dogs, but their ability to distinguish between dog breeds varied.

Among the three models, VGG achieved the best overall performance, with:

     

    ✅ 100% accuracy for dog identification
    ✅ 100% accuracy for non-dog identification
    ✅ 93.3% accuracy for dog-breed classification

Therefore, based on the project's objectives and experimental results, VGG is the recommended architecture for this particular task.
