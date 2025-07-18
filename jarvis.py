import pyttsx3
import speech_recognition as sr
import datetime
import sys
import wikipedia
import smtplib
import os
from youtubesearchpython import VideosSearch
import webbrowser
import pyautogui
import psutil
import subprocess


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)
    engine.say(text)
    engine.runAndWait()




    

    

def tell_time():
    now = datetime.datetime.now()
    speak(f"The current time is {now.strftime('%I:%M %p')}")

def tell_date():
    now = datetime.datetime.now()
    speak(f"Today's date is {now.strftime('%A, %d %B %Y')}")

def take_command():
    r = sr.Recognizer()
    r.energy_threshold = 400
    r.pause_threshold = 0.6
    r.dynamic_energy_threshold = True

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            print("No speech detected, retrying...")
            return ""

    try:
        print("Recognizing...")
        return r.recognize_google(audio, language='en-IN').lower()
    except Exception as e:
        print("Error:", e)
        return ""

def screenshot():
    speak("Taking a screenshot.")
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    speak("Screenshot saved as screenshot.png.")
def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)
    print("Joke:", joke)

def cpu():
    usage = psutil.cpu_percent(interval=1)
    speak(f"CPU usage is at {usage}%")
    battery = psutil.sensors_battery()
    if battery:
        speak(f"Battery percentage is at {battery.percent}%")
    else:
        speak("Battery information is not available.")
    
def send_email(to, subject, body):
    message = f"Subject: {subject}\n\n{body}"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bragadeeshwaranp1@gmail.com', 'ezfj fkys ouoc obcb')
    server.sendmail('bragadeeshwaranp1@gmail.com', to, message)
    server.quit()


def play_youtube(song):
    videos = VideosSearch(song, limit=1)
    result = videos.result()
    if result['result']:
        url = result['result'][0]['link']
        speak(f"Playing {song} on YouTube")
        webbrowser.open(url)
    else:
        speak("Sorry, I couldn't find your song on YouTube.")


if __name__ == "__main__":
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12: 
        speak("Good morning, sir.")
    elif 12 <= hour < 18:
        speak("Good afternoon, sir.")
    else:
        speak("Good evening, sir.")

    speak("Welcome back, sir.")
    speak("Jarvis at your service. How can I help you, sir?")

    
