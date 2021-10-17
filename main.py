from logging import root
import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.image import Image as CoreImage
from kivy.uix.screenmanager import CardTransition, ScreenManager,  Screen, ShaderTransition, SlideTransition
from kivy.uix.checkbox import CheckBox
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.videoplayer import VideoPlayer
import random
import webbrowser

one_spades = (1, 2, 'One of Spades', "Images/ace_spades.png", 1)
two_spades = (2, 2, 'Two of Spades', "Images/two_spades.png", 1)
three_spades = (3, 2, 'Three of Spades', "Images/three_spades.png", 1)
four_spades = (4, 2, 'Four of Spades', "Images/four_spades.png", 1)
five_spades = (5, 2, 'Five of Spades', "Images/five_spades.png", 1)
six_spades = (6, 2, 'Six of Spades', "Images/six_spades.png", 1)
seven_spades = (7, 2, 'Seven of Spades', "Images/seven_spades.png", 1)
eight_spades = (8, 2, 'Eight of Spades', "Images/eight_spades.png", 1)
nine_spades = (9, 2, 'Nine of Spades', "Images/nine_spades.png", 1)
ten_spades = (10, 2, 'Ten of Spades', "Images/ten_spades.png", 1)
joker_spades = (11, 2, 'Jack of Spades', "Images/jack_spades.png", 1)
queen_spades = (12, 2, 'Queen of Spades', "Images/queen_spades.png", 1)
king_spades = (13, 2, 'King of Spades', "Images/king_spades.png", 1)
one_clubs = (1, 2, 'One of Clubs', "Images/ace_clubs.png", 2)
two_clubs = (2, 2, 'Two of Clubs', "Images/two_clubs.png", 2)
three_clubs = (3, 2, 'Three of Clubs', "Images/three_clubs.png", 2)
four_clubs = (4, 2, 'Four of Clubs', "Images/four_clubs.png", 2)
five_clubs = (5, 2, 'Five of Clubs', "Images/five_clubs.png", 2)
six_clubs = (6, 2, 'Six of Clubs', "Images/six_clubs.png", 2)
seven_clubs = (7, 2, 'Seven of Clubs', "Images/seven_clubs.png", 2)
eight_clubs = (8, 2, 'Eight of Clubs', "Images/eight_clubs.png", 2)
nine_clubs = (9, 2, 'Nine of Clubs', "Images/nine_clubs.png", 2)
ten_clubs = (10, 2, 'Ten of Clubs', "Images/ten_clubs.png", 2)
joker_clubs = (11, 2, 'Jack of Clubs', "Images/jack_clubs.png", 2)
queen_clubs = (12, 2, 'Queen of Clubs', "Images/queen_clubs.png", 2)
king_clubs = (13, 2, 'King of Clubs', "Images/king_clubs.png", 2)
one_dmnds = (1, 1, 'One of Diamonds', "Images/ace_diamonds.png", 3)
two_dmnds = (2, 1, 'Two of Diamonds', "Images/two_diamonds.png", 3)
three_dmnds = (3, 1, 'Three of Diamonds', "Images/three_diamonds.png", 3)
four_dmnds = (4, 1, 'Four of Diamonds', "Images/four_diamonds.png", 3)
five_dmnds = (5, 1, 'Five of Diamonds', "Images/five_diamonds.png", 3)
six_dmnds = (6, 1, 'Six of Diamonds', "Images/six_diamonds.png", 3)
seven_dmnds = (7, 1, 'Seven of Diamonds', "Images/seven_diamonds.png", 3)
eight_dmnds = (8, 1, 'Eight of Diamonds', "Images/eight_diamonds.png", 3)
nine_dmnds = (9, 1, 'Nine of Diamonds', "Images/nine_diamonds.png", 3)
ten_dmnds = (10, 1, 'Ten of Diamonds', "Images/ten_diamonds.png", 3)
joker_dmnds = (11, 1, 'Jack of Diamonds', "Images/jack_diamonds.png", 3)
queen_dmnds = (12, 1, 'Queen of Diamonds', "Images/queen_diamonds.png", 3)
king_dmnds = (13, 1, 'King of Diamonds', "Images/king_diamonds.png", 3)
one_hearts = (1, 1, 'One of Hearts', "Images/ace_hearts.png", 4)
two_hearts = (2, 1, 'Two of Hearts', "Images/two_hearts.png", 4)
three_hearts = (3, 1, 'Three of Hearts', "Images/three_hearts.png", 4)
four_hearts = (4, 1, 'Four of Hearts', "Images/four_hearts.png", 4)
five_hearts = (5, 1, 'Five of Hearts', "Images/five_hearts.png", 4)
six_hearts = (6, 1, 'Six of Hearts', "Images/six_hearts.png", 4)
seven_hearts = (7, 1, 'Seven of Hearts', "Images/seven_hearts.png", 4)
eight_hearts = (8, 1, 'Eight of Hearts', "Images/eight_hearts.png", 4)
nine_hearts = (9, 1, 'Nine of Hearts', "Images/nine_hearts.png", 4)
ten_hearts = (10, 1, 'Ten of Hearts', "Images/ten_hearts.png", 4)
joker_hearts = (11, 1, 'Jack of Hearts', "Images/jack_hearts.png", 4)
queen_hearts = (12, 1, 'Queen of Hearts', "Images/queen_hearts.png", 4)
king_hearts = (13, 1, 'King of Hearts', "Images/king_hearts.png", 4)

