﻿# The script of the game goes in this file.

# suitors
default tech_bro = 0
default bigfoot = 0
default ghost = 0 # la llorona
default babayaga = 0
default satan = 0

default suitorsInOrder = []
default current_suitor = "no one"
default suitorIndex = 0

# characters

define f = Character("Fortune Teller")

# backgrounds

image bg clouds = "clouds.png"
image bg room = "FortuneTeller.png"

image bg tech_bro_bg = "stocks.png"
image bg bigfoot_bg = "bigfoot.png"
# image bg ghost_bg =
image bg babayaga_bg = "FortuneTeller.png"
image bg satan_bg = "satan.png"

# The game starts here.

label start:

    scene bg clouds
    with fade

    "You find yourself ensnared in the throes of a loveless existence."

    "After years of pining and sadness..."

    "the labyrinths of fate have led you to the doorstep of whispered promises and clandestine whispers— 
    "

    # fortune teller fades in
    scene bg room
    with fade

    "You hear of a mysterious fortune teller who can take you out of your misery. 
    "
    
    "By giving you a peek into what the universe holds for you. 
    "
    
    "Beneath the watchful gaze of the fortune teller, every word uttered carries the weight of consequence. 
    "
    
    "No earthly treasures are sought, no material offerings to appease her ancient wisdom—only the raw honesty that resides within your heart. 
    "
    
    "And so, with bated breath and trembling resolve, you surrender yourself to the mercy of fate, placing your trust in the hands of the fortune teller… 
    "

    "She closes her eyes and mumbles to herself and when she open them again they are milky and distant. 
    "

    "Mirroring the swirling lit up patterns on the crystal ball. 
    "

    f "What brings you here?"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    f "Howdy"

    # Start Questionnaire

    # Question 1
    f "Pray tell me... what virtue do you hold close to your heart?"
    menu:
        "Ambition":
            $ tech_bro += 1
        "Justice":
            $ satan += 1
        "Sustainability":
            $ bigfoot += 1
        "Wisdom":
            $ babayaga += 1
        "Devotion":
            $ ghost += 1

    # Question 2
    f "What kind of soul would you like to befriend?"
    menu:
        "Someone with a wild spirit":
            $ satan += 1
        "A foodie":
            $ babayaga += 1
        "A self-proclaimed Slytherin":
            $ tech_bro += 1
        "An empath":
            $ ghost += 1
        "I don't need friends":
            $ bigfoot += 1

    # Question 3
    f "You find yourself with a rare moment of reprieve. How will you spend your time?"
    menu:
        "Lounging in a warm sauna":
            $ satan += 1
        "Working on a nice cozy DIY project":
            $ babayaga += 1
        "Quality time with family":
            $ ghost += 1
        "Hiking by myself":
            $ bigfoot += 1
        "Top golf":
            $ tech_bro += 1

    # Question 4
    f "You look through a keyhole in a dimly lit room, what do you see?"
    menu: 
        "A room on fire":
            $ satan += 1
        "Home":
            $ ghost += 1
        "A lush open field with flowers strewn about":
            $ bigfoot += 1
        "A game room with FIFA loaded up":
            $ tech_bro += 1
        "A kitchen stocked with every ingredient imaginable":
            $ babayaga += 1

    # Question 5
    f "Now my child, I'll tell you a story, and you answer how you see fit."
    f "You find yourself lost in the woods... What do you do next?"
    menu: 
        "Climb to a high vantage point": 
            $ tech_bro += 1
        "Find the closest body of water": 
            $ ghost += 1
        "Find food and shelter": 
            $ babayaga +=1
        "Set it on fire": 
            $ satan += 1
        "I feel at home...":
            $ bigfoot += 1

    # Question 6
    f "You hear rustling from a nearby bush. What emerges to greet you?"
    menu:
        "A deer":
            $ bigfoot += 1
        "A dog!":
            $ tech_bro += 1
        "A ram":
            $ satan += 1
        "Another person, lost in the woods":
            $ babayaga += 1
        "It was just the wind":
            $ ghost += 1

    # Question 7
    f "You've finally found your way out of the woods. What do you do first?"
    menu:
        "Cry tears of relief":
            $ ghost += 1
        "Eat a hearty meal":
            $ babayaga += 1
        "Check on your stonks":
            $ tech_bro += 1
        "Run back into the woods! I miss it already!":
            $ bigfoot += 1
        "Take vengeance on whoever got you lost in the first place":
            $ satan += 1

    # End Questionnaire

    f "Ooh! I see some exciting things in your future!"
    f "You'll find a suitor soon... They are just around the corner..."

    # CALCULATE COMPATABILITY #
    # Create list of suitors
    $ suitors = [("Tech Bro", tech_bro), ("Bigfoot", bigfoot), ("Ghost", ghost), ("Baba Yaga", babayaga), ("Satan", satan)]
    
    # Sorting by the second element of each tuple (compatability points, highest to lowest)
    $ suitors.sort(key=lambda x: x[1], reverse=True)
    
    # Assigning the sorted list
    $ suitorsInOrder = suitors

    # Current suitor is the first suitor in the list
    $ current_suitor = suitorsInOrder[0][0]

    if current_suitor == "Tech Bro":
        jump tech_bro_ending
    elif current_suitor == "Bigfoot":
        jump bigfoot_ending
    elif current_suitor == "Ghost":
        jump ghost_ending
    elif current_suitor == "Baba Yaga":
        jump babayaga_ending
    elif current_suitor == "Satan":
        jump satan_ending

    # This ends the game.
    return


    label tech_bro_ending:
        f "You should be with..."

        scene bg tech_bro_bg
        with fade
        f "A tech bro!"

        # This ends the game.
        return

    label bigfoot_ending:
        f "You should be with..."

        scene bg bigfoot_bg
        with fade

        f "Bigfoot!"

        # This ends the game.
        return

    label ghost_ending:
        f "You should be with..."

        scene bg ghost_bg
        with fade

        f "La Llorona!"

        # This ends the game.
        return


    label babayaga_ending:
        f "Enchantress of wisdom, with a penchant for creating a quirky cozy surrounding for herself."
        f "She loves fried food and she longs to welcome you into her fantastical home and her heart."
        f "Your eternal life partner is none other than..."

        scene bg babayaga_bg
        with fade

        f "Baba Yaga!"

        # This ends the game.
        return


    label satan_ending:
        f "Dark allure, fiery passion..."
        f "He seeks a soul bold enough for his eternal dance..."
        f "Oh wait, did I say eternal? Sorry I meant infernal dance."
        f "Your life partner is none other than..."

        scene bg satan_bg
        with fade

        f "Satan!"

        # This ends the game.
        return



