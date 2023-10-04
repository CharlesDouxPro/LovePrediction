import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import tkinter as tk
import pickle
from tkinter import ttk
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score , cross_val_predict
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import tkinter as tk




data = pd.read_csv("aaa.csv", sep = ';')
data.head()

X = data.drop('Divorce', axis= 1)
y = data['Divorce']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2 )


model = RandomForestClassifier()

model.fit(X_train,y_train)


importances = model.feature_importances_

indices = np.argsort(importances)[::-1]


responses = []

valeurs = {
    "never": 0,
    "a little": 1,
    "Sometimes": 2,
    "often": 3,
    "Always": 4
}

resultats = {
    0: "Divorce",
    1: "Pas de divorce"
}

def afficher_questions_importantes(fenetre_parent):
    nouvelle_fenetre_questions = tk.Toplevel()
    nouvelle_fenetre_questions.title("Questions importantes")

    label_questions = tk.Label(nouvelle_fenetre_questions, text="Questions importantes:")
    label_questions.pack()

    for i in range(5):
        if i >= len(important_questions):
            break
        question = important_questions[i]
        label = tk.Label(nouvelle_fenetre_questions, text=f"{i+1}. {question}")
        label.pack()

    bouton_retour = tk.Button(nouvelle_fenetre_questions, text="Retour", command=lambda: retour_fenetre_principale(nouvelle_fenetre_questions, fenetre))
    bouton_retour.pack()

def retour_fenetre_principale(fenetre_courante, fenetre_principale):
    fenetre_courante.destroy()
    fenetre_principale.deiconify()


def afficher_fenetre_questions():
    nouvelle_fenetre_questions = tk.Toplevel()
    nouvelle_fenetre_questions.title("Questions importantes")
    
    label_message = tk.Label(nouvelle_fenetre_questions, text="Voici les questions qui ont eu le plus de poids dans la prédiction. Cela signifie que si la réponse ne vous convient pas, ce sont sur ces sujets qu'il sera interessant de partager vos réponses et d'en discuter.")
    label_message.pack(pady=10)

    bouton_afficher_questions = tk.Button(nouvelle_fenetre_questions, text="Voir les questions", command=lambda: afficher_questions_importantes(nouvelle_fenetre_questions))
    bouton_afficher_questions.pack()


def soumettre():
    global responses
    responses = []
    for i in range(54):
        response = valeurs[questions[i].get()]
        responses.append(response)
    
    responses_matrix = np.array(responses).reshape((1, 54))
    result = model.predict(responses_matrix)
    
    result_qualitatif = [resultats[r] for r in result]
    
    label_resultat.config(text=f"Résultat : {', '.join(result_qualitatif)}")
    fenetre.withdraw()

    nouvelle_fenetre = tk.Toplevel()
    nouvelle_fenetre.title("Chargement")
    nouvelle_fenetre.geometry("400x150")

    progressbar = ttk.Progressbar(nouvelle_fenetre, length=300, mode="determinate")
    progressbar.pack(pady=20)

    message_label = tk.Label(nouvelle_fenetre, font=("Helvetica", 14))
    message_label.pack(pady=10)

    def charger():
        message_label.configure(text="Assis toi...")
        nouvelle_fenetre.update()
        for i in range(25):
            progressbar['value'] = i * 2
            nouvelle_fenetre.update()
            time.sleep(0.2)

        message_label.configure(text="ATTENTIOOOOOONNNN SUSPENSEEE")
        nouvelle_fenetre.update()
        for i in range(26, 51):
            progressbar['value'] = i * 2
            nouvelle_fenetre.update()
            time.sleep(0.2)


        message_label.configure(text=f"Résultat : {', '.join(result_qualitatif)}")
        nouvelle_fenetre.update()
        for i in range(52, 100):
            progressbar['value'] = i * 2
            nouvelle_fenetre.update()
            time.sleep(0.1)
            
        
        nouvelle_fenetre.destroy()
        afficher_fenetre_questions()

 
    nouvelle_fenetre.after(100, charger)


fenetre = tk.Tk()
fenetre.title("QUESTIONAIRE")

largeur = fenetre.winfo_screenwidth() // 2  #AAAAAAAAAAAHHHHHHHHHHHHHHH
hauteur = fenetre.winfo_screenheight() // 2  #TU LIS MON CODE ??????

