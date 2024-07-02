# Python-SAPI-Voice-for-Windows

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contribution](#contribution)


## Project Overview
This Python script utilizes the win32com library to access the Windows Speech API (SAPI) for text-to-speech functionality. It prompts the user to input words or phrases to be spoken aloud, continuously looping until the user enters "-1" to terminate the program. Upon receiving user input, it speaks the inputted text using the default text-to-speech engine provided by Windows, facilitating an interactive text-to-speech experience directly within the console environment.


## Installation
This project requires Python 3.12.1 or later.
To set up the project:
1. Ensure Python 3.12.1 or a later version is installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
2. Clone or download the repository to your local machine.

            git clone <https://github.com/jaiswalchitransh/Python-SAPI-Voice-for-Windows>

3. Open the project in your preferred Python environment (e.g., IDE or terminal).
4. Install win32com library using pip:
   
            pip install pypiwin32

5. Run the script (`speaks.py`) and observe the output.


## Usage
Ensure Python 3.x is installed. Run the script:

            python speaks.py
  
- Enter words or phrases when prompted. Each input will be spoken aloud immediately.
- To stop the program, type "-1" and press Enter.


## Features
- **Text-to-Speech**: Utilizes the Windows Speech API (SAPI) for converting text input to spoken output.
- **Interactive**: Allows continuous input and speech output until terminated by the user.
- **Ease of Use**: Provides a simple interface within the console environment for speech synthesis.


## Contribution
I, **Chitransh Jaiswal** developed this Project Individually. I was responsible for all aspects of the project, including design, development, testing, and documentation.
Contributions to improve the efficiency, readability, or functionality of the code are welcome. To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.

Please ensure your contributions adhere to the coding standards and follow the existing style and structure.

---

Thank you for your interest in the Python SAPI Voice for Windows. 
