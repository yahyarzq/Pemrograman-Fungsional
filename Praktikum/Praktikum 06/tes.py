



def hgefh():
    gajah = 0
    def dhdh():
        global gajah
        gajah = 33
    
    return dhdh
    
    

hdj = hgefh()

#print(hdj())

damage_calculator_lmda = lambda current_hp,atk : (current_hp - atk) if current_hp > atk else 0 



#print(damage_calculator_lmda(1000,50))


def input_trycatch(func,display_text,err_display_text):
    try:
      return func(input(display_text))
    except:
      
      print(err_display_text)
      input_trycatch(func,display_text,err_display_text)


hdh=input_trycatch(int,"masukkan nilai int","error bruh")

print(hdh)
    