deck = [(one_spades), (two_spades), (three_spades), (four_spades), (five_spades), (six_spades), (seven_spades), (eight_spades), (nine_spades), (ten_spades), (joker_spades), (queen_spades), (king_spades), (one_clubs), (two_clubs), (three_clubs), (four_clubs), (five_clubs), (six_clubs), (seven_clubs), (eight_clubs), (nine_clubs), (ten_clubs), (joker_clubs), (queen_clubs), (king_clubs), (one_dmnds), (two_dmnds), (three_dmnds), (four_dmnds), (five_dmnds), (six_dmnds), (seven_dmnds), (eight_dmnds), (nine_dmnds), (ten_dmnds), (joker_dmnds), (queen_dmnds), (king_dmnds), (one_hearts), (two_hearts), (three_hearts), (four_hearts), (five_hearts), (six_hearts), (seven_hearts), (eight_hearts), (nine_hearts), (ten_hearts), (joker_hearts), (queen_hearts), (king_hearts)]

# stage deck will be used to move cards into, out of the main deck so they can be used for reference
# in higher rounds, the deck will then be cleared
stage_deck = []

drinks = 0
rb_pick = 0
rb_play = 1
hl_play = 1
oe_play = 1
io_play = 0
su_play = 0

# adds all "cards" back to the deck after finishing or quitting the round
def rebuild_deck():
    global deck, drinks
    deck = [(one_spades), (two_spades), (three_spades), (four_spades), (five_spades), (six_spades), (seven_spades), (eight_spades), (nine_spades), (ten_spades), (joker_spades), (queen_spades), (king_spades), (one_clubs), (two_clubs), (three_clubs), (four_clubs), (five_clubs), (six_clubs), (seven_clubs), (eight_clubs), (nine_clubs), (ten_clubs), (joker_clubs), (queen_clubs), (king_clubs), (one_dmnds), (two_dmnds), (three_dmnds), (four_dmnds), (five_dmnds), (six_dmnds), (seven_dmnds), (eight_dmnds), (nine_dmnds), (ten_dmnds), (joker_dmnds), (queen_dmnds), (king_dmnds), (one_hearts), (two_hearts), (three_hearts), (four_hearts), (five_hearts), (six_hearts), (seven_hearts), (eight_hearts), (nine_hearts), (ten_hearts), (joker_hearts), (queen_hearts), (king_hearts)]
    drinks = 0
    return deck, drinks

#  deletes cards from "stage deck", and clears for next go
def clear_stage_deck():
    stage_deck.clear()
    print(stage_deck)

# sets the reference to the preferred font
LabelBase.register(name='Fredoka', 
                   fn_regular='FredokaOne-Regular.ttf')

class WindowManager(ScreenManager):
    pass

