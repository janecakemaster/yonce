from flask import Flask, request, redirect
import twilio.twiml
from random import randint

app = Flask(__name__)

songs = ["drunkinlove", "loveontop", "runtheworld", "singleladies", "halo",
         "sweetdreams", "crazyinlove", "irreplacable"]
bucket_url = "https://s3.amazonaws.com/yonce/"


@app.route("/", methods=['GET', 'POST'])
def start_call():
    """Welcome caller and present menu of songs."""

    resp = twilio.twiml.Response()
    resp.say("THIS IS THE GREETING FOR THE CALLER")
    resp.say("more stuff")
    resp.say("Listen up for the menu options")
    # Play an MP3
    with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
        g.say("""Press 1 for a random song.
                 Press 2 for Drunk in Love.
                 Press 3 for Love on Top.
                 Press 4 for Run The World (Girls).
                 Press 5 for Single Ladies (Put A Ring On It).
                 Press 6 for Halo.
                 Press 7 for Sweet Dreams.
                 Press 8 for Crazy In Love (Featuring Jay-Z).
                 Press 9 for Irreplacable.
                 To hear the menu again, wait or press 0.""")
    return str(resp)


@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
    """Handle key press from a user."""

    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == "1":
        resp = twilio.twiml.Response()
        rando = random.randint(0, 7)
        resp.play(bucket_url + songs[rando] + ".mp3")
        return str(resp)

    elif digit_pressed == "2":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[0] + ".mp3")
        return str(resp)

    elif digit_pressed == "3":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[1] + ".mp3")
        return str(resp)

    elif digit_pressed == "4":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[2] + ".mp3")
        return str(resp)

    elif digit_pressed == "5":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[3] + ".mp3")
        return str(resp)

    elif digit_pressed == "6":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[4] + ".mp3")
        return str(resp)

    elif digit_pressed == "7":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[5] + ".mp3")
        return str(resp)

    elif digit_pressed == "8":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[6] + ".mp3")
        return str(resp)

    elif digit_pressed == "9":
        resp = twilio.twiml.Response()
        resp.play(bucket_url + songs[7] + ".mp3")
        return str(resp)

    # If the caller pressed anything but 1, redirect them to the homepage.
    else:
        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
