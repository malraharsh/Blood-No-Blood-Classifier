# Blood-No-Blood-Classifier

To detect the faces with blood and no-blood.

## Sample Images
### Faces with Blood
|<img src= width='250' height='250' /> |
<img src= width='250' height='250' />|
### Faces with no blood
|<img src= width='250' height='250' />|
<img src= width='250' height='250' />|


# Steps
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
5. Predicting:
  * Getting predictions from trained model.
  * Displaying the images along with the predictions.

