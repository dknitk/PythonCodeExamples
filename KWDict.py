sounds = {
    "cat": "meow",
    "dog": "woof"
}
sounds["tiger"] = "grrr"
sound = sounds["cat"]
print(sound)
for sound in sounds:
    print(sound)

for sound in sounds.keys():
    print(sound)

for sound in sounds.values():
    print(sound)

for sound in sounds.items():
    print(sound)

for animal, sound in sounds.items():
    print(animal, "goes", sound)