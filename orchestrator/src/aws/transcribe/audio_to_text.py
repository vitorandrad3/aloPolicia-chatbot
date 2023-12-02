from src.env_variables import EnvConstants
import boto3
import time
import requests
import json

def audio_to_text(key, messagesid):
    transcribe = boto3.client('transcribe')

    job_name = f"transcription{messagesid}"

    transcribe.start_transcription_job(
                        TranscriptionJobName=job_name,
                        Media={'MediaFileUri': f"s3://{EnvConstants.s3_media_bucket}/{key}"},
                        MediaFormat='ogg',
                        LanguageCode='pt-BR' 
                        )

    while True:
        status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
        if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
            break
        
        time.sleep(2)

    response = transcribe.get_transcription_job(
   TranscriptionJobName= job_name
    )
    transcript_uri = response['TranscriptionJob']['Transcript']['TranscriptFileUri']
    transcribe_file = requests.get(transcript_uri).content
    transcribe_file = json.loads(transcribe_file)
    
    text = transcribe_file['results']['transcripts'][0]['transcript']

    text.replace('.','').replace(',','')
    
    return text