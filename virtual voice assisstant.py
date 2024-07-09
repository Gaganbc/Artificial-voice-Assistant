import speech_recognition as sr 
import pyttsx3
import webbrowser
import datetime
import wikipedia 
import pyjokes 
import requests
engine = pyttsx3.init()
voices = engine.getProperty('voices') engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()
def speak(text): engine.say(text) engine.runAndWait()
def interrupt_speech(): engine.stop()
def listen():
with sr.Microphone() as source: print("Listening...") 
recognizer.adjust_for_ambient_noise(source) audio = recognizer.listen(source)
 try:
print("Recognizing...")
query = recognizer.recognize_google(audio) print(f"User said: {query}")
return query.lower()
except Exception as e:
print("Sorry, I couldn't understand that.") return ""
def play_song(song_name):
search_query = "youtube " + song_name
url = f"https://www.youtube.com/results?search_query={search_query}" webbrowser.open(url)
speak(f"Now playing {song_name} on YouTube.")
def get_time():
current_time = datetime.datetime.now().strftime("%I:%M %p") return current_time
def get_date():
current_date = datetime.datetime.now().strftime("%A, %B %d, %Y") return current_date
def get_wikipedia_details(topic): try:
result = wikipedia.summary(topic, sentences=2) print("Fetching Wikipedia details...")
return result

 print(e.options)
return ""
except wikipedia.exceptions.PageError as e:
print("No Wikipedia page found for the given query.") return ""
def tell_joke():
joke = pyjokes.get_joke() speak(joke)
def get_weather(city):
api_key = "YOUR_OPENWEATHERMAP_API_KEY"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
try:
response = requests.get(url) response.raise_for_status() data = response.json()
if data["cod"] == 200:
weather_info = data["weather"][0]["description"]
temperature = data["main"]["temp"]
speak(f"The weather in {city} is {weather_info} with a temperature of {temperature} degrees
Celsius.") else:
speak("Sorry, I couldn't fetch the weather information for that city.")
except requests.exceptions.RequestException as e:
speak("Sorry, I couldn't fetch the weather information. Please check your internet connection.") except Exception as e:
speak("Sorry, an error occurred while fetching the weather information.")

 def get_news(city):
news_api_key = "YOUR_NEWS_API_KEY"
url = f"https://newsapi.org/v2/top-headlines?q={city}&apiKey={news_api_key}"
try:
response = requests.get(url) response.raise_for_status() data = response.json()
if data["status"] == "ok":
articles = data["articles"]
speak(f"Here are the top headlines for {city}:")
for article in articles:
speak(article["title"])
else:
speak(f"Sorry, I couldn't fetch the news for {city}.")
except requests.exceptions.RequestException as e:
speak("Sorry, I couldn't fetch the news. Please check your internet connection.") except Exception as e:
speak("Sorry, an error occurred while fetching the news.")
def get_city():
speak("Which city's news would you like to know?") city = listen()
return city
def main():
speak("Hello! I am your virtual assistant. How can I help you today?")
while True:
command = listen()
 if "hi" in command: speak("Hi there!")
elif "how are you" in command: speak("I'm doing well, thank you!")
elif "are you single" in command:
speak("No, I'm in a relationship with Wi-Fi.")
elif "go" in command: speak("No, Not Interested")
elif "about you" in command:
speak("Hii!! I am a virtual voice assistant. I am here to help you with whatever you need. If
you want anything, let me know....thank you") elif "play some music" in command:
speak("Sure! What song would you like to play?") song_name = listen()
play_song(song_name)
elif "time" in command:
current_time = get_time()
speak(f"The current time is {current_time}")
elif "date" in command: current_date = get_date() speak(f"Today is {current_date}")
elif "weather" in command:
speak("Sure! Which city's weather would you like to know?") city = listen()
get_weather(city)
elif "news" in command: city = get_city() get_news(city)
elif "search" in command:
speak("What do you want to search for on Wikipedia?")
 search_query = listen()
wikipedia_details = get_wikipedia_details(search_query) if wikipedia_details:
speak("Here is what I found on Wikipedia:")
speak(wikipedia_details) else:
speak("Sorry, I couldn't find any information on Wikipedia.") elif "joke" in command:
tell_joke()
elif "goodbye" in command:
speak("Goodbye! Have a great day!") elif "goodnight" in command:
speak("Goodnight! Sweet dreams!!")
break else:
speak("Sorry, I don't understand that. Could you say that again?")
if __name__ == "__main__": main()