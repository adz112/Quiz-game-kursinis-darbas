import tkinter as tk
from tkinter import messagebox
import csv




def load_questions(filename):
    questions = []

    with open(filename, newline='', encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            questions.append({
                "question": row["question"],
                "options": row["options"].split("|"),
                "answer": row["answer"]
            })

    return questions




class StartScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game - Start")
        self.root.geometry("300x200")

        self.label = tk.Label(root, text="Enter your name:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.button = tk.Button(root, text="Start Game", command=self.start_game)
        self.button.pack(pady=10)

    def start_game(self):
        name = self.entry.get()

        if name == "":
            messagebox.showwarning("Warning", "Enter your name!")
            return

        self.root.destroy()

        new_root = tk.Tk()
        QuizGUI(new_root, name)
        new_root.mainloop()




class QuizGUI:
    def __init__(self, root, player_name):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("400x300")

        self.player_name = player_name
        self.questions = load_questions("questions.csv")

        self.index = 0
        self.score = 0

        self.label = tk.Label(root, text="", wraplength=350, font=("Arial", 12))
        self.label.pack(pady=20)

        self.buttons = []

        for i in range(4):
            btn = tk.Button(root, text="", width=25,
                            command=lambda i=i: self.check_answer(i))
            btn.pack(pady=3)
            self.buttons.append(btn)

        self.load_question()

    def load_question(self):
        if self.index >= len(self.questions):
            self.end_game()
            return

        q = self.questions[self.index]
        self.label.config(text=q["question"])

        for i, option in enumerate(q["options"]):
            self.buttons[i].config(text=option)

    def check_answer(self, index):
        q = self.questions[self.index]

        if q["options"][index] == q["answer"]:
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showerror("Result", "Wrong!")

        self.index += 1
        self.load_question()

    def end_game(self):
        messagebox.showinfo(
            "Game Over",
            f"{self.player_name}, your score: {self.score}/{len(self.questions)}"
        )
        self.root.quit()




if __name__ == "__main__":
    root = tk.Tk()
    StartScreen(root)
    root.mainloop()