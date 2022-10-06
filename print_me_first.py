from datetime import datetime

"""
Function name: print_me_first
Function description: To write the program information at the bottom right
                      of the window next to quit button including author and
                      current time
@param author - author of the program
@return msg - info to be printed
"""
def print_me_first(author):
    #Initialize and sets variables
    currentTime = datetime.now()
    timestampStr = currentTime.strftime("%m-%d-%y %H:%M:%S")

    #Creates strings for name, program name, and time
    #and storing it all in msg
    name = author + " - CNET 142" + "\n"
    time = timestampStr + "\n"
    msg = name + time

    return msg
