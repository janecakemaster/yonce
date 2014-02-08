from flask import Flask, request, redirect
import twilio.twiml
<<<<<<< HEAD
from twilio.rest import TwilioRestClient

app = Flask(__name__)

account_sid = "ACd7e41c537e6666301b0318d0d4c7b927"
auth_token = "1ff12b5965e927f8267ff451fff8687d"
client = TwilioRestClient(account_sid, auth_token)

request_data = {}
=======
from random import randint

app = Flask(__name__)

songs = ["misscarter", "womp", "ifiwereaboy", "memyselfandi", "irreplacable",
         "singleladies", "freakumdress", "diva", "runtheworld", "flawless"]
bucket_url = "https://s3.amazonaws.com/yonce/"
>>>>>>> 25ff68f51a95e23a9b83a603209acafc6687ab7b


@app.route("/", methods=['GET', 'POST'])
def start_call():
    """Welcome caller and present menu of songs."""

    resp = twilio.twiml.Response()
<<<<<<< HEAD
    # Greet the caller by name
    resp.say("Do you identify with Beyonce-ay or Jay Zeeeee?")
    # Play an MP3
    #resp.play("https://s3.amazonaws.com/yonce/upgradeu.mp3")
    resp.record(maxLength="2", transcribeCallback="/transcribed")
    return str(resp)


@app.route("/handle-recording", methods=['GET', 'POST'])
def handle_recording():
    transcription = request_data["TranscriptionText"]
    resp = twilio.twiml.Response()
    resp.say(transcription)
=======
    resp.say("Who's the better half: Beyonsay or Jay zee?")
    with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
        g.say("""Press 1 for Beyonce-ay.
                 Press 2 for Jay zee.""")
    return str(resp)


@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
    """Get fierceness rating."""

    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == "1":
        resp = twilio.twiml.Response()
        with resp.gather(numDigits=1, action="/pick-song", method="POST") as g:
            g.say("""On a scale of one to nine, how fierce do you feel today?
                     Select a number from 1 to 9.""")
        return str(resp)
    elif digit_pressed == "2":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[0] + ".mp3")
        return str(resp)
    else:
        return redirect("/")


@app.route("/pick-song", methods=['GET', 'POST'])
def pick_song():
    if digit_pressed == "1":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[1] + ".mp3")
        return str(resp)
    elif digit_pressed == "2":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[2] + ".mp3")
        return str(resp)

>>>>>>> 25ff68f51a95e23a9b83a603209acafc6687ab7b
    return str(resp)


@app.route("/transcribed", methods=['POST'])
def transcribed():
    resp = twilio.twiml.Response()
    resp.say("It's in the transcribed")
    '''RecordingUrl = self.request.get("RecordingUrl")
    TranscriptionStatus = self.request.get("TranscriptionStatus")
    Caller = self.request.get("Caller")
    TranscriptionText = self.request.get("TranscriptionText")
    request_data = json.loads(request.data)
    transcription = request_data["TranscriptionText"]
    resp = twilio.twiml.Response()
    resp.say(transcription)'''
    #return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
