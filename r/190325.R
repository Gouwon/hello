install.packages(c("twitteR", "RCurl", "RJSONIO", "stringr", "streamR", "ROAuth"))
library(twitteR); library(RCurl); library(RJSONIO); library(stringr)
library(streamR); library(ROAuth)

install.packages(c("rJava", "memoise", "KoNLP"))
library(rJava); library(KoNLP)

searchTwitter(enc2utf8('승리'), n=100, lan='ko')
# searchTwitter([검색어], 검색결과수, 언어) ==> document 로 리턴.

tweets = searchTwitter(enc2utf8('승리'), n=100, lan='ko', 
                       since='2019-03-11', until='2019-03-31')
tdf = twListToDF(tweets)
nrow(tdf)
colnames(tdf)
names(tdf)
head(tdf)

tdf = tdf %>% filter(!isRetweet) %>% select(text)
tdf %>% filter(regexpr('광고',text) == -1)    # 특정 단어 포함된 문서 제거
unique(tdf$text)
tw = unique(tdf$text)
?gsub

tw = gsub("[[:cntrl:]]", "", tw)                      # 제어문자(\n, \t등) 제거
tw = gsub("http[s]?://[[:alnum:].\\/]+", "", tw)     # link 제거
tw = gsub("&[[:alnum:]]+;", "", tw)            # escape(&amp; &lt;등) 제거
tw = gsub("@[[:alnum:][:punct:]]+[:]?", "", tw)             # 트위터 계정 부분 제거
tw = gsub("[ㄱ-ㅎㅏ-ㅣ]","",tw)                   # 한글 불용어(ㅋㅋㅎㅎ ㅠㅜ등) 제거
tw = gsub("\\s{2,}", " ", tw)                  # 2개이상 공백을 한개의 공백으로 처리
tw = gsub("[[:punct:]]", "", tw)               # 특수 문자 제거 (앞의 처리 때문에 마지막에 해야 함!!)
gsub('\\p{So}|\\p{Cn}', '', some_tweets, perl = TRUE)
tw = gsub('\\p{So}|\\p{Cn}', '', tw, perl = TRUE)

head(tw, 20)
tail(tw)

# 1. 명사 추출
nouns = sapply(tdf, extractNoun, USE.NAMES = F)
wc = sapply(tw, extractNoun, USE.NAMES = F)
ul = unlist(wc)
ul = ul[nchar(ul) > 1]
wc1 = table(ul)
names(wc1)
length(wc1)
# 2. 상위 n 개 추출
wc2 = head(sort(wc1, decreasing = T), 50)
wc2

# 3. wordcloud
library(RColorBrewer)
library(wordcloud)
pal = brewer.pal(9, "Set1")
wordcloud(names(wc2), freq=wc2, scale=c(5,0.5), rot.per=0.25, 
            min.freq = 1, random.order = F, random.color = T, colors = pal)

# try this
keyword = "백종원"; n = 100; draw_n = 20; since = '2019-03-01'; until = '2019-03-24'

draw_key_wordcolud(keyword = "백종원", n = 100, draw_n = 20, since = '2019-03-01', until = '2019-03-24')
draw_key_wordcolud = function(keyword, n, draw_n, since, until){
  tweets = searchTwitter(enc2utf8(keyword), n=n, lan='ko', 
                         since=since, until=until)
  tdf = twListToDF(tweets)
  tw = unique(tdf$text)
  
  tw = gsub("[[:cntrl:]]", "", tw)
  tw = gsub("http[s]?://[[:alnum:].\\/]+", "", tw)
  tw = gsub("&[[:alnum:]]+;", "", tw)
  tw = gsub("RT @[[:alnum:][:punct:]]+[:]?", "", tw)
  tw = gsub("[ㄱ-ㅎㅏ-ㅣ]","",tw)
  tw = gsub("\\s{2,}", " ", tw)
  tw = gsub("[[:punct:]]", "", tw)
  tw = gsub('\\p{So}|\\p{Cn}', '', tw, perl = TRUE)
  
  wc = sapply(tw, extractNoun, USE.NAMES = F)
  ul = unlist(wc)
  ul = ul[nchar(ul) > 1]
  wc1 = table(ul)
  wc2 = head(sort(wc1, decreasing = T), draw_n)
  
  library(RColorBrewer)
  library(wordcloud)
  pal = brewer.pal(9, "Set1")
  wordcloud(names(wc2), freq=wc2, scale=c(5, 0.5), rot.per=0.25, 
            min.freq = 1, random.order = F, random.color = T, colors = pal)
}

tw