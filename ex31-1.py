late = "You're late to work. You're fired!"
sick = "You call in sick and play Xbox all day. Good job!"

print "You leave your house for work. Which route do you take?"
print "1. I-95"
print "2. Hart Expressway"

route = raw_input("> ")

if route == "1":
    print "Traffic is at a standstill. What do you do?"
    print "1. Take a different route."
    print "2. Wait it out."
    print "3. Turn around and go home."

    traffic = raw_input("> ")

    if traffic == "2":
        print late
    if traffic == "3":
        print sick

if route == "2" or traffic == "1":
    print "There's an accident on the bridge! What do you do?"
    print "1. Take a different route."
    print "2. Wait it out."
    print "3. Turn around and go home."

    accident = raw_input("> ")

    if accident == "2":
        print late
    if accident == "3":
        print sick

if accident == "1":
    print "Traffic is backed up here too! What do you do?"
    print "1. Wait it out."
    print "2. Turn around and go home."

    final = raw_input("> ")

    if final == "1":
        print late
    if final == "2":
        print sick
