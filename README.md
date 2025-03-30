# Crop Pest Classification Using Deep Learning

## 🌾 Project Overview
AGRIGUARD: Automated Pest Classification for Agriculture utilizes a Convolutional Neural Network (CNN)-based model to identify pests affecting crops such as rice, wheat, and maize. The system integrates web, mobile, and API interfaces to enable real-time pest detection and provide pest management recommendations. By automating pest classification, AGRIGUARD helps farmers make informed decisions and reduce the overuse of pesticides.

## 🧩 Key Components
Web Interface: Allows users to upload crop images and receive classification results with confidence scores.

Mobile Application: Provides real-time pest detection using the device’s camera, with an offline mode to store images in low-connectivity areas.

Command-Line Interface (CLI): Enables developers and researchers to train, test, and evaluate the model efficiently.

API Integration: RESTful API facilitates seamless communication between the model and external agricultural systems, returning classification results in JSON format.

## 🚀 Features
High-Accuracy Classification: CNN model achieves over 97% accuracy, outperforming baseline models.

Pesticide Recommendation System: Suggests suitable pesticides based on identified pests.

Cloud and Edge Computing Support: Ensures real-time inference on cloud platforms and IoT-enabled devices like Raspberry Pi.

Grad-CAM Visualizations: Provides saliency maps to validate and interpret model predictions.

User Alerts: Sends real-time notifications and alerts to farmers for pest detection and management updates.

## 📊 Model & Database Integration
The CNN model processes pest images uploaded through the web or mobile interface and stores the classification results in a database. SQL/NoSQL databases, such as MySQL or MongoDB, manage user data, pest images, and model predictions. Flask-based APIs ensure smooth communication between the application and database, enabling seamless data retrieval and result visualization.

## 🎯 Conclusion
AGRIGUARD enhances agricultural pest management by automating pest classification and providing accurate recommendations. It reduces pesticide overuse and promotes sustainable farming practices. Future improvements include integrating federated learning for data privacy and utilizing hyperspectral imaging for cross-regional pest analysis, ensuring better adaptability and scalability.
