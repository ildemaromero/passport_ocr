from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import json
import validators
import base64
import os

load_dotenv()

class PassportOCR:
    def __init__(self):
        self.MODEL = "gpt-4o-mini"
        self.client = OpenAI(api_key=os.getenv('API_KEY'))
        
    def is_local_path(self, string):
        return Path(string).exists() and Path(string).is_file()

    def is_url(self, string):
        return validators.url(string)
    
    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def get_passport_data(self, img_url):
        try:
            describe_system_prompt = (
'''
You are a OCR specialize in passport data extraction, you read passports info from images and return as plain text in JSON format without markdown. 
The data must be transform and translate it into English.

JSON example:
{
  "first_name": "John",
  "last_name": "Doe",
  "passport_number": "123456789",
  "nationality": "Venezuelan",
  "issue_date": "2020-01-01",
  "expiration_date": "2030-01-01",
  "place_of_birth": "Caracas, Venezuela",
  "date_of_birth": "1990-01-01",
  "gender": "M",
  "passport_country": "VEN"
}
'''
            )

            if self.is_local_path(img_url):
                enconded_image = self.encode_image(img_url)
                url_data = {"url": f"data:image/jpeg;base64,{enconded_image}"}
            elif self.is_url(img_url):
                url_data = {"url": img_url}
            else:
                return {"ERROR": "Invalid Image URL or PATH"}
                


            # Generar la respuesta usando OpenAI GPT-4
            response = self.client.chat.completions.create(
                model=self.MODEL,
                temperature=0.2,
                messages=[
                    {"role": "system", "content": describe_system_prompt},
                    {"role": "user", "content": [{"type": "image_url", "image_url": url_data}]},
                    {"role": "user", "content": "passport"}
                ],
                max_tokens=300
            )

            passport_data = response.choices[0].message.content
            passport_dict = json.loads(passport_data)

            return passport_dict

        except Exception as e:
            print(f"ERROR while processing image: {e}")
            return None


