import random
# Author @Tom ; @Felix
# Version 1.0
# Date 05.12.2023

# ein triviales Frage-Antwort-Spiel

# Klasse der Fragen, eine Frage beinhaltet die Frage, Antwortoptionen und eine Antwort
class Question:
    def __init__(self, question, options, answer) -> None:              # Kontrucktor
        self.question: str = question
        self.options = options
        self.answer: int = answer

    def display_question(self):                                        # Methode um die Fragen auszugeben
        print(self.question)
        for i, option in enumerate(self.options, 1):
            print(f"{i}: {option}")

    def check_answer(self, player_answer: int):                         # Methode um die Spielerantwort zu überprüfen
        return player_answer == self.answer



# Klasse der Spieler, ein Spieler hat einen Namen und eine Punktzahl
class Player:
    def __init__(self, name) -> None:
        self.name = name                                                # Jeder Speieler benötigt einen eindeutigen namen
        self.score: int = 0                                             

    def update_score(self, points: int):                                # set-Methode für die Anpassung des Punktestands
        self.score += points

# ####### Klasse aller Spiele ########
class TrivialGame:
    def __init__(self, players: list, rounds: int, questions: list) -> None:
        self.players = players
        self.rounds = rounds
        self.questions = questions
        self.round_count: int = 1


# Klasse eines Spiels, hier wird das Spiel mit Spielern und Fragen erstellt
    def game(self):                                
        if self.rounds > len(self.questions):                                          # Es können nicht mehr runden als Fragen existieren
            print("### zu viele Runden, zu wenig Fragen ###")
            return

        for round_to_play in range(1, self.rounds + 1):                                # es werden so viele Fragen wie gewünschte Runden gespielt
            
            print(f" ####  Runde Nummer: {round_to_play}  #### ")    

            round_question = random.choice(self.questions)
            self.questions.remove(round_question)

            for p in self.players:                                                      # für jeden Spieler wird die Frage wiederholt        
                # Frage Ausgeben
                print(f"{p.name}, du bist am Zug, deine Frage: ")
                round_question.display_question()
                # Antwort des Spielers
                player_answer: int = int(input("Wähle deine Antwort: "))
                # Auswertung
                if round_question.check_answer(player_answer):
                    p.update_score(1)
                    print("# Deine Antwort ist richtig #")
                else:
                    print(f"Du Blöd? -> das ist falsch!!! Das wäre die korrete Antwort: {round_question.options[round_question.answer - 1]} ")
                # Nächster Spieler       
            # Runde beenden und zur nächsten überleiten    

        self.end_game()

    def end_game(self):

        champ: Player = self.players[0]

        for p in self.players:
            #### evtl. Sieger ermitteln #### 
            print(f"{p.name} hat eine finale Punktzahl von: {p.score} / {self.rounds}")


### Fragen erstellen: ###
question1 = Question("Was ist der größte Planet in unserem Sonnensystem?", ["Erde", "Jupiter", "Mars", "Saturn"], 2)
question2 = Question("Welches Element hat das chemische Symbol 'H'?", ["Helium", "Wasserstoff", "Hassium", "Hafnium"], 2)
question3 = Question("In welchem Jahr erreichte Christoph Kolumbus die Amerikas?", ["1492", "1520", "1607", "1620"], 1)
question4 = Question("Was ist die Hauptstadt von Japan?", ["Peking", "Seoul", "Tokio", "Bangkok"], 3)
question5 = Question("Wer schrieb 'Romeo und Julia'?", ["Charles Dickens", "Jane Austen", "William Shakespeare", "Mark Twain"], 3)
question6 = Question("Welcher Planet wird als der 'Rote Planet' bezeichnet?", ["Venus", "Mars", "Jupiter", "Saturn"], 2)
question7 = Question("Was ist der Hauptbestandteil der Erdatmosphäre?", ["Stickstoff", "Sauerstoff", "Kohlendioxid", "Argon"], 1)
question8 = Question("Wer entwickelte die Relativitätstheorie?", ["Isaac Newton", "Albert Einstein", "Stephen Hawking", "Galileo Galilei"], 2)
question9 = Question("Welcher Ozean ist der größte auf der Erde?", ["Atlantik", "Indischer Ozean", "Südlicher Ozean", "Pazifik"], 4)
question10 = Question("Was ist die Währung von Deutschland?", ["Euro", "Britisches Pfund", "US-Dollar", "Yen"], 1)
question11 = Question("Wie viele Kontinente gibt es auf der Erde?", ["4", "6", "7", "5"], 3)
question12 = Question("Wer ist der Verfasser von 'Die Odyssee'?", ["Homer", "Platon", "Aristoteles", "Sophokles"], 2)
question13 = Question("In welchem Jahr endete der Zweite Weltkrieg?", ["1943", "1945", "1950", "1939"], 2)
question14 = Question("Welches Tier ist das größte auf der Erde?", ["Elefant", "Blauwal", "Giraffe", "Nashorn"], 2)
question15 = Question("Wer malte die Mona Lisa?", ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"], 2)
question16 = Question("Welche Farbe hat die Schneewittchen-Story?", ["Rot", "Blau", "Gelb", "Schwarz"], 1)
question17 = Question("Was ist die Hauptzutat in Guacamole?", ["Tomaten", "Avocado", "Zwiebeln", "Mais"], 2)
question18 = Question("Welcher Planet ist der Sonne am nächsten?", ["Mars", "Venus", "Merkur", "Jupiter"], 3)
question19 = Question("Welches ist das längste Fluss der Welt?", ["Nil", "Amazonas", "Jangtsekiang", "Mississippi"], 2)
question20 = Question("Wer schrieb 'Die Verwandlung'?", ["Franz Kafka", "Friedrich Nietzsche", "Thomas Mann", "Hermann Hesse"], 1)


questions_list = [question1, question2, question3, question4, question5, question6, question7, question8, question9, question10, question11, question12, question13, question14, question15, question16, question17, question18, question19, question20 ]


### Spieler erstellen ###
players: list = []

i: int = int(input("Wie Viele Spieler soll es geben?: "))
for j in range(i):
    name = input(f"Wie heißt Spieler {j+1}?: ")
    new_player = Player(name)
    players.append(new_player)

#####################
### Spiel Starten ###
#####################

rounds: int = int(input("Wie viele Runden wollt ihr spielen? "))
print("########  Los gehts ########")
my_game = TrivialGame(players, rounds, questions_list)
my_game.game()
