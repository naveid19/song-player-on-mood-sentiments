##### music player testing version_____1.0 --- developing phase


from pygame import mixer
  
# Starting the mixer
mixer.init()

p = "Impossible - Alan Walker (Lyrics).mp3"
r = "Nurko - Faith (ft. Dia Frampton).mp3"
q = "Taylor Swift - End Game (feat. Ed Sheeran  Future) [mp3clan].mp3"
s = "With Løve - So Long (Lyrics) ft. Hvnnibvl.mp3"
t = "Taylor Swift - Blank Space (Gibs Ft. Noize Remix 2015) [320].mp3"

sarr = [p,r,q,s,t]

def player(path_song):
    # Loading the song
    mixer.music.load(path_song)
    
    # Setting the volume
    mixer.music.set_volume(0.7)
    
    # Start playing the song
    mixer.music.play()


        # infinite loop
    while True:
        
        print("Press 'p' to pause, 'r' to resume, n to next")
        # print("Press 'e' to exit the program")
        query = input("  ")
        
        if query == 'p':
    
            # Pausing the music
            mixer.music.pause()     
        elif query == 'r':
    
            # Resuming the music
            mixer.music.unpause()
        elif query == 'n':
    
            # next song
            mixer.music.stop()
            break
        # elif query == 'e':
        #     break
    

#calling function
for i in range (len(sarr)+1):


    pp = sarr[i]
    player(pp)