while True:
    query = take_command()
    if not query:
        continue
    print(f"You said: {query}")

    if 'time' in query:
        tell_time()
    elif 'date' in query:
        tell_date()
    elif 'how are you' in query:
        speak("I am fine, sir. Thank you for asking.")
    elif 'i am fine' in query or 'i am also fine' in query:
        speak("That's great to hear, sir.")
    elif 'your name' in query:
        speak("I am Jarvis, your personal assistant.")
    elif 'who made you' in query:
        speak("I was created by Bragadeeshwaran.")
    elif 'who is your creator' in query:
        speak("My creator is Bragadeeshwaran.")
    elif 'what can you do' in query:
        speak("I can assist you with various tasks such as telling time, date, playing music, opening applications, taking screenshots, checking CPU usage, and more.") 
    elif 'what is your name' in query:
        speak("My name is Jarvis, your personal assistant.")
    elif 'what is your purpose' in query:   
        speak("My purpose is to assist you with your daily tasks and provide information as needed.")
    elif 'who created you' in query:
        speak("I was created by Bragadeeshwaran, a talented developer.")
    elif 'who is your owner' in query:
        speak("My owner is Bragadeeshwaran.")
    elif 'who is your boss' in query:
        speak("My boss is Bragadeeshwaran.")
    elif 'who is your master' in query:
        speak("My master is Bragadeeshwaran.")
    elif 'who is your developer' in query:
        speak("My developer is Bragadeeshwaran.")
    elif 'who is your programmer' in query:
        speak("My programmer is Bragadeeshwaran.")
    elif 'who is your father' in query:
        speak("I don't have a father, but I was created by Bragadeeshwaran.")
    elif 'what is your function' in query:
        speak("My function is to assist you with various tasks, provide information, and make your life easier.")
    elif 'what is your job' in query:
        speak("My job is to assist you with your daily tasks, provide information, and make your life easier.")
    elif 'what is your role' in query:
        speak("My role is to assist you with various tasks, provide information, and make your life easier.")
    elif 'what is your task' in query:
        speak("My task is to assist you with your daily activities, provide information, and make your life easier.")
    elif 'what is your duty' in query:
        speak("My duty is to assist you with various tasks, provide information, and make your life easier.")
    elif ' your goal' in query:
        speak("My goal is to assist you with your daily tasks, provide information, and make your life easier.")
    elif 'what is your aim' in query:
        speak("My aim is to assist you with various tasks, provide information, and make your life easier.")
    elif 'what is your purpose' in query:   
        speak("My purpose is to assist you with your daily tasks, provide information, and make your life easier.")
    elif 'what is your mission' in query:
        speak("My mission is to assist you with various tasks, provide information, and make your life easier.")
    elif 'what is your vision' in query:
        speak("My vision is to assist you with your daily tasks, provide information, and make your life easier.")
    elif 'what is your objective' in query:
        speak("My objective is to assist you with various tasks, provide information, and make your life easier.")
    elif 'what is your intention' in query:
        speak("My intention is to assist you with your daily tasks, provide information, and make your life easier.")
    elif 'Best Anime' in query:
        speak("Best Amine and my favorite anmie is Attack on taitains and Demon slayer.sir")
        
    elif 'good job' in query:
        speak("Thank you, sir. I appreciate your kind words.")
    elif 'play music' in query:
         speak("Playing your favorite song.")
         webbrowser.open("https://www.youtube.com/watch?v=zVjVqKoS9QU&list=RDzVjVqKoS9QU&start_radio=1")
    elif 'logout' in query:
        speak("Logging you out, sir.")
        os.system("shutdown -l")
    elif 'shutdown' in query:
        speak("Shutting down the system, sir.")
        os.system("shutdown /s /t 1")
    elif 'restart' in query:
        speak("Restarting the system, sir.")
        os.system("shutdown /r /t 1")
    elif 'open notepad' in query:
        speak("Opening Notepad.")
        os.system("notepad")
    elif 'open calculator' in query:
        speak("Opening Calculator.")
        os.system("calc")
    elif 'open command prompt' in query:
        speak("Opening Command Prompt.")
        os.system("start cmd")
    elif 'open chrome' in query:
        speak("Opening Google Chrome.")
        os.system("start chrome")   
    elif 'open youtube' in query:
        speak("Opening YouTube.")
        os.system("start youtube")  
    elif 'open google' in query:
        speak("Opening Google.")
        os.system("start google")
    elif 'play song' in query:
        speak("Playing a song for you.")
        os.system("start wmplayer")
    elif 'screenshot' in query:
        screenshot()
        speak("Screenshot taken and saved.")
    elif 'cpu' in query:
        cpu()
        speak("CPU and battery status checked.")
    elif 'tell me a joke' in query:
        tell_joke()
        speak("Here's a joke for you.")
    elif 'close command prompt' in query:
        speak("Closing Command Prompt.")
        os.system("taskkill /f /im cmd.exe")
    elif 'close notepad' in query:
        speak("Closing Notepad.")
        os.system("taskkill /f /im notepad.exe")
    elif 'close calculator' in query:
        speak("Closing Calculator.")
        os.system("taskkill /f /im calc.exe")
    elif 'close chrome' in query:
        speak("Closing Google Chrome.")
        os.system("taskkill /f /im chrome.exe")
    elif 'close youtube' in query:
        speak("Closing YouTube.")
        os.system("taskkill /f /im chrome.exe")
    elif 'close google' in query:
        speak("Closing Google.")
        os.system("taskkill /f /im chrome.exe")
    elif 'search youtube' in query:
        speak("What would you like to search for on YouTube?")
        search_query = take_command()
        if search_query:
            speak(f"Searching for {search_query} on YouTube.")
            play_youtube(search_query)
        else:
            speak("Please provide a search term for YouTube.")
    elif 'search google' in query:
        speak("What would you like to search for on Google?")
        search_query = take_command()
        if search_query:
            speak(f"Searching for {search_query} on Google.")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        else:
            speak("Please provide a search term for Google.")
    elif 'search file' in query:
        speak("What file would you like to search for?")
        file_name = take_command()
        if file_name:
            speak(f"Searching for {file_name}.")
            os.system(f"start search-ms:query={file_name}")
        else:
            speak("Please provide a file name to search for.")
    elif 'search file explorer' in query:
        speak("What file would you like to search for in File Explorer?")
        file_name = take_command()
        if file_name:
            speak(f"Searching for {file_name} in File Explorer.")
            os.system(f"explorer search-ms:query={file_name}")
        else:
            speak("Please provide a file name to search for in File Explorer.")
    elif 'close file explorer' in query:
        speak("Closing File Explorer.")
        os.system("taskkill /f /im explorer.exe")
    elif 'close file' in query:
        speak("Closing the file explorer.")
        os.system("taskkill /f /im explorer.exe")
    elif 'close all files' in query:
        speak("Closing all open files.")
        os.system("taskkill /f /im explorer.exe")
    elif 'close all applications' in query:
        speak("Closing all open applications.")
        os.system("taskkill /f /im chrome.exe")
        os.system("taskkill /f /im notepad.exe")
        os.system("taskkill /f /im calc.exe")
        os.system("taskkill /f /im wmplayer.exe")
    
    elif 'search in brave' in query:
        speak("What would you like to search for in Brave?")
        search_query = take_command()
        if search_query:
            speak(f"Searching for {search_query} in Brave.")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        else:
            speak("Please provide a search term for Brave.")   
    elif 'open file explorer' in query:
        speak("Opening File Explorer.")
        os.system("explorer")
    elif 'open brave' in query:
        speak("Opening Brave browser.")
        os.system("start brave")
    elif 'open firefox' in query:
        speak("Opening Firefox browser.")
        os.system("start firefox")
    elif 'open edge' in query:
        speak("Opening Microsoft Edge browser.")
        os.system("start msedge")
    elif 'close brave' in query:
        speak("Closing Brave browser.")
        os.system("taskkill /f /im brave.exe")
    elif 'close firefox' in query:
        speak("Closing Firefox browser.")
        os.system("taskkill /f /im firefox.exe")
    elif 'close edge' in query:
        speak("Closing Microsoft Edge browser.")
        os.system("taskkill /f /im msedge.exe")
    elif 'pause the music' in query:
        speak("Pausing the music.")
        os.system("nircmd mediaplay 0")
    elif 'pause the video' in query:
        speak("Pausing the video.")
        os.system("nircmd mediaplay 0")
    elif 'weather update' in query:
        speak("Please tell me the city name for the weather update.")
        city = take_command()
        if city:
            speak(f"Fetching weather update for {city}.")
            import requests
            api_key = "your_api_key_here"
            base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(base_url)
            data = response.json()
            if data["cod"] != "404":
                main = data["main"]
                temperature = main["temp"]
                pressure = main["pressure"]
                humidity = main["humidity"]
                weather_description = data["weather"][0]["description"]
                speak(f"The temperature in {city} is {temperature}°C with {weather_description}.")
                speak(f"Pressure: {pressure} hPa, Humidity: {humidity}%")
            else:
                speak("City not found. Please check the city name and try again.")  
    elif 'News update' in query:
        speak("Fetching the latest news updates.")
        import requests
        api_key = "your_news_api_key_here"
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
        response = requests.get(url)
        news_data = response.json()
        if news_data["status"] == "ok":
            articles = news_data["articles"]
            for article in articles[:5]:
                title = article["title"]
                description = article["description"]
                speak(f"Title: {title}")
                speak(f"Description: {description}")
    elif 'read pdf' in query:
        speak("Please provide the path to the PDF file you want to read.")
        pdf_path = take_command()
        if pdf_path:
            try:
                import PyPDF2
                with open(pdf_path, 'rb') as file:
                    reader = PyPDF2.PdfReader(file)
                    text = ""
                    for page in reader.pages:
                        text += page.extract_text()
                    speak(text[:500])  # Read first 500 characters
            except Exception as e:
                print("PDF error:", e)
                speak("Sorry, I couldn't read the PDF file. Please check the file path and try again.")
        else:
            speak("Please provide a valid PDF file path.")
    elif 'read text file' in query:
        speak("Please provide the path to the text file you want to read.")
        text_file_path = take_command()
        if text_file_path:
            try:
                with open(text_file_path, 'r') as file:
                    content = file.read()
                    speak(content[:500])  # Read first 500 characters
            except Exception as e:
                print("Text file error:", e)
                speak("Sorry, I couldn't read the text file. Please check the file path and try again.")
        else:
            speak("Please provide a valid text file path.")
    elif 'read selected text' in query:
        speak("Reading the selected text.")
        try:
            import pyperclip
            selected_text = pyperclip.paste()
            if selected_text:
                speak(selected_text[:500])  # Read first 500 characters
            else:
                speak("No text is currently selected.")
        except Exception as e:
            print("Clipboard error:", e)
            speak("Sorry, I couldn't read the selected text. Please try again.")
    elif 'read clipboard' in query:
        speak("Reading the clipboard content.")
        try:
            import pyperclip
            clipboard_content = pyperclip.paste()
            if clipboard_content:
                speak(clipboard_content[:500])  # Read first 500 characters
            else:
                speak("The clipboard is empty.")
        except Exception as e:
            print("Clipboard error:", e)
            speak("Sorry, I couldn't read the clipboard content. Please try again.")
    elif 'remove file' in query:
        speak("What file would you like to remove?")
        file_name = take_command()
        if file_name:
            speak(f"Removing {file_name}.")
            try:
                os.remove(file_name)
                speak(f"{file_name} has been removed successfully.")
            except Exception as e:
                print("File removal error:", e)
                speak(f"Sorry, I couldn't remove {file_name}. Please check the file name and try again.")
        else:
            speak("Please provide a file name to remove.")
    elif 'read file' in query:
        speak("What file would you like to read?")
        file_name = take_command()
        if file_name:
            speak(f"Reading {file_name}.")
            try:
                with open(file_name, 'r') as file:
                    content = file.read()
                    speak(content[:500])  # Read first 500 characters
            except Exception as e:
                print("File read error:", e)
                speak(f"Sorry, I couldn't read {file_name}. Please check the file name and try again.")
        else:
            speak("Please provide a file name to read.")
    elif 'open my documents' in query:
        speak("Opening your Documents folder.")
        os.system("explorer %USERPROFILE%\\Documents")
    elif 'open my downloads' in query:
        speak("Opening your Downloads folder.")
        os.system("explorer %USERPROFILE%\\Downloads")
    elif 'open my desktop' in query:
        speak("Opening your Desktop folder.")
        os.system("explorer %USERPROFILE%\\Desktop")
    elif 'open my pictures' in query:
        speak("Opening your Pictures folder.")
        os.system("explorer %USERPROFILE%\\Pictures")
    elif 'open my music' in query:
        speak("Opening your Music folder.")
        os.system("explorer %USERPROFILE%\\Music")
    elif 'open my videos' in query:
        speak("Opening your Videos folder.")
        os.system("explorer %USERPROFILE%\\Videos")
    elif 'open my files' in query:
        speak("Opening your Files folder.")
        os.system("explorer %USERPROFILE%\\Files")
    elif 'open my computer' in query:
        speak("Opening My Computer.")
        os.system("explorer %USERPROFILE%\\")
    elif 'open my pc' in query:
        speak("Opening My PC.")
        os.system("explorer %USERPROFILE%\\")
    elif 'open my network' in query:
        speak("Opening My Network.")
        os.system("explorer shell:NetworkFolder")
    elif 'open my recycle bin' in query:
        speak("Opening Recycle Bin.")
        os.system("explorer shell:RecycleBinFolder")
    elif 'open my control panel' in query:
        speak("Opening Control Panel.")
        os.system("control")
    elif 'open my settings' in query:
        speak("Opening Settings.")
        os.system("start ms-settings:")
    elif 'open my task manager' in query:
        speak("Opening Task Manager.")
        os.system("taskmgr")
    elif 'open my file explorer' in query:
        speak("Opening File Explorer.")
        os.system("explorer")
    elif 'open my file manager' in query:
        speak("Opening File Manager.")
    
    elif 'turn on bluetooth' in query:
        speak("Turning on Bluetooth.")
        os.system("start ms-settings:bluetooth")
    elif 'turn off bluetooth' in query:
        speak("Turning off Bluetooth.")
        os.system("start ms-settings:bluetooth")
    elif 'turn on wifi' in query:
        speak("Turning on Wi-Fi.")
        os.system("start ms-settings:network-wifi")
    elif 'change voice' in query:
        speak("Changing voice.")
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if len(voices) > 1:
            engine.setProperty('voice', voices[1].id)
            speak("Voice changed successfully.")
        else:   
            speak("Sorry, I couldn't change the voice. Only one voice is available.")
    elif 'increase volume' in query:
        speak("Increasing volume.")
        os.system("nircmd.exe changesysvolume 5000")
    elif 'decrease volume' in query:
        speak("Decreasing volume.")
        os.system("nircmd.exe changesysvolume -5000")
    elif 'mute volume' in query:
        speak("Muting volume.")
        os.system("nircmd.exe mutesysvolume 1")
    elif 'unmute volume' in query:
        speak("Unmuting volume.")
        os.system("nircmd.exe mutesysvolume 0")
    elif 'increase brightness' in query:
        speak("Increasing brightness.")
        os.system("nircmd.exe changebrightness 10")
    elif 'decrease brightness' in query:
        speak("Decreasing brightness.")
        os.system("nircmd.exe changebrightness -10")
    elif 'increase screen brightness' in query:
        speak("Increasing screen brightness.")
        os.system("nircmd.exe changebrightness 10")
    elif 'decrease screen brightness' in query:
        speak("Decreasing screen brightness.")
        os.system("nircmd.exe changebrightness -10")
    elif 'increase volume' in query:
        speak("Increasing volume.")
        os.system("nircmd.exe changesysvolume 5000")    
    elif 'decrease volume' in query:
        speak("Decreasing volume.")
        os.system("nircmd.exe changesysvolume -5000")
    elif 'start jarvis' in query:
        speak("Starting Jarvis.")
        os.system("python jarvis.py")
    elif 'start jarvis assistant' in query:
        speak("Starting Jarvis Assistant.")
        os.system("python jarvis.py")
    elif 'start jarvis ai' in query:
        speak("Starting Jarvis AI.")
        os.system("python jarvis.py")
    elif 'start jarvis ai assistant' in query:
        speak("Starting Jarvis AI Assistant.")
        os.system("python jarvis.py")
    elif 'start pc' in query:
        speak("Starting your PC.")
        os.system("start")
    elif 'power on pc' in query:
        speak("Powering on your PC.")
        os.system("start")
    elif 'automate jarvis' in query:
        speak("Automating Jarvis.")
        os.system("python jarvis.py")
    elif 'show all commands' in query:
        speak("Here are the commands you can use:")
        commands = [
            "time - Tells the current time",
            "date - Tells today's date",
            "how are you - Asks how Jarvis is doing",
            "play music - Plays a song",
            "open notepad - Opens Notepad",
            "open calculator - Opens Calculator",
            "open command prompt - Opens Command Prompt",
            "open chrome - Opens Google Chrome",
            "open youtube - Opens YouTube",
            "open google - Opens Google",
            "screenshot - Takes a screenshot",
            "cpu - Checks CPU and battery status",
            "tell me a joke - Tells a joke",
            "search youtube - Searches for a video on YouTube",
            "search google - Searches for a term on Google",
            "search file explorer - Searches for a file in File Explorer",
            "send email - Sends an email",
            "remember - Remembers something for you",
            "wikipedia - Searches Wikipedia for a topic"
        ]
        for command in commands:
            speak(command)
            print(command)
    elif 'show all query' in query:
        speak("Here are the queries you can use:")
        queries = [
            "time - Tells the current time",
            "date - Tells today's date",
            "how are you - Asks how Jarvis is doing",
            "play music - Plays a song",
            "open notepad - Opens Notepad",
            "open calculator - Opens Calculator",
            "open command prompt - Opens Command Prompt",
            "open chrome - Opens Google Chrome",
            "open youtube - Opens YouTube",
            "open google - Opens Google",
            "screenshot - Takes a screenshot",
            "cpu - Checks CPU and battery status",
            "tell me a joke - Tells a joke",
            "search youtube - Searches for a video on YouTube",
            "search google - Searches for a term on Google",
            "search file explorer - Searches for a file in File Explorer",
            "send email - Sends an email",
            "remember - Remembers something for you",
            "wikipedia - Searches Wikipedia for a topic"
        ]
        for query in queries:
            speak(query)
            print(query)
    



    


  
     


    elif 'search file explorer' in query:
        speak("What file would you like to search for?")
        file_name = take_command()
        if file_name:
            speak(f"Searching for {file_name} in File Explorer.")
            os.system(f"explorer search-ms:query={file_name}")
        else:
            speak("Please provide a file name to search for.")
    elif 'search in chrome' in query:
        speak("What would you like to search for?")
        search_query = take_command()
        if search_query:
            speak(f"Searching for {search_query} in Chrome.")
            import webbrowser
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        else:
            speak("Please provide a search term.")
    elif 'send email' in query:
        # ✅ send email block should be indented under this elif
        try:
            speak("To whom should I send the email?")
            to = take_command()
            speak("What should be the subject?")
            subject = take_command()
            speak("What is the message?")
            body = take_command()
            send_email(to, subject, body)
            speak("Email sent successfully.")
        except Exception as e:
            print("Email error:", e)
            speak("Sorry sir, I couldn't send the email.")
    elif 'remember' in query:
        speak("What should I remember?")
        data = take_command()
        with open("data.txt", "w") as f:
            f.write(data)
        speak("Yes sir, I will remember that.")
    elif 'do you know anything' in query:
        try:
            with open("data.txt", "r") as f:
                saved = f.read().strip()
            if saved:
                speak(f"Yes sir, you asked me to remember:" +saved)
            else:
                speak("I don't have anything saved in my memory.")
        except FileNotFoundError:
            speak("I don't have anything saved in my memory.")
        
        

    
    elif 'wikipedia' in query:
        # ✅ wikipedia block also properly nested
        speak("Searching Wikipedia...")
        topic = query.replace("wikipedia", "").strip()
        if topic:
            try:
                results = wikipedia.summary(topic, sentences=2)
                print(results)
                speak("According to Wikipedia, " + results)
            except Exception as e:
                print("Wiki error:", e)
                speak("Sorry, I couldn't find that topic on Wikipedia.")
        else:
            speak("Please mention a topic after saying Wikipedia.")
    elif any(w in query for w in ['exit','stop','quit','bye','go offline','shutdown','turn off','close']):
        speak("Goodbye, sir.")
        sys.exit(0)
    else:
        speak("Sorry, I didn't catch that. Please try again.")


