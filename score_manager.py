class ScoreManager:
    def __init__(self, filename):
        self.filename = filename

    def save_score(self, player):
        with open(self.filename, "a") as f:
            f.write(f"{player.name},{player.score}\n")

    def show_scores(self):
        try:
            with open(self.filename, "r") as f:
                print("\n--- Scores ---")
                print(f.read())
        except FileNotFoundError:
            print("No scores yet.")