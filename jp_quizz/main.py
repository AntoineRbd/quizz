from multiprocessing.connection import answer_challenge
from tkinter.messagebox import QUESTION
from question import Question


question_prompts = [
    "En quelle année a été créé Jurassic Park ?\n(a) 1993\n(b) 1995 \n(c) 1997\n(d) 1999\n\n",
    "Quel est le nom du professeur paléontologue ?\n(a) Yann Malcolm\n(b) Yann Crant\n(c) Alan Grant\n(d) Owen Grady\n\n",
    "Pourquoi John Hammond a-t-il fait appel à Alan, Elie et Yann ?\n(a) Pour leur faire visiter le parc en avant première\n(b) Pour avoir un avis d'expert sur la viabilité du parc\n(c) Pour l'aider à retrouver ses enfants\n(d) Il ne sait plus il a l'alzheimer\n\n",
    "Quel animal le parc donne à manger au T-rex ?\n(a) Une Chêvre\n(b) Un cochon\n(c) Une vache\n(d) Un mouton\n\n",
    "Que dit toujours Mr Hammond ?\n(a) Mon parc est le plus beau\n(b) J'ai dépensé sans compter\n(c) Cette fois-ci on a mis du 12 volts\n\n",
    "Que dit Yann Malcolm quand le T-rex sort le l'enclos ?\n(a) Ho mon dieu\n(b) C'est prévu dans la visite ça ?\n(c) J'en ai marre d'avoir toujours raison\n(d) Il faut aller aider les enfants\n\n",
    "Dans quoi Dennis Nedry met-il les echantillons ADN des dinosaures ?\n(a) Une malette\n(b) Une bombe de mousse à raser\n(c) Une bombe chantilly\n(d) Ses poches\n\n",
    "Quel est le dinosaure préférer d'Alan Grant ?\n(a) Un T-rex\n(b) Un vélociraptor\n(c) Un tricératops\n(d) Un stégosaure\n\n",
    "Que dit Tim quand Alan va le récupérer dans la voiture ?\n(a) J'ai vomis\n(b) J'ai peur\n(c) Je veux pas bouger\n(d) J'ai le vertige\n\n",
    "Comment s'appelle l'île sur laquelle se situe le parc ?\n(a) Isla Sorna\n(b) Isla Nublar\n(c) Isla Matanceros\n(d) Isla Muerta\n\n",
    "Qui est mangé par le Tyrannosaure ?\n(a) Nedry\n(b) Gennaro\n(c) Arnold\n(d) Malcolm\n\n",
    "Quel animal les savants de Jurassic Park ont-ils utilisé pour combler les manques dans la séquence ADN des dinosaures ?\n(a) Un serpent\n(b) Un crocodile\n(c) Un lézard\n(d) Une grenouille\n\n",
    "Comment appelle-t-on un dinosaure aveugle, d'après Tim ?\n(a) Un myoposaure\n(b) Un ophtalmolosaure\n(c) Un témirosaure\n(d) Un biglosaure\n\n",
    "Parmi ces attractions, laquelle n'est pas citée par John Hammond comme ayant fait partie de son cirque de puces ?\n(a) Un carrousel\n(b) Une balançoire\n(c) Un toboggan\n(d) Un tout petit trapèze\n\n",
    "Pour les convaincre de venir, John Hammond propose à Alan et Ellie de prendre en charge le financement de leurs fouilles pour 3 ans?\n(a) Vrai\n(b) Faux\n\n",
    "Les dinosaures qui naissent ne sont que des femelles?\n(a) Vrai\n(b) Faux\n\n",
    "Completez la phrase suivante du Dr Malcolm : La vie trouve toujours...\n(a) ...un passage\n(b) ...sa route\n(c) ...son sentier\n(d) ...son chemin\n\n",
    "Selon le professeur Ian Malcolm, que semble-t-il manquer dans ce parc à dinosaures ?\n(a) De la sécurité\n(b) Des dinosaures\n(c) Des hotels\n(d) Des attractions\n\n",
    "Qui a composé la musique de Jurassic Park ?\n(a) John Hammond\n(b) Hans Zimmer\n(c) John Williams\n(d) John Lennon\n\n",
    "Comment s'appellent les petits enfants de John Hammond ?\n(a) Lise et Tom\n(b) Lex et Tim\n(c) Jules et Jim\n(d) Gert et John junior\n\n",
    "Tous les dinosaures de Jurassic Park sont du Jurassique ?\n(a) Vrai\n(b) Faux\n\n",
    "Quel est le dinosaure sur le logo du film ?\n(a) Un vélociraptor\n(b) Un carnotaure\n(c) Un térizinosaure\n(d) Un Tyranosaurus Rex\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "a"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "c"),
    Question(question_prompts[6], "b"),
    Question(question_prompts[7], "c"),
    Question(question_prompts[8], "a"),
    Question(question_prompts[9], "b"),
    Question(question_prompts[10], "b"),
    Question(question_prompts[11], "d"),
    Question(question_prompts[12], "c"),
    Question(question_prompts[13], "c"),
    Question(question_prompts[14], "a"),
    Question(question_prompts[15], "a"),
    Question(question_prompts[16], "d"),
    Question(question_prompts[17], "b"),
    Question(question_prompts[18], "c"),
    Question(question_prompts[19], "b"),
    Question(question_prompts[20], "b"),
    Question(question_prompts[21], "d"),
]

if __name__ == "__main__":
    print("""
          \n
          ===============================================
          ==== Bienvenue dans le quizz Jurassic Park ====
          ===============================================
          """)
    
    score = 0
    
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        
    print("Votre score est de " + str(score) + " / " + str(len(questions)))