from flask import Flask, request, redirect, render_template
import twilio.twiml
from random import randint

app = Flask(__name__)

songs = ["itsbey", "womp", "ifiwereaboy", "memyselfandi", "irreplaceable",
         "singleladies", "freakumdress", "diva", "runtheworld", "flawless",
         "bonus", "mscarter"]
bucket_url = "https://s3.amazonaws.com/yonce/"


@app.route("/", methods=['GET', 'POST'])
def start_call():
    """Welcome caller and present menu of songs."""

    resp = twilio.twiml.Response()
    resp.play(bucket_url + songs[0] + ".mp3")
    resp.say("Who's the better half: Beyonsay or Jay zee?")
    with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
        g.say("""Press 1 for Beyonce-ay.
                 Press 2 for Jay zee.""")
    return render_template("template.html")

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
        resp.play(bucket_url + songs[11] + ".mp3")
        return str(resp)
    else:
        return redirect("/")


@app.route("/pick-song", methods=['GET', 'POST'])
def pick_song():
    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == "1":
        resp = twilio.twiml.Response()
        # resp.say("something")
        resp.play(bucket_url + songs[1] + ".mp3")
        return str(resp)
    elif digit_pressed == "2":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[2] + ".mp3")
        return str(resp)
    elif digit_pressed == "3":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[3] + ".mp3")
        return str(resp)
    elif digit_pressed == "4":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[4] + ".mp3")
        return str(resp)
    elif digit_pressed == "5":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[5] + ".mp3")
        return str(resp)
    elif digit_pressed == "6":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[6] + ".mp3")
        return str(resp)
    elif digit_pressed == "7":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[7] + ".mp3")
        return str(resp)
    elif digit_pressed == "8":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[8] + ".mp3")
        return str(resp)
    elif digit_pressed == "9":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[9] + ".mp3")
        return str(resp)
    else:
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[10] + ".mp3")
        return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
