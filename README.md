# bitverxel
# bitverxel
SINDESI

 Description
Project Overview: Real-Time Interpreter for Speech to Sign and Sign to Speech

The goal of this project is to create a real-time interpreter that will help hearing and deaf people communicate, especially in educational environments. OpenVINO, MediaPipe, and a voice recognition model are integrated into the system to facilitate smooth translation between spoken and sign language.



Important Elements



1. Sign-to-Speech: The system records sign language movements with a webcam by using MediaPipe. Deaf students can express their ideas and queries during lectures thanks to the real-time processing of the motions into spoken language.



2. Speech-to-Sign: This technique recognizes spoken words from peers or teachers and translates them into animated signs. This makes it easier for deaf pupils to follow lectures.



3. OpenVINO: With this toolkit, the model is optimized for for performance, guaranteeing excellent accuracy and minimal delay when interpreting data in real time. It makes it possible for the program to function well across a range of hardware systems.

Advantages for Students Who Are Hard of Hearing or Deaf:
Enhanced Learning: Deaf students can participate and comprehend more in class discussions when they participate more actively.
Better Interaction: By eliminating language barriers, the technology promotes improved communication between students and teachers.
Inclusivity: The project fosters a more inclusive learning environment by meeting a range of communication demands.
Application Integration: A desktop or mobile application that acts as a platform for communication may be the project's ultimate product. Features might consist of:

Real-Time Interpretation: Using an app that translates their signs into spoken language and vice versa, students can have direct conversations in sign language with teachers or peers.
Text-to-Sign and Sign-to-Text: When users enter messages, the software interprets them as animations in sign language. It can also record sign language and translate it back into text.
Interactive Learning Tools: The app might provide quizzes to improve language skills, video lectures, and tools for learning sign language.
For deaf and hard-of-hearing students, this project has the potential to greatly enhance their educational experience by facilitating more accessible and fluid communication in real-time classroom settings.
Acknowledgements
This project is built upon the work of others. Special thanks to:

- Hand-gesture-recognition-mediapipe(github.com/kinivi/hand-gesture-recognition-mediapipe) by kinivi
  - We have used this model to create the base for sign to speech to start with basic hand gesture recognition 
- github.com/SufiyaanNadeem/Sign-Language-Translator by Sufiyaan Nadeem
  - We have used thid repository to train our own sign language signs using the available ml model

Our speech to sign model recognises speech and gives the appropriate video/image for the speech recognised and the dataset used is our own dataset.

The codes are also subjected to future enhancements.
