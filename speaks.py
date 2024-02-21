# Python SAPI Voice
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

print("Enter the word you want to speak (-1 to stop)")
s = input()
while s != "-1":
    speaker.Speak(s)
    print("Enter the word you to speak (-1 to stop)")
    s = input()
