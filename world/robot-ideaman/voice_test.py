try:
    import pyttsx3
except ImportError:
    print("pyttsx3 is not installed.")
    print("Run: pip install pyttsx3")
    raise SystemExit(1)

speaker = pyttsx3.init()
speaker.setProperty("rate", 180)
speaker.setProperty("volume", 1.0)

print("Testing The Idea Dealer voice...")
speaker.say("Ladies and gentlemen, The Idea Dealer is now speaking.")
speaker.runAndWait()
print("Voice test finished.")
