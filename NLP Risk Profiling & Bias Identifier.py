# Importing required libraries
import streamlit as st
import spacy
from collections import defaultdict
import random
from fuzzywuzzy import process #For handling spelling mistakes
import re 

# Load spaCy model
nlp = spacy.load("en_core_web_md") 

def category_keywords():
    """
    Return refined categories with keywords for better classification, 
    with emphasis on affinity bias markers.
    """
    return {
        "Conservative": [
            "low risk", "safe", "stable", "capital preservation", "predictable returns",
            "guaranteed returns", "minimize losses", "secure investment", "steady growth",
            "fixed income", "bonds", "long-term stability", "principal protection",
            "low volatility", "risk-averse", "safety first", "preserve wealth", "risk minimization",
            "preservation of capital", "income stability", "low-risk assets", 
            "familiar investments", "local investments", "community bank", 
            "tried and true", "what I know", "avoiding the unknown", "invest in what I know",
            "avoid new things", "stick to what works", "careful growth", "protect my savings",
            "slow and steady wins", "predictable income"
        ],
        "Moderate": [
            "balanced risk", "diversified", "moderate growth", "acceptable risk",
            "growth with stability", "medium volatility", 
            "not too risky, not too safe", "risk-balanced portfolio",
            "moderate volatility", "equity and fixed income mix", "steady growth potential",
            "long-term growth with some risk", "diversified investments", "sustainable returns",
            "moderate capital appreciation", "some risk", "mix of investments",
            "reasonable returns", "managed risk", "strategic investing"
        ],
        "Aggressive": [
            "high risk", "high return potential", "market speculation", "capital appreciation",
            "bold investments", "growth at all costs", "short-term gains", "risk-taker",
            "highly volatile", "speculative", "big bets", "fast-growing sectors",
            "leveraged investing", "chasing high returns", "exponential growth",
            "maximize profit", "venture investments", "high-growth potential",
            "venture capital opportunities", "innovative investments", "dynamic growth"
        ],
     
    }


def bias_keywords():
    """
    Return refined biases with keywords for better classification.
    """
    return {
        "Loss Aversion": [
            "fear of loss", "avoid losses", "hesitate to sell", "hold losing investments",
            "pain of losing money", "underperforming assets", "protecting principal",
            "cutting losses is hard", "minimize downside", "losses hurt more than gains",
            "risk avoidance", "prefer stability", "selling at a loss is difficult"
        ],
        "Overconfidence Bias": [
            "beat the market", "trust my instincts", "rarely wrong", "confident predictions",
            "superior judgment", "my strategy always works", "believe in my expertise",
            "highly skilled investor", "better than average", "rarely consult others",
            "strong market knowledge", "trust my analysis", "not worried about risk",
            "self-assured decisions", "high conviction trades"
        ],
        "Status Quo Bias": [
            "stick to familiar", "avoid change", "same asset classes", "resist adjustments",
            "prefer past strategies", "safe over change", "loyal to my portfolio",
            "fear of switching", "no need to adjust", "prefer familiarity", 
            "unchanged strategy", "comfortable with routine", "don’t fix what isn’t broken"
        ],
        "Regret Aversion": [
            "fear of regret", "hesitate on opportunities", "avoid bold decisions",
            "worry about mistakes", "play it safe", "miss out due to fear",
            "second-guessing", "safer options", "scared to take a chance",
            "afraid of making the wrong choice", "prefer low risk", 
            "what if I’m wrong?", "overthink investment choices"
        ],
        "Affinity Bias": [
            "invest in familiar brands", "trust industries I know", "invest in products I use",
            "align with values", "emotional connection", "personal loyalty",
            "ignore red flags", "feel good about investment", "trust based on recognition",
            "support companies I like", "buy stocks from favorite brands",
            "invest in what I love", "brand loyalty", "comfort in familiarity",
            "familarity","people I know","local ties","companies I understand",
            "investments that reflect my values","local","support local business",
            "investment in my neighbourhood"
        ]
    }

