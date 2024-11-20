from deepgram import DeepgramClient, PrerecordedOptions
from dotenv import load_dotenv
import os

load_dotenv()

# The API key we created in step 3
DEEPGRAM_API_KEY = os.getenv('DEEPGRAM_API_KEY')

# Replace with your file path
PATH_TO_FILE = 'audio.mp3'

def main():
    deepgram = DeepgramClient(DEEPGRAM_API_KEY)

    with open(PATH_TO_FILE, 'rb') as buffer_data:
        payload = { 'buffer': buffer_data }

        options = PrerecordedOptions(
            smart_format=True, model="nova-2", language="en-US"
        )

        response = deepgram.listen.prerecorded.v('1').transcribe_file(payload, options)
        print(response.to_json(indent=4))

if __name__ == '__main__':
    main()