class StartDisplay(Screen):
    secs = 0

    def __init__(self, **kwargs):
        super(StartDisplay, self).__init__(**kwargs)
        self.orientation = "vertical"
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, sec):
        self.secs = self.secs+1
        '''  30 seconds'''
        if self.secs == 1:
            self.ids.gif.anim_delay = 1/20
        if self.secs == 5:
            self.ids.gif.source = "Images/cheersLogoExpanded.png"
        if self.secs == 8:
            self.parent.current = "mainmenuwindow"

class MainMenu(Screen):
    # prints out all the rounds that will be played, information purposes
    def update(self):
        global rb_play, hl_play, oe_play, io_play, su_play
        print(rb_play)
        print(hl_play)
        print(oe_play)
        print(io_play)
        print(su_play)

    # only three windows available to be "starting point", as HighLow and InOut both need pre-req rounds
    def start(self):
        if rb_play == 1:
            self.parent.current = "redblackwindow"
        elif oe_play == 1:
            self.parent.current = "oddevenwindow"
        elif su_play == 1:
            self.parent.current = "suitswindow"

    def settings(self, *args):
        self.parent.current = "settingswindow"

    def credits(self, *args):
        self.parent.current = "creditswindow"

    def exit(self):
        quit()
# Settings complete
class SettingsMenu(Screen):
    def update(self, *args):
        global rb_play, hl_play, oe_play, io_play, su_play
        # disableds might be able to be deleted?
        self.ids.rb_check.disabled = False
        self.ids.hl_check.disabled = False
        self.ids.oe_check.disabled = False
        self.ids.io_check.disabled = False
        self.ids.su_check.disabled = False
        # switches change label colours, and changed round variables
        if self.ids.rb_check.active == True:
            self.ids.rbtext.color = "green"
            rb_play = 1
        elif self.ids.rb_check.active == False:
            self.ids.rbtext.color = "black"
            rb_play = 0
        if self.ids.hl_check.active == True:
            self.ids.hltext.color = "green"
            hl_play = 1
        elif self.ids.hl_check.active == False:
            self.ids.hltext.color = "black"
            hl_play = 0
        if self.ids.oe_check.active == True:
            self.ids.oetext.color = "green"
            oe_play = 1
        elif self.ids.oe_check.active == False:
            self.ids.oetext.color = "black"
            oe_play = 0
        if self.ids.io_check.active == True:
            self.ids.iotext.color = "green"
            io_play = 1
        elif self.ids.io_check.active == False:
            self.ids.iotext.color = "black"
            io_play = 0
        if self.ids.su_check.active == True:
            self.ids.sutext.color = "green"
            su_play = 1
        if self.ids.su_check.active == False:
            self.ids.sutext.color = "black"
            su_play = 0
        # rules - always keep one activated
        if int(rb_play + hl_play + oe_play + io_play + su_play) == 0:
            self.ids.rb_check.active = True
        # rules - HighLow needs RedBlack requirement
        if self.ids.rb_check.active == False:
            self.ids.hl_check.active = False
            self.ids.hl_check.disabled = True
        if self.ids.rb_check.active == True:
            self.ids.hl_check.disabled = False
        # rules - InOut needs two pre-rounds
        if int(rb_play + hl_play + oe_play) < 2:
            self.ids.io_check.active = False
            self.ids.io_check.disabled = True
        if int(rb_play + hl_play + oe_play) >= 2:
            self.ids.io_check.disabled = False
        return rb_play, hl_play, oe_play, io_play, su_play 

    def back(self, *args):
        self.parent.current = "mainmenuwindow"
# Credits complete
class Credits(Screen):
    def donate(self):
        webbrowser.open("https://www.paypal.com/donate?business=79LPXR4HHHWCC&no_recurring=0&item_name=All+donations+towards+OTPP+are+greatly+appreciated+and+go+towards+sustenance.&currency_code=NZD")
    def back(self, *args):
        self.parent.current = "mainmenuwindow"
