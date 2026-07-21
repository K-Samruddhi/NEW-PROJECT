import random

DUCK_RESPONSES = [ "Hmm... have you tried reading the error?", "Quack. It's probably a missing comma.", "The bug fears eye contact.", "Works on my pond.", "Have you tried turning the developer off and on again?" ]

def debug(): print("🦆 Rubber Duck listens patiently...") input("Explain your bug to the duck:\n> ") print("\n🦆", random.choice(DUCK_RESPONSES))

if name == "main": debug()
