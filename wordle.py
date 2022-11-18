from random import choice
import json
from tkinter import *
import re


class FrameApp(Frame):
    def __init__(self, master):
        super(FrameApp, self).__init__(master)
        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.app_running = True
        self.current_grid_cell = 0
        self.current_game = []
        self.five_letter_words = []
        self.regex1 = re.compile('[a-z]')   # lower case English words with and without apostrophes
        self.regex2 = re.compile('[a-z]*\W')  # lower case English, only words with apostrophes
        self.json_past_words_file = False
        self.json_five_letter_words_file = False
        self.past_words = []
        self.word_of_the_day = ''
        self.my_guess = ''
        self.game_over = False

        self.grid_font = "Ariel 24 bold"
        self.black = "dimgrey"
        self.grey = "#cccccc"
        self.yellow = "#ffcc00"
        self.green = "limegreen"
        self.border_width = 4
        self.main_box = None

        self.initialize_gui()
        self.initialize_past_words()
        self.initialize_five_letter_words()
        self.set_game()

    def initialize_five_letter_words(self):
        """
        Initialize five letter word list from json file
        :return:
        """
        try:
            with open('five_letter_words.json', 'r') as f:
                data = json.load(f)
                print(f'Five letter words: {data}')
                self.five_letter_words = data
                self.json_five_letter_words_file = True

        except FileNotFoundError:
            self.json_five_letter_words_file = False
            print("five_letter_words.json FILE NOT FOUND")

        finally:
            print("FINALLY - initialize_five_letter_words")

        if not self.json_five_letter_words_file:
            # five_letter_words = ["alpha"]
            self.update_five_letter_word_list()
            five_letter_words = self.five_letter_words
            with open('five_letter_words.json', 'w') as json_file:
                json.dump(five_letter_words, json_file)

    def initialize_past_words(self):
        """
        Initialize past words list from json file
        :return:
        """
        try:
            with open('pastwords.json', 'r') as f:
                data = json.load(f)
                print(f'Past words of the day: {data}')
                self.past_words = data
                self.json_past_words_file = True

        except FileNotFoundError:
            self.json_past_words_file = False
            print("pastwords.json FILE NOT FOUND")

        finally:
            print("FINALLY - initialize_past_words")

        if not self.json_past_words_file:
            past_words = ["catch"]
            with open('pastwords.json', 'w') as json_file:
                json.dump(past_words, json_file)

    def set_key(self, alpha, bg_color):
        """
        Set key color during gameplay
        :param alpha:
        :param bg_color:
        :return:
        """
        this_relief = "raised"

        if bg_color == self.black:
            this_relief = "sunken"
        if "a" == alpha:
            self.A_KEY.config(bg=bg_color, relief=this_relief)
        elif "b" == alpha:
            self.B_KEY.config(bg=bg_color, relief=this_relief)
        elif "c" == alpha:
            self.C_KEY.config(bg=bg_color, relief=this_relief)
        elif "d" == alpha:
            self.D_KEY.config(bg=bg_color, relief=this_relief)
        elif "e" == alpha:
            self.E_KEY.config(bg=bg_color, relief=this_relief)
        elif "f" == alpha:
            self.F_KEY.config(bg=bg_color, relief=this_relief)
        elif "g" == alpha:
            self.G_KEY.config(bg=bg_color, relief=this_relief)
        elif "h" == alpha:
            self.H_KEY.config(bg=bg_color, relief=this_relief)
        elif "i" == alpha:
            self.I_KEY.config(bg=bg_color, relief=this_relief)
        elif "j" == alpha:
            self.J_KEY.config(bg=bg_color, relief=this_relief)
        elif "k" == alpha:
            self.K_KEY.config(bg=bg_color, relief=this_relief)
        elif "l" == alpha:
            self.L_KEY.config(bg=bg_color, relief=this_relief)
        elif "m" == alpha:
            self.M_KEY.config(bg=bg_color, relief=this_relief)
        elif "n" == alpha:
            self.N_KEY.config(bg=bg_color, relief=this_relief)
        elif "o" == alpha:
            self.O_KEY.config(bg=bg_color, relief=this_relief)
        elif "p" == alpha:
            self.P_KEY.config(bg=bg_color, relief=this_relief)
        elif "q" == alpha:
            self.Q_KEY.config(bg=bg_color, relief=this_relief)
        elif "r" == alpha:
            self.R_KEY.config(bg=bg_color, relief=this_relief)
        elif "s" == alpha:
            self.S_KEY.config(bg=bg_color, relief=this_relief)
        elif "t" == alpha:
            self.T_KEY.config(bg=bg_color, relief=this_relief)
        elif "u" == alpha:
            self.U_KEY.config(bg=bg_color, relief=this_relief)
        elif "v" == alpha:
            self.V_KEY.config(bg=bg_color, relief=this_relief)
        elif "w" == alpha:
            self.W_KEY.config(bg=bg_color, relief=this_relief)
        elif "x" == alpha:
            self.X_KEY.config(bg=bg_color, relief=this_relief)
        elif "y" == alpha:
            self.Y_KEY.config(bg=bg_color, relief=this_relief)
        elif "z" == alpha:
            self.Z_KEY.config(bg=bg_color, relief=this_relief)

    def set_grid_cell(self, i, l, bg):
        if i == 0:
            self.l0.config(text=l, bg=bg)
        elif i == 1:
            self.l1.config(text=l, bg=bg)
        elif i == 2:
            self.l2.config(text=l, bg=bg)
        elif i == 3:
            self.l3.config(text=l, bg=bg)
        elif i == 4:
            self.l4.config(text=l, bg=bg)
        elif i == 5:
            self.l5.config(text=l, bg=bg)
        elif i == 6:
            self.l6.config(text=l, bg=bg)
        elif i == 7:
            self.l7.config(text=l, bg=bg)
        elif i == 8:
            self.l8.config(text=l, bg=bg)
        elif i == 9:
            self.l9.config(text=l, bg=bg)
        elif i == 10:
            self.l10.config(text=l, bg=bg)
        elif i == 11:
            self.l11.config(text=l, bg=bg)
        elif i == 12:
            self.l12.config(text=l, bg=bg)
        elif i == 13:
            self.l13.config(text=l, bg=bg)
        elif i == 14:
            self.l14.config(text=l, bg=bg)
        elif i == 15:
            self.l15.config(text=l, bg=bg)
        elif i == 16:
            self.l16.config(text=l, bg=bg)
        elif i == 17:
            self.l17.config(text=l, bg=bg)
        elif i == 18:
            self.l18.config(text=l, bg=bg)
        elif i == 19:
            self.l19.config(text=l, bg=bg)
        elif i == 20:
            self.l20.config(text=l, bg=bg)
        elif i == 21:
            self.l21.config(text=l, bg=bg)
        elif i == 22:
            self.l22.config(text=l, bg=bg)
        elif i == 23:
            self.l23.config(text=l, bg=bg)
        elif i == 24:
            self.l24.config(text=l, bg=bg)
        elif i == 25:
            self.l25.config(text=l, bg=bg)
        elif i == 26:
            self.l26.config(text=l, bg=bg)
        elif i == 27:
            self.l27.config(text=l, bg=bg)
        elif i == 28:
            self.l28.config(text=l, bg=bg)
        elif i == 29:
            self.l29.config(text=l, bg=bg)

    def check_my_guess(self):
        """
        Check my guess
        :return:
        """
        if self.game_over:
            self.lab_entry.config(text=f'GAME OVER - Hit reset to play again!')
            self.word.delete(0, 10)
            self.word.focus()
            print(f'GAME OVER, it was {self.word_of_the_day}.')
        else:
            self.my_guess = self.word.get()

            if self.my_guess in self.five_letter_words:

                if self.my_guess == self.word_of_the_day:
                    print(f'WINNER + {self.my_guess}')
                    self.lab_entry.config(text=f'{self.word_of_the_day} is the WINNER!!!')
                    self.game_over = True
                else:
                    print(f'Sorry, {self.my_guess} is NOT the winner.')
                    self.lab_entry.config(text="NOPE")

                letter_color = self.black
                self.current_grid_cell = len(self.current_game)
                print(self.current_grid_cell)

                for letter in self.my_guess:
                    self.current_game.append(letter)

                i = 0
                for alpha in self.my_guess:

                    if alpha not in self.word_of_the_day:
                        letter_color = self.black

                    elif alpha != self.word_of_the_day[i]:
                        letter_color = self.yellow

                    elif alpha == self.word_of_the_day[i]:
                        letter_color = self.green

                    self.set_key(alpha, letter_color)
                    print(f'{self.my_guess[i]} and {self.word_of_the_day[i]} -- {letter_color}')

                    self.set_grid_cell(self.current_grid_cell, alpha, letter_color)
                    self.current_grid_cell += 1
                    i += 1

                if self.current_grid_cell >= 30:
                    self.game_over = True
                    print(f'GAME OVER, it was {self.word_of_the_day}.')

                if self.game_over:
                    self.append_past_words_list(self.word_of_the_day)

            else:
                self.lab_entry.config(text="Not in word list.")
                print(f'{self.my_guess} is NOT valid.')

            self.word.select_range(0, 'end')

    def update_five_letter_word_list(self):
        """
        Update past words list and generate five letter word list
        :return:
        """
        with open('/usr/share/dict/words') as file:  # /usr/share/dict/words
            for word in (w.rstrip() for w in file):
                if self.regex1.match(word) and not self.regex2.match(word) and len(word) == 5:
                    self.five_letter_words.append(word)

    def set_game(self):
        """
        Algorithm for generating a random word not previously used.
        :return:
        """
        self.game_over = False
        self.current_game = []
        self.current_grid_cell = 0
        self.my_guess = ''

        for letter in self.alphabet:
            self.set_key(letter, self.grey)

        for i in range(30):
            self.set_grid_cell(i, " ", self.black)

        # two ways to clone a list; slicing and copying
        # apparently slicing is faster
        words = self.five_letter_words[:]
        # words = self.five_letter_words.copy()

        for pword in self.past_words:
            words.remove(pword)

        w = choice(words)

        self.word_of_the_day = w
        self.lab_entry.config(text=f'Enter word here - {w}')
        self.word.delete(0, 10)
        self.word.focus()

        print(f'$$$ {self.word_of_the_day} $$$')

    def append_past_words_list(self, word):
        """
        append past words list with completed game word
        :param word:
        :return:
        """
        self.past_words.append(word)
        # print(self.past_words)

        if self.json_past_words_file:
            with open('pastwords.json', 'w') as json_file:
                json.dump(self.past_words, json_file)

    def initialize_gui(self):
        """
        Messy UI code initialization.
        :return:
        """
        self.grid()

        self.main_box = Frame(self)
        self.main_box.grid(row=1, column=1, columnspan=10, padx=8, pady=8)

        # Row 1
        self.l0 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l0.grid(sticky=('n', 's', 'w', 'e'), row=2, column=1)

        self.l1 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l1.grid(sticky=('n', 's', 'w', 'e'), row=2, column=2)

        self.l2 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l2.grid(sticky=('n', 's', 'w', 'e'), row=2, column=3)

        self.l3 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l3.grid(sticky=('n', 's', 'w', 'e'), row=2, column=4)

        self.l4 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l4.grid(sticky=('n', 's', 'w', 'e'), row=2, column=5)

        # Row 2
        self.l5 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l5.grid(sticky=('n', 's', 'w', 'e'), row=3, column=1)

        self.l6 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l6.grid(sticky=('n', 's', 'w', 'e'), row=3, column=2)

        self.l7 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l7.grid(sticky=('n', 's', 'w', 'e'), row=3, column=3)

        self.l8 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l8.grid(sticky=('n', 's', 'w', 'e'), row=3, column=4)

        self.l9 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l9.grid(sticky=('n', 's', 'w', 'e'), row=3, column=5)

        # Row 3
        self.l10 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l10.grid(sticky=('n', 's', 'w', 'e'), row=4, column=1)

        self.l11 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l11.grid(sticky=('n', 's', 'w', 'e'), row=4, column=2)

        self.l12 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l12.grid(sticky=('n', 's', 'w', 'e'), row=4, column=3)

        self.l13 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l13.grid(sticky=('n', 's', 'w', 'e'), row=4, column=4)

        self.l14 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l14.grid(sticky=('n', 's', 'w', 'e'), row=4, column=5)

        # Row 4
        self.l15 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l15.grid(sticky=('n', 's', 'w', 'e'), row=5, column=1)

        self.l16 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l16.grid(sticky=('n', 's', 'w', 'e'), row=5, column=2)

        self.l17 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l17.grid(sticky=('n', 's', 'w', 'e'), row=5, column=3)

        self.l18 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l18.grid(sticky=('n', 's', 'w', 'e'), row=5, column=4)

        self.l19 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l19.grid(sticky=('n', 's', 'w', 'e'), row=5, column=5)

        # Row 5
        self.l20 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l20.grid(sticky=('n', 's', 'w', 'e'), row=6, column=1)

        self.l21 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l21.grid(sticky=('n', 's', 'w', 'e'), row=6, column=2)

        self.l22 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l22.grid(sticky=('n', 's', 'w', 'e'), row=6, column=3)

        self.l23 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l23.grid(sticky=('n', 's', 'w', 'e'), row=6, column=4)

        self.l24 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l24.grid(sticky=('n', 's', 'w', 'e'), row=6, column=5)

        # Row 6
        self.l25 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l25.grid(sticky=('n', 's', 'w', 'e'), row=7, column=1)

        self.l26 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l26.grid(sticky=('n', 's', 'w', 'e'), row=7, column=2)

        self.l27 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l27.grid(sticky=('n', 's', 'w', 'e'), row=7, column=3)

        self.l28 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l28.grid(sticky=('n', 's', 'w', 'e'), row=7, column=4)

        self.l29 = Label(self.main_box, text=" ", fg="white", bg=self.black, font=self.grid_font, width=4, padx=8, pady=8, borderwidth=self.border_width, relief="sunken")
        self.l29.grid(sticky=('n', 's', 'w', 'e'), row=7, column=5)

        self.lab_entry = Label(self.main_box, text="Enter guess here", font=("Poppins bold", 15))
        self.lab_entry.grid(row=8, column=1, columnspan=5)

        self.word = Entry(self.main_box, font=("Ariel", 15), borderwidth=self.border_width, relief="sunken")
        self.word.grid(row=9, column=1, columnspan=5)
        self.word.bind('<Return>', handler)

        self.b_reset = Button(self.main_box, text="Reset", command=self.set_game, bg='Lavender', width=4)
        self.b_reset.grid(sticky='e', row=11, column=2, columnspan=2)

        self.b_exit = Button(self.main_box, text="Exit", command=exit_app, bg='Lavender', width=4)
        self.b_exit.grid(sticky='w', row=11, column=4, columnspan=3)

        # Keyboard
        self.keyboard_box = Frame(self.main_box)
        self.keyboard_box.grid(row=100, column=1, columnspan=10, padx=2, pady=2)

        # Keyboard Row 1
        self.Q_KEY = Button(self.keyboard_box, text="Q", fg="white", bg=self.grey, relief="raised")
        self.Q_KEY.grid(row=100, column=0, padx=2, pady=2, sticky="e")

        self.W_KEY = Button(self.keyboard_box, text="W", fg="white", bg=self.grey, relief="raised")
        self.W_KEY.grid(row=100, column=1, padx=2, pady=2)

        self.E_KEY = Button(self.keyboard_box, text="E", fg="white", bg=self.grey, relief="raised")
        self.E_KEY.grid(row=100, column=2, padx=2, pady=2)

        self.R_KEY = Button(self.keyboard_box, text="R", fg="white", bg=self.grey, relief="raised")
        self.R_KEY.grid(row=100, column=3, padx=2, pady=2)

        self.T_KEY = Button(self.keyboard_box, text="T", fg="white", bg=self.grey, relief="raised")
        self.T_KEY.grid(row=100, column=4, padx=2, pady=2)

        self.Y_KEY = Button(self.keyboard_box, text="Y", fg="white", bg=self.grey, relief="raised")
        self.Y_KEY.grid(row=100, column=5, padx=2, pady=2)

        self.U_KEY = Button(self.keyboard_box, text="U", fg="white", bg=self.grey, relief="raised")
        self.U_KEY.grid(row=100, column=6, padx=2, pady=2)

        self.I_KEY = Button(self.keyboard_box, text="I", fg="white", bg=self.grey, relief="raised")
        self.I_KEY.grid(row=100, column=7, padx=2, pady=2)

        self.O_KEY = Button(self.keyboard_box, text="O", fg="white", bg=self.grey, relief="raised")
        self.O_KEY.grid(row=100, column=8, padx=2, pady=2, sticky="w")

        self.P_KEY = Button(self.keyboard_box, text="P", fg="white", bg=self.grey, relief="raised")
        self.P_KEY.grid(row=100, column=9, padx=2, pady=2, sticky="w")

        # Keyboard Row 2
        self.A_KEY = Button(self.keyboard_box, text="A", fg="white", bg=self.grey, relief="raised")
        self.A_KEY.grid(row=101, column=0, padx=2, pady=2, sticky="e")

        self.S_KEY = Button(self.keyboard_box, text="S", fg="white", bg=self.grey, relief="raised")
        self.S_KEY.grid(row=101, column=1, padx=2, pady=2)

        self.D_KEY = Button(self.keyboard_box, text="D", fg="white", bg=self.grey, relief="raised")
        self.D_KEY.grid(row=101, column=2, padx=2, pady=2)

        self.F_KEY = Button(self.keyboard_box, text="F", fg="white", bg=self.grey, relief="raised")
        self.F_KEY.grid(row=101, column=3, padx=2, pady=2)

        self.G_KEY = Button(self.keyboard_box, text="G", fg="white", bg=self.grey, relief="raised")
        self.G_KEY.grid(row=101, column=4, padx=2, pady=2)

        self.H_KEY = Button(self.keyboard_box, text="H", fg="white", bg=self.grey, relief="raised")
        self.H_KEY.grid(row=101, column=5, padx=2, pady=2)

        self.J_KEY = Button(self.keyboard_box, text="J", fg="white", bg=self.grey, relief="raised")
        self.J_KEY.grid(row=101, column=6, padx=2, pady=2)

        self.K_KEY = Button(self.keyboard_box, text="K", fg="white", bg=self.grey, relief="raised")
        self.K_KEY.grid(row=101, column=7, padx=2, pady=2)

        self.L_KEY = Button(self.keyboard_box, text="L", fg="white", bg=self.grey, relief="raised")
        self.L_KEY.grid(row=101, column=8, padx=2, pady=2, sticky="w")

        # Keyboard Row 3

        self.ENTER_KEY = Button(self.keyboard_box, text="ENTER", command=self.check_my_guess, fg="white", bg=self.grey, relief="raised")
        self.ENTER_KEY.grid(row=102, column=0, padx=2, pady=2)

        self.Z_KEY = Button(self.keyboard_box, text="Z", fg="white", bg=self.grey, relief="raised")
        self.Z_KEY.grid(row=102, column=1, padx=2, pady=2)

        self.X_KEY = Button(self.keyboard_box, text="X", fg="white", bg=self.grey, relief="raised")
        self.X_KEY.grid(row=102, column=2, padx=2, pady=2)

        self.C_KEY = Button(self.keyboard_box, text="C", fg="white", bg=self.grey, relief="raised")
        self.C_KEY.grid(row=102, column=3, padx=2, pady=2)

        self.V_KEY = Button(self.keyboard_box, text="V", fg="white", bg=self.grey, relief="raised")
        self.V_KEY.grid(row=102, column=4, padx=2, pady=2)

        self.B_KEY = Button(self.keyboard_box, text="B", fg="white", bg=self.grey, relief="raised")
        self.B_KEY.grid(row=102, column=5, padx=2, pady=2)

        self.N_KEY = Button(self.keyboard_box, text="N", fg="white", bg=self.grey, relief="raised")
        self.N_KEY.grid(row=102, column=6, padx=2, pady=2)

        self.M_KEY = Button(self.keyboard_box, text="M", fg="white", bg=self.grey, relief="raised")
        self.M_KEY.grid(row=102, column=7, padx=2, pady=2)

        self.BACK_KEY = Button(self.keyboard_box, text="BACK", fg="white", bg=self.grey, relief="raised")
        self.BACK_KEY.grid(row=102, column=8, padx=2, pady=2, columnspan=2)


def handler(e):
    """
    Handle enter key, submit enter
    :param e:
    :return:
    """
    app.check_my_guess()


def exit_app():
    """
    Quit wordle gracefully.
    :return:
    """
    app.app_running = False
    app.destroy()
    window.quit()


window = Tk()
window.geometry("575x640")
window.title("Wordle")

app = FrameApp(window)

while app.app_running:
    """
    runs mainloop of program
    """

    try:
        app.update()
    except TclError:
        # Someone closed the app using the Close 'X' instead of the Exit button
        pass
