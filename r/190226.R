Sys.getlocale()
options(encoding = 'utf-8')
data = read.csv('./data/성적.csv')
data$반
dim(data)
str(data)
summary(data)
head(data, 20)
tail(data)
nrow(data)
ncol(data)
data$학번
data[10,1]
data[,2]
c(1, 5)
c(1, 5, 7)
c(1:5)
seq(1,5)
data[100:104, c(1,3)]
data[101:110, c(1,3,4)]  ##학번,성별,국어성적 출력
data[101:110, c('학번','성별','국어')]
data[101:110, c('국어')] = 0
data[101:110, c('학번','성별','국어')]
data[201:300, c('영어','과학')] = 100
data[201:300, c('영어','과학')]
?read.csv

table(data$'수학')
plot(data$'수학')
order(data$'수학')
data[c(3,5,7),]
data[order(data$'수학'),]
plot(data[order(data$'수학'),]$'수학')
d1 = data[order(data$'수학'),]
plot(d1$'수학')
write.csv(d1, "./data/result1.csv")
read.csv("./data/result1.csv")
write.table(d1)
write.table(d1, sep=",")
write.table(d1, sep=",", col.names = F, row.names = F)

fn = function(data, line=5) {
  print(head(data, line))
  print(tail(data, line))
}
fn(d1, 10)

fn2 = function(row) {
  data[row,]
}
fn2(10)

class(5)
is.numeric(5)
class('sss')
is.character('sss')

factor(1, levels = 1:3, labels = c('A','B','C'))
factor(1, levels = 3:1, labels = c('A','B','C'))

d = 1:30
rowcnt = 5
d1 = matrix(d, ncol = length(d)/rowcnt, byrow=F)
colcnt = 6
d1 = matrix(d, nrow = length(d)/colcnt, byrow=T)

# 1,2,3,4를 입력하면 해당 혈액형(A, B, O, AB)을 factor로 출력하는 함수를 작성하시오.
blood_type = function(x=1) {
  result = factor(x, levels = seq(1,4), labels = c('A', 'B', 'O', 'AB'))
  return(as.vector(result))
}
blood_type(1)

# 1차원 vector와 신규 입력값을 전달 받아 vector에 값을 추가하는 append 함수를 작성하시오
?append

add_vector = function(vector, value) {
  vector[length(vector) + 1] = value
  return(vector)
}
vector = c(1:5)
vector = add_vector(vector, 6)
vector

# 숫자로 된 10x20 matrix를 정의하고,열 이름을 알파벳 대문자순으로, 행 이름을 소문자로 변경하시오.(단, 10번째, 20번째 컬럼명은 알파벳 뒤에 10, 20을 붙이시오)

data = seq(1,200)
length(data)
rowcnt = 10
newcol = c("", "", "", "", "", "", "", "", "", 10, "", "", "", "", "", "", "", "", "", 20)
col1 = LETTERS[1:ncol(test_matrix)]
test_matrix = matrix(data, ncol = length(data)/rowcnt, byrow = T)
colnames(test_matrix) = paste(col1, newcol, sep = "")
rownames(test_matrix) = letters[1:nrow(test_matrix)]
test_matrix

b = paste('a', 10, sep="")
b = paste0(c('a','b','c'), c(10, 20, 30))
b

start = Sys.time()
read.csv('data/성적.csv')
Sys.time() - start

install.packages('data.table')
library('data.table')
start = Sys.time()
fread('data/성적.csv', encoding = 'UTF-8')
Sys.time() - start
