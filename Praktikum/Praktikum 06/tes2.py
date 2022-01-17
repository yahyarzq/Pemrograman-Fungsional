import os
character = [{"Name": "Eula", "Element": "Cryo", "Weapon Type": "Claymore", "Weapon": "Waster Greatsword", "ATK": 50},
                {"Name": "Raiden Shogun", "Element": "Electro",
                    "Weapon Type": "Polearm", "Weapon": "Beginner's Protector", "ATK": 40},
                {"Name": "Sangonomiya Kokomi", "Element": "Hydro",
                    "Weapon Type": "Catalyst", "Weapon": "Apprentice's Notes", "ATK": 30},
                {"Name": "Jean", "Element": "Anemo", "Weapon Type": "Sword",
                    "Weapon": "Dull Blade", "ATK": 20},
                {"Name": "Mona", "Element": "Hydro", "Weapon Type": "Catalyst",
                    "Weapon": "Apprentice's Notes", "ATK": 30},
                {"Name": "Kaedahara Kazuha", "Element": "Anemo",
                    "Weapon Type": "Sword", "Weapon": "Dull Blade", "ATK": 20},
                {"Name": "Kamisato Ayaka", "Element": "Cryo",
                    "Weapon Type": "Sword", "Weapon": "Dull Blade", "ATK": 50},
                {"Name": "Keqing", "Element": "Electro", "Weapon Type": "Sword", "Weapon": "Dull Blade", "ATK": 40}]

sword = [{"Name": "Mistsplitter Reforged", "ATK": 200},
         {"Name": "Aquila Favonia", "ATK": 200},
         {"Name": "Freedom-Sworn", "ATK": 100},
         {"Name": "Dull Blade", "ATK": 10}]
catalyst = [{"Name": "Everlasting Moonglow", "ATK": 300},
            {"Name": "Dodoco Tales", "ATK": 200},
            {"Name": "Solar Pearl", "ATK": 200},
            {"Name": "Apprentice's Notes", "ATK": 10}]
claymore = [{"Name": "Song of Broken Pines", "ATK": 300},
            {"Name": "Skyward Pride", "ATK": 200},
            {"Name": "Akuoumaru", "ATK": 100},
            {"Name": "Waster Greatsword", "ATK": 10}]
polearm = [{"Name": "Engulfing Lightning", "ATK": 300},
           {"Name": "Staff of Homa", "ATK": 250},
           {"Name": "The Catch", "ATK": 150},
           {"Name": "Beginner's Protector", "ATK": 10}]

def clear():
    return os.system('cls')

def input_trycatch(func,display_text,err_display_text):
    try:
      return func(input(display_text))
    except:
      print(err_display_text)
      input_trycatch(func,display_text,err_display_text)
      

def selectChar(character_a):
    print("Select 4 character you want to play")

    def formatter(h, i): return "No : {}\nCharacter Name : {}\nElement Type : {}\nWeapon : {} | Weapon Type : {} | ATK : {}\n".format(
        h, i["Name"], i["Element"], i["Weapon"], i["Weapon Type"], i["ATK"])
    
    for i in range(len(character_a)):
        print(formatter(i, character_a[i]))

    def charSelector():
        selection = []

        def inner_wrapper():
            try:
                input_data = input("Masukkan Character Pilihan Anda : ")
                temp_selection = character_a[int(input_data)]
                if temp_selection in selection:
                    print("Tidak Bisa Memilih Karakter Yang Sama")
                else:
                    selection.append(temp_selection)
            except:
                print('Inputan Anda Salah')
            if len(selection) != 4:
                inner_wrapper()
        inner_wrapper()

        return selection
    val = charSelector()
    return val


def checkChar(character_cc):
    def fmat(h, i): return "No : {}\nCharacter Name : {}\nElement Type : {}\nWeapon : {} | Weapon Type : {} | ATK : {}\n".format(
        h, i["Name"], i["Element"], i["Weapon"], i["Weapon Type"], i["ATK"])

    for i in range(len(character_cc)):
        print(fmat(i, character_cc[i]))


