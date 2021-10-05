import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.image import Image as CoreImage
from kivy.uix.screenmanager import ScreenManager,  Screen, ShaderTransition, SlideTransition
from kivy.uix.checkbox import CheckBox
import random

one_spades = (1, 2, 'One of Spades', "Images/ace_spades.png")
two_spades = (2, 2, 'Two of Spades', "Images/two_spades.png")
three_spades = (3, 2, 'Three of Spades', "Images/three_spades.png")
four_spades = (4, 2, 'Four of Spades', "Images/four_spades.png")
five_spades = (5, 2, 'Five of Spades', "Images/five_spades.png")
six_spades = (6, 2, 'Six of Spades', "Images/six_spades.png")
seven_spades = (7, 2, 'Seven of Spades', "Images/seven_spades.png")
eight_spades = (8, 2, 'Eight of Spades', "Images/eight_spades.png")
nine_spades = (9, 2, 'Nine of Spades', "Images/nine_spades.png")
ten_spades = (10, 2, 'Ten of Spades', "Images/ten_spades.png")
joker_spades = (11, 2, 'Jack of Spades', "Images/jack_spades.png")
queen_spades = (12, 2, 'Queen of Spades', "Images/queen_spades.png")
king_spades = (13, 2, 'King of Spades', "Images/king_spades.png")
one_clubs = (1, 2, 'One of Clubs', "Images/ace_clubs.png")
two_clubs = (2, 2, 'Two of Clubs', "Images/two_clubs.png")
three_clubs = (3, 2, 'Three of Clubs', "Images/three_clubs.png")
four_clubs = (4, 2, 'Four of Clubs', "Images/four_clubs.png")
five_clubs = (5, 2, 'Five of Clubs', "Images/five_clubs.png")
six_clubs = (6, 2, 'Six of Clubs', "Images/six_clubs.png")
seven_clubs = (7, 2, 'Seven of Clubs', "Images/seven_clubs.png")
eight_clubs = (8, 2, 'Eight of Clubs', "Images/eight_clubs.png")
nine_clubs = (9, 2, 'Nine of Clubs', "Images/nine_clubs.png")
ten_clubs = (10, 2, 'Ten of Clubs', "Images/ten_clubs.png")
joker_clubs = (11, 2, 'Jack of Clubs', "Images/jack_clubs.png")
queen_clubs = (12, 2, 'Queen of Clubs', "Images/queen_clubs.png")
king_clubs = (13, 2, 'King of Clubs', "Images/king_clubs.png")
one_dmnds = (1, 1, 'One of Diamonds', "Images/ace_diamonds.png")
two_dmnds = (2, 1, 'Two of Diamonds', "Images/two_diamonds.png")
three_dmnds = (3, 1, 'Three of Diamonds', "Images/three_diamonds.png")
four_dmnds = (4, 1, 'Four of Diamonds', "Images/four_diamonds.png")
five_dmnds = (5, 1, 'Five of Diamonds', "Images/five_diamonds.png")
six_dmnds = (6, 1, 'Six of Diamonds', "Images/six_diamonds.png")
seven_dmnds = (7, 1, 'Seven of Diamonds', "Images/seven_diamonds.png")
eight_dmnds = (8, 1, 'Eight of Diamonds', "Images/eight_diamonds.png")
nine_dmnds = (9, 1, 'Nine of Diamonds', "Images/nine_diamonds.png")
ten_dmnds = (10, 1, 'Ten of Diamonds', "Images/ten_diamonds.png")
joker_dmnds = (11, 1, 'Jack of Diamonds', "Images/jack_diamonds.png")
queen_dmnds = (12, 1, 'Queen of Diamonds', "Images/queen_diamonds.png")
king_dmnds = (13, 1, 'King of Diamonds', "Images/king_diamonds.png")
one_hearts = (1, 1, 'One of Hearts', "Images/ace_hearts.png")
two_hearts = (2, 1, 'Two of Hearts', "Images/two_hearts.png")
three_hearts = (3, 1, 'Three of Hearts', "Images/three_hearts.png")
four_hearts = (4, 1, 'Four of Hearts', "Images/four_hearts.png")
five_hearts = (5, 1, 'Five of Hearts', "Images/five_hearts.png")
six_hearts = (6, 1, 'Six of Hearts', "Images/six_hearts.png")
seven_hearts = (7, 1, 'Seven of Hearts', "Images/seven_hearts.png")
eight_hearts = (8, 1, 'Eight of Hearts', "Images/eight_hearts.png")
nine_hearts = (9, 1, 'Nine of Hearts', "Images/nine_hearts.png")
ten_hearts = (10, 1, 'Ten of Hearts', "Images/ten_hearts.png")
joker_hearts = (11, 1, 'Jack of Hearts', "Images/jack_hearts.png")
queen_hearts = (12, 1, 'Queen of Hearts', "Images/queen_hearts.png")
king_hearts = (13, 1, 'King of Hearts', "Images/king_hearts.png")
deck = [(one_spades), (two_spades), (three_spades), (four_spades), (five_spades), (six_spades), (seven_spades), (eight_spades), (nine_spades), (ten_spades), (joker_spades), (queen_spades), (king_spades), (one_clubs), (two_clubs), (three_clubs), (four_clubs), (five_clubs), (six_clubs), (seven_clubs), (eight_clubs), (nine_clubs), (ten_clubs), (joker_clubs), (queen_clubs), (king_clubs), (one_dmnds), (two_dmnds), (three_dmnds), (four_dmnds), (five_dmnds), (six_dmnds), (seven_dmnds), (eight_dmnds), (nine_dmnds), (ten_dmnds), (joker_dmnds), (queen_dmnds), (king_dmnds), (one_hearts), (two_hearts), (three_hearts), (four_hearts), (five_hearts), (six_hearts), (seven_hearts), (eight_hearts), (nine_hearts), (ten_hearts), (joker_hearts), (queen_hearts), (king_hearts)]

