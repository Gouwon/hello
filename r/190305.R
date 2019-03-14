?rep
x = seq(1:5)
rep.int(x, times = 2)
set.seed(4); sample(1:5, size = 3)
?sample
?runif
?grep
head(data)

grep(pattern='^2.*0$', x=data$학번, value = T)
?sub

install.packages('lubridate')
library(lubridate)
?quarter()
?foreach()


f = 1
x = 5
for (i in 1:x)
  f = f * i
print(paste("The factorial of", x, "is", f))

i = 0
while(TRUE) { 
  i = i + 1
  if (i %% 2 == 0)
    next
  if (i > 10)
    break
  print(i)
}

?apply
?vapply
?rep
?replicate

?dimnames
?matrix

# data$group 컬럼에 A조~C조 랜덤으로 160명씩 고르게 분포시키시오.

head(data)
data$group = rep(LETTERS[1:3], length.out=480)
dim(data[data$group=='A',])

sample(c(rep("A", 160), rep("B", 160), rep("C", 160))) -> data$group


# fibonacci.R 파일을 작성하고 console에서 실행하시오.

source('fibonacci.R')


# apply를 이용하여 smdt에 과목별 평균점수 행을 추가하고, 총점과 평균 변수(컬럼)을 추가하시오.

set.seed(100)
smdt = data.frame(stuno = 1:5, 
                  Korean=sample(60:100, 5),
                  English=sample((5:10) * 10, 5),
                  Math=sample(50:100, 5))
class(smdt$stuno)
smdt$stuno = as.character(smdt$stuno)
apply(smdt[, 2:4], MARGIN = 2, FUN = mean)
l1 = c("계", apply(smdt[, 2:4], MARGIN = 2, FUN = mean))
smdt = rbind(smdt, l1)
smdt$Korean = as.integer(smdt$Korean)
smdt$English = as.integer(smdt$English)
smdt$Math = as.integer(smdt$Math)
smdt$'total' = apply(smdt[, 2:4], MARGIN = 1, FUN = sum)
smdt$'avg' = round(apply(smdt[, 2:4], MARGIN = 1, FUN = mean), 0)
smdt


# 2016~2019년 연도별 1월(Jan) ~ 12월(Dec) 매출액 데이터를`no year Jan Feb … Dec` 형태로 만든 다음, 아래와 같이 출력하시오.

dfsum = cbind(data.frame(no=1:4, year=2016:2019), 
               matrix(round(runif(4 * 12), 3) * 1000000, nrow=4, 
                      dimnames = list(NULL, month.abb) ))
dfsum

library('reshape2')
meltsum = melt(dfsum[,2:ncol(dfsum)], id.vars = "year", variable.name = 'month', value.name = "saleamt")
head(meltsum)
?melt
