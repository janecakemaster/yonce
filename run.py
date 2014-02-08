from flask import Flask, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient

app = Flask(__name__)


account_sid = "ACd7e41c537e6666301b0318d0d4c7b927"
auth_token  = "1ff12b5965e927f8267ff451fff8687d"
client = TwilioRestClient(account_sid, auth_token)
 

# Try adding your own number to this list!
callers = {
    "+12014463242": "Jane",
    "+16467633964": "Lisa",
    "+13046462355": "Melissa"
}


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Say a caller's name, and play an MP3 for them."""

    from_number = request.values.get('From', None)
    if from_number in callers:
        caller = callers[from_number]
    else:
        caller = "Monkey"

    resp = twilio.twiml.Response()
    # Greet the caller by name
    resp.say("Do you identify with Beyonce-ay or Jay Zeeeeeee?")
    # Play an MP3
    #resp.play("https://s3.amazonaws.com/yonce/upgradeu.mp3")
    resp.record(maxLength="2", transcribe="true" action="/handle-recording")

    return str(resp)


@app.route("/handle-recording", methods=['GET', 'POST'])
def handle_recording():
    """Play back the caller's recording."""
 
 	transcription = client.transcriptions.get("TR8c61027b709ffb038236612dc5af8723")
	resp = twilio.twiml.Response()
	resp.say(resptranscription.transcription_text)
 '''   recording_url = request.values.get("RecordingUrl", None)
 
    resp = twilio.twiml.Response()
    resp.say("Thanks for howling... take a listen to what you howled.")
    resp.play(recording_url)
    resp.say("Goodbye.")'''
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