def half_build_deck():
    global deck
    deck = [(one_spades), (two_spades), (three_spades), (four_spades), (five_spades), (six_spades), (seven_spades), (eight_spades), (nine_spades), (ten_spades), (joker_spades), (queen_spades), (king_spades), (one_clubs), (two_clubs), (three_clubs), (four_clubs), (five_clubs), (six_clubs), (seven_clubs), (eight_clubs), (nine_clubs), (ten_clubs), (joker_clubs), (queen_clubs), (king_clubs), (one_dmnds), (two_dmnds), (three_dmnds), (four_dmnds), (five_dmnds), (six_dmnds), (seven_dmnds), (eight_dmnds), (nine_dmnds), (ten_dmnds), (joker_dmnds), (queen_dmnds), (king_dmnds), (one_hearts), (two_hearts), (three_hearts), (four_hearts), (five_hearts), (six_hearts), (seven_hearts), (eight_hearts), (nine_hearts), (ten_hearts), (joker_hearts), (queen_hearts), (king_hearts)]
    return deck

drinks = 0
deck_pick = 0
rb_play = 1
hl_play = 1
oe_play = 1
io_play = 0
su_play = 0


class WindowManager(ScreenManager):
    pass

class MainMenu(Screen):
    def update(self):
        global rb_play, hl_play, oe_play, io_play, su_play
        print(rb_play)
        print(hl_play)
        print(oe_play)
        print(io_play)
        print(su_play)
    def start(self):
        if rb_play == 1:
            self.parent.current = "redblackwindow"
        elif oe_play == 1:
            self.parent.current = "oddevenwindow"
    def settings(self, *args):
        self.parent.current = "settingswindow"
        pass
    def credits(self, *args):
        #self.parent.current = "creditswindow"
        pass
    def exit(self):
        quit()

