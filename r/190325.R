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


install.packages(c("arules", "igraph", "combinat", "arulesViz", "visNetwork"))
?apriori
library(arules); library(igraph); library(combinat)

nouns = sapply(wc, unique)
nouns1 = sapply(nouns, function(x) {
  Filter(function(y='') { nchar(y) <= 4 && nchar(y) > 1 && is.hangul(y) }, x)
})
wtrans = as(nouns1, "transactions")
rules = apriori(wtrans, parameter = list(supp=0.015, conf=0.5))
inspect(sort(rules))

# confidence 기준으로 상위 30개만을 시각화
subrules2 <- head(sort(rules, by="confidence"), 30)
ig <- plot( subrules2, method="graph", control=list(type="items") )

# interactive
ig_df <- get.data.frame( ig, what = "both" )
visNetwork(
  nodes = data.frame(id = ig_df$vertices$name,
                     value = ig_df$vertices$support, ig_df$vertices),
  edges = ig_df$edges
) %>% visEdges(ig_df$edges) %>%visOptions( highlightNearest = T )


# interative
install.packages(c("arulesViz", "visNetwork"))
library(arulesViz); library(visNetwork)

# lift 기준으로 상위 20개만을 시각화
subrules2 <- head(sort(rules, by="lift"), 20)
ig <- plot( subrules2, method="graph", control=list(type="items") )

# interactive
ig_df <- get.data.frame( ig, what = "both" )
visNetwork(
  nodes = data.frame(id = ig_df$vertices$name,
                     value = ig_df$vertices$support, ig_df$vertices),
  edges = ig_df$edges
) %>% visEdges(ig_df$edges) %>%visOptions( highlightNearest = T )


# naver news
install.packages('rvest')
install.packages('httr')
install.packages('stringr')

library(rvest); library(httr); library(stringr); library(dplyr)
newsUrl = "https://news.naver.com/main/ranking/popularDay.nhn?mid=etc&sid1=111"
html = read_html(newsUrl)
links = html_attr(html_nodes(html, '.content dt a'), 'href')
links = links[!is.na(links)]       # NA 제거
news = list()       # 변수 초기화

# 내용 수집
for (i in 1:length(links)) {
  try({
    htxt = read_html(paste0('https://news.naver.com', links[i]))
    comments = html_nodes(htxt, '#articleBodyContents')
    # repair_encoding(html_text(comments), from='utf-8')
    get_news = repair_encoding(html_text(comments))
    news[i] = str_trim(get_news)
  }, silent = F)
}
news1 = news
news = news1
?try
?trySilent
for(i in 1:length(links)) {
  news[[i]][1] = removeStopword(news[[i]][1])
}

removeStopword = function(tw){
  tw = gsub("[[:cntrl:]]", " ", tw)
  tw = gsub("http[s]?://[[:alnum:].\\/]+", " ", tw)
  tw = gsub('[[:alnum:].?[:alnum:]]+@[[:alnum:].]+', ' ', tw)
  tw = gsub("&[[:alnum:]]+;", " ", tw)
  tw = gsub("RT @[[:alnum:][:punct:]]+[:]?", " ", tw)
  tw = gsub("[ㄱ-ㅎㅏ-ㅣ]"," ",tw)
  tw = gsub("\\s{2,}", " ", tw)
  tw = gsub("[[:punct:]]", "", tw)
  tw = gsub(" flash 오류를 우회하기 위한 함수 추가 function flash removeCallback ",'', tw)
  tw = gsub(' flash 오류를 우회하기 위한 함수 추가','',tw)
  tw = gsub(' function flashremoveCallback ','',tw)
  tw = gsub('\\p{So}|\\p{Cn}', '', tw, perl = TRUE)
  tw = gsub("\\s{2,}", " ", tw)
}

news[[20]][1]
gsub("(\\s|\\t)[:alnum:]@[[:alnum:]\\.]", "", news[[1]][1])
gsub("\\s.*@.*.kr", "", news[[1]][1])
gsub('[[:alnum:]]+@[[:alnum:].]+', '', news[[1]][1]) # kimhyoj@yna.co.kr
gsub(" flash 오류를 우회하기 위한 함수 추가 function flash removeCallback ",'',news[[20]][1])
news[[20]][1]
gsub("function flash removeCallback", "", news[[20]][1])

tw = news[[20]][1]

tw = gsub("[[:cntrl:]]", " ", tw)
tw = gsub("http[s]?://[[:alnum:].\\/]+", " ", tw)
tw = gsub('[[:alnum:].?[:alnum:]]+@[[:alnum:].]+', ' ', tw)
tw = gsub("&[[:alnum:]]+;", " ", tw)
tw = gsub("RT @[[:alnum:][:punct:]]+[:]?", " ", tw)
tw = gsub("[ㄱ-ㅎㅏ-ㅣ]"," ",tw)
tw = gsub("\\s{2,}", " ", tw)
tw = gsub("[[:punct:]]", "", tw)
tw = gsub(" flash 오류를 우회하기 위한 함수 추가 function flash removeCallback ",'', tw)
tw = gsub(' flash 오류를 우회하기 위한 함수 추가','',tw)
tw = gsub(' function flashremoveCallback ','',tw)
tw = gsub('\\p{So}|\\p{Cn}', '', tw, perl = TRUE)
tw = gsub("\\s{2,}", " ", tw)



