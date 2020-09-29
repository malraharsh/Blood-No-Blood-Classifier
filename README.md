# Blood-No-Blood-Classifier

To detect the faces with blood and no-blood.

## Sample Images

### Faces with Blood

|<img src='https://github.com/malraharsh/Blood-No-Blood-Classifier/blob/master/Sample_Images/Original%20Faces/blood/blood_396.jpg' width='250' height='250' /> |
<img src='https://github.com/malraharsh/Blood-No-Blood-Classifier/blob/master/Sample_Images/Original%20Faces/blood/blood_397.jpg' width='250' height='250' />|

### Faces with no blood

|<img src='https://github.com/malraharsh/Blood-No-Blood-Classifier/blob/master/Sample_Images/Original%20Faces/noblood/noblood_12.jpg' width='250' height='250' />|
<img src='https://github.com/malraharsh/Blood-No-Blood-Classifier/blob/master/Sample_Images/Original%20Faces/noblood/noblood_7.jpg' width='250' height='250' />|


## Approach:
1. Used a trained a Mobile Net model by adding new layers on top of it in Original image.
2. Cropped the images to contain only face region, and used above model.
3. Modified the image to only contain the red channel. 

## Steps

1. Removing the corrupt images. 

2. Processing the images:
  * Find the face area.
  * Crop it to create dataset containing only face region.
  
3. Training:
  * Using Transfer Learning with Mobile Net Model with pretrained imagenets weight.
  * Adding additional layers on top of it.
  * Training the model for 30 epochs.
  
4. Testing:
  * Visualizing the plot of Accuracy.
  * Printing the classification report.
  
5. Displaying the images along with the predictions.

## Further Improvements:
 * Segmenting the color in upper and lower red range. Then using the segmented region for predictions.
 * Removing the skin color from image and using remaining region for predictions.
 * Creating artificial data, by adding artificial blood on no blood faces by OpenCV.
 * Most obvious one, is to get a descent amount of data.
