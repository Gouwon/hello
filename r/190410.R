data

## 3월 8일
# 1번문제) '죽반과 매반의 수학성적은 차이가 없다'라는 가설을 검정하시오.

## H0 : 죽반과 매반의 수학성적은 같다.
## H1 : 죽반과 매반의 수학성적은 다르다.

## 죽반과 매반이라는 2개 이상의 집단을 비교함으로 독립표본 검정(평균차이검정)을 한다.

## 1. 데이터 분석(표본 및 기술 통계 확인)

data %>% filter(반 %in% c('매', '죽')) %>% select(반, 수학) -> sampledata

head(sampledata)
summary(sampledata)

sampledata$반 = factor(sampledata$반, levels=c('매', '죽'), labels=c('매', '죽'))

library(psych)
describeBy(sampledata$수학, sampledata$반, mat = T)

## 2. 데이터 분석(표본 데이터 확인)
orgpar = par(no.readonly = T) 
boxplot(sampledata$수학 ~ sampledata$반)
layout(matrix(c(1,1,2,3), 2, 2, byrow = T))
boxplot(sampledata$수학 ~ sampledata$반)
hist(sampledata$수학[sampledata$반 == '매'])
hist(sampledata$수학[sampledata$반 == '죽'])
par(orgpar)

## 3. 등분산 검정

## H0 : 두 집단의 분산은 같다.
## H1 : 두 집단의 분산은 다르다.

var.test(sampledata$수학 ~ sampledata$반, data = sampledata)  # p-value = 0.876

# 0.05 < p-value임으로 귀무가설을 기각하지 못한다. 따라서 두 집단의 분산은 같다고 본다.


## 4. 독립 표본 검증(등분산 가정 하의 t-검정 Levene의 등분산 검정...)

t.test(sampledata$수학 ~ sampledata$반, data = sampledata,
         alternative = c("two.sided"),
         var.equal = T,                 # 등분산검증의 p-value < 0.05 이면 False로!
         conf.level = 0.95)             # p-value = 0.901 > 0.025(=(1-a)/2) 양측검정.

# p-value = 0.901 > 0.05(=1-a)임으로 귀무가설(죽반과 매반의 수학성적은 같다.) 을 기각하지 못한다.

# 5. 결과 graph 작도
mu = 63.84167; se = 2.114145; rn = sort(rnorm(120, mu, se))  #describeBy의 첫번째 그룹의 mean, se
plot(rn, dnorm(rn, mu, se), col='green', type = 'l', main = '평균점수',
       xlim = c(55, 75), ylim = c(0, 0.25)) 
abline(v=mu, col="green", lty=5)


par(new = T)          # 겹쳐 그리기
mu =63.46667; se = 2.144661; rn = sort(rnorm(120, mu, se)) #describeBy의 두번째 그룹의 mean, se
plot(rn, dnorm(rn, mu, se), col='red', type = 'l', main = '평균점수',
       xlim = c(55, 75), ylim = c(0, 0.25))
abline(v=mu, col="red", lty=5)
par(orgpar)



# 2번문제) 4개반 수학성적의 유사도(동질의 정도)를 분석하시오.

## 3개 이상의 집단에 대한 분석임으로 ANOVA 분석을 실시한다.

## H0 : 4개반의 수학 평균 성적의 동질적이다.
## H1 : 4개반 중 1개라도 수학 평균 성적은 동질적이지 않다.

## 1. 데이터 분석(표본 및 기술 통계 확인)

data %>% select(반, 수학) -> sampledata1

describeBy(sampledata1$수학, sampledata1$반, mat = T) -> summary_sampledata1

## 국 평균 : 63.59167 se : 2.020535
## 난 평균 : 63.08333 se : 2.028632
## 매 평균 : 63.84167 se : 2.114145
## 죽 평균 : 63.46667 se : 2.144661

summary_sampledata1 %>% select(group1, mean, se) -> summary_sampledata1


## 2. 데이터 분석(표본 데이터 확인)
library(ggplot2)
ggplot(sampledata1, aes(x=반, y=수학)) +
  geom_boxplot(outlier.color = 'blue') +
  ggtitle("각반 수학 성적")

ggplot(sampledata1, aes(x=수학)) +
  geom_histogram(binwidth = 10, col='white') +
  facet_grid(. ~ sampledata1$반)

## 3. 등분산 검정

## H0 : 각 집단의 분산은 같다.
## H1 : 적어도 하나의 집단의 분산은 다르다.

bartlett.test(sampledata1$수학 ~ sampledata1$반, data=sampledata1)

# p-value = 0.8893
# p-value > 0.05임으로 귀무가설을 기각하지 못한다. 따라서 4개반의 분산은 다르다고 할 수 없다.
# 따라서 ANOVA (등분산 가정 하의 Levene의 등분산 검정...)

## 4. ANOVA

aov(sampledata1$수학 ~ sampledata1$반, data=sampledata1) -> aaa
summary(aaa)   

# Pr(>F) 0.995  --->  p-value(Pr) > 0.0163 임으로 귀무가설을 기각하지 못한다. 따라서 4개반의 수학 성적은 다르다고 할 수 없다.