# try this

# 네이버 뉴스 1면의 기사들을 수집하시오.(https://news.naver.com/main/home.nhn)

removeStopword = function(tw){
  tw = gsub("\\s{2,}", " ", tw)
  tw = gsub("[[:cntrl:]]", " ", tw)
  tw = gsub("http[s]?://[[:alnum:].\\/]+", " ", tw)
  tw = gsub('[[:alnum:].]+@[[:alnum:].]+', ' ', tw)
  tw = gsub("&[[:alnum:]]+;", " ", tw)
  tw = gsub("RT @[[:alnum:][:punct:]]+[:]?", " ", tw)
  tw = gsub("[ㄱ-ㅎㅏ-ㅣ]"," ",tw)
  tw = gsub("\\s{2,}", " ", tw)
  tw = gsub("[[:punct:]]", " ", tw)
  # tw = gsub("flash 오류를 우회하기 위한 함수 추가 function flash removeCallback",'', tw)
  tw = gsub('flash 오류를 우회하기 위한 함수 추가','',tw)
  tw = gsub('function flashremoveCallback',' ', tw)
  tw = gsub("function flash removeCallback", " ", tw)
  tw = gsub("_flash_removeCallback()", " ", tw)
  tw = gsub('\\p{So}|\\p{Cn}', '', tw, perl = TRUE)
  tw = gsub("\\s{2,}", " ", tw)
}

library(rvest); library(httr); library(stringr); library(dplyr)

newsUrl = "https://news.naver.com/main/home.nhn"
html = read_html(newsUrl)
links = html_attr(html_nodes(html, '.main_component.droppable li a'), 'href')
links = links[!is.na(links)]
news = list()


j = 1
for (i in 1:5) {
  try({
    # htxt = read_html(paste0('https://news.naver.com', links[i]))
    htxt = read_html(links[i])
    comments = html_nodes(htxt, '#articleBodyContents')
    # repair_encoding(html_text(comments), from='utf-8')
    get_news = repair_encoding(html_text(comments))
    if(is.null(get_news)) next
    
    news[j] = str_trim(get_news)
    j = j + 1
    
    # ch = html_children(comments)
    # for (i in 1:length(ch)) {
    #   chtxt = html_text(ch[i])
    #   if (chtxt == "") next
    #   get_news = stri_replace_all(get_news, "", fixed=html_text(ch[i]))
    # }
  }, silent = F)
}
news
length(news)
news1 = news

for (i in 1:length(news1)){
  try({news1[[i]][1] = removeStopword(news1[[i]][1])
      news1[[i]][1] = gsub('function flashremoveCallback',' ', news1[[i]][1])}, silent = T)
}

# 수집 된 뉴스로 WordCloud를 작도하시오.
library(rJava); library(KoNLP)

wc = head(sapply(news1, extractNoun, USE.NAMES = F), 30)
data_unlist = unlist(wc)
data_unlist <- Filter(function(x){nchar(x)>=2}, data_unlist)
wc1 = table(data_unlist)
wc1
names(wc1); length(wc1)
# wc2 = head(sort(wc1, decreasing = T), 100)
# for(i in 1:length(wc2)){
#   wc2[i] = as.character(wc2[i])
# }

library(RColorBrewer); library(wordcloud)
pal = brewer.pal(9, "Set1")
wordcloud(names(wc2), freq=wc2, scale=c(2,0.05), rot.per=0.5, 
            min.freq = 1, random.order = F, random.color = T, colors = pal)


# 연관성 분석

wc3 = head(sort(wc1, decreasing = T), 600)
library(arules); library(igraph); library(combinat)

nouns = sapply(wc, unique)
nouns1 = sapply(nouns, function(x) {
  Filter(function(y='') { nchar(y) > 1 && nchar(y) <= 4}, x)
})
wtrans = as(nouns1, "transactions")


rules = apriori(wtrans, parameter = list(supp=0.5, conf=0.5, minlen=2, maxlen=5))
inspect(sort(rules))
?inspect

library(arulesViz); library(visNetwork)
subrules2 <- head(sort(rules, by="lift"), 20) ## lift 기준으로 상위 20개만을 시각화
ig <- plot( subrules2, method="graph", control=list(type="items") )

ig_df <- get.data.frame( ig, what = "both" )
visNetwork(
  nodes = data.frame(id = ig_df$vertices$name,
                     value = ig_df$vertices$support, ig_df$vertices),
  edges = ig_df$edges
) %>% visEdges(ig_df$edges) %>%visOptions( highlightNearest = T )

subrules2 <- head(sort(rules, by="confidence"), 30)
ig <- plot( subrules2, method="graph", control=list(type="items") )
# saveAsGraph seems to render bad DOT for this case
ig_df <- get.data.frame( ig, what = "both" )

ig_df <- get.data.frame( ig, what = "both" )
visNetwork(
  nodes = data.frame(id = ig_df$vertices$name,
                     value = ig_df$vertices$support, ig_df$vertices),
  edges = ig_df$edges
) %>% visEdges(ig_df$edges) %>%visOptions( highlightNearest = T )