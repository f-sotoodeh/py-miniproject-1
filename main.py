templates = [
    "It was about (Number) (Measure of time) ago when I arrived at the hospital in a (Mode of Transportation). The hospital is a/an (Adjective) place, there are a lot of (Adjective2) (Noun) here. There are nurses here who have (Color) (Part of the Body). If someone wants to come into my room I told them that they have to (Verb) first. I’ve decorated my room with (Number2) (Noun2). Today I talked to a doctor and they were wearing a (Noun3) on their (Part of the Body 2). I heard that all doctors (Verb) (Noun4) every day for breakfast. The most (Adjective3) thing about being in the hospital is the (Silly Word) (Noun5) !",
    "This weekend I am going camping with (Proper Noun (Person’s Name)). I packed my lantern, sleeping bag, and (Noun). I am so (Adjective (Feeling)) to (Verb) in a tent. I am (Adjective (Feeling) 2) we might see a(n) (Animal), I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and (Verb2). I have heard that the (Color) lake is great for (Verb (ending in ing)). Then we will (Adverb (ending in ly)) hike through the forest for (Number) (Measure of Time). If I see a (Color) (Animal) while hiking, I am going to bring it home as a pet! At night we will tell (Number) (Silly Word) stories and roast (Noun2) around the campfire!!",
    "Dear (Proper Noun (Person’s Name)), I am writing to you from a (Adjective) castle in an enchanted forest. I found myself here one day after going for a ride on a (Color) (Animal) in (Place). There are (Adjective2) (Magical Creature (Plural)) and (Adjective3) (Magical Creature (Plural)2) here! In the (Room in a House) there is a pool full of (Noun). I fall asleep each night on a (Noun2) of (Noun(Plural)3) and dream of (Adjective4) (Noun (Plural)4). It feels as though I have lived here for (Number) (Measure of time). I hope one day you can visit, although the only way to get here now is (Verb (ending in ing)) on a (Adjective5) (Noun5)!!",
]

# Let user pick template
print("Choose a template:")
for i, t in enumerate(templates, 1):
    print(f"{i}. {t[:50]}...")
while True:
    try:
        choice = int(input("Enter number (1-3): "))
        if 1 <= choice <= 3:
            template = templates[choice - 1]
            break
        else:
            print("Please enter 1, 2, or 3!")
    except ValueError:
        print("Please enter a valid number!")


# extract placeholders from template
def extract_placeholders(template):
    placeholders = []
    level = 0
    start = None
    for i, ch in enumerate(template):
        if ch == "(":
            if level == 0:
                start = i + 1
            level += 1
        elif ch == ")":
            level -= 1
            if level == 0 and start is not None and i - start > 3:
                placeholders.append(template[start - 1 : i + 1])
    return placeholders


def get_valid_input(prompt, is_number=False):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be blank!")
            continue
        if is_number and not value.isdigit():
            print("Please enter a valid number!")
            continue
        return value


placeholders = extract_placeholders(template)

# get user inputs for each placeholder
user_inputs = {}
for placeholder in placeholders:
    article = "an" if placeholder[1] in "AEIOUaeiou" else "a"
    is_num = "Number" in placeholder
    user_inputs[placeholder] = get_valid_input(
        f"Please enter {article} {placeholder}: ", is_num
    )

# fill in the template with user inputs
for placeholder, user_input in user_inputs.items():
    template = template.replace(placeholder, user_input)

# print the final story
print("\nHere is your story:\n")
print(template)
