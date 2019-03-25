install.packages('tm')
library(tm)

getSources()
getReaders()

folder = system.file("texts", "txt", package="tm")
txtSource = DirSource(folder)   # dir 경로로 Corpus 생성
class(txtSource); str(txtSource)   
doc = VCorpus(txtSource, readerControl = list(language='lat'))
class(doc); summary(doc)

meta(doc)
meta(doc, type = 'local')
inspect(doc)
inspect(doc[1])
doc[[1]]
writeCorpus(doc, path="data", filenames = names(doc))

getTransformations()
doc = tm_map(doc, stripWhitespace)

data("crude")
crude[[1]]  
crude[[1]][1]

crude = tm_map(crude, content_transformer(tolower))
crude = tm_map(crude, removePunctuation)
crude = tm_map(crude, removeWords, stopwords("english"))
crude = tm_map(crude, stripWhitespace)

install.packages("SnowballC")
library("SnowballC")
crude = tm_map(crude, stemDocument, language="english")

tdm = TermDocumentMatrix(crude)
tdm = removeSparseTerms(tdm, 0.8)

rowSums(as.matrix(tdm))     
wFreq = sort(rowSums(as.matrix(tdm)), decreasing = T)
wFreq = subset(wFreq, wFreq > 10)
wFreq

install.packages('RColorBrewer')  
library(RColorBrewer)
darks = brewer.pal(8, 'Dark2')

install.packages("wordcloud")     
library(wordcloud)
wordcloud(words = names(wFreq), freq=wFreq, min.freq = 10,
          random.order = F, colors = darks)

# try this

folder = system.file("texts", "txt", package="tm")
txtSource = DirSource(folder)   # dir 경로로 Corpus 생성
class(txtSource); str(txtSource)   
doc = VCorpus(txtSource, readerControl = list(language='lat'))

doc_converted = tm_map(doc, content_transformer(tolower))
doc_converted = tm_map(doc_converted, removePunctuation)
doc_converted = tm_map(doc_converted, removeWords, stopwords("romanian"))
doc_converted = tm_map(doc_converted, stripWhitespace)
doc_converted[[1]][1]
?stopwords

doc_converted = tm_map(doc_converted, stemDocument, language="romanian")

tdm_latin = TermDocumentMatrix(doc_converted)
tdm_latin = removeSparseTerms(tdm_latin, 0.8)

rowSums(as.matrix(tdm_latin))     
wFreq_latin = sort(rowSums(as.matrix(tdm_latin)), decreasing = T)
wFreq_latin = subset(wFreq_latin, wFreq_latin > 1)
wFreq_latin

darks = brewer.pal(8, 'Dark2')
wordcloud(words = names(wFreq_latin), freq=wFreq_latin, min.freq = 1, scale=c(2.5,0.5), rot.per = 1, random.order = F, colors = darks)
warnings()