class SettingsMenu(Screen):
    def update(self, *args):
        global rb_play, hl_play, oe_play, io_play, su_play
        self.ids.hl_check.disabled = False
        if self.ids.rb_check.active == True:
            self.ids.rbtext.color = "green"
            self.ids.oe_check.disabled = False
            rb_play = 1
        
        elif self.ids.rb_check.active == False:
            self.ids.rbtext.color = "black"
            self.ids.oe_check.active = True
            self.ids.oe_check.disabled = True
            rb_play = 0
        
        if self.ids.hl_check.active == True:
            self.ids.hltext.color = "green"
            self.ids.rb_check.active = True
            self.ids.rb_check.disabled = True
            hl_play = 1
        
        elif self.ids.hl_check.active == False:
            self.ids.rb_check.disabled = False
            self.ids.hltext.color = "black"
            hl_play = 0
        
        if self.ids.oe_check.active == True:
            self.ids.oetext.color = "green"
            oe_play = 1

        elif self.ids.oe_check.active == False:
            self.ids.oetext.color = "black"
            self.ids.rb_check.active = True
            self.ids.rb_check.disabled = True
            oe_play = 0

        if int(rb_play + hl_play + oe_play) < 2:
            self.ids.io_check.active = False
            self.ids.io_check.disabled = True
        if int(rb_play + hl_play + oe_play) >= 2:
            self.ids.io_check.disabled = False

        if self.ids.io_check.active == True:
            self.ids.iotext.color = "green"
        elif self.ids.io_check.active == False:
            self.ids.iotext.color = "black"    
        return rb_play, hl_play, oe_play, io_play, su_play 

    def rb_checked(self):
        pass
    def hl_checked(self):
        pass
    def oe_checked(self):
        pass
    def io_checked(self, *args):
        pass
    def back(self, *args):
        self.parent.current = "mainmenuwindow"

class RedBlack(Screen):
    global drinks, deck_pick, hl_play, oe_play
    def __init__(self, **kwargs):
        super(RedBlack, self).__init__(**kwargs)
        Clock.schedule_once(self.update)

    def update(self, dt):
        self.ids.red.disabled = False
        self.ids.black.disabled = False
        self.ids.drinks.text = f'Drinks: {drinks}'
        self.ids.waiting.text = "Waiting..."
        self.ids.cardimage.source = "Images/card_back.png"
        self.ids.cardimage.reload()

    def pressed(self, pick):
        global drinks, deck_pick, card_img
        self.ids.red.disabled = True
        self.ids.black.disabled = True
        n = random.randint(0, len(deck)-1)
        self.ids.cardimage.source = (deck[n][3])
        self.ids.cardimage.reload()
        print(deck[n][2])
        if pick == (deck[n][1]):
            if len(deck) == 1:
                self.parent.current = "nomorecards"
            elif hl_play == 0:
                del deck[n]
                print("Correct")
                print(f"Cards left: {len(deck)}")
                self.ids.waiting.text = "Correct"
                Clock.schedule_once(self.next_question, 1)
                return deck_pick, drinks
            else:
                deck_pick = n
                print("Correct")
                print(f"Cards left: {len(deck)}")
                self.ids.waiting.text = "Correct"
                Clock.schedule_once(self.next_question, 1)
                return deck_pick, drinks
        else:
            del deck[n]
            if len(deck) == 0:
                self.parent.current = "nomorecards" 
            else:
                drinks += 1
                print ("Wrong")
                print(f"Cards left: {len(deck)}")
                self.ids.waiting.text = "Incorrect"
                Clock.schedule_once(self.update, 1)
                
    def next_question(self, *args):
        if hl_play == 1:
            self.parent.current = "highlowwindow"
        elif oe_play == 1:
            self.parent.current = "oddevenwindow"
        else:
            self.parent.current = "nextplayerwindow"

    def exit(self):
        half_build_deck()
        self.parent.current = "mainmenuwindow"
    
