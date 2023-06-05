import random
from getpass import getpass

def get_word_for_single_player():
    word_list = [
    "hei", "velkommen", "takk", "hjelp", "elsker", "viking", "fjord", "bok", "skole", 
    "bil", "hus", "hund", "katt", "mat", "vann", "himmel", "regn", "sol", "måne", 
    "stjerne", "nord", "sør", "øst", "vest", "god", "dårlig", "stor", "liten", 
    "lang", "kort", "varm", "kald", "rask", "sakte", "venn", "fiende", "familie", 
    "glede", "sorg", "lys", "mørke", "dag", "natt", "tidlig", "sen", "yngre", 
    "eldre", "sterk", "svak", "liv", "død", "kaffe", "te", "frokost", "lunsj", 
    "middag", "kjøtt", "fisk", "brød", "ost", "museum", "bibliotek", "universitet", 
    "buss", "tog", "fly", "havn", "sykehus", "politiet", "brannstasjon", "post", 
    "bank", "kirke", "tempel", "synagoge", "moske", "idrett", "fotball", "ski", 
    "løping", "svømming", "musikk", "dans", "teater", "film", "kunst", "maleri", 
    "skulptur", "fotografi", "natur", "skog", "fjell", "elv", "sjø", "hav", 
    "blomst", "tre", "dyr", "insekt", "fugl", "fisk", "reptil", "amfibium", 
    "pattedyr", "kontinent", "land", "stat", "provins", "by", "landsby", "vei", 
    "gate", "bro", "tunnel", "høyhus", "stasjon", "lufthavn", "hotel", "restaurant", 
    "kafé", "butikk", "marked", "park", "strand", "stadium", "arena", "klubb", 
    "bar", "diskotek", "festival", "konsert", "utstilling", "konkurranse", "mesterskap", 
    "turnering", "ol", "vm", "em", "serie", "cup", "trofé", "medalje", "rekord", 
    "prestasjon", "seier", "nederlag", "uavgjort", "spiller", "trener", "dommer", 
    "supporter", "publikum", "lag", "klubb", "forening", "organisasjon", "bedrift", 
    "firma", "etablissement", "institusjon", "myndighet", "departement", "kommune", 
    "fylke", "region", "distrikt", "sonen", "område", "sted", "punkt", "linje", 
    "flate", "volum", "form", "farge", "størrelse", "avstand", "høyde", "bredde", 
    "dybde", "lengde", "vinkel", "grad", "prosent", "mengde", "tall", "nummber", 
    "bokstav", "ord", "setning", "spørsmål", "svar", "navn", "tittel", "kategori", 
    "type", "klasse", "gruppe", "serie", "rekke", "liste", "samling", "system", 
    "modell", "metode", "teknikk", "strategi", "plan", "program", "prosjekt", 
    "oppgave", "aktivitet", "øvelse", "test", "eksamen", "kurs", "studium", "utdanning", 
    "forskning", "vitenskap", "teknologi", "medisin", "jus", "økonomi", "politikk", 
    "historie", "kultur", "religion", "filosofi", "psykologi", "sosiologi", "geografi", 
    "biologi", "fysikk", "kjemi", "matematikk", "statistikk", "informatikk", "design", 
    "arkitektur", "journalistikk", "litteratur", "poesi", "prosa", "drama", "fiksjon", 
    "sannhet", "realitet", "fantasi", "drøm", "håp", "frykt", "glede", "tristhet", 
    "sinne", "kjærlighet", "hat", "lykke", "ulykke", "fred", "krig", "frihet", 
    "fengsel", "rikdom", "fattigdom", "likestilling", "diskriminering", "rettferdighet", 
    "urettferdighet"
]
    return random.choice(word_list)

def get_word_for_multiplayer():
    word = getpass("Spiller 1, Venligst skriv et ord: ").lower()
    if len(word) != 0:
        return word
    else:
        print("Du må skrive et ord.\n")
        get_word_for_multiplayer()

def hangman(chosen_word):
    stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        """
    ]

    guessed_letters = []
    tries = len(stages) - 1

    print("La oss spille Hangman!")
    print('_ ' * len(chosen_word))
    print("\n")

    while tries > 0:
        guess = input("Gjett en bokstav: ").lower()
        if len(guess) != 1:
            print("Vennligst gjett en bokstav om gangen.")
        elif guess in guessed_letters:
            print("Du har allerede gjettet den bokstaven, prøv noe annet.")
        elif guess not in chosen_word:
            print(guess, "er ikke i ordet. Du mister et forsøk.")
            tries -= 1
        else:
            print("Bra jobbet,", guess, "er i ordet!")
            guessed_letters.append(guess)

        word_so_far = ''
        for letter in chosen_word:
            if letter in guessed_letters:
                word_so_far += letter + ' '
            else:
                word_so_far += '_ '
        print(word_so_far)
        print(stages[len(stages) - 1 - tries])

        if word_so_far.replace(" ", "") == chosen_word:
            break

    if tries:
        print("Gratulerer! Du gjettet ordet!")
    else:
        print("Beklager, du gikk tom for forsøk. Ordet var", chosen_word)

while True:
    mode = input("Velg en game mode: (1) Single Player, (2) Multiplayer: ")
    if mode == '1':
        chosen_word = get_word_for_single_player()
        hangman(chosen_word)
        break
    elif mode == '2':
        chosen_word = get_word_for_multiplayer()
        hangman(chosen_word)
        break
    else:
        print("Ugyldig game mode valgt, Venligst prøv igjen, og velg 1 eller 2\n")