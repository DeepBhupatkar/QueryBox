## Project Title: QueryBox: OCR, Android, Azure

## Description
QueryBox is an Android application designed to respond to image queries or questions using Optical Character Recognition (OCR) and ChatGPT. The application integrates with the ChatGPT API to provide responses within 13 seconds. It utilizes an Azure-hosted Python server for ChatGPT interaction, ensuring efficient and reliable performance. The project has the potential for publication on the Google Play Store.

## Features
1. **OCR Integration:** Utilizes OCR to extract text from images.
2. **ChatGPT Integration:** Integrates with the ChatGPT API to generate responses to user queries/questions.
3. **Fast Response Time:** Provides responses within 13 seconds, ensuring a smooth user experience.
4. **Azure Hosting:** Hosts the Python server on Azure for reliable and scalable performance.
5. **Potential for Publication:** Designed with the intention of publishing on the Google Play Store for wider accessibility.

## Setup Instructions
1. Clone the repository to your local machine.
2. Set up the Android development environment and import the project into Android Studio.
3. Deploy the Python server on Azure or your preferred hosting platform.
4. Update the server endpoint URL in the Android application code to point to the deployed server.
5. Build and run the Android application on an emulator or physical device.

## Usage Guidelines
- Open the QueryBox application on your Android device.
- Capture or select an image containing text.
- Submit the image query/question.
- Wait for the response generated by ChatGPT.
- Review and interact with the response as needed.

## Contributing
- I welcome contributions to enhance the QueryBox app.
  
## Repository Structure
- **App:** This Android application utilizes the Quickstart ML Kit of Google, written in Kotlin, to enhance its functionality.
- **Server:** Contains the Python server code hosted on Azure.
- **FileStructure&Output:**  Below image shows the path and some info path:vision-quickstart/app/src/main/java/com/google/mlkit/vision/demo
<img width="1352" alt="Screenshot 2024-05-24 at 12 30 46 PM" src="https://github.com/DeepBhupatkar/QueryBox/assets/144551847/2a50469f-2dc9-4ed7-a033-d66ee3569005">
