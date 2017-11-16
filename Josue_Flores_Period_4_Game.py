attempt_one = "false"
attempt_two = "false"
key = "false"
def leche():
    print (''' _______  _______  _______  _______  _______  _______  \n'''
        '''(  ____ \(  ____ \(  ____ \(  ___  )(  ____ )(  ____ \ \n'''
        '''| (    \/| (    \/| (    \/| (   ) || (    )|| (    \/ \n'''
        '''| (__    | (_____ | |      | (___) || (____)|| (__   \n'''  
        '''|  __)   (_____  )| |      |  ___  ||  _____)|  __)   \n''' 
        '''| (            ) || |      | (   ) || (      | (       \n'''
        '''| (____/\/\____) || (____/\| )   ( || )      | (____/\ \n'''
        '''(_______/\_______)(_______/|/     \||/       (_______/ \n''')
    print ('''\nBy Josue Flores\n'''
            '''and Cameron Silva\n'''
            '''and Gabriel Bermudez''')
    milk()
def milk():
    initiate = raw_input("Type 'start' to start game: ")
    if initiate == "start":
        print "You are laying on the ground with your eyes closed. The air smells a bit dusty. You can hear the distant sound of nothing ringing in your ears. Your head is throbbing. You should wake up." 
        sandia()
    elif initiate != "start":
        print "Please follow directions"
        milk()
def sandia():
    rise = raw_input("Type 'open': ")
    if rise == "open":
        print "What do you want to open?"
        watermelon()
    elif rise != "open":
        print "Try again"
        sandia()
def watermelon():
    okay = raw_input("Now type 'eyes' to open your eyes: ")
    if okay == "eyes":
        print "You open your eyes to see that you are in a small cuboidal room. All the walls are a very bright white. The only two things you can see in this room are a door and a key."
        cup()
    elif okay == "mouth":
        print "You open your mouth. Great. Now you're just letting the dusty air into your mouth. You can literally taste the room. In fact, you have such a heightened sense of taste that you can suddenly see in flavors. Overwhelmed by all the stimuli, you quickly close your mouth."
        watermelon()
    elif okay != "eyes" or "mouth":
        print "You can't open that"
        watermelon()
def cup():
        lettuce = raw_input("What do you want to do?")
        if lettuce == "open":
            bowl()
        elif lettuce == "pick up":
            plate()
        elif lettuce != "open" or "pick up":
            print "You are physically incapable of doing that. Try something else."
            cup()
def bowl():
    tomato = raw_input("What do you want to open")
    if key == "false":
        if tomato == "door":
            if attempt_one == "false":
                attempt_one = "true"
                print "You try jiggling the door knob, but the door doesn't seem to open. You gently touch the door and politely ask it to open, but it still refuses to budge. How rude. You begin knocking on the door aggressively, yelling at it to open. After about 5 minutes, the door still hasn't opened. You give up and step back. the door in front of you is very stubborn. It obviously isn't going to listen to you. Maybe the key over there can be a bit more persuasive. You should definitely go pick up that key, and totally not try opening the door again until you do. You wink at yourself."
                cup()
            elif attempt_one == "true":
                if attempt_two == "false":
                    attempt_two ="true"
                    print "You're in front of the door again. You have flashbacks to your previous attempts to open this stubborn object that satnds in your way. You begin kicking the door furiously. You succeeded in doing some damage....to your foot. You try intimidating the door, You begin to stare it down. If you could beat this door aty a staring contest, it will surely open. A minute into this hopeless contest, your eyes are tearing up profusely. The pain is almsot unbearable, yet it hurts so good. You blink. Defeated, you back away from the door. Maybe next time."
                    cup()
                elif attempt_two == "true":
                    print "This is it. You're finally going to get that door open. you are standing across from the door, as far back against the wall as you can be. You ready yourself to charge staright into the door. If this doesn't open the door, you don't know what will. You odnw in your head....3....2....1....GO. You sprint staright at the door. The door gets closer and closer and closer....and then you hit it. The world goes dark. You managed to open the door, but you also somehow snapped your neck on the door. You may have rammed your head into it a bit too hard. On the bright side, you also took your greatest enemy down with you...the door."
                    print "The End"
        elif tomato != "door":
            print "You can't open that. It either can't open, or it's not coded into the game. Why don't you try something that will work, like the door."
            bowl()
    elif key == "true":
        if tomato == "door":
            print "You take the key out of your pocket. With a shaky hand, you slowly move the key toward the door. Slowly....Slowly....Slowly....The key hits the door with a thunk. You missed the lock. You adjust your aim and try again. Slowly....Slowly....Slowly....The key slide gently into the lock on the door. You turn the key, and the lock clicks. You push on the door and it opens to reveal a bright white light."
            ending()
        elif tomato != "door":
            print "That's not going to work. You are in possession of a key. There is a door in front of you. Try making a connection."
            bowl()
def plate():
    potato = raw_input("What do you want to pick up?")
    if potato == "key":
        if key == "false":
            print "The key is lying on top of a pedestal. You walk up to it and look at the key. What a nice key. The key has some nice key-like qualities. You almost feel unworthy to pick up such a perfect key. You gently place a finger on the key, and immediately experience a moment of euphoria. Your vision blurs and you collapse to the floor. You begin spazzing out on the ground while you're in complete bliss. The world goes black. You passed out on the floor. You must now wait a minute to regain consciousness."
            time.sleep(60)
            print "You wake up after taking a nice minute long nap. You stand up and stare at the key. You quickly swipe the key off its pedestal and place it into your pocket. The presence of the key in your pocket sends shivers down your spine. *You got a key*"
            key = "true"
            cup()
        elif key == "true":
            print "You already picked up the key. Go do something with it."
            cup()
    elif potato != "key":
        print "There's literally nothing else in this room that you can pick up other than that key. I don't even know what you were thinking trying to pick that up. Try again."
        plate()
def ending():
    decision = raw_input("Type 'forward' to go through the door: ")
    if decision == "forward":
        print "You step through the door. Immediately, you feel your stomach drop as you begin to fall. You suddenly hit the floor and pass out before you even have time to think or panic. After an undetermined amount of time, you wake up. You stand up and look around to see that you are in a cubiodal room with a white walls on all sides. There is nothing in the room but a key....and a door...."
        print "The End"
    elif decision == "close":
        screwed()
    elif decision != "forward" or "close":
        print "You can't do that. You can really only do two things in this situation: Go forward, or close the door. Let's try this again."
        ending()
def screwed():
    wow = raw_input("What do you want to close?")
    if wow == "door":
        print "You grab the key and chuck it out into the bright light. You grab the handle of the door, and slam it shut. It locks automatically. Now, you are stuck. There is no hope. All you can do is sit in this bright white room, with nothing to do but think. Nice work. You goofed. You end up sitting in this room for what seems like an eternity, until you eventually slip into a peaceful sleep. A sleep that you never woke up from again."
        print "The End"
    elif wow != "door":
        print "There's only one thing in this room that you can close at the moment. I don't even have to tell you what it is. I'll give you a hint though. The name of the thing you can close starts with 'd' and ends with 'oor'."
        screwed()
leche()