def get_questions():
    """Returns 8 open-ended questions, each addressing one category."""
    return [
      "How do you typically react to market volatility, and what actions do you take?",
      "Describe your ideal balance between potential gains and potential losses in your investments.",
      "Have you ever stuck with a familiar investment even if it wasn't performing well? Why?",
      "What influences your confidence in your investment choices, and how often do you re-evaluate them?",
      "Share a time you avoided an investment due to fear. What did you learn?",
      "How do you approach diversification in your investment portfolio?",
      "What would make you change your investment strategy, and how quickly do you adapt to new market conditions?",
      "How do you feel when your investments don't meet your expectations, and what do you do about it?"
    ]



#Define vocabulary from categories and biases for fuzzy matching
def get_vocabulary():
    """Extracts all possible words from categories and biases to use in fuzzy matching."""
    categories = category_keywords()
    biases =bias_keywords()
    vocabulary = set()

    for words_list in list (categories.values()) + list(biases.values()):
        for phrase in words_list:
            vocabulary.update(re.findall(r'\b\w+\b',phrase.lower())) #Extract words

    return list(vocabulary)

VOCABULARY = get_vocabulary() #Precompute vocabulary

# -- Helper Functions ---
def correct_spelling(input_text):
    """Corrects misspelled words using fuzzy matching with predefined vocabulary."""
    words = input_text.split()
    corrected_words = []

    for word in words:
        best_match, score = process.extractOne(word,VOCABULARY) #Find closest word
        corrected_words.append(best_match if score > 80 else word) #Correct if high similarity

    return ' '.join(corrected_words)

def match_category_with_similarity(input_text, category_sentences, threshold=0.7):
    """
    Matches input text to a category based on semantic similarity.
    """
    if not input_text.strip():
        return None  # Return None if the input is empty

    corrected_text = correct_spelling(input_text) #Apply fuzzy correction
    input_doc = nlp(input_text)
    best_match = None
    best_score = threshold

    for category, sentences in category_sentences.items():
        for sentence in sentences:
            similarity = input_doc.similarity(nlp(sentence))
            if similarity > best_score:
                best_score = similarity
                best_match = category

    return best_match

# -- Streamlit App --
def main():
    """Main function for risk profiling and bias identification."""
    st.title("Risk Profiling and Bias Identifier")

    risk_categories = category_keywords()
    biases = bias_keywords()
    questions = get_questions()
    
    risk_scores = defaultdict(int)
    bias_scores = defaultdict(int)

    # Initialize session state for question index and responses if they don't exist
    if 'question_index' not in st.session_state:
        st.session_state.question_index =0
        st.session_state.responses = {} #Store responses

    # Display Question
    if st.session_state.question_index < len(questions):
        question = questions[st.session_state.question_index]
        st.write(f"**Question {st.session_state.question_index + 1}:** {question}")

        user_response = st.text_area("Your response:", key=f"response_{st.session_state.question_index}",height=100)

        if st.button("Submit"):
            if user_response.strip():
                st.session_state.responses[st.session_state.question_index] = user_response
                risk_category = match_category_with_similarity(user_response, risk_categories)
                bias_category = match_category_with_similarity(user_response, biases)

                if risk_category:
                    risk_scores[risk_category] += 1
                if bias_category:
                    bias_scores[bias_category] += 1

                st.session_state.question_index += 1 #Move to next question
                st.rerun() # Refresh to display next question
            else:
                st.warning("Please enter a valid response.")

    else:
        # --- Analysis and Results ---
        highest_risk_category = max(risk_scores, key=risk_scores.get, default="None")
        highest_bias_category = max(bias_scores, key=bias_scores.get, default="None")

        st.header("Test Completed! Here are your results:")
        st.write(f"**Overall Risk Profile:** {highest_risk_category}")
        st.write(f"**Dominant Behavioral Bias:** {highest_bias_category}")

        # --- Display Responses ---
        st.subheader("Your Responses:")
        for i, response in st.session_state.responses.items():
            st.write(f"**Question {i+1}:** {questions[i]}")
            st.write(f"**Your Answer:** {response}")
            st.write("---")

# Run the app
if __name__ == "__main__":
    main()

