
import streamlit as st

# ==================================================
# 1. PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Sumerian Language Quiz",
    page_icon="𒀭",
    layout="centered"
)

# ==================================================
# 2. TRANSLATIONS: ENGLISH / FRENCH
# ==================================================

translations = {
    "English": {
        "title": "𒀭 Sumerian Language Quiz",
        "subtitle": "Test your knowledge of the Sumerian language and cuneiform!",
        "description": """
### Welcome to the Sumerian Quiz!

Test your knowledge of:

- **Sumerian vocabulary and meanings**
- **Cuneiform sign recognition**
- **Sumerian writing and numbers**
- **Grammar and linguistic concepts**

There are **30 questions**. Each correct answer earns one point.
""",
        "language": "Select Application Language",
        "instructions": "Choose one answer for each question. Good luck!",
        "participant": "Participant Information",
        "name": "Enter participant's name:",
        "level": "Select your Sumerian knowledge level:",
        "levels": ["Beginner", "Intermediate", "Advanced"],
        "questions": "The 30 Questions",
        "choose": "Choose your answer:",
        "confidence": "How confident are you about your Sumerian knowledge?",
        "feedback": "Comments or suggestions about this quiz:",
        "submit": "Submit Quiz",
        "missing_name": "Please enter the participant's name.",
        "missing_answers": "Please answer all 30 questions before submitting.",
        "results": "𒀭 Quiz Results",
        "score": "Final Score",
        "excellent": "Excellent! You have demonstrated excellent knowledge of Sumerian and cuneiform!",
        "very_good": "Very good! You have a good understanding of Sumerian language and writing.",
        "fair": "Fair result. Further study of Sumerian is recommended.",
        "poor": "Keep studying! Your knowledge of Sumerian and cuneiform needs improvement.",
        "review": "Detailed Answer Review",
        "correct": "Correct!",
        "incorrect": "Incorrect",
        "your_answer": "Your answer",
        "correct_answer": "Correct answer",
        "thank_you": "Thank you for participating in the Sumerian Language and Cuneiform Quiz!",
        "feedback_received": "Participant feedback",
        "confidence_result": "Confidence",
        "level_result": "Knowledge level",
        "name_result": "Participant",
        "info": "Select your answers and submit the quiz to discover your score.",
        "creator": "Created by Rami Ibrahim",
        "percentage": "Percentage",
        "footer": "Sumerian Language and Cuneiform Knowledge Assessment"
    },

    "Français": {
        "title": "𒀭 Quiz de langue sumérienne",
        "subtitle": "Testez vos connaissances de la langue sumérienne et de l’écriture cunéiforme !",
        "description": """
### Bienvenue dans le quiz sur la langue sumérienne !

Évaluez vos connaissances dans les domaines suivants :

- **Vocabulaire sumérien et signification des mots**
- **Reconnaissance des signes cunéiformes**
- **Écriture et numération sumériennes**
- **Grammaire et notions linguistiques**

Le quiz comprend **30 questions**. Chaque bonne réponse rapporte un point.
""",
        "language": "Choisir la langue de l’application",
        "instructions": "Choisissez une réponse pour chaque question. Bonne chance !",
        "participant": "Informations sur le participant",
        "name": "Saisissez le nom du participant :",
        "level": "Sélectionnez votre niveau de connaissance du sumérien :",
        "levels": ["Débutant", "Intermédiaire", "Avancé"],
        "questions": "Les 30 questions",
        "choose": "Choisissez votre réponse :",
        "confidence": "Quel est votre degré de confiance dans vos connaissances du sumérien ?",
        "feedback": "Commentaires ou suggestions concernant ce quiz :",
        "submit": "Soumettre le quiz",
        "missing_name": "Veuillez saisir le nom du participant.",
        "missing_answers": "Veuillez répondre aux 30 questions avant de soumettre le quiz.",
        "results": "𒀭 Résultats du quiz",
        "score": "Score final",
        "excellent": "Excellent ! Vous avez démontré une très bonne maîtrise de la langue sumérienne et de l’écriture cunéiforme !",
        "very_good": "Très bien ! Vous avez une bonne connaissance de la langue et de l’écriture sumériennes.",
        "fair": "Résultat satisfaisant. Nous vous recommandons d’approfondir votre étude du sumérien.",
        "poor": "Continuez vos études ! Vos connaissances du sumérien et de l’écriture cunéiforme méritent d’être approfondies.",
        "review": "Correction détaillée des réponses",
        "correct": "Bonne réponse !",
        "incorrect": "Réponse incorrecte",
        "your_answer": "Votre réponse",
        "correct_answer": "Bonne réponse",
        "thank_you": "Merci d’avoir participé au quiz sur la langue sumérienne et l’écriture cunéiforme !",
        "feedback_received": "Commentaires du participant",
        "confidence_result": "Degré de confiance",
        "level_result": "Niveau de connaissance",
        "name_result": "Participant",
        "info": "Sélectionnez vos réponses et soumettez le quiz pour découvrir votre résultat.",
        "creator": "Créé par Rami Ibrahim",
        "percentage": "Pourcentage",
        "footer": "Évaluation des connaissances de la langue sumérienne et de l’écriture cunéiforme"
    }
}

