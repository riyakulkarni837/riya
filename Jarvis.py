
from __future__ import print_function
from tkinter import *
import calendar
import cv2
import roman as roman
import speech_recognition as sr
import playsound
import wikipedia as wikipedia
import wolframalpha as wolframalpha
from gtts import gTTS
import random
import requests
import webbrowser
import yfinance as yf
import time
import os
import datetime
import subprocess
import os.path




window = Tk()
global var
global var1

var = StringVar()
var1 = StringVar()

class person:
    name = ''
    def setName(self, name):
        self.name = name

    def setCity(self, city):
        self.city = city

numbers = {'hundred':100, 'thousand':1000, 'lakh':100000}
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october","november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]



client = wolframalpha.Client('6VL4LG-67QE6478K7')
api_key = 'AIzaSyB5w1zA-2WsEyjBuNf8w9yxrR-zSjkvRo4'
link = 'url = "https://maps.googleapis.com/maps/api/staticmap?"'

def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en-in')
    audio_file = 'Sofia_Assistant.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    var.set(f"Sofia: {audio_string}")
    window.update()
    print(f"Sofia: {audio_string}")

    os.remove(audio_file)



def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning " )
        window.update()
        var.set("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon ")
        window.update()
        var.set("Good Afternoon")

    else:
        speak("Good Evening ")
        window.update()
        var.set("Good Evening ")

    speak("How can I help you")
    return None







def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th','17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']


    return 'Today is '+weekday+', '+ordinalNumbers[dayNum - 1]+' of '+month_names[monthNum-1]+'. '

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":","-") + "-note.txt"
    with open(file_name,"w") as f:
        f.write(text)


    subprocess.Popen(["notepad.exe",file_name])








r = sr.Recognizer()
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        query = ''
        try:
            query = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down')
        var1.set(f">> {query.lower()}")
        window.update()
        print(f">> {query.lower()}")
        return query.lower()









