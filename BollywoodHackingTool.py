import pyttsx3
import time
import random

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('voice', 'english')  # Set voice (may vary by system)
engine.setProperty('rate', 150)  # Speed of speech

def speak(text):
    """Function to make the tool 'speak' with dramatic flair."""
    print(f"🔊 {text}")
    engine.say(text)
    engine.runAndWait()

def fake_progress_bar(duration):
    """Simulate a dramatic progress bar."""
    for i in range(101):
        print(f"\rHacking Progress: [{i}%] {'█' * (i // 5)}", end="")
        time.sleep(duration / 100)
    print()

def bollywood_hacking_simulation():
    """Main function to simulate Bollywood-style hacking."""
    speak("Initializing Bollywood Hacking Tool! Coded by the legendary Pakistani Ethical Hacker, Mr. Sabaz Ali Khan!")
    time.sleep(2)
    
    print("🌟 Welcome to the Ultimate Cyber Bollywood Experience 🌟")
    speak("Accessing global networks. This is no ordinary hack!")
    time.sleep(1)
    
    # Fake network scanning
    print("🔍 Scanning International Servers...")
    fake_progress_bar(5)
    speak("Servers located! Bypassing firewalls with Bollywood-style encryption!")
    
    # Fake data breach
    print("⚠️ Attempting to Breach Mainframe...")
    time.sleep(2)
    speak("Mainframe compromised! Downloading top-secret Bollywood scripts!")
    fake_progress_bar(3)
    
    # Dramatic twist
    print("🚨 Alert: Counter-Hack Detected!")
    speak("Oh no! The villains are fighting back! Activating Khan's Secret Algorithm!")
    time.sleep(2)
    
    # Fake countermeasure
    print("🔐 Deploying Anti-Hack Shield...")
    fake_progress_bar(4)
    speak("Counter-hack neutralized! Sabaz Ali Khan never fails!")
    
    # Victory message
    print("🎉 Hack Complete! Bollywood Database Unlocked!")
    speak("Mission accomplished! The world is safe, thanks to Mr. Sabaz Ali Khan!")
    print("💾 Data Secured: 1 TB of Bollywood Movie Secrets")
    print("🔥 Shutting Down System to Avoid Trace...")
    time.sleep(2)
    speak("System offline. Until next time, stay filmy, stay safe!")

if __name__ == "__main__":
    try:
        bollywood_hacking_simulation()
    except KeyboardInterrupt:
        speak("Hack aborted! Sabaz Ali Khan is disappointed!")
        print("\n🛑 Hack Terminated by User")