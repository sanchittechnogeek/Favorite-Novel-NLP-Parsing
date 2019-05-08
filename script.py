#importing the nltk and tokenizer functions
import nltk
from nltk import pos_tag, RegexpParser
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter, vp_chunk_counter

#opening and reading the novel
text = open("the_wizard_of_oz.txt",encoding='utf-8').read().lower()

#we can now see the novel in lower text
print(text,'\n')

#
sentence_tokenizer = PunktSentenceTokenizer(text)
sentence_tokenized = sentence_tokenizer.tokenize(text)

#prints individual sentence 15
print(sentence_tokenized[15],'\n')
#total individual sentences
print(len(sentence_tokenized),'\n')

#storing the words in sentence as a list
word_tokenized = list()
for sentence in sentence_tokenized:
  #tokenizing the string sentence using word_tokenize() function
  word_tokenized.append(word_tokenize(sentence))
  
print(word_tokenized[15],'\n')
print(len(word_tokenized),'\n')

#downloading dataset | one time only!
#nltk.download('averaged_perceptron_tagger')

#speech tagged sentence
pos_tagged_text = list()
for sentence in word_tokenized:
  pos_tagged_text.append(pos_tag(sentence))
  
  
print(pos_tagged_text[10],'\n')
#speech tagging uses abbreviations 
#for eg. ('was', 'VBD')
# VBD is Verb, past tense

#using regular expression (RegExp) to find Nouns (NN) phrases
chunk_grammer = "NP: {<DT>?<JJ>*<NN>}"
#using regular expression (RegExp) to find Verb prases (VB.) phrases
vp_chunk_grammer = "VP: {<VB.*><DT>?<JJ>*<NN><RB.?>?}"
#passing the chunk grammer to chunk out the phrases
chunk_parser = RegexpParser(chunk_grammer)
vb_chunk_parser = RegexpParser(vp_chunk_grammer)

chunked_sentence = chunk_parser.parse(pos_tagged_text[10])

#printing the chunked sentence
print(chunked_sentence)

#creating separate lists for Noun phrases
#creating separate lists for Verb phrases
np_chunked_sentences = list()
vp_chunked_sentences = list()

#
for sentence in pos_tagged_text:
  np_chunked_sentences.append(chunk_parser.parse(sentence))
  vp_chunked_sentences.append(vb_chunk_parser.parse(sentence))

print(np_chunked_sentences[222])

most_common_np_chunks = np_chunk_counter(np_chunked_sentences)
most_common_vp_chunks = vp_chunk_counter(vp_chunked_sentences)

print('NP Chunks')
print(most_common_np_chunks,'\n')

print('VP Chunks')
print(most_common_vp_chunks)