# ==================================================
# 3. SIDEBAR AND LANGUAGE SELECTOR
# ==================================================

st.sidebar.title("🌐 Language / Langue")

language = st.sidebar.radio(
    "Select language / Choisissez la langue",
    ["English", "Français"],
    index=0
)

t = translations[language]

st.sidebar.markdown("---")
st.sidebar.info(t["info"])
st.sidebar.markdown("---")
st.sidebar.markdown(f"**{t['creator']}**")

# ==================================================
# 4. QUESTION BANK - 30 QUESTIONS
# ==================================================
#
# Each question contains:
# English question
# French question
# English options
# French options
# Correct answer index
# English explanation
# French explanation
#
# ==================================================

questions = [

    # QUESTION 1
    (
        "1. What does the Sumerian word 'dingir' mean?",
        "1. Que signifie le mot sumérien « DINGIR » ?",
        ["King", "God / deity", "Water", "House"],
        ["Roi", "Dieu / divinité", "Eau", "Maison"],
        1,
        "DINGIR means god or deity. Its cuneiform sign is 𒀭.",
        "DINGIR signifie dieu ou divinité. Son signe cunéiforme est 𒀭."
    ),

    # QUESTION 2
    (
        "2. Which cuneiform sign represents AN?",
        "2. Quel signe cunéiforme représente AN ?",
        ["𒂍", "𒀭", "𒆠", "𒈗"],
        ["𒂍", "𒀭", "𒆠", "𒈗"],
        1,
        "𒀭 is the sign AN, associated with heaven and the sky.",
        "𒀭 est le signe AN, associé au ciel."
    ),

    # QUESTION 3
    (
        "3. What does the Sumerian word 'é' mean?",
        "3. Que signifie le mot sumérien « É » ?",
        ["Water", "House / temple", "Sun", "Man"],
        ["Eau", "Maison / temple", "Soleil", "Homme"],
        1,
        "É means house or temple. Its cuneiform sign is 𒂍.",
        "É signifie maison ou temple. Son signe cunéiforme est 𒂍."
    ),

    # QUESTION 4
    (
        "4. Which sign represents LUGAL (king)?",
        "4. Quel signe représente LUGAL (roi) ?",
        ["𒈗", "𒀭", "𒊩", "𒌓"],
        ["𒈗", "𒀭", "𒊩", "𒌓"],
        0,
        "𒈗 is LUGAL, meaning king.",
        "𒈗 est le signe LUGAL, qui signifie roi."
    ),

    # QUESTION 5
    (
        "5. What does the Sumerian word 'ki' mean?",
        "5. Que signifie le mot sumérien « KI » ?",
        ["Earth / place", "Fire", "King", "Moon"],
        ["Terre / lieu", "Feu", "Roi", "Lune"],
        0,
        "KI means earth, ground or place. Its sign is 𒆠.",
        "KI signifie terre, sol ou lieu. Son signe est 𒆠."
    ),

    # QUESTION 6
    (
        "6. Which sign represents UD (sun / day)?",
        "6. Quel signe représente UD (soleil / jour) ?",
        ["𒌓", "𒂍", "𒀭", "𒈗"],
        ["𒌓", "𒂍", "𒀭", "𒈗"],
        0,
        "𒌓 is UD, associated with the sun and day.",
        "𒌓 est le signe UD, associé au soleil et au jour."
    ),

    # QUESTION 7
    (
        "7. What does LUGAL mean?",
        "7. Que signifie LUGAL ?",
        ["Priest", "King", "Farmer", "Scribe"],
        ["Prêtre", "Roi", "Agriculteur", "Scribe"],
        1,
        "LUGAL means king and is written 𒈗.",
        "LUGAL signifie roi et s’écrit 𒈗."
    ),

    # QUESTION 8
    (
        "8. Which sign represents A (water)?",
        "8. Quel signe représente A (eau) ?",
        ["𒀀", "𒂍", "𒆠", "𒌓"],
        ["𒀀", "𒂍", "𒆠", "𒌓"],
        0,
        "𒀀 is the sign A, meaning water.",
        "𒀀 est le signe A, qui signifie eau."
    ),

    # QUESTION 9
    (
        "9. What does AMA mean?",
        "9. Que signifie AMA ?",
        ["Father", "Mother", "Son", "Daughter"],
        ["Père", "Mère", "Fils", "Fille"],
        1,
        "AMA means mother in Sumerian.",
        "AMA signifie mère en sumérien."
    ),

    # QUESTION 10
    (
        "10. Which sign represents DUMU (child / son)?",
        "10. Quel signe représente DUMU (enfant / fils) ?",
        ["𒌉", "𒀭", "𒈗", "𒊩"],
        ["𒌉", "𒀭", "𒈗", "𒊩"],
        0,
        "𒌉 is DUMU, meaning child or son.",
        "𒌉 est le signe DUMU, qui signifie enfant ou fils."
    ),

    # QUESTION 11
    (
        "11. Which Sumerian word means woman?",
        "11. Quel mot sumérien signifie femme ?",
        ["LU₂", "NIN", "MUNUS", "DUMU"],
        ["LU₂", "NIN", "MUNUS", "DUMU"],
        2,
        "MUNUS means woman or female. Its sign is 𒊩.",
        "MUNUS signifie femme ou féminin. Son signe est 𒊩."
    ),

    # QUESTION 12
    (
        "12. Which cuneiform sign represents MUNUS?",
        "12. Quel signe cunéiforme représente MUNUS ?",
        ["𒊩", "𒀭", "𒂍", "𒌓"],
        ["𒊩", "𒀭", "𒂍", "𒌓"],
        0,
        "𒊩 is the sign MUNUS, meaning woman or female.",
        "𒊩 est le signe MUNUS, qui signifie femme ou féminin."
    ),

    # QUESTION 13
    (
        "13. What is the Unicode name of 𒐕?",
        "13. Quel est le nom Unicode du signe 𒐕 ?",
        ["One GESH2", "Five ASH", "One GESHU", "Two GESH2"],
        ["One GESH2", "Five ASH", "One GESHU", "Two GESH2"],
        0,
        "𒐕 is CUNEIFORM NUMERIC SIGN ONE GESH2 (U+12415).",
        "𒐕 porte le nom Unicode CUNEIFORM NUMERIC SIGN ONE GESH2 (U+12415)."
    ),

    # QUESTION 14
    (
        "14. What are the sign values in 𒀭𒈗?",
        "14. Quelles sont les valeurs des signes dans 𒀭𒈗 ?",
        ["AN and LUGAL", "E2 and KI", "A and UD", "DUMU and MUNUS"],
        ["AN et LUGAL", "E2 et KI", "A et UD", "DUMU et MUNUS"],
        0,
        "The two signs have the values AN and LUGAL respectively.",
        "Les deux signes ont respectivement les valeurs AN et LUGAL."
    ),

    # QUESTION 15
    (
        "15. Which writing system was used to record Sumerian?",
        "15. Quel système d’écriture était utilisé pour transcrire le sumérien ?",
        ["Phoenician alphabet", "Greek alphabet", "Cuneiform", "Latin alphabet"],
        ["Alphabet phénicien", "Alphabet grec", "Écriture cunéiforme", "Alphabet latin"],
        2,
        "Sumerian was recorded using cuneiform in ancient Mesopotamia.",
        "Le sumérien était transcrit au moyen de l’écriture cunéiforme dans l’ancienne Mésopotamie."
    ),

    # QUESTION 16
    (
        "16. What is one common meaning of KUR?",
        "16. Quel est l’un des sens courants de KUR ?",
        ["Mountain / land", "Water", "Mother", "Temple"],
        ["Montagne / pays", "Eau", "Mère", "Temple"],
        0,
        "KUR can mean mountain or land, depending on context.",
        "KUR peut signifier montagne ou pays, selon le contexte."
    ),

    # QUESTION 17
    (
        "17. Which cuneiform sign represents KUR?",
        "17. Quel signe cunéiforme représente KUR ?",
        ["𒆳", "𒅗", "𒈬", "𒃲"],
        ["𒆳", "𒅗", "𒈬", "𒃲"],
        0,
        "𒆳 is the cuneiform sign KUR.",
        "𒆳 est le signe cunéiforme KUR."
    ),

    # QUESTION 18
    (
        "18. What does GIS mean in Sumerian?",
        "18. Que signifie GIS en sumérien ?",
        ["Tree / wood", "Water", "King", "Woman"],
        ["Arbre / bois", "Eau", "Roi", "Femme"],
        0,
        "GIS is associated with tree and wood.",
        "GIS est associé à l’arbre et au bois."
    ),

    # QUESTION 19
    (
        "19. Which sign represents GIS?",
        "19. Quel signe représente GIS ?",
        ["𒄑", "𒀀", "𒌓", "𒂍"],
        ["𒄑", "𒀀", "𒌓", "𒂍"],
        0,
        "𒄑 is the cuneiform sign GIS.",
        "𒄑 est le signe cunéiforme GIS."
    ),

    # QUESTION 20
    (
        "20. What does KA mean in Sumerian?",
        "20. Que signifie KA en sumérien ?",
        ["Mouth", "House", "Earth", "Sun"],
        ["Bouche", "Maison", "Terre", "Soleil"],
        0,
        "KA means mouth in Sumerian.",
        "KA signifie bouche en sumérien."
    ),

    # QUESTION 21
    (
        "21. Which sign represents KA?",
        "21. Quel signe représente KA ?",
        ["𒅗", "𒆠", "𒀭", "𒈗"],
        ["𒅗", "𒆠", "𒀭", "𒈗"],
        0,
        "𒅗 is the cuneiform sign KA.",
        "𒅗 est le signe cunéiforme KA."
    ),

    # QUESTION 22
    (
        "22. What is one common meaning of MU?",
        "22. Quel est l’un des sens courants de MU ?",
        ["Name", "Mountain", "Woman", "Temple"],
        ["Nom", "Montagne", "Femme", "Temple"],
        0,
        "MU can mean name; it also has other readings and meanings.",
        "MU peut signifier nom ; ce signe possède également d’autres lectures et significations."
    ),

    # QUESTION 23
    (
        "23. Which cuneiform sign represents MU?",
        "23. Quel signe cunéiforme représente MU ?",
        ["𒈬", "𒃲", "𒆳", "𒊩"],
        ["𒈬", "𒃲", "𒆳", "𒊩"],
        0,
        "𒈬 is the cuneiform sign MU.",
        "𒈬 est le signe cunéiforme MU."
    ),

    # QUESTION 24
    (
        "24. What does GAL mean in Sumerian?",
        "24. Que signifie GAL en sumérien ?",
        ["Great / big", "Small", "Water", "Child"],
        ["Grand / important", "Petit", "Eau", "Enfant"],
        0,
        "GAL means great or big.",
        "GAL signifie grand ou important."
    ),

    # QUESTION 25
    (
        "25. Which cuneiform sign represents GAL?",
        "25. Quel signe cunéiforme représente GAL ?",
        ["𒃲", "𒀀", "𒂍", "𒌉"],
        ["𒃲", "𒀀", "𒂍", "𒌉"],
        0,
        "𒃲 is the cuneiform sign GAL.",
        "𒃲 est le signe cunéiforme GAL."
    ),

    # QUESTION 26
    (
        "26. Which sign represents the Sumerian word MUNUS?",
        "26. Quel signe représente le mot sumérien MUNUS ?",
        ["𒊩", "𒈗", "𒌓", "𒆳"],
        ["𒊩", "𒈗", "𒌓", "𒆳"],
        0,
        "𒊩 is the sign MUNUS, associated with woman or female.",
        "𒊩 est le signe MUNUS, associé à la femme ou au féminin."
    ),

    # QUESTION 27
    (
        "27. What is the usual basic word order in a Sumerian clause?",
        "27. Quel est l’ordre habituel des mots dans une proposition sumérienne ?",
        [
            "Subject – Object – Verb",
            "Subject – Verb – Object",
            "Verb – Subject – Object",
            "Object – Verb – Subject"
        ],
        [
            "Sujet – Objet – Verbe",
            "Sujet – Verbe – Objet",
            "Verbe – Sujet – Objet",
            "Objet – Verbe – Sujet"
        ],
        0,
        "Sumerian clauses typically use Subject–Object–Verb order.",
        "Les propositions sumériennes suivent généralement l’ordre Sujet–Objet–Verbe (SOV)."
    ),

    # QUESTION 28
    (
        "28. How is Sumerian generally classified morphologically?",
        "28. Comment le sumérien est-il généralement classé sur le plan morphologique ?",
        [
            "Agglutinative",
            "Isolating",
            "Fusional",
            "Polysynthetic"
        ],
        [
            "Agglutinant",
            "Isolant",
            "Flexionnel",
            "Polysynthétique"
        ],
        0,
        "Sumerian is generally described as an agglutinative language.",
        "Le sumérien est généralement décrit comme une langue agglutinante."
    ),

    # QUESTION 29
    (
        "29. How is Sumerian classified in terms of its demonstrated genetic relationships?",
        "29. Comment le sumérien est-il classé du point de vue de ses liens génétiques démontrés avec d’autres langues ?",
        [
            "Language isolate",
            "Semitic language",
            "Indo-European language",
            "Turkic language"
        ],
        [
            "Langue isolée",
            "Langue sémitique",
            "Langue indo-européenne",
            "Langue turcique"
        ],
        0,
        "Sumerian is generally treated as a language isolate because no genetic relationship with another language family has been demonstrated.",
        "Le sumérien est généralement considéré comme une langue isolée, car aucune parenté génétique avec une autre famille linguistique n’a été démontrée."
    ),

    # QUESTION 30
    (
        "30. What does the term 'cuneiform' refer to?",
        "30. À quoi le terme « cunéiforme » fait-il référence ?",
        [
            "Wedge-shaped writing",
            "Circular alphabetic writing",
            "Hieroglyphic painting",
            "Knotted writing"
        ],
        [
            "Une écriture en forme de coins",
            "Une écriture alphabétique circulaire",
            "Une écriture hiéroglyphique",
            "Une écriture utilisant des nœuds"
        ],
        0,
        "Cuneiform refers to the wedge-shaped impressions used in this writing system.",
        "Le terme cunéiforme fait référence aux empreintes en forme de coin utilisées dans ce système d’écriture."
    )
]

