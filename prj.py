import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

class CricketScorePredictor:
    def __init__(self, master):
        self.master = master
        self.master.title("Cricket Score Predictor")

        self.label = tk.Label(self.master, text="Predict the cricket score:")
        self.label.pack()

        self.predict_button = tk.Button(self.master, text="Predict", command=self.predict_score)
        self.predict_button.pack()

    def predict_score(self):
        try:
            # Fetch live cricket score from Cricbuzz
            url = "https://www.cricbuzz.com"
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")
            score_tag = soup.find("div", {"class": "cb-col cb-col-100 cb-ltst-wgt-hdr"})
            score_info = score_tag.text.strip() if score_tag else "No live match found"
            messagebox.showinfo("Prediction", f"The live score is: {score_info}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    root = tk.Tk()
    app = CricketScorePredictor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
