
print('''
                                              _____________
                                  ..---:::::::-----------. ::::;;.
                               .'""""""                  ;;   \  ":.
                            .''                          ;     \   "\__.
                          .'                            ;;      ;   \\";
                        .'                              ;   _____;   \\/
                      .'                               :; ;"     \ ___:'.
                    .'--...........................    : =   ____:"    \ \
               ..-""                               """'  o"""     ;     ; :
          .--""  .----- ..----...    _.-    --.  ..-"     ;       ;     ; ;
       .""_-     "--""-----'""    _-"        .-""         ;        ;    .-.
    .'  .'                      ."         ."              ;       ;   /. |
   /-./'                      ."          /           _..  ;       ;   ;;;|
  :  ;-.______               /       _________==.    /_  \ ;       ;   ;;;;
  ;  / |      """"""""""".---."""""""          :    /" ". |;       ; _; ;;;
 /"-/  |                /   /                  /   /     ;|;      ;-" | ;';
:-  :   """----______  /   /              ____.   .  ."'. ;;   .-"..T"   .
'. "  ___            "":   '""""""""""""""    .   ; ;    ;; ;." ."   '--"
 ",   __ """  ""---... :- - - - - - - - - ' '  ; ;  ;    ;;"  ."
  /. ;  """---___                             ;  ; ;     ;|.""
 :  ":           """----.    .-------.       ;   ; ;     ;:
  \  '--__               \   \        \     /    | ;     ;;
   '-..   """"---___      :   .______..\ __/..-""|  ;   ; ;
       ""--..       """--"        m l s         .   ". . ;
             ""------...                  ..--""      " :
                        """"""""""""""""""    \        /
                                               "------"
''')
print("Welcome to your Getaway Chase!")
print("Your mission is to get away from the police")
print("\nYour getting chased by the police")
first = input("Do you take the next 'left' or 'right' turn? ").lower()

if first == "left":
    second = input("You are approaching a red light. Do you 'wait' or 'run' the light? ").lower()

    if second == "wait":
        print("You have managed to get some distance between you and the police.")
        print("You find yourself in front of three warehouse.")
        
        third = input("Which warehouse to you hide in: 'Red', 'Blue' or 'Yellow'? ").lower()

        if third == "yellow":
            print("Congats. You have managed to excape the police.")
        elif third == "red":
            print("You have managed to hide in the red warehouse, but this warehouse is on fire!")
            print("You run out of the burning warehouse to find the police waiting for you.")
            print("You are arrested.\nGAME OVER")
        elif third == "blue":
            print("You drive through the warehouse doors")
            print("You car loses control and you crash into a hugh container of water.")
            print("The water fills the warehouse and flows out of its doors.")
            print("The police see the water and find you inside.")
            print("GAME OVER")
        else:
            print("GAME OVER")
    else:
        print("You run the lights. A truck was coming and you crashed!")
        print("GAME OVER")
else:
    print("You turn into a dead end. You have been arrested")
    print("GAME OVER")

input("press enter to close")