from nltk.corpus import wordnet as wn
import twilio.twiml

def synonym_lists(key_word):
    #where lovelife = string describing caller's love life
    mergedlist = []
    #get synonyms for word
    for ss in wn.synsets(key_word):
#get similar words
        for sim in ss.similar_tos():
            syns = [n.replace('_', ' ') for n in ss.lemma_names]
            syns += [n.replace('_', ' ') for n in sim.lemma_names]
            #combine similar words into one list 
            mergedlist = mergedlist + syns
            #convert list to a set to remove duplicates
            merged_set = set(mergedlist)
    return merged_set

def find_song(answer):
    #key_words
    words = ["confident", "single", "in_love"]
    #making a dictionary to associate song titles with synonyms
    the_dict = dict()
    the_dict["Flawless"] = synonym_lists(words[0])
    the_dict["Single Ladies"] = synonym_lists(words[1])
    the_dict["Crazy in Love"] = synonym_lists(words[2])
    song = "Telephone"
    for key in the_dict:
        for synonym in the_dict[key]:
            if synonym in answer:
                print("You should play " + key)
                song = key
    play_bey(song)

def play_bey(song_title):
    resp = twilio.twiml.Response()
    if song_title == "Flawless":
        resp.play("https://s3.amazonaws.com/yonce/upgradeu.mp3")
    elif song_title == "Single Ladies":
        resp.play("https://s3.amazonaws.com/yonce/upgradeu.mp3")
    elif song_title == "Crazy in Love":
        resp.play("https://s3.amazonaws.com/yonce/upgradeu.mp3")
    else:
        resp.play("https://s3.amazonaws.com/yonce/upgradeu.mp3")

#should print yes
play_bey("I am confident")
#should print nothing
play_bey("I am dasd")
