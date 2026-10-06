import console_draw
import console_drawASCII
import console_drawASCII_toTXT
import console_drawASCII_colored

print("Hello, it is ASCII-Arter made by den-merk.")

while True:
    print("What type of art do you want?")
    print("1. Pixel art (colored)")
    print("2. ASCII art (not colored)")
    print("3. ASCII art (colored)")
    print("4. ASCII art into out.txt file (not colored)")

    type_ASCI = int(input(": "))

    if type_ASCI not in [1, 2, 3, 4]:
        print("Err: Not expected type of art, you must type a number 1 - 4")
    else:
        print("Ok.")
        f_of_c = input("What factor of contrast do you want? (normal is 1, standart is 1.25): ")
        
        if f_of_c == "":
            f_of_c = 1.25
        else:
            f_of_c = int(f_of_c)
        
        match type_ASCI:
            case 1:
                console_draw.draw(f_of_c)
            case 2:
                console_drawASCII.draw(f_of_c)
            case 3:
                console_drawASCII_colored.draw(f_of_c)
            case 4:
                console_drawASCII_toTXT.draw(f_of_c)