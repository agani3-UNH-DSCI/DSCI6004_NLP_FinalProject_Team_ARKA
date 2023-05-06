# DSCI6004 TEAM ARKA


Jupyter Notebook Link: https://colab.research.google.com/drive/1PSaV-AOXgBSSWr04eT9rrYEXYm1uAH_8?usp=sharing

## Cyberbullying Detection

## Abstract: 

Natural language processing (NLP) can be used to help detect and prevent cyberbullying, which is an issue that is becoming more and more prevalent in today's digital environment. The goal of this project is to apply NLP methods to create a model that can precisely identify instances of cyberbullying by using BLSTM architecture and Glove. 

## Cyberbullying:
Cyberbullying is a prevalent problem on social media that can quite upsetting and troubling. It can take on many different forms, but most social networks tend to see it as text.
Automated detection of these situations requires the use of sophisticated and intelligent technologies. Existing tools for detecting cyberbullying have a lot of constraints. They only touch on one subject, which is cyberbullying. Additionally, they rely on profanity. We demonstrate how deep learning-based models can get beyond these roadblocks.

To effectively train our models, we want to employ publicly accessible datasets, each of which covers a different aspect of cyberbullying. Examples of racism can be seen, for instance, in the Twitter dataset. Additionally, there exist statistics that include instances of sexism. We train our model utilizing Deep Neural Network (DNN) based models like BLSTM. Word embedding is used to model words in order to capture the semantics and similarities between words. Global Vector (GloVe) was selected for word embedding because it has outperformed other models in named entity recognition and word similarity.
Users who publish content that promotes cyberbullying will be reported to the helpline through mail. The algorithm also examines posts about cyberbullying that are viewable by the user.

## LSTM's

Recurrent neural networks (RNNs) of the type of Long Short-Term Memory (LSTM) are created to address the vanishing gradient problem, which is a prevalent problem in conventional RNNs. The gradient signal shrinks steadily as it backpropagates through time, which is known as the "vanishing gradient problem," making it challenging for models to learn long-term relationships. 

To selectively forget or remember data from earlier time steps, LSTM employs a set of gates. The gates are made up of a sigmoid function that outputs a value between 0 and 1, indicating how much information should be remembered or forgotten. The input gate, forget gate, and output gate are some of the gates. 

The input gate regulates how much fresh input should be permitted into the network's memory, or cell state. Which data from the previous cell state should be forgotten is decided by the forget gate. Finally, the output gate chooses what data from the cell state should be output as the prediction. 


![lstm](https://user-images.githubusercontent.com/115109673/236608255-3ebfce7b-0128-49a1-8ea6-ab0df03f8774.jpg)

<img width="689" alt="Bilstm" src="https://user-images.githubusercontent.com/115109673/236608165-89267f52-a405-40bb-9695-3fab67a064e5.png">

## GloVe for Vectorization:
A pre-trained word embedding method that captures the semantic and syntactic meaning of words was also included in our analysis. GloVe has demonstrated to be very successful in NLP tasks and learns word embeddings using a co-occurrence matrix. In our model, we made use of the 100-dimensional GloVe vectors that were trained on 6 billion words. 

In natural language processing (NLP), a word embedding paradigm known as GloVe embeddings, or Global Vectors for Word Representation, is frequently employed. Since each word is represented by a vector of 100 real-valued values, the "100d" in "100d GloVe embeddings" refers to the dimensionality of the embeddings. These embeddings, which capture the semantic and syntactic links between words, are created through training on huge corpora of text data. The 100d GloVe embeddings strike a balance between computing effectiveness and the ability to capture fine-grained semantic nuances. They have been widely used in many NLP tasks, including sentiment analysis, named entity recognition, and text categorization, and they provide important contextual information for better language understanding and downstream tasks. 

![glove](https://user-images.githubusercontent.com/115109673/236608338-772521c1-7c00-4a19-913f-d551cd4015c3.jpg)

## References:
"GloVe: Global Vectors for Word Representation" Authors: Jeffrey Pennington, Richard Socher, Christopher D. Manning Published: 2014: https://nlp.stanford.edu/pubs/glove.pdf 
"NLP and Machine Learning Techniques for Detecting Insulting Comments on Social Networking Platforms" https://ieeexplore-ieee-org.unh-proxy01.newhaven.edu/document/8441728
"LSTM with working memory" https://ieeexplore.ieee.org/document/7965940 


