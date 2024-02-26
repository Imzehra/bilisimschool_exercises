import time 
import game 
class game:
    def __init__(self):
        self.opponent_energy = 100
        self.player_energy = 100
        self.round = 1
def print_game_state(self):
    print("Yere erişilene kadar kalan zaman:", self.round * 10)
    print("Saldırgan Enerjisi:", self.opponent_energy)
    print("Oyuncu Enerjisi:", self.player_energy)
    
def player_attack(self):
    self.opponent_energy -= 10
    self.player_energy -= 5
    if self.opponent_energy <= 0:
        self.opponent_energy = 0
    if self.player_energy <= 0:
        self.player_energy = 0

def player_defend(self):
    self.player_energy += 10
    if self.player_energy > 100:
        self.player_energy = 100

def opponent_attack(self):
    self.player_energy -= 20
    if self.player_energy <= 0:
        self.player_energy = 0
def start_game(self):
    while self.round <= 5:
        self.print_game_state()
        action = input("Yapmak istediğiniz işlemi girin (saldır/engelle/kes): ")
        if action == "saldır":
            self.player_attack()
        elif action == "engelle":
            self.player_defend()
        elif action == "kes":
            self.opponent_attack()
        else:
            print("Geçersiz işlem")
        time.sleep(5)
        self.round += 1
    self.print_game_state()
    if self.opponent_energy <= 0:
        print("Tebrikler! Saldırganı mahveddiniz.")
    elif self.player_energy <= 0:
        print("Maalesef yere ulaşamadınız.")
if __name__ == "__main__":
    game = Game()
    game.start_game(5)