def respond():
    speak("Initializing...")
    window.update()
    var.set("Initializing")
    wishMe()

    def there_exists(terms):
        for term in terms:
            if term in voice_audio:
                return True

    while True:
        voice_audio = record_audio()
        if there_exists(['hey', 'hi', 'hello']):
            greetings = [f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}",
                         f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
            greet = greetings[random.randint(0, len(greetings) - 1)]
            speak(greet)
            window.update()
            var.set(greet)

        if there_exists(["am I audible", "are you there", "can you listen me"]):
            speak("Sorry for inconvenience.. Having some connectivity issues ")
            window.update()
            var.set("Sorry for inconvenience.. Having some connectivity issues ")

        if there_exists(["very good", "good", "awesome", "good job", "best"]):
            appreciation = ["thank you", "my pleasure", "welcome"]
            appriciate = appreciation[random.randint(0, len(appreciation) - 1)]
            speak(appriciate)
            window.update()
            var.set(appriciate)

        if there_exists(["what is your name", "what's your name", "tell me your name"]):
            if person_obj.name:
                speak("my name is Sofia")
                window.update()
                var.set("my name is sofia")
            else:
                speak("my name is Sofia. what's your name?")
                window.update()
                var.set("my name is Sofia. what's your name?")

        if there_exists(["my name is"]):
            person_name = voice_audio.split("is")[-1].strip()
            speak(f"okay, i will remember that {person_name}")
            window.update()
            var.set(f"okay, i will remember that {person_name}")
            person_obj.setName(person_name)

        if there_exists(["how are you", "how are you doing"]):
            speak(f"I'm very well, thanks for asking {person_obj.name}")
            window.update()
            var.set(f"I'm very well, thanks for asking {person_obj.name}")

        if there_exists(["time"]):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{person_obj.name}, the time is {strTime}")
            window.update()
            var.set(f"{person_obj.name}, the time is {strTime}")

        if there_exists(["date", "today"]):
            get_date = getDate()
            print(get_date)
            speak(get_date)
            window.update()
            var.set(get_date)

            if there_exists(['calculation']):
                sum = 0
                var.set('Yes Sir, please tell the numbers')
                window.update()
                speak('Yes Sir, please tell the numbers')
                while True:
                    query = record_audio()
                    if 'answer' in query:
                        var.set('here is result' + str(sum))
                        window.update()
                        speak('here is result' + str(sum))
                        break
                    elif query:
                        if query == 'x**':
                            digit = 30
                        elif query in numbers:
                            digit = numbers[query]
                        elif 'x' in query:
                            query = query.upper()
                            digit = roman.fromRoman(query)
                        elif query.isdigit():
                            digit = int(query)
                        else:
                            digit = 0
                        sum += digit

            #    if there_exists(["search"]) and 'youtube' not in voice_audio:
            #       search_term = voice_audio.split("for")[-1]
            #      url = f"https://google.com/search?q={search_term}"
            #     webbrowser.get().open(url)
            #    speak(f'Here is what I found for {search_term}')

        if there_exists(["search"]) and 'youtube' not in voice_audio:
            try:
                try:
                    res = client.query(voice_audio)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak(results)
                    window.update()
                    var.set(results)

                except:
                    results = wikipedia.summary(voice_audio, sentences=2)
                    speak('WIKIPEDIA says - ')
                    speak(results)
                    window.update()
                    var.set(results)

            except:
                webbrowser.open('www.google.com')

        if there_exists(["youtube"]):
            search_term = voice_audio.split("for")[-1]
            url = f"https://www.youtube.com/results?search_query={search_term}"
            webbrowser.get().open(url)
            speak(f'Here is what I found for {search_term} ')
            window.update()
            var.set(f'Here is what I found for {search_term} ')

        if there_exists(["close chrome", "close gmail", "close udemy", "close netflix", "close primevideo",
                         "close cognitive classes"]):
            os.system("taskkill /f /im chrome.exe")

        if there_exists(["open gmail"]):
            url = "gmail.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        if there_exists(["open udemy"]):
            url = "udemy.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        if there_exists(["open netflix"]):
            url = "netflix.com/browse"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        if there_exists(["open prime video"]):
            url = "primevideo.com"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        if there_exists(["open cognitive classes"]):
            url = "https://courses.cognitiveclass.ai/dashboard"
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open(url)

        if there_exists(["open command prompt"]):
            os.system("start cmd")

        if there_exists(["close command prompt"]):
            os.system("taskkill /f /im cmd.exe")

        if there_exists(["open calculator"]):
            os.system("calc")

        if there_exists(["close calculator"]):
            os.system("taskkill /f /im Calculator.exe")

        if there_exists(["open my computer"]):
            os.system("explorer.exe")

        if there_exists(["close my computer"]):
            os.system("taskkill /f /im explorer.exe")

        if there_exists(["open android studio"]):
            android_dir = "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Android Studio/Android Studio.lnk"
            os.startfile(os.path.join(android_dir))

        if there_exists(["play music"]):
            speak("What should I play")
            window.update()
            var.set("What should I play")
            songs_dir = "C:/Users/Admin/Music"
            songs = os.listdir(songs_dir)
            print(songs)
            window.update()
            var.set(songs)
            k = record_audio()
            speak('playing ' + k + ' for you')
            window.update()
            var.set('playing ' + k + ' for you')
            os.startfile('C:/Users/Admin/Music/' + k + '.mp3')

        if there_exists(["joke", "jokes", "tell me a joke"]):
            res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept": "application/json"}
            )
            if res.status_code == requests.codes.ok:
                speak(str(res.json()['joke']))
                window.update()
                var.set(str(res.json()['joke']))
            else:
                speak('oops!I ran out of jokes')
                window.update()
                var.set('oops!I ran out of jokes')

        if there_exists(["shutdown"]):
            speak('shutting down your computer')
            window.update()
            var.set('shutting down your computer')
            os.system('shutdown -s')

        if there_exists(["open notepad", "make a note", "remeber this"]):
            speak('Do you want me to take notes for you?')
            window.update()
            var.set('Do you want me to take notes for you?')
            ans = record_audio()
            if 'yes' in ans:
                speak("what would you like me to write down")
                window.update()
                var.set("what would you like me to write down")
                notes = record_audio()
                note(notes)
                speak("I have made note of that")
                window.update()
                var.set("I have made note of that")
            elif 'no' in ans:
                speak("okay")
                window.update()
                var.set("okay")
                notepad_dir = "C:\\Users\\Admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk"
                os.startfile(os.path.join(notepad_dir))
            else:
                speak("Facing connectivity issue...")
                window.update()
                var.set("Facing connectivity issue...")


        if there_exists(["close notepad"]):
            os.system("taskkill /f /im notepad.exe")

        if there_exists(["open python", "open pycharm"]):
            python_dir = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition 2020.1.lnk"
            os.startfile(os.path.join(python_dir))

        if there_exists(["who created you", "who are you"]):
            speak("I am Sofia, the virtual assistant, created by Ms.Riya Kulkarni")
            window.update()
            var.set("I am Sofia, the virtual assistant, created by Ms.Riya Kulkarni")

        if there_exists(["find location", "find place"]):
            location = record_audio("What is the location?")
            url = 'https://google.nl/maps/place/' + location + '/&amo;'
            webbrowser.get().open(url)
            speak('Here is the location of ' + location)
            window.update()
            var.set('Here is the location of ' + location)

        if there_exists(["photo","picture"]):
            stream = cv2.VideoCapture(0)
            grabbed, frame = stream.read()
            if grabbed:
                cv2.imshow('pic', frame)
                cv2.imwrite('pic.jpg', frame)
            stream.release()

        if there_exists(["record video"]):
            cap = cv2.VideoCapture(0)
            out = cv2.VideoWriter('output.avi', -1, 20.0, (640, 480))
            while (cap.isOpened()):
                ret, frame = cap.read()
                if ret:

                    out.write(frame)

                    cv2.imshow('frame', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break
            cap.release()
            out.release()
            cv2.destroyAllWindows()

        if there_exists(["price of"]):
            search_term = voice_audio.lower().split(" of ")[-1].strip()
            stocks = {
                "apple": "AAPL",
                "microsoft": "MSFT",
                "facebook": "FB",
                "tesla": "TSLA",
                "bitcoin": "BTC-USD"
            }
            try:
                stock = stocks[search_term]
                stock = yf.Ticker(stock)
                price = stock.info["regularMarketPrice"]

                speak(f'price of {search_term} is {price} {stock.info["currency"]} {person_obj.name}')
                window.update()
                var.set(f'price of {search_term} is {price} {stock.info["currency"]} {person_obj.name}')
            except:
                speak('oops, something went wrong')
                window.update()
                var.set('oops, something went wrong')

        if there_exists(["exit", "quit", "goodbye", "bye"]):
            speak("going offline")
            window.update()
            var.set("going offline")
            exit()










time.sleep(1)

person_obj = person()

def update(ind):
    frame = frames[(ind)%100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)


label1 = Label(window, textvariable=var, bg='#ADD8E6')
label1.config(font=("Courier", 20))
label1.pack()

label2 = Label(window, textvariable = var1, bg = '#FAB60C')
label2.config(font=("Courier", 20))
label2.pack()


frames = [PhotoImage(file='Assistant.gif',format = 'gif -index %i' %(i)) for i in range(100)]
window.title('SOFIA')

label = Label(window, width = 500, height = 500)
label.pack()
window.after(0, update, 0)

btn1 = Button(text = 'START',width = 20, command = respond, bg = '#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()







window.mainloop()