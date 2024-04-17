# The script of the game goes in this file.

# suitors
default tech_bro = 0
default swampy = 0
default ghost = 0
default babayaga = 0
default satan = 0

default suitorsInOrder = []
default current_suitor = "no one"
default suitorIndex = 0

# characters

define f = Character("Fortune Teller")

# backgrounds

image bg room = "FortuneTeller.png"

image bg title = "Opening Slide.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg black
    with fade

    "You find yourself ensnared in the throes of a loveless existence."

 

    "After years of pining and sadness..."
 
    # fortune teller fades in
    scene bg room
 

    "the labyrinths of fate have led you to the doorstep of whispered promises and clandestine whispers— 
    "

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

    # choices
    f "You find yourself lost in the woods… What do you do next?"

    menu: 
        "Climb to a high vantage point": #(tech bro) 
            $ tech_bro += 1
        "Find the closest water body": # (Swamp Thing) 
            $ swampy += 1
        "Give up": # (ghost?) 
            $ ghost += 1
        "Find food and shelter": # (baba yaga) 
            $ babayaga +=1
        "Set it on fire": # (satan) 
            $ satan += 1

    # create order of 
    # Original list of tuples
    $ suitors = [("Tech Bro", tech_bro), ("Swamp Creature", swampy), ("Ghost", ghost), ("Baba Yaga", babayaga), ("Satan", satan)]
    
    # Sorting by the second element of each tuple (points)
    $ suitors.sort(key=lambda x: x[1], reverse=True)
    
    # Assigning with the sorted list
    $ suitorsInOrder = suitors
    
    "[suitorsInOrder]"
    "[suitorsInOrder[0][0]]"

    $ current_suitor = suitorsInOrder[0][0]

    if current_suitor == "Tech Bro":
        jump tech_bro_ending
    elif current_suitor = "Swamp Creature":
        jump swampy_ending
    elif current_suitor = "Ghost":
        jump ghost_ending
    elif current_suitor = "Baba Yaga":
        jump babayaga_ending
    elif current_suitor = "Satan":
        jump satan_ending

    # This ends the game.
    return


    label tech_bro_ending:
        f "You should be with a tech bro"

        # This ends the game.
        return

    label swampy_ending:
        f "You should be with a swamp creature"

        # This ends the game.
        return

    label ghost_ending:
        f "You should be with a ghost"

        # This ends the game.
        return


    label babayaga_ending:
        f "You should be with Baba Yaga"

        # This ends the game.
        return


    label satan_ending:
        f "You should be with satan"

        # This ends the game.
        return



