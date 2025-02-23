# ADS509-Text-mining-Final-Project

## Exploring DeepSeek’s Media Narrative: A Text Mining Analysis of News Coverage Trends and Progression
### Overview
This project applies text mining techniques to analyze media coverage of DeepSeek by examining news articles collected through NewsAPI. The goal is to understand how DeepSeek is portrayed across various media outlets and track how its narrative evolves over time.

By leveraging natural language processing (NLP), classification models, and topic modeling methods, we aim to:

* Identify key themes and trends in media coverage related to DeepSeek.
* Track the evolution of AI-related discussions in the media.
* Gain insights into public sentiment and DeepSeek’s position in the AI space.

### Dataset
Data Source: NewsAPI
Number of Variables: 7
* source (includes id and name)
* author
* title
* description
* url
* urlToImage
* publishedAt
#### Size of Dataset:
The dataset is continuously expanding as new articles are collected.
### Preprocessing
* Collected and cleaned text data from multiple news sources.
* Removed stopwords, punctuation, and special characters.
* Applied tokenization and lemmatization for better text representation.
* Transformed text data using TF-IDF vectorization.
### Models Used
We applied four classification models to categorize news articles and analyze coverage trends:
* Naive Bayes – A probabilistic model for text classification.
* Logistic Regression – A linear model for binary and multi-class classification.
* Support Vector Machine (SVM) – A model that finds optimal decision boundaries.
* XGBoost – A gradient-boosting algorithm known for high performance in text classification.

Additionally, we used topic modeling techniques such as:
* Latent Dirichlet Allocation (LDA)
* Non-Negative Matrix Factorization (NMF)
* Latent Semantic Analysis (LSA)

### Training & Evaluation
* Data Split: Training and test datasets were created to evaluate model performance.
* Feature Extraction: TF-IDF was used to transform text data into numerical features.
* Performance Metrics: Accuracy, Precision, Recall, and F1-score were used to assess classification models.
### Results & Comparison
* A detailed classification report and confusion matrix were generated for each model.
* A visualization comparing model performance is provided to highlight accuracy and effectiveness.
### Conclusion & Recommendations
* The best-performing classification model was XGBoost, achieving the highest accuracy and balanced performance across categories.
* Naive Bayes had lower precision but worked well for some categories with high recall.
* SVM and Logistic Regression showed competitive results but struggled with certain class imbalances.
* Future work includes incorporating sentiment analysis and expanding the dataset for more robust insights.
