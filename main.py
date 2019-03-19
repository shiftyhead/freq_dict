import nltk
from collections import Counter
import csv


nltk.download('stopwords')
from nltk.collocations import *
from nltk.tokenize import word_tokenize
from nltk.metrics.association import QuadgramAssocMeasures
bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
quadgram_measures = QuadgramAssocMeasures()
w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()
stopwords = nltk.corpus.stopwords.words('english')


def main():
    # print(stopwords)
    with open('target.txt') as f:
        # ws = w_tokenizer.tokenize(f.read())
        t = f.read()
        # print(t)
        cleaned = t.replace('\n', ' ').strip()
        ws = [i for i in nltk.regexp_tokenize(cleaned, '\w*') if i]
        # ls = [lemmatizer.lemmatize(i).lower() for i in ws if i.lower not in stopwords]
        ls = []
        collocations = []
        for w in ws:
            # print(w)
            if w.lower() in stopwords:
                pass
            else:
                l = lemmatizer.lemmatize(w).lower()
                ls.append(l)
            collocations.append(w.lower())
        # print(collocations)
        # finder = BigramCollocationFinder.from_words(collocations)
        # finder.apply_freq_filter(3)
        # print(finder.nbest(bigram_measures.likelihood_ratio, 20))
        # finder = TrigramCollocationFinder.from_words(collocations)
        # finder.apply_freq_filter(3)
        # print(finder.nbest(trigram_measures.likelihood_ratio, 20))
        finder = QuadgramCollocationFinder.from_words(collocations)
        finder.apply_freq_filter(3)
        print(finder.nbest(quadgram_measures.likelihood_ratio, 20))
    cntr = Counter(ls)
    print(len(cntr))
    for i in range(0, len(cntr)):
        l = cntr.most_common(len(cntr))[i]
        write_csv(l)
        # print(l)
def write_csv(data):
    with open('friends_counter.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)



if __name__ == '__main__':
    main()
