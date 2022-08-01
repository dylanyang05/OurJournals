print("hello")
print("I have no idea")
def main ():
    path = path.cwd()/"OURJOURNALS"/"cash_on_hand.csv"
    home = path.home()
    file_path = home/"OURJOURNALS"
    cash_on_hand = path.glob("*.txt")
    print(cash_on_hand)
