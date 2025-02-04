# AgroTechHub
AgroTechHub is a full-stack mobile application developed using Flutter for the frontend and Django for the backend, aimed at transforming the agricultural industry by connecting farmers and wholesalers directly. The platform facilitates the buying and selling of agricultural products in bulk, eliminating traditional middlemen, reducing costs, and ensuring fair pricing for both parties. The app provides a streamlined, modern solution for farmers and wholesalers.

## Features

- **User Roles**: 
  - **Farmers**: Add products, update details, and upload images.
  - **Buyers**: Browse products, make bulk purchases.
  - **Role-based access** during registration (farmer or buyer).

- **Authentication & Security**:
  - Secure login with **JWT Authentication**.
  - **OTP Generation** for additional password security.

- **Chat Functionality**:
  - Real-time messaging using **WebSocket** for live communication.
  - Integrated **Gemini API** chatbot for user interaction.

- **Product Management**:
  - Farmers can upload and update product details.
  - Buyers can view and purchase products directly.

- **Expense Management**:
  - Track transaction expenses for both farmers and buyers.

- **Post Creation & Comments**:
  - Farmers can create posts, upload images or files.
  - Buyers can comment and interact with posts.

- **Video Upload**: 
  - Upload and view videos related to products.

## Technologies Used

- **Frontend**:
  - **Flutter** for cross-platform mobile development.
  - **WebSocket** for real-time messaging.
  - **Bloc** for state management.
  - **image_picker** and **file_picker** for uploading images and files.
  - **video_player** for video streaming.
  - **Geolocator** for user location tracking.

- **Backend**:
  - **Django** for handling backend logic and APIs.
  - **JWT Authentication** for secure access.
  - **Django REST Framework** for API development.
  - **SQlite** for database management.

- **Additional Libraries**:
  - **flutter_gemini** for chatbot integration.
  - **flutter_secure_storage** for secure data storage.
  - **shared_preferences** for local data storage.
  - **fluttertoast** for displaying notifications.

## Project Architecture

- **Frontend** (Flutter):
  - Designed with an intuitive UI for both farmers and buyers.
  - Responsive design for Android and iOS platforms.

- **Backend** (Django):
  - **Django REST Framework** to handle product management, chat, and expense tracking.
  - **WebSocket** integration for real-time communication.

## Workflow

1. **User Registration**: 
   - Users sign up with JWT and OTP-based verification. Select their role (farmer or buyer).

2. **Farmer Operations**: 
   - Add products, update details, and manage expenses.
   - Interact with buyers through real-time chat.

3. **Buyer Operations**: 
   - Browse products, make purchases, and interact with farmers.


