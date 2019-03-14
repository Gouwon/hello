# mpg 데이터에서 통합 연비(도시와 고속도로 평균)가 높은 순으로 출력하시오.

mpg = as.data.frame(ggplot2::mpg)
mpg1 = mpg
mpg1$average_mileage = (mpg1[, "cty"] + mpg1[, "hwy"]) / 2
head(mpg1, 10)

# mpg 데이터에서 생산연도별 연료 종류에 따른 통합연비를 연도순으로 출력하시오.

mpg2 = aggregate(data=mpg1, average_mileage~(year+fl), mean)
head(mpg2)
mpg2[order(mpg2$year),]


# midwest 데이터를 data.frame으로 불러온 후, 전체인구와 아시아계인구 데이터의 특징을 설명하시오. (state별 비교 설명)

midwest = as.data.frame(ggplot2::midwest)
data.frame(midwest)
library(psych)
dim(midwest)
describe(midwest[c('popasian', 'poptotal')])
summary(midwest[c('popasian', 'poptotal')])
midwest1 = aggregate(data=midwest, popasian~state, mean)
midwest11 = aggregate(data=midwest, poptotal~state, mean)
aggregate(data=midwest, percasian~state, mean)
midwest111 = cbind(midwest1, midwest11$poptotal)
head(midwest111)
summary(midwest111)
plot(midwest111$popasian, midwest111$`midwest11$poptotal`)
?plot
boxplot(midwest$percasian~midwest$state, data=midwest, xlab = "state", ylab="popasian")
boxplot(midwest111$`midwest11$poptotal`~midwest1$state, data=midwest1, xlab = "state", ylab="poptotal")

# poptotal 변수(컬럼)를 total로, popasian 변수를 asian으로 변수명을 변경하는 코드를 작성하시오.

midwest2 = midwest
colnames(midwest2)
names(midwest2)[5] = c("total")
names(midwest2)[10] = c("asian")


# 전체 아시아계 인구수와, asian 변수를 이용해 `전체 아시아계 인구 대비 아시아계 인구 백분율` 파생변수(asianpct)를 추가하고, 히스토그램을 그리시오.

popasiantotal = sum(midwest2$asian)
midwest2$asianpct = (midwest2$asian / popasiantotal) * 100
hist(midwest2$asianpct)
midwest22 = midwest2[midwest2$asianpct < 0.01,]
head(midwest2[order(midwest2$asianpct, decreasing = F),])
hist(midwest22$asianpct, breaks =30)

# 도시(state 또는 county)기준으로 아시아계 인구가 어떻게 분포하는지 설명하시오.

head(midwest2)
midwest21 = aggregate(data=midwest2, asianpct~county, mean)
head(midwest21[order(-midwest21$asianpct),])
midwest[midwest$county == "COOK",]

# 아시아계 인구 백분율(asianpct)의 전체 평균을 구하고, 평균을 초과하면 "lg", 그 외는 "sm"을 부여하는 파생변수(asianrate)를 추가하는 코드를 작성하시오.

average_asianpct = mean(midwest21$asianpct)
average_asianpct
midwest2$asianrate = ifelse(midwest2$asianpct > average_asianpct, "lg", "sm")
head(midwest21)
head(midwest2)

# "lg"와 "sm"에 해당하는 지역이 얼마나 되는지 빈도 막대그래프(qplot)을 그려보시오.

qplot(midwest2$asianrate)