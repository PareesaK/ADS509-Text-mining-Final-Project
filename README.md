# ADS509-Text-mining-Final-Project

## text Mining DeepSeek’s Media Narrative: Trends & Insights

### Overview
This project utilizes text mining techniques to analyze media coverage of DeepSeek, focusing on how it is portrayed across various news outlets and how its narrative has evolved over time. We aim to apply natural language processing (NLP) methods to identify key themes and trends in coverage related to DeepSeek’s development and impact. The analysis will help uncover public news and monitor AI trends, providing insights into DeepSeek's representation in the media.

By leveraging natural language processing (NLP), classification models, and topic modeling methods, we aim to:

* Identify key themes and trends in media coverage related to DeepSeek.
* Track the evolution of AI-related discussions in the media.
*  How different sources are framing the conversation.​
*  Whether the overall narrative is shifting over time.​
  
### Dataset
Data Source: NewsAPI
Number of Variables: 5
* Source
* Date
* Title
* Description
* Text

### Installation
1. Clone repo
2. Edit `api.py` and save your API key
3. Install dependencies
>```
>pip install -r requirements.txt
>```
3. Run python script
> ```
> python fetch_data.py
> ```

#### Additional Setup:

Download required NLTK resources:
>```
>import nltk
>nltk.download('punkt')
>nltk.download('stopwords')
>nltk.download('wordnet')

### Usage
Run the main analysis script:
>```
>python ADS 509 Text Mining Project.ipynb

#### Size of Dataset:
The dataset is continuously expanding as new articles are collected. A total of 856 datapoints were collected. 
### Preprocessing
* Collected and cleaned text data from multiple news sources.
* Removed stopwords,whitespace, punctuation, special characters, and duplicated.
* Applied tokenization and lemmatization for better text representation.
* Transformed text data using TF-IDF vectorization.

### Topic Modeling
* Latent Dirichlet Allocation (LDA), Non-Negative Matrix Factorization (NMF), and Latent Semantic Analysis (LSA) were used.
* TF-IDF and Count Vectorization extracted key features, reducing noise and emphasizing important terms.​
* Feature selection (top 5,000 words) and filtering thresholds focused on relevant terms.​
* Topics were ranked based on significance for thematic analysis.​ 

### Models Used
Five NMF topics grouped into three AI-related categories:​
* AI Companies and Products ​
* AI Technology and Research ​
* Other AI Topics ​
#### We applied four classification models to categorize news articles and analyze coverage trends:
* Random Forest
* Logistic Regression 
* Support Vector Machine (SVM) 
* XGBoost 
* Performance Metrics: Accuracy, Precision, Recall, and F1-score were used to assess classification models.
  
### Results & Comparison
* A detailed classification report and confusion matrix were generated for each model.
* A visualization comparing model performance is provided to highlight accuracy and effectiveness.
  
### Conclusion & Recommendations
* Fine-tune hyperparameters.​
* Justification or optimization of the number of topics​
* Add confidence thresholds for critical classifications.​
* Develop a monitoring system for model drift.​
* Collect more training data for underrepresented categories.​
* Use active learning for difficult cases.​
* Conduct regular data quality assessments.​
* Remove "deepseek" as a topic word​

### Contributors
* Lorena Dorado
* Parisa Kamizi
