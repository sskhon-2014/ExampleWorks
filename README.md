# ExampleWorks
Here is an example of some of my work. Please take some time to look around!

# CosineSimilarityAlgorithm.ipynb
This is a cosine similarity algorithm I designed. It uses gensim's word2vec model trained on text8, 10^9 bytes of the English Wikipedia. Through repetition and the use of thresholds, this algorithm can effectively calculate the percent similarity between documents. The only downside of this algorithm is, however, that it does not efficiently compute the percent similarity in large documents. This algorithm was used to convert the local diagnoses in ResultCare's database to the universal standard ICD9. This is a novel approach to Natural Language Processing and it essentially implents a highly complex word search. Wheras a normal word search looks at bits of letters present in different documents, this algorithm takes almost any word in the english language and computes the percent similarity between that word and its closest neighbors. After creating such a model, we can enter in any two sentences as arguements and get the percent similarity between them. 

You can see the output of this algorithm below:

<p align="center">
  <img src="screenshot.png" width="350"/>
  </p>
  
# ResultCare's Data Entry Website 
I have also included the html code of the landing page of the data entry platform I designed for ResultCare. You can visit the website at: http://zealous-agnesi-df0732.bitballoon.com 
This websites validation functions submitted data as AJAX requests to google sheets. This website is completely functional so please do not submit any information here. 
