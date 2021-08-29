########## project module 1 version 1.0 --- developing phase



#enter the number of your sentiments
import os
mood = ["Sad", "Happy", "Normal"]
print (mood)
sentimments = input("enter your mood  ")
songs_for_sad = [ "Sad1", "Sad2", "Sad3" ]
songs_for_Happy = ["Happy1", "Happy2", "Happy3"]
songs_for_Normal = ["Normal1","Normal2", "Normal3"]
path_file = ""

if sentimments in mood:

    for songs in range(len(mood)) :


        if sentimments == mood[songs]:
            for i in range(len (songs_for_sad)):
                song = songs_for_sad[i]
                os.system("start " +song + ".mp3")
            break

        if sentimments == mood[songs]:
            for i in range(len (songs_for_sad)):
                print (songs_for_Happy[i])
            break

        if sentimments == mood[songs]:
            for i in range(len (songs_for_sad)):
                print (songs_for_Normal[i])
            break



else:
    print("wrong entry")


