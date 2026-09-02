# Chinese Zodiac Program

year = int(input("Enter year of birth: "))

# Check if the year is valid
if year < 1900:
    print("Invalid Year, it should not be earlier than 1900")
else:
    remainder = year % 12
    
    if remainder == 0:
        print("Your Zodiac Sign is: Monkey — 猴 (Hóu)")
        print("Traits: Sharp, smart.")
    elif remainder == 1:
        print("Your Zodiac Sign is: Rooster — 鸡 (Jī)")
        print("Traits: Observant, hardworking.")
    elif remainder == 2:
        print("Your Zodiac Sign is: Dog — 狗 (Gǒu)")
        print("Traits: Lovely, honest.")
    elif remainder == 3:
        print("Your Zodiac Sign is: Pig — 猪 (Zhū)")
        print("Traits: Compassionate, generous.")
    elif remainder == 4:
        print("Your Zodiac Sign is: Rat — 鼠 (Shǔ)")
        print("Traits: Clever, resourceful.")
    elif remainder == 5:
        print("Your Zodiac Sign is: Ox — 牛 (Niú)")
        print("Traits: Diligent, dependable.")
    elif remainder == 6:
        print("Your Zodiac Sign is: Tiger — 虎 (Hǔ)")
        print("Traits: Brave, confident.")
    elif remainder == 7:
        print("Your Zodiac Sign is: Rabbit — 兔 (Tù)")
        print("Traits: Quiet, elegant.")
    elif remainder == 8:
        print("Your Zodiac Sign is: Dragon — 龙 (Lóng)")
        print("Traits: Powerful, lucky.")
    elif remainder == 9:
        print("Your Zodiac Sign is: Snake — 蛇 (Shé)")
        print("Traits: Enigmatic, intelligent.")
    elif remainder == 10:
        print("Your Zodiac Sign is: Horse — 马 (Mǎ)")
        print("Traits: Animated, active.")
    elif remainder == 11:
        print("Your Zodiac Sign is: Goat — 羊 (Yáng)")
        print("Traits: Gentle, shy.")