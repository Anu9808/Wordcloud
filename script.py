'''
 Python program to translate 
 speech to text and make a wordcloud of important words after filtering out the unimportant
 words and puctuation.
'''
#MOTIVE
'''
 With the help of the wordcloud we can get the idea what is the speech or audio about
 e.g. now we know speech is about iot use in business organisations.
'''

import speech_recognition as sr 
import wordcloud
from matplotlib import pyplot as plt
#print(sr.__version__)

# Initialize the recognizer  
# r = sr.Recognizer() 
# fe = sr.AudioFile('female.wav')
# with fe as source:
#     audio = r.record(source)

#print(type(audio))  

#text extracted from audio file with the help of with GOOGLE WEB SPEECH Api

# textfile = r.recognize_google(audio)
  

file_contents=''' IoT is essential to business. IoT provides businesses with a real-time look into how their systems really work, d
into everything from the performance of machines to supply chain and logistics operations.
IoT is most abundant in manufacturing, transportation and utility organizations, making use of sensors and other IoT devices; however, it has also found use cases for organizations within the agriculture, infrastructure
and home automation industries, leading some organizations toward digital transformation. .'''

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    #punctuations = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    str2=""
    frequencies={}

    for ch in file_contents:
        if ch.isalpha() or ch==" " :
            str2+=ch

    list1=[]
    list2=[]
    list1=str2.split(" ")
    
    for word in list1:
        if word not in uninteresting_words:
            list2.append(word)

    for word in list2:
        if word not in frequencies:
            frequencies[word]=1

        else:
            frequencies[word]+=1
            
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()

# Display your wordcloud image
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
