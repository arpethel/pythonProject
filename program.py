import os
import openai
import speech_recognition as sr

# Set OpenAI key
openai.api_key = os.getenv('OPENAI_KEY')

def transcribe_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = recognizer.listen(source)
        
        try:
            return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand your audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {0}".format(e))

def generate_response(question):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=question,
      max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    question = transcribe_speech()
    if question is not None:
        print("You asked: ", question)
        response = generate_response(question)
        print("GPT-3 responded: ", response)

if __name__ == "__main__":
    main()
