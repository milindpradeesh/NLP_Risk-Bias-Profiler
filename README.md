# Risk Profiling and Behavioral Bias Identifier 
The Risk Profiling and Behavioral Bias Identifier is a Python-based tool designed to assess an individual's investment risk profile and behavioral biases based on their textual responses. It uses Natural Language Processing (NLP) to match user inputs with predefined categories of risk-taking behavior and psychological biases.

## How It Works
1) The program presents 8 open-ended questions related to investment decision-making.
2) User responses are processed using spaCy for semantic similarity analysis.
3) Fuzzy matching is used to correct minor spelling mistakes and improve classification accuracy.
4) The tool assigns the user a risk profile and identifies their dominant behavioral bias based on their responses.

## Key Features

* ✅ Three Risk Profiles: Conservative, Moderate, Aggressive
* ✅ Five Behavioral Biases: Loss Aversion, Overconfidence, Status Quo Bias, Regret Aversion, Affinity Bias
* ✅ Fuzzy Matching for Typos: Ensures accurate keyword identification
* ✅ Semantic Similarity Matching: Uses spaCy to analyze user responses beyond keyword matching
* ✅ Interactive Questioning: Engages users through an intuitive Q&A format

## Methodology

### Risk Profile Categories
* Conservative: Prefers stability, low-risk investments, and wealth preservation.
* Moderate: Balances risk and return with a diversified approach.
* Aggressive: Seeks high returns through high-risk investments.

### Behavioral Biases
* Loss Aversion: Fear of losing money leads to risk avoidance.
* Overconfidence Bias: Overestimates personal ability to predict the market.
* Status Quo Bias: Prefers familiar investments and resists change.
* Regret Aversion: Hesitates due to fear of making wrong decisions.
* Affinity Bias: Invests based on familiarity or emotional attachment.

## Contributions
Contributions are welcome! If you have improvements or new features to suggest, feel free to create a pull request.
