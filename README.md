# Data_Processor.ipynb
A project for [ResultCare](https://www.resultcare.com/) in which I clean and anaylze a lot of PubMed articles. The input is an HTML file with matched abstracts from a Perl script and output is an excel sheet with the correct categorization of data values.



### Requirements:
* [Python3](https://www.python.org/downloads/)
* [jupyter](http://jupyter.org/install.html)
* [Numpy](https://scipy.org/install.html)


You can run either 'Data_Processor.ipynb' or 'Data_Processor.py' to clean the html file. 

### Instructions for running `Data_Processor.ipynb`
1. Make sure you have the repo cloned and jupyter installed
2. Open your command line program and run the command `jupyter notebook` in the directory
3. Open up the notebook from the Home UI


### Instructions for running `Data_Processor.py`
1. Save  `Data_Processor.py` to your Desktop
2. Navigate to the correct repository using your terminal by typing in "cd ~/Desktop/PubMed_DataExtraction"
3. Run the python script using the python reader by entering "python3 Data_Processor.py"

# Data_Cleaning.ipynb
This script cleans data from an excel sheet that contains data from PubMed. It removes any repeats and incomplete data that was extracted from PubMed with the help of a pearl script. The data is then prepared for multinomial naive bayes classification. 

### Requirements:
* [Python3](https://www.python.org/downloads/)
* [jupyter](http://jupyter.org/install.html)
* [Numpy](https://scipy.org/install.html)
* [sklearn](http://scikit-learn.org/stable/install.html)


### Instructions for running `Data_Cleaning.ipynb`
1. Make sure you have the repo cloned and jupyter installed
2. Open your command line program and run the command `jupyter notebook` in the directory
3. Open up the notebook from the Home UI.

# ExampleWorks
Here is an example of some of my work. Please take some time to look around!

# CosineSimilarityAlgorithm.ipynb
This is a cosine similarity algorithm I designed. It uses gensim's word2vec model trained on text8, 10^9 bytes of the English Wikipedia. Through repetition and the use of thresholds, this algorithm can effectively calculate the percent similarity between documents. The only downside of this algorithm is that it does not efficiently compute the percent similarity in large documents. This algorithm was used to convert the local diagnoses in ResultCare's database to the universal standard ICD9. This is a novel approach to Natural Language Processing and it essentially implents a highly complex word search. Wheras a normal word search looks at bits of letters present in different documents, this algorithm takes almost any word in the english language and computes the percent similarity between that word and its closest neighbors. With this model, we can enter in any two sentences as arguements and get the percent similarity between them. 

You can see the output of this algorithm below:

<p align="center">
  <img src="screenshot.png" width="400"/>
  </p>
  
# ResultCare's Data Entry Website 
I have also included the html code of the landing page of the data entry platform I designed for ResultCare. This was used to manually enter data from PubMed into the ResultCare database. You can visit the website at: http://resultcare.bitballoon.com.
There is also an accompanying javascript file called validation-functions.js. This script submits data from the website as AJAX requests to google sheets. This website is completely functional so please do not submit any information here. 



# Acknowledgments
- Deok Gun Park, conceptvector, Hedonmeter vs Word2vec Cosine Similarity.ipynb (2016), https://github.com/intuinno/conceptvector/blob/master/experiment/Hedonmeter%20vs%20Word2vec%20Cosine%20Similarity.ipynb

- Martin Hawksey (2014), https://mashe.hawksey.info/2014/07/google-sheets-as-a-database-insert-with-apps-script-using-postget-methods-with-ajax-example/
