from gtts import gTTS
from playsound import playsound

def text_to_speech(text, lang='hi'):
    speech = gTTS(text=text, lang=lang, slow=False)
    speech.save("output.mp3")
    playsound("output.mp3")

if __name__ == "__main__":
    input_text = input("Enter the Hindi text: ")
    text_to_speech(input_text)

#कर्म करो फल की इच्छा मत करो
    #कर्म करो फल की इच्छा मत करो, ज़िंदा रहना है तो मोदी मोदी कहना होगा