fenetre.geometry(f"{largeur}x{hauteur}") #Evidement que chatgpt m'a aidé, mais tkinter j'avais appris en républiqque tcheque mouahahahv puis pour le model dataset sur kaggle deja néttoyé
frame_questions = tk.Frame(fenetre)#j'ai utilisé un random classifier avec le parametre scoring "roc_auc" qui m'a permis justement de connaitre les features avec le plus d'importance
frame_questions.pack(fill="both", expand=True)#J'ai juste eu a chargé le model puis crée le software qui est super simple mais c'est la ou chatgpt m'a aidé parce qu'il est bon et rapide la dedans

scrollbar = ttk.Scrollbar(frame_questions)
scrollbar.pack(side="right", fill="y")

canvas = tk.Canvas(frame_questions, yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)

scrollbar.config(command=canvas.yview)

scrollable_frame = tk.Frame(canvas)
scrollable_frame.pack(fill="both", expand=True)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

questions = []
question_texts = [
"If one of us apologizes when our discussion deteriorates, the discussion ends.",
"I know we can overlook our differences, even when things get tough.",
"When needed, we can restart our discussions with my spouse and correct them.",
"When I communicate openly and regularly with my spouse, it pays off.",
"The time I spend with my wife is special.",
"We don't have time at home as partners.",
"We are like two strangers sharing the same environment at home rather than a family.",
"I enjoy our vacations with my wife.",
"I enjoy traveling with my wife.",
"Most of our goals are shared with my spouse.",
"I think one day in the future, when I look back, I will see that my spouse and I have been in harmony...",
"My spouse and I have similar values in terms of personal freedom.",
"My spouse and I have a similar sense of entertainment.",
"Most of our goals for people (children, friends, etc.) are the same.",
"Our dreams with my spouse are similar.",
"We are compatible with my spouse in terms of how love should be.",
"We share the same views on happiness.",
"My spouse and I have similar ideas about how marriage should be.",
"My spouse and I have similar ideas about how roles should be in marriage.",
"My spouse and I have similar values regarding trust.",
"I know exactly what my spouse likes.",
"I know how my spouse wants to be taken care of when they're sick.",
"I know their favorite food.",
"I can tell you what kind of stress my spouse faces in their life.",
"I know my spouse's inner world.",
"I know my spouse's basic anxieties.",
"I know my spouse's current sources of stress.",
"I know my spouse's hopes and wishes.",
"I know my spouse very well.",
"I know my spouse's friends and their social relationships.",
"I feel aggressive when I argue with my spouse.",
"When I discuss with my spouse, I usually use expressions like 'you always' or 'you never'.",
"I can make negative statements about my spouse's personality during our discussions.",
"I can use offensive expressions during our discussions.",
"I can insult my spouse during our discussions.",
"I can be demeaning during our discussions.",
"My discussions with my spouse are not calm.",
"I hate how my spouse approaches a subject.",
"Our discussions often arise suddenly.",
"We simply start a discussion before I know what's going on.",
"When I talk to my spouse about something, my calm suddenly breaks.",
"When I argue with my spouse, I simply leave and don't say a word.",
"I mostly remain silent to calm the atmosphere a bit.",
"Sometimes, I think it's good for me to leave the house for a while.",
"I prefer to remain silent rather than argue with my spouse.",
"Even if I'm right in the discussion, I stay silent to avoid hurting my spouse.",
"When I discuss with my spouse, I remain silent because I'm afraid I won't be able to control my anger...",
"I feel in the right in our discussions.",
"I have nothing to do with what I'm accused of.",
"In reality, it's not me who is guilty of what I'm accused of.",
"I am not the one who is wrong in the issues.",
"I wouldn't hesitate to tell my spouse they are incompetent.",
"When I argue, I remind my spouse of their incompetence.",
"I wouldn't hesitate to tell my spouse they stink."
]

importances = model.feature_importances_
indices = np.argsort(importances)[::-1]

important_questions = [question_texts[idx] for idx in indices]


for i in range(54):
    label = tk.Label(scrollable_frame, text=f"Question {i+1}: {question_texts[i]}")
    label.pack()
    question = tk.StringVar(scrollable_frame)
    question.set(" - ") 
    menu = tk.OptionMenu(scrollable_frame, question, *valeurs.keys())
    menu.pack()
    questions.append(question)

label_resultat = tk.Label(fenetre, text="Résultat : ")
label_resultat.pack()

bouton = tk.Button(fenetre, text="Soumettre", command=soumettre)
bouton.pack()




scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))


canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-1 * (event.delta // 120), "units"))


fenetre.mainloop()
