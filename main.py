import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
listener = sr.Recognizer()
cortana = pyttsx3.init()
voices = cortana.getProperty('voices')
cortana.setProperty('voice', voices[1].id)

def talk(text):
        cortana.say(text)
        cortana.runAndWait()

def take_command():
        try:
           with sr.Microphone() as source:
               print('listening...')
               voice = listener.listen(source)
               command = listener.recognize_google(voice)
               command = command.lower()
               if 'cortana' in command:
                  command = command.replace('cortana', '')

        except:
            pass
        return command

def run_cortana():
     command = take_command()
     # time
     if 'time' in command:
         time = datetime.datetime.now().strftime('%I:%M %p')
         print(time)
         talk('Current time is' + time)
     # song
     elif 'play' in command:
         song = command.replace('play', '')
         talk('playing ' + song)
         pywhatkit.playonyt(song)
     # wikipedia
     elif 'tell me about' in command:
         look_for = command.replace('tell me about', '')
         info = wikipedia.summary(look_for, 1)
         print(info)
         talk(info)
     # jokes
     elif 'joke' in command:
         jokes = pyjokes.get_joke()
         print(jokes)
         talk(jokes)

     # if cortana don't understand the command
     else:
          talk('I did not get it but I am going to search it for you')
          pywhatkit.search(command)
     # To run continously
while True:
    run_cortana()