# RedBlack complete
class RedBlack(Screen):

    def update(self, dt):
        self.ids.red.disabled = False
        self.ids.black.disabled = False
        self.ids.drinks.text = f'Drinks: {drinks}'
        self.ids.waiting.text = "Waiting..."
        self.ids.cardimage.source = "Images/card_back.png"
        self.ids.cardimage.reload()

    def pressed(self, pick):
        global drinks
        self.ids.red.disabled = True
        self.ids.black.disabled = True

        n = random.randint(0, len(deck)-1)
        self.ids.cardimage.source = (deck[n][3])
        self.ids.cardimage.reload()
        print(deck[n][2])

        if pick == (deck[n][1]):
            # if the pick is correct, remove from "deck", and place in "stage deck"
            stage_deck.append(deck.pop(n))
            print(stage_deck)
            print (len(deck))
            if len(deck) == 0:
                self.parent.current = "nomorecards"
            else:
                print(f"Cards left: {len(deck)}")
                self.ids.waiting.text = "Correct"
                Clock.schedule_once(self.next_question, 0.7)
        else:
            # if the pick is wrong, del from "deck", AND clear "stage deck". Keep it uniform
            clear_stage_deck()
            del deck[n]
            if len(deck) == 0:
                self.parent.current = "nomorecards" 
            else:
                drinks += 1
                print(f"Cards left: {len(deck)}")
                self.ids.waiting.text = "Incorrect"
                Clock.schedule_once(self.update, 0.7)
                return drinks
                
    def next_question(self, *args):
        if hl_play == 1:
            self.parent.current = "highlowwindow"
        elif oe_play == 1:
            self.parent.current = "oddevenwindow"
        elif io_play == 1:
            self.parent.current = "inoutwindow"
        elif su_play == 1:
            self.parent.current = "suitswindow"
        else:
            self.parent.current = "nextplayerwindow"
            
    def exit(self):
        clear_stage_deck()
        rebuild_deck()
        self.parent.current = "mainmenuwindow"
# HighLow complete, PLUS has reverse direction transition on "back_question"
class HighLow(Screen):

    def update(self, dt):
        self.ids.higher.disabled = False
        self.ids.lower.disabled = False
        self.ids.drinks.text = f'Drinks: {drinks}'
        self.ids.waiting.text = "Waiting..."
        self.ids.cardimage.source = (stage_deck[0][3])
        self.ids.cardimage.reload()

    def pressed(self, pick):
        global drinks
        self.ids.higher.disabled = True
        self.ids.lower.disabled = True

        m = random.randint(0, len(deck)-1)
        self.ids.cardimage.source = (deck[m][3])
        self.ids.cardimage.reload()
        print(deck[m][2])
        # setting formula to assess whether "higher" or "lower"
        if pick == 1:
            answer_two = (deck[m][0]) > (stage_deck[0][0])
        elif pick == 2:
            answer_two = (stage_deck[0][0]) > (deck[m][0])

        if answer_two == True:
            # if the pick is correct, remove from "deck", and place in "stage deck"
            stage_deck.append(deck.pop(m))
            print (stage_deck)
            print (len(deck))
            if len(deck) == 0:
                self.parent.current = "nomorecards"
            else:
                print(f"Cards left: {len(deck)}")
                self.ids.waiting.text = "Correct"
                Clock.schedule_once(self.next_question, 0.7)
        else:
            # if the pick is wrong, del from "deck", AND clear "stage deck". Keep it uniform
            clear_stage_deck()
            del deck[m]
            if len(deck) == 0:
                self.parent.current = "nomorecards"
            else:
                drinks += 1
                print(f"Cards left: {len(deck)}")
                self.ids.waiting.text = "Incorrect"
                Clock.schedule_once(self.back_question, 0.7)
                return drinks

    def back_question(self, *args):
        self.parent.transition = CardTransition(direction = "right")
        self.parent.current = "redblackwindow"

    def next_question(self, *args):
        if oe_play == 1:
            self.parent.current = "oddevenwindow"
        elif io_play == 1:
            self.parent.current = "inoutwindow"
        elif su_play == 1:
            self.parent.current = "suitswindow"
        else:
            self.parent.current = "nextplayerwindow"
        
    def exit(self):
        clear_stage_deck()
        rebuild_deck()
        self.parent.current = "mainmenuwindow"
