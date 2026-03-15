 # ### ### # # ### ### ### ### ### ###
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###
def layer1(num):
    layer_1 = []

    for ch in num:
        if ch == "1":
            layer_1.append("    #")
        elif ch == "4":
            layer_1.append("#   #")
        else:
            layer_1.append("#####")
    
    layer_1 = " ".join(layer_1)
    return layer_1

def layer2(num):
    layer_2 = []

    for ch in num:
        if ch in ("1" , "2" , "3" , "7") :
            layer_2.append("    #")
        elif ch in ("5" , "6"):
            layer_2.append("#    ")
        else:
            layer_2.append("#   #")
    
    layer_2 = " ".join(layer_2)
    return layer_2

def layer3(num):
    layer_3 = []

    for ch in num:
        if ch in ("1" , "7") :
            layer_3.append("    #")
        elif ch in ("0"):
            layer_3.append("#   #")
        else:
            layer_3.append("#####")
    
    layer_3 = " ".join(layer_3)
    return layer_3

def layer4(num):
    layer_4 = []

    for ch in num:
        if ch in ("2") :
            layer_4.append("#    ")
        elif ch in ("6" , "8" , "0"):
            layer_4.append("#   #")
        else:
            layer_4.append("    #")
    
    layer_4 = " ".join(layer_4)
    return layer_4

def layer5(num):
    layer_5 = []

    for ch in num:
        if ch in ("1" , "4" , "7") :
            layer_5.append("    #")
        else:
            layer_5.append("#####")
    
    layer_5 = " ".join(layer_5)
    return layer_5

def seven_segment(num):

    print(layer1(num))
    print(layer2(num))
    print(layer3(num))
    print(layer4(num))
    print(layer5(num))


while True:
    try:
        num = int(input("Enter number to convert: "))
        num = str(num)
        if num == "629":
            break
        if num:
            seven_segment(num)

        
        
    except ValueError:
        print("Not an integer")




