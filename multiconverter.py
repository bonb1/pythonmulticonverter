#Starte hier:
#Drei Conversion Formeln definieren: 
#knots/kilometer, fahrenheit/celsius/, inch/centimeter

def node_speed(hoursKilometer): 
    return (hoursKilometer * 1.852)
    


def fahrenheit(celsius):
    return ((celsius - 32) * 5/9)


def inch(centimeter):
    return (centimeter * 2.54)




#Ask user if user wants to convert Y/N

def ask_continue():
    answer = input("Do you want to convert a value? Print: Yes or No? ")
    
    if answer == "Yes": 
        return True        #Why Boolean and not if, else if and else?
    elif answer == "yes": 
        return True
    else:
        return False
    
   

    


#Ask user to select conversion type
def ask_select():    
    answer = input("Which conversion would you like to do? knots / fahrenheit / inches ")
    return answer

   

    
#Ask user to enter a value
def ask_value():
    answer = input("Please enter a value to convert: ")
    return answer

    






#Check which conversion: (hier weiter BAUSTELLE)


while(ask_continue()):
    conversion_type = ask_select()
    conversion_value = ask_value()
    result_message = "The result of the conversion is "


    if conversion_type == "knots": 
        result_message += str(node_speed(float(conversion_value))) + " knots."  # Achtung String umwandlung nicht vergessen.1. Umwandlung in Zahl (Number) 2. Das ganze zurück in Text 
          
    
    elif conversion_type == "fahrenheit": 
        result_message += str(fahrenheit(float(conversion_value))) + " fahrenheit."
    
    elif conversion_type == "inches": 
        result_message += str(inch(float(conversion_value))) + " inches."
    else:
        result_message = "Sorry. I can't do this conversion!"

    


print(result_message)








# Main:
# -Continue while user wants to convert something.



#-Check which conversion

#- Get value

# -display result



    
    


#try: except: quit() bei fehlerhafter Eingabe durch den user

# vom dritten Fenster wieder auf das erste springen (yes) oder quit bei (no):
#Do you want to convert a value: yes or no? 

#nicht vergessen: Einzahl und Mehrzahl programmieren z.b. knot und knots