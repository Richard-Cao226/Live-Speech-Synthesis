import pyttsx3

engine = pyttsx3.init()

print("Commands:")
print("/faster")
print("/slower")
print("/change_voice")
print("\n")
voices = engine.getProperty("voices")
current_voice = 0
text = ""
text = input()
while len(text) > 0:
	if text == "/faster":
		engine.setProperty("rate", engine.getProperty("rate") + 100)
		engine.runAndWait()
	elif text == "/slower":
		engine.setProperty("rate", engine.getProperty("rate") - 100)
		engine.runAndWait()
	elif text == "/change_voice":
		if current_voice == len(voices) - 1:
			current_voice = 0
		else:
			current_voice += 1
		engine.setProperty("voice", voices[current_voice].id)
	else:
		engine.say(text)
		engine.runAndWait()
	text = input()