# OddeEven complete, reverse direction transition written
class OddEven(Screen):

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
        # setting formula to assess whether "odd" or "even"      
        if pick == 1:
            odd_or_even = (deck[o][0]) % 2 >= 1
        elif pick == 2:
            odd_or_even = (deck[o][0]) % 2 == 0
            
        if odd_or_even == True:
            # if the pick is correct, remove from "deck", and place in "stage deck"
            stage_deck.append(deck.pop(o))
            print(stage_deck)
            print (len(deck))
            if len(deck) == 0:
                self.parent.current = "nomorecards"
            else:          
                print(f"Cards left: {len(deck)}")
                self.ids.waiting.text = "Correct"
                Clock.schedule_once(self.next_question, 0.7)
        else:
            # if the pick is wrong, del from "deck", AND clear "stage deck". Keep it uniform
            clear_stage_deck()
            del deck[o]
            if len(deck) == 0:
                self.parent.current = "nomorecards"
            else:
                drinks += 1
                print(f"Cards left: {len(deck)}")
                self.ids.waiting.text = "Incorrect"
                Clock.schedule_once(self.back_question, 0.7)
                return drinks

    def back_question(self, *args):
        self.parent.transition = CardTransition(direction = "right")
        if rb_play == 1:
            self.parent.current = "redblackwindow"
        elif rb_play == 0:
            Clock.schedule_once(self.update, 1)    

    def next_question(self, *args):
        if io_play == 1:
            self.parent.current = "inoutwindow"
        elif su_play == 1:
            self.parent.current = "suitswindow"
        else:
            self.parent.current = "nextplayerwindow"

    def exit(self):
        clear_stage_deck()
        rebuild_deck()
        self.parent.current = "mainmenuwindow"
# InOut complete, reverse direction transition written
class InOut(Screen):

    def update(self, dt):
        # shorten "stage_deck" to two here, so card images can be accessed
        if len(stage_deck) == 3:
            del stage_deck[0]

        self.ids.inn.disabled = False
        self.ids.out.disabled = False
        self.ids.drinks.text = f'Drinks: {drinks}'
        self.ids.waiting.text = "Waiting..."
        self.ids.cardimageone.source = (stage_deck[0][3])
        self.ids.cardimagetwo.source = (stage_deck[1][3])
        self.ids.cardimageone.reload()
        self.ids.cardimagetwo.reload()

    def pressed(self, pick):
        global drinks
        self.ids.inn.disabled = True
        self.ids.out.disabled = True

        p = random.randint(0, len(deck)-1)
        self.ids.layouttwo.remove_widget(self.ids.cardimagetwo)
        self.ids.cardimageone.source = (deck[p][3])
        self.ids.cardimageone.reload()
        print(deck[p][2])
        # setting formula to assess whether "odd" or "even"    
        if int(stage_deck[0][0]) < int(stage_deck[1][0]):
            is_inbetween = int(deck[p][0]) in range(int(stage_deck[0][0]), int(stage_deck[1][0]))
        else:
            is_inbetween = int(deck[p][0]) in range(int(stage_deck[1][0]), int(stage_deck[0][0]))
        if pick == 1:
            choice = True
        elif pick == 2:
            choice = False

        if is_inbetween == choice:
            # if the pick is correct, remove from "deck", and place in "stage deck"
            stage_deck.append(deck.pop(p))
            print (stage_deck)
            print (len(deck))
            if len(deck) == 0:
                self.parent.current = "nomorecards"
            else:          
                print(f"Cards left: {len(deck)}")
                self.ids.waiting.text = "Correct"
                Clock.schedule_once(self.next_question, 1)
        else:
            # if the pick is wrong, del from "deck", AND clear "stage deck". Keep it uniform
            clear_stage_deck()
            del deck[p]
            if len(deck) == 0:
                self.parent.current = "nomorecards"
            else:
                drinks += 1
                print(f"Cards left: {len(deck)}")
                self.ids.waiting.text = "Incorrect"
                Clock.schedule_once(self.back_question, 1)
                return drinks
    
    def leave(self, *args):
        # add second image back after removal
        self.ids.layouttwo.add_widget(self.ids.cardimagetwo)

    def back_question(self, *args):
        self.parent.transition = CardTransition(direction = "right")
        if rb_play == 1:
            self.parent.current = "redblackwindow"
        elif oe_play == 1:
            self.parent.current = "oddevenwindow"
        else:
            Clock.schedule_once(self.update, 1)    

    def next_question(self, *args):
        if su_play == 1:
            self.parent.current = "suitswindow"
        else:
            self.parent.current = "nextplayerwindow"
        
    def exit(self):
        clear_stage_deck()
        rebuild_deck()
        self.parent.current = "mainmenuwindow"
