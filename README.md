Project Description:

This project involves developing a deep learning-based Image Classification System to accurately classify skin cancer lesions and conditions using convolutional neural networks (CNN) and pre-trained models like EfficientNetB1,ResNet152 ,VGG19 & DenseNet121. It aims to improve dermatological diagnosis by enhancing diagnostic accuracy, patient outcomes, and early detection. The project includes establishing an image classification pipeline, optimizing model performance, and providing detailed classification reports.

How to aceess and use FLask app:

1.Clone this repositry.

2.Install requirement.txt file in local enviorment.

3.Run the flask app usinf "python app.py".

4.Open "http://127.0.0.1:5000" in your browser.

![Screenshot 2024-08-19 201430](https://github.com/user-attachments/assets/31677f51-72f6-42bf-bc4f-2f7e9162892b)

5. Upload any  Skin lesion image and click on classify button.

6.The image will be classsified into any of the 8 classes ['Actinic keratosis', 'Basal cell carcinoma', 'Benign keratosis', 'Dermatofibroma', 'Melanocytic nevus', 'Melanoma', 'Squamous cell carcinoma', 'Vascular lesion']

The Flask uses ENB1_8CLass30.h5 model weight to classify the images, the model weights were trained in ISIC_Skin_Classifiaction.ipymb file.
