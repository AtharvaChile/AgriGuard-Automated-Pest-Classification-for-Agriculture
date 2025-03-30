# Crop Pest Classification Using Deep Learning

This project focuses on building an efficient and automated system for identifying and classifying crop pests using deep convolutional neural networks (DCNN) and transfer learning. This system aims to aid farmers and agricultural practitioners in detecting pests early and implementing precise pest control measures, enhancing food security and promoting sustainable agricultural practices.

## Project Overview

- **Objective**: To develop a robust system that accurately classifies various crop pests from images, leveraging deep learning and transfer learning techniques.
- **Motivation**: Address challenges in agriculture related to food security, economic impact, and sustainability by using advanced machine learning techniques for early pest detection.

## Key Components

1. **Data Collection and Preprocessing**:
   - Collected images of various crop pests and applied preprocessing techniques like image normalization and data augmentation to improve model robustness.

2. **Deep Convolutional Neural Network (DCNN)**:
   - Utilized pre-trained models such as ResNet for feature extraction and fine-tuning to adapt to crop pest classification.
   - Employed transfer learning to leverage the knowledge from large-scale datasets, improving performance with limited agricultural datasets.

3. **Classification System**:
   - A multi-class classification model that identifies pest types based on input images, facilitating informed pest management decisions.
   - Integrated a user-friendly interface for uploading images and viewing pest classification results in real time.

4. **Pesticide Recommendation System**:
   - Provides suggested pesticides based on the identified pests, aiding in precise pest control measures.

## Features

- **Real-Time Pest Classification**: Quickly and accurately classifies pest images, allowing for timely interventions.
- **Transfer Learning**: Enhances model performance by using pre-trained networks, reducing computational resources required for training.
- **User-Friendly Interface**: A simple interface that allows users to upload images and receive pest classification and pesticide recommendations.

## System Requirements

- **Programming Language**: Python
- **Frameworks and Libraries**:
  - TensorFlow and Keras for deep learning
  - OpenCV for image processing
- **Database**: MySQL for storing pest information and related data
- **Hardware**: Requires GPU support for efficient model training and inference

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/KaustubhLabade/ATM_Machine_UI.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database and load pest data.
4. Run the application and navigate to the web interface to upload images and view results.

## Future Enhancements

- Integration with real-time notifications and alerts.
- Optimization for faster model inference.
- Enhanced recommendations based on weather and crop type.
- Expand the dataset to improve model generalization across diverse crop types and regions.

## Contributors

- Kaustubh Labade
- Rohit Magar
- Shreyaans Das
- Onkar Darekar

## License

This project is open-source and available under the MIT License.