def changeWeapon(character_cwp, sword_cwp, catalyst_cwp, claymore_cwp, polearm_cwp):

    def weapon_formatter(index,character_wft):
        return "No : {}\nWeapon Name : {} | ATK : {}\n".format(index,character_wft["Name"],character_wft["ATK"])
    
    def weaponSelector(weapon_type,character_wst,index_char):
        def inner_wrapper():
            character_wst_inner = character_wst
            try:
                input_wp = int(input("Masukkan Weapon Pilihan Anda : "))
                character_wst_inner[index_char]["Weapon"] = weapon_type[input_wp]["Name"]
                character_wst_inner[index_char]["ATK"] = weapon_type[input_wp]["ATK"]

            except:
                print('Inputan Anda Salah')
            return character_wst_inner
        data = inner_wrapper()
        return data
    
    def weapon_sword(character_wp_sword,index_char):
        for i in range(len(sword_cwp)):
            print(weapon_formatter(i,sword_cwp[i]))
        data = weaponSelector(sword_cwp,character_wp_sword,index_char)
        return data
        
    def weapon_catalyst(character_wp_catalyst,index_char):
        for i in range(len(catalyst_cwp)):
            print(weapon_formatter(i,catalyst_cwp[i]))
        data = weaponSelector(catalyst_cwp,character_wp_catalyst,index_char)
        return data

    def weapon_claymore(character_wp_claymore,index_char):
        for i in range(len(claymore_cwp)):
            print(weapon_formatter(i,claymore_cwp[i]))
        data = weaponSelector(claymore_cwp,character_wp_claymore,index_char)
        return data

    def weapon_polearm(character_wp_polearm,index_char):
        for i in range(len(polearm_cwp)):
            print(weapon_formatter(i,polearm_cwp[i]))
        data = weaponSelector(polearm_cwp,character_wp_polearm,index_char)
        return data
    
    def characterSelector():
        clear()
        changed_wp_char = character_cwp
        print("Change Character Weapon")
        checkChar(changed_wp_char)
        #input_no_char = int(input("Select Character Weapon You Want To Change : "))
        input_no_char = input_trycatch(int,"Select Character Weapon You Want To Change : ","Inputan Salah !!!")
        clear()
        if changed_wp_char[input_no_char]["Weapon Type"] == "Sword":
            
            changed_wp_char = weapon_sword(changed_wp_char,input_no_char)
        elif changed_wp_char[input_no_char]["Weapon Type"] == "Catalyst":
            
            changed_wp_char = weapon_catalyst(changed_wp_char,input_no_char)
        elif changed_wp_char[input_no_char]["Weapon Type"] == "Claymore":
            
            changed_wp_char = weapon_claymore(changed_wp_char,input_no_char)
        elif changed_wp_char[input_no_char]["Weapon Type"] == "Polearm":
            
            changed_wp_char = weapon_polearm(changed_wp_char,input_no_char)
        else:
            print("Inputan Salah")
        
        clear()
        checkChar(changed_wp_char)
        
        #input_no2_char = input("Change Character Weapon Again (Y/y)? : ")
        input_no2_char = input_trycatch(str,"Change Character Weapon Again (Y/y)? : ","Inputan Salah !!!")
        if input_no2_char == "y" or input_no2_char == "Y":
            characterSelector()
        else:
            clear()
        return changed_wp_char
    
    return characterSelector()


def fight(character_fgt):
    
    azhdaha_hp = 10000
    
    def dmg_multipler_calculator(data):
        Cryo = 5
        Electro = 4
        Hydro = 3
        Anemo = 2
        if data["Element"] == "Cryo":
            data["ATK"]*=Cryo
        elif data["Element"] == "Electro":
            data["ATK"]*=Electro
        elif data["Element"] == "Hydro":
            data["ATK"]*=Hydro
        elif data["Element"] == "Anemo":
            data["ATK"]*=Anemo
        return data

    def damage_calculator(current_hp,atk):
        current_hp = current_hp - atk
        if current_hp < 0:
            current_hp  = 0
        return current_hp
    
    damage_calculator_lmda = lambda current_hp,atk : (current_hp - atk) if current_hp > atk else 0 
    
    character_atk_calculated = list(map(dmg_multipler_calculator,character_fgt))
    print("Fight Azhdaha")
    while azhdaha_hp > 0:
        print("\n")
        checkChar(character_atk_calculated)
        #input_char = int(input("Select Characater To Attack : "))
        input_char = input_trycatch(int,"Select Characater To Attack : ","Inputan Salah !!!")
        azhdaha_hp = damage_calculator_lmda(azhdaha_hp,character_atk_calculated[input_char]["ATK"])
        print("\nHp Azhdaha : {} | Elemental Reaction : {}".format(azhdaha_hp,character_atk_calculated[input_char]["Element"]))
        if azhdaha_hp == 0:
            print("Challenge Success")

def main():
    clear()
    selected_character = selectChar(character)
    clear()
    while True:
        print("Welcome to mini Genshin Impact Game \n")
        print("1. Check Characters")
        print("2. Change Weapon")
        print("3. Fight Azhdaha")
        print("4. Exit")
        input_menu = input("Select Menu : ")
        if input_menu == "1":
            checkChar(selected_character)
        elif input_menu == "2":
            selected_character = changeWeapon(selected_character, sword,
                         catalyst, claymore, polearm)
        elif input_menu == "3":
            fight(selected_character)
        elif input_menu == "4":
            exit()
        else:
            pass
    

if __name__ == "__main__":
    main()