# Suits complete, reverse direction transition written
class Suits(Screen):

    def update(self, dt):
        self.ids.spades.disabled = False
        self.ids.clubs.disabled = False
        self.ids.hearts.disabled = False
        self.ids.diamonds.disabled = False
        self.ids.drinks.text = f'Drinks: {drinks}'
        self.ids.waiting.text = "Waiting..."
        self.ids.cardimage.source = "Images/card_back.png"
        self.ids.cardimage.reload()

    def pressed(self, pick):
        global drinks
        self.ids.spades.disabled = True
        self.ids.clubs.disabled = True
        self.ids.hearts.disabled = True
        self.ids.diamonds.disabled = True

        q = random.randint(0, len(deck)-1)
        self.ids.cardimage.source = (deck[q][3])
        self.ids.cardimage.reload()
        print(deck[q][2])

        if pick == (deck[q][4]):
            # if the pick is correct, del card. "stage deck no longer needed"
            del deck[q]
            if len(deck) == 0:
                self.parent.current = "nomorecards"
            else:          
                print(f"Cards left: {len(deck)}")
                self.ids.waiting.text = "Correct"
                Clock.schedule_once(self.next_question, 1)
        else:
            # if the pick is wrong, del from "deck", AND clear "stage deck". Keep it uniform
            clear_stage_deck()
            del deck[q]
            if len(deck) == 0:
                self.parent.current = "nomorecards"
            else:
                drinks += 1
                print(f"Cards left: {len(deck)}")
                self.ids.waiting.text = "Incorrect"
                Clock.schedule_once(self.back_question, 1)
                return drinks

    def back_question(self, *args):
        self.parent.transition = CardTransition(direction = "right")
        if rb_play == 1:
            self.parent.current = "redblackwindow"
        elif oe_play == 1:
            self.parent.current = "oddevenwindow"
        else:
            Clock.schedule_once(self.update, 1)    

    def next_question(self, *args):
        self.parent.current = "nextplayerwindow"

    def exit(self):
        rebuild_deck()
        self.parent.current = "mainmenuwindow"
# NextPlayer complete?
class NextPlayer(Screen):

    def update(self, dt):
        self.ids.nextplayer.disabled = False
        global drinks
        if drinks == 0:
            self.ids.drinkstally.text = f'Alright tin ass! You\'re safe.'
        elif drinks == 1:
            self.ids.drinkstally.text = f'Ok, ok your done, but you\'ve got {drinks} drink to consume first!'
        else:
            self.ids.drinkstally.text = f'Well your done but you\'ve racked up {drinks} drinks! Unluggy'

    def pressed(self):
        global drinks
        self.ids.nextplayer.disabled = True
        drinks = 0
        clear_stage_deck()
        Clock.schedule_once(self.restart, 1)
        return drinks

    def restart(self, *args):
        if rb_play == 1:
            self.parent.current = "redblackwindow"
        elif oe_play == 1:
            self.parent.current = "oddevenwindow"
        elif su_play == 1:
            self.parent.current = "suitswindow"
# NoMoreCards complete
class NoMoreCards(Screen):

    def update(self, dt):
        self.ids.rebuild.disabled = False
        global drinks
        self.ids.finaldrinks.text = f'Bruh! \nNo one cares if you\ngot that guess right...\nTheres no more cards left\nThat\'s a vessel!\nPlus the {drinks} drinks you racked up!'
        
    def restart(self, *args):
        self.ids.rebuild.disabled = True
        global drinks
        drinks = 0
        rebuild_deck()
        Clock.schedule_once(self.start, 2)
        
    def start(self, *args):
        if rb_play == 1:
            self.parent.current = "redblackwindow"
        elif oe_play == 1:
            self.parent.current = "oddevenwindow"
        elif su_play == 1:
            self.parent.current = "suitswindow"

    def exit(self):
        clear_stage_deck()
        rebuild_deck()
        self.parent.current = "mainmenuwindow"
        
kv = Builder.load_file("redorblack.kv")

class RedOrBlackApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        return kv

if __name__ == "__main__":
    RedOrBlackApp().run()