class HighLow(Screen):
    global drinks, deck_pick
    def __init__(self, **kwargs):
        super(HighLow, self).__init__(**kwargs)
        Clock.schedule_once(self.update)

    def update(self, dt):
        global deck_pick
        self.ids.higher.disabled = False
        self.ids.lower.disabled = False
        self.ids.drinks.text = f'Drinks: {drinks}'
        self.ids.waiting.text = "Waiting..."
        self.ids.cardimage.source = (deck[deck_pick][3])
        self.ids.cardimage.reload()

    def pressed(self, pick):
        global drinks, deck_pick
        self.ids.higher.disabled = True
        self.ids.lower.disabled = True
        m = random.randint(0, len(deck)-1)
        while m == int(deck_pick):
            m = random.randint(0, len(deck)-1)
        self.ids.cardimage.source = (deck[m][3])
        self.ids.cardimage.reload()
        print(f"Previous number value: {(deck[deck_pick][0])}")             # info print - delete
        print(f"New number value: {(deck[m][0])}")                          # info print - delete
        print(deck[m][2])  
        if pick == 1:
            answer_two = (deck[m][0]) > (deck[int(deck_pick)][0])
        elif pick == 2:
            answer_two = (deck[int(deck_pick)][0]) > (deck[m][0])
        if answer_two == True:
            if m > int(deck_pick):
                del deck[m]
                del deck[int(deck_pick)]
            else:
                del deck[int(deck_pick)]
                del deck[m]
            if len(deck) == 0:
                self.parent.current = "nomorecards"
            else:
                print(f"Cards left: {len(deck)}")
                print("Correct")
                self.ids.waiting.text = "Correct"
                Clock.schedule_once(self.next_question, 1)
        else:
            if m > int(deck_pick):
                del deck[m]
                del deck[int(deck_pick)]
            else:
                del deck[int(deck_pick)]
                del deck[m]
            if len(deck) == 0:
                self.parent.current = "nomorecards"
            else:
                drinks += 1
                print(f"Cards left: {len(deck)}")
                print ("Wrong")
                self.ids.waiting.text = "Incorrect"
                Clock.schedule_once(self.back_question, 1)

    def back_question(self, *args):
        self.parent.current = "redblackwindow"

    def next_question(self, *args):
        if oe_play == 1:
            self.parent.current = "oddevenwindow"
        elif oe_play == 0:
            self.parent.current = "nextplayerwindow"
        
    def exit(self):
        half_build_deck()
        self.parent.current = "mainmenuwindow"

class OddEven(Screen):
    global drinks
    def __init__(self, **kwargs):
        super(OddEven, self).__init__(**kwargs)
        Clock.schedule_once(self.update)
    
    def update(self, dt):
        self.ids.odd.disabled = False
        self.ids.even.disabled = False
        self.ids.drinks.text = f'Drinks: {drinks}'
        self.ids.waiting.text = "Waiting..."
        self.ids.cardimage.source = "Images/card_back.png"
        self.ids.cardimage.reload()
    
    def pressed(self, pick):
        global drinks
        self.ids.odd.disabled = True
        self.ids.even.disabled = True
        o = random.randint(0, len(deck)-1)
        self.ids.cardimage.source = (deck[o][3])
        self.ids.cardimage.reload()
        print(deck[o][2])
        if pick == 1:
            odd_or_even = (deck[o][0]) % 2 >= 1
        elif pick == 2:
            odd_or_even = (deck[o][0]) % 2 == 0
        if odd_or_even == True:
            del deck[o]
            if len(deck) == 0:
                self.parent.current = "nomorecards"
            else:          
                print(f"Cards left: {len(deck)}")                       # delete print later
                print(f"Drinks: {drinks}")                              # delete print later
                self.ids.waiting.text = "Correct"
                Clock.schedule_once(self.finish, 1)
                return drinks
        else:
            del deck[o]
            if len(deck) == 0:
                self.parent.current = "nomorecards"
            else:
                drinks += 1
                print(f"Cards left: {len(deck)}")                       # delete print later
                print(f"Drinks: {drinks}")  
                self.ids.waiting.text = "Incorrect"
                Clock.schedule_once(self.back_question, 1)
    
    def finish(self, *args):
        self.parent.current = "nextplayerwindow"
    def back_question(self, *args):
        if rb_play == 1:
            self.parent.current = "redblackwindow"
        elif rb_play == 0:
            Clock.schedule_once(self.update, 1)
    def exit(self):
        half_build_deck()
        self.parent.current = "mainmenuwindow"

