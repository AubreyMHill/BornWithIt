import wave
import pyaudio
import time
global user
def set_globvar_to_one():
    global user    # Needed to modify global copy of globvar
    user = "default"
def path_to_wav(number):
    # this is the chain l   ogic of the crap
    global user
    print("Current User is :  " + user)
    if (number == "14850070"):
        user = "David"
        print("new user is   " + user)
    if (number == "05892054"):
        user = "Marilyn"
        print("new user is   " + user)
    if(user is "David"):
        return "/Users/Aubrey/Desktop/MSBWI/MSBWI/David/" + number + ".wav"
    if(user is "Marilyn"):
        return "/Users/Aubrey/Desktop/MSBWI/MSBWI/Marilyn/" + number + ".wav"
def py_game_play(number):
    chunk = 1024
    try:
        f = wave.open(path_to_wav(number), "rb")
    except FileNotFoundError:
        print("File does not exist")
        return
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    data = f.readframes(chunk)
    print("should be playing the song now")
    while len(data) > 0:
        stream.write(data)
        data = f.readframes(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("Done")
def main():
    print("Starting")
main()
set_globvar_to_one()
tapped =False
while tapped != True:
    tapped = True
    currentRfid = input("Please Enter Your RFID ")
    if currentRfid.isdigit()and len(currentRfid)>= 8:
        print ("Your rfid is " + currentRfid)
        py_game_play(currentRfid)
    else:
        print ("This is an invalid card try again.")
    time.sleep(.5)
    tapped= False
