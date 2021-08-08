import random

print("Welcome to my YouTube :)")

current_video = None
is_paused = False
playlist_name = None

another_command = True
while another_command is True:
    command = input("What would you like to do- \nSHOW ALL VIDEOS \nPLAY \nSTOP \nPLAY RANDOM \nPAUSE "
                    "\nCONTINUE \nSHOW PLAYING \n")

    if command == "SHOW ALL VIDEOS":
        print("Here's a list of all available videos:")
        video_file = open("videos.txt", "r")

        for video in video_file.readlines():

            print(video)

        video_file.close()  # Always need to close the file.

    elif command.upper() == "PLAY":

        valid_input = False

        while valid_input is False:

            video_title = input("Please enter the video title: ")

            if video_title == "Amazing Cats":
                valid_input = True
                is_paused = False

            elif video_title == "Funny Dogs":
                valid_input = True
                is_paused = False

            elif video_title == "Another Cat Video":
                valid_input = True
                is_paused = False

            elif video_title == "Life At Google":
                valid_input = True
                is_paused = False

            elif video_title == "Video About Nothing":
                valid_input = True
                is_paused = False

            else:
                print("Cannot play video: Video does not exist.")
                valid_input = False

            if current_video is None and valid_input is True:
                print("Playing video: " + video_title)
                current_video = video_title
            elif current_video is not None and valid_input is True:
                print("Stopping video: " + current_video)
                print("Playing video: " + video_title)
                current_video = video_title

    elif command.upper() == "STOP":

        if current_video is None:
            print("Cannot stop video: No video is currently playing")
        else:
            print("Stopping video: " + current_video)
            current_video = None

    elif command.upper() == "PLAY RANDOM":

        with open("videos.txt", "r") as file:
            all_videos = file.read()
            videos = list(map(str, all_videos.splitlines()))
            video_title = random.choice(videos)

        if current_video is None:
            print("Playing video: " + video_title)
            current_video = video_title
        elif current_video is not None:
            print("Stopping video: " + current_video)
            print("Playing video: " + video_title)
            current_video = video_title
        else:
            print("No videos available")

    elif command.upper() == "PAUSE":
        if current_video is None:
            print("Cannot pause video: No video is currently playing")
        elif current_video is not None and is_paused is False:
            print("Pausing video: " + current_video)
            is_paused = True
        elif current_video is not None and is_paused is True:
            print("Video already paused: " + current_video)

    elif command.upper() == "CONTINUE":
        if is_paused is True and current_video is not None:
            is_paused = False
            print("Continuing video: " + video_title)
        elif is_paused is False and current_video is not None:
            print("Cannot continue video: Video is not paused")
        elif current_video is None:
            print("Cannot continue video: No video is currently playing")

    elif command.upper() == "SHOW PLAYING":
        if current_video is None:
            print("No video is currently playing")
        elif current_video is not None and is_paused is False:
            print("Currently playing: " + current_video)
        elif current_video is not None and is_paused is True:
            print("Currently playing: " + current_video + " - PAUSED")

    else:
        print("No command " + command + ". Please try again.")
        another_command = True

    command_enter = input("Would you like to enter another command? YES or NO: ")

    if command_enter.upper() == "YES":
        another_command = True
    elif command_enter.upper() == "NO":
        another_command = False
        print("YouTube closed.")
    else:
        print("Error")
