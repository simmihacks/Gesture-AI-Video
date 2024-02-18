import os
import csv
import json
import time
import pandas as pd
import replicate as _replicate

from openai import OpenAI


openai_client = OpenAI(api_key="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")


class VideoGenerator:

    __data__ = "template_videos"
    __audio__ = "audio"
    __output__ = "outputs"
    __model__ = "cjwbw/video-retalking:db5a650c807b007dc5f9e5abe27c53e1b62880d1f94d218d27ce7fa802711d67"

    def __init__(self, filename: str, script: str = None, contacts: pd.DataFrame = None):
        """
        """
        self.video_path = os.path.join(VideoGenerator.__data__, filename)
        self.audio_path = os.path.join(VideoGenerator.__audio__)
        self.output_path = VideoGenerator.__output__
        self.script = script
        self.contacts = contacts

    def create(self, audio_path: str):
        output = _replicate.run(
            VideoGenerator.__model__,
            input={
                "face": "https://replicate.delivery/pbxt/KQLb1VEFwqvFr2RGRhl7lVVIbpkAaSpu5RYSZt1y9spzpeDn/abandoned_cart.mp4",
                "input_audio": "https://replicate.delivery/pbxt/KQLb1vwDGGA7YnvWIueVTxfWmNHCIqa2EhM4KpWLPamI6pIP/abandoned_cart_audio.wav",
            }
        )
        print(output)

        "https://replicate.delivery/pbxt/i0SU5QMBxoJcBtFbIgDJ7c2mH3fRMCyu8CWJfjFTWTcan2XSA/output.mp4",

    def process(self):
        """
        Loop through all contacts and generate a personalized video.
        Utilizes first name, last name, company name, language
        """
        pass


model = VideoGenerator('abandoned_cart.mov')
model.create('audio/abandoned_cart_audio.mp4a')