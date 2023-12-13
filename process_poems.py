#from textblob import TextBlob
#from ibm_watson import ToneAnalyzerV3
#from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json

def extract_poem_data(poem_data):
    with open('poems.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    poem_data = {}
    current_poem_number = 0
    current_poem_text = ''
    current_poem_title = ''

    for line in lines:
        line = line.strip()
        if line.startswith(str(current_poem_number + 1) + "."):
            if current_poem_number != 0:
                poem_data[current_poem_number] = {'title': current_poem_title, 'text': current_poem_text.strip()}
            current_poem_number = int(line.split('.')[0])
            current_poem_text = ''
            current_poem_title = line[line.find("'")+1:line.rfind("'")] if line.count("'") >= 2 else ''
        elif current_poem_number != 0:
            current_poem_text += line + " "

    # Add the last poem
    if current_poem_number != 0:
        poem_data[current_poem_number] = {'title': current_poem_title, 'text': current_poem_text.strip()}

    
  # Print the number of parsed poems
    return poem_data


if __name__ == "__main__":
    poem_data = {}
    poem_data = extract_poem_data(poem_data)
    with open('poem_data.json', 'w') as file:
        json.dump(poem_data, file, indent=4)


    # conduct sentiment analysis of the letters
    # for i in range(366):
    #     index = i + 1
    #     text = poem_data[index]['text']
    #     blob = TextBlob(text)
    #     sentiment = blob.sentiment.polarity
    #     poem_data[index]['sentiment'] = sentiment
    # print(poem_data)

# def process_letters(input):
#   with open(input, 'r', encoding='utf-8') as file:
#       lines = file.readlines()

# from ibm_watson import ToneAnalyzerV3
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# def analyze_emotion_ibm(text):
#     authenticator = IAMAuthenticator('YOUR_API_KEY')  # Replace 'YOUR_API_KEY' with your actual API key
#     tone_analyzer = ToneAnalyzerV3(
#         version='2017-09-21',
#         authenticator=authenticator
#     )

#     tone_analyzer.set_service_url('YOUR_SERVICE_URL')  # Replace 'YOUR_SERVICE_URL' with the service URL

#     # Analyzing tone
#     tone_analysis = tone_analyzer.tone(
#         {'text': text},
#         content_type='application/json'
#     ).get_result()

#     # Extracting emotions
#     emotions = []
#     if 'document_tone' in tone_analysis and 'tones' in tone_analysis['document_tone']:
#         emotions = [tone['tone_name'] for tone in tone_analysis['document_tone']['tones']]

#     return emotions

# # Example text
# text_to_analyze = "Your text goes here."

# # Analyze emotions using IBM Watson Tone Analyzer and get emotions as an array
# emotions_detected = analyze_emotion_ibm(text_to_analyze)
# print(emotions_detected)