# ==================================================
# 5. VALIDATE QUESTION BANK
# ==================================================

assert len(questions) == 30, (
    f"Expected 30 questions, but found {len(questions)}."
)

for i, q in enumerate(questions, start=1):
    assert len(q) == 7, f"Question {i} must contain 7 elements."
    assert len(q[2]) == 4, f"Question {i} must have 4 English options."
    assert len(q[3]) == 4, f"Question {i} must have 4 French options."
    assert 0 <= q[4] < 4, f"Question {i} has an invalid answer index."

# ==================================================
# 6. APPLICATION HEADER
# ==================================================

st.title(t["title"])
st.subheader(t["subtitle"])

st.markdown(t["description"])
st.info(t["instructions"])
st.markdown("---")

# ==================================================
# 7. PARTICIPANT INFORMATION
# ==================================================

st.markdown(f"### {t['participant']}")

name = st.text_input(t["name"])

level_index = st.selectbox(
    t["level"],
    range(3),
    format_func=lambda x: t["levels"][x]
)

st.markdown("---")

# ==================================================
# 8. DISPLAY ALL 30 QUESTIONS
# ==================================================

st.markdown(f"### {t['questions']}")

user_answers = []

for i, q in enumerate(questions):

    question_text = q[0] if language == "English" else q[1]
    options = q[2] if language == "English" else q[3]

    st.write(f"**{question_text}**")

    answer = st.radio(
        t["choose"],
        options,
        index=None,
        key=f"question_{i}"
    )

    user_answers.append(answer)

    st.markdown("---")

