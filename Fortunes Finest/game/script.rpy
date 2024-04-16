# The script of the game goes in this file.

# characters

define f = Character("Fortune Teller")

# backgrounds

image bg room = "FortuneTeller.png"

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

    f "What brings you here, my child?"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    f "Yo!"

    # This ends the game.

    return
