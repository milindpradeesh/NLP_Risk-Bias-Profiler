# Risk Profiling and Behavioral Bias Identifier Streamlit App
This interactive web application is designed to help users identify their risk tolerance and dominant behavioral biases by asking a series of open-ended questions. It leverages Natural Language Processing (NLP) and fuzzy matching techniques to analyze user responses and provide insights into financial decision-making behavior.

## Features:
* Risk Tolerance Profiling: Categorizes responses into one of three risk categories—Conservative, Moderate, or Aggressive—based on user inputs.
* Bias Identification: Detects common biases, such as Loss Aversion, Overconfidence, and Affinity Bias, that influence investment behavior.
* NLP Analysis: Uses the spaCy NLP model to analyze semantic similarity and classify responses accurately.
* Fuzzy Matching: Implements fuzzywuzzy for spelling correction, ensuring that minor spelling errors do not affect the results.

## How It Works:
* User Interaction: The app presents a series of 8 open-ended questions related to investment behavior and decision-making.
* Text Analysis: Each response is processed using:
* Spelling Correction: The fuzzywuzzy library corrects potential spelling mistakes.
* Semantic Matching: spaCy computes semantic similarity to match responses with pre-defined keywords for risk categories and biases.
* Scoring: The app maintains scores for each risk category and behavioral bias based on user responses.
* Results: Once all questions are answered, the app displays the user's overall risk profile (Conservative, Moderate, or Aggressive) and their dominant behavioral bias.

## Libraries Used:
* streamlit: For building the interactive web application.
* spaCy: For natural language processing and semantic analysis.
* fuzzywuzzy: For correcting spelling mistakes and ensuring accurate keyword matching.
* re: For regular expressions used in vocabulary extraction.

## Ideal Users:
* Investors seeking to better understand their financial behavior and risk preferences.
* Individuals looking for insights into their decision-making biases, such as overconfidence or loss aversion.
  
This tool is an excellent resource for anyone interested in improving their financial decision-making process by uncovering hidden biases and gaining a clearer understanding of their investment strategy.