## 4-1. 사후검정
TukeyHSD(aaa)
## 4-2. 동질성 결과 그래프
plot(TukeyHSD(aaa))       # 가운데 선이 0이면 일치


draw = function(rn, mu, se, col) {
plot(rn, dnorm(rn, mu, se), col=col, type = 'l',
     xlim = c(50, 80), ylim = c(0, 0.25))
abline(v=mu, col=col, lty=5)
}

## 5. 결과 graph 작도

draw = function(rn, mu, se, col) {
  plot(rn, dnorm(rn, mu, se), col=col, type = 'l',
       xlim = c(50, 80), ylim = c(0, 0.25))
  abline(v=mu, col=col, lty=5)
}

orgpar = par(no.readonly = T) 
mu = 62.6; se = 2.097331; rn = sort(rnorm(1000, mu, se))
draw(rn, mu, se, 'red')
par(new = T)
mu = 59.4; se = 1.975140; rn = sort(rnorm(1000, mu, se))
draw(rn, mu, se, 'blue')
par(new = T)
mu = 64.2833; se = 1.9523; rn = sort(rnorm(1000, mu, se))
draw(rn, mu, se, 'darkgreen')
par(new = T)
mu = 66.6; se = 1.964653; rn = sort(rnorm(1000, mu, se))
draw(rn, mu, se, 'black')
par(orgpar)

legend('topright',
       legend=c('국', '난', '매', '죽'),
       pch=8,
       col=c('red', 'blue', 'darkgreen', 'black'),
       bg='gray')

# 3번문제) 전교생의 국어성적과 영어성적에 대한 상관분석(Correlation)을 수행하시오.

# H0 : 우리 학교의 국어성적과 영어성적은 상관관계를 가지고 있다.
# H1 : 우리 학교의 국어성적과 영어성적은 상관관계를 가지고 있지 않다.

## 1. 데이터 준비 

data %>% select(국어, 영어) -> sampledata2
head(sampledata2)

## 2. 기술 통계 확인

library(psych)
describe(sampledata2)

## 3. 그래프로 데이터 확인하기

pairs.panels(sampledata2)          

# 국어와 영어의 상관계수는 -0.02임으로 -0.1 ~ 0.1 사이에 위치하여 무시할만한 관계를 가지고 있다고 본다.

# 4. 상관분석
cor(sampledata2, use = "complete.obs",
      method = c("pearson"))        

# 5. 결과 그래프

plot(국어 ~ 영어, data=sampledata2)
abline(lm(국어 ~ 영어, data=sampledata2), col='red')  

# 실제 국어와 영어 간의 상관계수는 -0.01684502이며 이는 전술한 바와 같이 무시할만한 관계를 가지고 있다고 할 수 있다. 2개의 변수 간의 그래프의 기울기가 보여주듯이 이 둘 사이에는 특별한 관계가 없으며, 따라서 귀무가설을 기각한다.


# 4번 문제) mpg데이터의 displ, cyl, trans, cty, hwy 중 1999년과 2008년 두 해의 고객 만족도가 0과 1이라고 했을 때, 어떤 요소가 만족도에 많은 기여를 했는지 로지스틱 회귀분석하시오.


# 1. 데이터 준비

library(ggplot2)
mpg = as.data.frame(ggplot2::mpg)

unique(mpg$trans); unique(mpg$year)

sampledata3 = mpg %>%
              mutate(trs = ifelse(substr(trans, 1, 4) == 'auto', 1, 0), 
              y = ifelse(year == 1999, 0, 1)) %>%
              select(y, displ, cyl, trs, cty, hwy)

head(sampledata3, 10)


# 2. 기본 통계치 확인

describe(sampledata3)
pairs.panels(sampledata3)


# 3. 분석
glmdata = glm(y ~ displ+cyl+cty+hwy+trs, family = binomial, data=sampledata3)

summary(glmdata)  # Estimate: 기울기(비례/반비례), Pr: 0.05보다 작으면 영향이 있다

# h0 : 해당 독립변수는 영향을 주지 않는다.
# h1 : 해당 독립변수는 영향을 준다.

orgpar = par(no.readonly = T) 
par(mfrow=c(2,2)) 
plot(glmdata)
par(orgpar)

# 4. coefficients(기울기+절편)와 confint(신뢰구간)로 LOR(Log Odd Ratio) 구하기
round(exp(cbind(LOR = coef(glmdata), confint(glmdata))), 2)

# 고객의 만족도에 영향을 주는 요인은 displ, hwy이며 이들은 고객의 만족도와 양의 상관관계를 가지고 있다. 나머지 cyl, cty, trs의 경우 통계적 유의성을 가지지 않기 때문에 이들에 대해서는 따로 분석을 해 볼 필요가 있다.


save(data, file = 'data/data.rda')

load("./data/data_eng.rda")
data


## 카이제곱은 두 변수간의 관계를 비율을 통해서 알아봄. 이 때 귀무가설은 두 변수간의 관계가 없다.이다.
# addmargins(nkdata) 은 sum을 붙여줌.