class InOut(Screen):
    global drinks
    def __init__(self, **kwargs):
        super(InOut, self).__init__(**kwargs)
        Clock.schedule_once(self.update)

    def update(self, dt):
        self.ids.inn.disabled = False
        self.ids.out.disabled = False
        self.ids.drinks.text = f'Drinks: {drinks}'
        self.ids.waiting.text = "Waiting..."
        self.ids.cardimage.source = "Images/card_back.png"
        self.ids.cardimage.reload()

    def pressed(self, pick):
        global drinks
        self.ids.inn.disabled = True
        self.ids.out.disabled = True
        p = random.randint(0, len(deck)-1)
        self.ids.cardimage.source = (deck[p][3])
        self.ids.cardimage.reload()
        print(deck[p][2])
        if pick == 1:
            in_or_out = (deck[p][0])
        elif pick == 2:
            in_or_out = (deck[p][0])
        if in_or_out == True:
            del deck[p]
            if len(deck) == 0:
                self.parent.current = "nomorecards"
            else:          
                print(f"Cards left: {len(deck)}")                       # delete print later
                print(f"Drinks: {drinks}")                              # delete print later
                self.ids.waiting.text = "Correct"
                Clock.schedule_once(self.next_question, 1)
                return drinks
        else:
            del deck[p]
            if len(deck) == 0:
                self.parent.current = "nomorecards"
            else:
                drinks += 1
                print(f"Cards left: {len(deck)}")                       # delete print later
                print(f"Drinks: {drinks}")  
                self.ids.waiting.text = "Incorrect"
                Clock.schedule_once(self.back_question, 1)
    
    def next_question(self, *args):
        self.parent.current = "nextplayerwindow"
    def back_question(self, *args):
        if rb_play == 1:
            self.parent.current = "redblackwindow"
        elif rb_play == 0:
            Clock.schedule_once(self.update, 1)
    def exit(self):
        half_build_deck()
        self.parent.current = "mainmenuwindow"


class NextPlayer(Screen):
    global drinks

    def __init__(self, **kwargs):
        super(NextPlayer, self).__init__(**kwargs)
        Clock.schedule_once(self.update)

    def update(self, dt):
        self.ids.nextplayer.disabled = False
        global drinks
        if drinks == 0:
            self.ids.drinkstally.text = f'Alright tin ass! Your safe.'
        elif drinks == 1:
            self.ids.drinkstally.text = f'Ok ok your done, but you\'ve got {drinks} drink to consume first!'
        else:
            self.ids.drinkstally.text = f'Well your done but you\'ve racked up {drinks} drinks! Unluggy'

    def pressed(self):
        self.ids.nextplayer.disabled = True
        global drinks
        drinks = 0
        Clock.schedule_once(self.restart, 1)
        return drinks

    def restart(self, *args):
        if rb_play == 1:
            self.parent.current = "redblackwindow"
        elif rb_play == 0 and oe_play == 1:
            self.parent.current = "oddevenwindow"

class NoMoreCards(Screen):
    def __init__(self, **kwargs):
        super(NoMoreCards, self).__init__(**kwargs)
        Clock.schedule_once(self.update)
        
    def update(self, dt):
        self.ids.rebuild.disabled = False
        global drinks
        self.ids.finaldrinks.text = f'Bruh! \nNo one cares if you\ngot that guess right...\nTheres no more cards left\nThat\'s a vessel!\nPlus the {drinks} drinks you racked up!'
    def restart(self, *args):
        self.ids.rebuild.disabled = True
        global drinks
        drinks = 0
        half_build_deck()
        Clock.schedule_once(self.start, 2)
    def start(self, *args):
        self.parent.current = "redblackwindow"
    def exit(self):
        half_build_deck()
        self.parent.current = "mainmenuwindow"
        
kv = Builder.load_file("my.kv")

class MyMainApp(App):
    def build(self):
        Window.clearcolor = (242/255.0, 242/255.0, 242/255.0, 1)    
        return kv

if __name__ == "__main__":
    MyMainApp().run()
