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
### Size of Dataset:
The dataset is continuously expanding as new articles are collected.
Preprocessing
* Collected and cleaned text data from multiple news sources.
* Removed stopwords, punctuation, and special characters.
* Applied tokenization and lemmatization for better text representation.
* Transformed text data using TF-IDF vectorization.
