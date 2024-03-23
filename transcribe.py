import os
from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
)

load_dotenv()
API_KEY = os.getenv('API_KEY')


def get_files():
    folder= "mp3"
    files = os.listdir(folder)
    
    return files


def transcribe(files):
    transcriptions=[]
    for file in files:

        try:
            AUDIO_FILE = AUDIO_FILE = os.path.join("mp3", file)
            print(AUDIO_FILE)
            # STEP 1 Create a Deepgram client using the API key
            deepgram = DeepgramClient(API_KEY)

            with open(AUDIO_FILE, "rb") as file:
                buffer_data = file.read()

            payload: FileSource = {

                "buffer": buffer_data,
            }

            #STEP 2: Configure Deepgram options for audio analysis
            options = PrerecordedOptions(
                model="nova-2",
                smart_format=True,
            )

            # STEP 3: Call the transcribe_file method with the text payload and options
            response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

            # STEP 4: Print the response
            # print(response.to_json(indent=4)) 
            transcription= response['results']['channels'][0]['alternatives'][0]['transcript']
            row = ({file: transcription})
            
            transcriptions.append(row)
            

        except Exception as e:
            print(f"Exception: {e}")
           
    

