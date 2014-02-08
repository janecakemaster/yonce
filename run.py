from flask import Flask, request, redirect
import twilio.twiml
from rdio import Rdio

app = Flask(__name__)

rdio = Rdio(("jxd3ma99xyzd52nkq88rsyp8", "94xBwq3Pkz"))

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
    resp.say("Do you identify with Beyonce-ay or Jay Zee?")
    # Play an MP3
    #resp.play("https://s3.amazonaws.com/yonce/upgradeu.mp3")
    resp.record(maxLength="30", action="/handle-recording")

    return str(resp)


@app.route("/play", methods=['GET', 'POST'])
def play_rdio():
    ian = rdio.call("findUser", {"vanityName": "ian"})
    if (ian["status"] == "ok"):
        return str(ian["result"]["lastName"])
    else:
        return str("ERROR: " + ian["message"])


@app.route("/handle-recording", methods=['GET', 'POST'])
def handle_recording():
    """Play back the caller's recording."""

    recording_url = request.values.get("RecordingUrl", None)

    resp = twilio.twiml.Response()
    resp.say("Thanks for howling... take a listen to what you howled.")
    resp.play(recording_url)
    resp.say("Goodbye.")
    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