# ==================================================
# 9. ADDITIONAL WIDGETS
# ==================================================

confidence = st.slider(
    t["confidence"],
    min_value=0,
    max_value=100,
    value=50,
    format="%d%%"
)

feedback = st.text_area(t["feedback"])

# ==================================================
# 10. SUBMIT BUTTON AND SCORE CALCULATION
# ==================================================

if st.button(t["submit"], type="primary"):

    if not name.strip():

        st.error(t["missing_name"])

    elif None in user_answers:

        st.warning(t["missing_answers"])

    else:

        score = 0
        total_questions = len(questions)

        # Calculate score
        for i, q in enumerate(questions):

            options = q[2] if language == "English" else q[3]
            correct_index = q[4]
            correct_answer = options[correct_index]

            if user_answers[i] == correct_answer:
                score += 1

        percentage = (score / total_questions) * 100

        # ------------------------------------------
        # DISPLAY RESULTS
        # ------------------------------------------

        st.markdown("---")
        st.header(t["results"])

        st.write(f"**{t['name_result']}:** {name}")

        st.write(
            f"**{t['level_result']}:** "
            f"{t['levels'][level_index]}"
        )

        st.write(
            f"**{t['confidence_result']}:** {confidence}%"
        )

        st.metric(
            label=t["score"],
            value=f"{score}/{total_questions}",
            delta=f"{percentage:.1f}%"
        )

        # ------------------------------------------
        # RESULT MESSAGE
        # ------------------------------------------

        if score >= 26:
            st.success(t["excellent"])

        elif score >= 18:
            st.success(t["very_good"])

        elif score >= 12:
            st.warning(t["fair"])

        else:
            st.error(t["poor"])

        # ------------------------------------------
        # DETAILED ANSWER REVIEW
        # ------------------------------------------

        st.markdown("---")
        st.subheader(t["review"])

        for i, q in enumerate(questions):

            options = q[2] if language == "English" else q[3]

            correct_index = q[4]
            correct_answer = options[correct_index]

            explanation = q[5] if language == "English" else q[6]

            question_text = q[0] if language == "English" else q[1]

            st.write(f"**{question_text}**")

            if user_answers[i] == correct_answer:

                st.success(
                    f"{t['correct']} {user_answers[i]}"
                )

            else:

                st.error(
                    f"{t['incorrect']} | "
                    f"{t['your_answer']}: {user_answers[i]} | "
                    f"{t['correct_answer']}: {correct_answer}"
                )

            st.caption(explanation)

        # ------------------------------------------
        # PARTICIPANT FEEDBACK
        # ------------------------------------------

        if feedback.strip():

            st.info(
                f"{t['feedback_received']}: {feedback}"
            )

        st.markdown("---")
        st.success(t["thank_you"])

# ==================================================
# 11. FOOTER / AUTHORSHIP
# ==================================================

st.markdown("---")

st.markdown(
    f"<div style='text-align:center; color:gray;'>"
    f"<strong>{t['creator']}</strong><br>"
    f"{t['footer']}"
    f"</div>",
    unsafe_allow_html=True
)
