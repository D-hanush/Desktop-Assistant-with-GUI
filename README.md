# Desktop-Assistant-with-GUI

# Della - Voice Assistant

Della is a voice-activated assistant built with Python that can perform various tasks such as fetching news, playing YouTube videos, telling jokes, opening websites, and more. This project utilizes several libraries including PyQt5 for the GUI, SpeechRecognition for recognizing voice commands, and pyttsx3 for text-to-speech functionality.

## Features

- Greets the user based on the time of day
- Tells the current time and date
- Plays YouTube videos based on voice commands
- Adjusts the system volume
- Fetches the latest news headlines
- Opens specified websites
- Tells jokes
- Sends messages and makes calls using Twilio
- Provides information from Wikipedia
- Activates a "how-to" mode to fetch step-by-step instructions
- Displays loading and additional gifs

## Requirements

- Python 3.6+
- `speech_recognition`
- `pyttsx3`
- `pyjokes`
- `wikipedia`
- `pywhatkit`
- `requests`
- `beautifulsoup4`
- `pyautogui`
- `twilio`
- `newsapi-python`
- `pywikihow`
- `PyQt5`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/della-voice-assistant.git
    cd della-voice-assistant
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Update the API keys in `MainThread` class for Twilio and NewsAPI.

4. Run the application:

    ```bash
    python main.py
    ```

## Usage

- Start the application by running the `main.py` script.
- Interact with Della using voice commands. For example:
  - "Tell me about Python"
  - "Play Despacito on YouTube"
  - "What's the news today?"
  - "Open Google"
  - "Tell me a joke"
  - "Send message"
  - "Make a call"
  - "What's my IP address?"
  - "What's the temperature?"
  - "Activate mode"
  - "No thanks" to exit

## Project Structure

- `main.py`: Main script to run the application
- `MYui.py`: Contains the PyQt5 UI setup
- `requirements.txt`: List of required Python packages

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by various Python projects and tutorials on voice assistants
- Special thanks to the developers of the libraries used in this project
