# Story Start - Intro
print(f"Hello, Wanderer. Today we have a story of EPIC proportions. A story that YOU get to be a part of.")
print(f"It's a story about a brave adventurer that some might even call....a Hero.")
print(f"Not just any adventurer or hero, but one of minute scale and enourmous hunger.")
input(f"\nPress the enter key to continue...")
print(f"Before we depart for our grand adventure, I must first ask you some questions.")
input(f"\nPress the enter key to continue...")


# Player Variable
 heroName = input("\nThis is a story of a miniature hero doing things of gargantuan importance. What should this hero be called?: ")
while len(heroName) == 0:
   heroName = input(f"The hero has to have a name. Come on. What's their name?: ")
    
#Second Question
                     
cityName = input(f"Very well, {heroName} it is. Interesting choice, and from what city does {heroName} hail?: ")
while len(cityName) == 0:
    cityName = input(f"...Really? From where does this hero hail?!?!: ")
    
print(
    f"Hmm....Well...As fate would have it, {heroName} from {cityName} is unaware that they are about to be sent on the most epic quest in the history of...quests.")
print("Wow...that's redudant...almost as reduntant as the ellipses that are being used for pause and dramatic effect...")
input(f"\nPress the enter key to continue... ")

oxName = input("\nEvery hero needs their valiant steed, right? In this case your hero's steed is a 3,000 pound Dwarven Ox. What would you like to call your Oxen steed of glory?: ")
print("Splendid. I couldn't have chosen a better name myself. Well, maybe, but I digress. This is your story, not mine. Onward.")

crowName = input(
    "Along the way you may or may not encounter a magically imbued Crow that has the ability to speak. What should we call this crow?: ")
print("*sigh* We can work with that I suppose.")
princessName = input(
    "Last question before we get to the meat and potatoes of this grand quest. Without going into too much detail, there is a Princess in this story. What should her name be?: ")
print(f"{princessName} certainly sounds like royalty to me. Very well, adventurer. Shall we begin? Who are we kidding, you've made it this far, of course you want to hear the story. Let's go. ")

input(f"\nPress the enter key to continue... (We both know you want to)")

# StoryBegins

print(
    f"Four score and seven...apologies, wrong story. We begin this story of {heroName} the Dwarf Paladin outside the city of {cityName}. You see, life as a dwarf wasn't always easy for {heroName}. ")
print(f"He was always the center of short jokes in the dwarven community, seeing as he had the misfortune of being a shorter than average dwarf. Though he was vertically challenged, he had a heart of gold and would do unspeakable things for food, as you'll soon discover.")
print(
    f"Often described as 'Strong, sturdy, and short. {heroName} was always looking for his next pint, and someone to smite.")

input(f"\nPress the enter key to continue... ")
print(f"As {heroName} and his valiant steed of glory, {oxName} were traveling down a winding road through the Valley of Forlorn Fairytales, not far from the city of {cityName}, {heroName} was stricken by an instatiable hunger.")
print("A hunger so intense that he heavily considered turning his 3,000 pound chariot of awesomeness into a feast worthy of Kings.")
print(f"{heroName} drew his battle ax and mentally prepared himself to carve his only friend into a hefty steak. Then, as he looked around to ensure no one was watching he noticed how far from {cityName} he had traveled and decided that we would rather deal with the hunger than to walk home.")
input(f"\nPress the enter key to continue... ")
# EnterCrow
print("Onward they pressed, farther into the Valley when suddenly a loud 'swooshing' sound was heard overhead.")
print(f"{heroName} ducked as a blue streak of light rocketed by his head.")
print(
    f"In shock, and quiet honestly confused, {heroName} looked around to see if he could identify the blue light or where it went.")
print("Just as he turned his head he noticed this absolutely hideous looking winged beast that appeared to be a crow perched on a log a short distance away.")
input(f"\nPress the enter key to continue... ")

print(
    f"In utter shock and disbelief that a creature could be so...visually repulsing, {heroName} opted to do this poor beast a favor and drew his bow with the intent of erasing this unsightly bird from existence.")
print("Just as he reached full draw a booming voice, as if from the heavens, thundered out of the beast's beak.")
print(f"'I am {crowName}, guardian of Princess {princessName}. It is my duty to inform you that the Princess has taken her leave from {cityName}, and is nowhere to be found.'")
print("'It is uncertain whether her leave was intentional or if she has befallen victim to foul play. Nevertheless, I seek your assistance in recovering her.'")

print(f"{heroName} stared deeply at this peculiar talking bird, and after a brief pause said 'No.' and grunted at {oxName} to continue down the road.")
print(f"As {heroName} and {oxName} began walking away the crow let out a sigh and said 'I don't have much to offer you, good Sir, but isn't the well-being of Princess {princessName} enough for your efforts?'")
print(f"To which {heroName} again, said 'No.'")
print(f"'Fine' said {crowName}. 'It is absolutely imperative that we find the Princess. What do you require as payment?'")
input(f"\nPress the enter key to continue... ")
# Hero agrees to assist crow.
print(f"Without hesitation {heroName} replied 'Listen, magical bird-man...thing. I am so hungry I almost ate me ox. If it wasn't a 15 mile walk back to {cityName} I'd be roasting this beefy bovine at this very moment. So unless you've got food, I'm not interested in ye games or ye Princess. Leave me be before I stick an arrow in ye. '")
print(f"{crowName} took a pause before explaining the importance of returning the Princess to {cityName}, and urged {heroName} once more to assist.")
print(
    f"It was only after a very lengthy discussion that {heroName} agreed to locate said Princess in exchange for one thing.")
print("The one thing his heart so desperately desired. The juciest, most savory smoked turkey leg that dwarven-kind has ever made.")
input("\nPress the enter key to continue... ")

# Player choice of path to take.
print(
    f"'Very well' said {crowName}. 'Before you there are two paths, both of which lead to the presumed location of the Princess.")
print("'To your left you will see a path leading through the Rolling Hills of Randomness. You should take caution here as the dangers are, well...random. There's nothing I can say to prepare you for the things you may encounter there.' ")
print("'The path you see to your right will take you through the Mountains of Mediocrity. The name itself should impose threats of the mediocre nature, but I can fly so that none of that concerns me.' said the crow.")
print(
    f"'Nevertheless, time is of the essence and you must make haste. Will you, {heroName} take the path through the Rolling Hills of Randomness?'")

pathChoice = input("\nEnter yes or no:")
while len(pathChoice) == 0:
    pathChoice = input(
        "Come on now, it's a yes or no question. Please enter yes or no:")
if pathChoice.lower() == "yes":
    print("Very well, through the Rolling Hills of Randomness you must traverse dangers unknown and threats uncertain. Good luck.")
else:
    print("I see. The Mountains of Mediocrity do seem a bit more fitting for a hero of your stature. Good luck.")

input("Press the enter key to continue...")
