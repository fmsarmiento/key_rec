import keyboard

print("Recording...")
recorded = keyboard.record(until='esc')
dat = []
for x in recorded:
    y = str(x)
    print(y.replace("KeyboardEvent",""))
    dat.append(y.replace("KeyboardEvent",""))
with open("st.txt","a+") as f:
    for x in dat:
        f.write(x+"\n")
print("Playing...")
#keyboard.play(recorded, speed_factor=3)
