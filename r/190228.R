# 엑셀파일(melontop100.xlsx)의 첫번째 시트만 읽어,마지막 합계 row는 삭제한 후, RData파일로 저장하시오.

mtx = read_excel('data/meltop100.xlsx', sheet = 1, col_names = T)
tail(mtx)
nrow(mtx)
mtx = mtx[-nrow(mtx), ]
save(mtx, file = 'data/meltop100.rda')
load("data/meltop100.rda")


# 엑셀파일(melontop100.xlsx)을 csv형태로 저장한 후 RStudio에서 read하시오. (read.table, read.csv모두 가능)

mtx = read_excel('data/meltop100.xlsx', sheet = 1, col_names = T)
mtx
write.table(mtx, file = 'data/melontop100.csv',sep = ',', col.names = TRUE, fileEncoding = 'utf-8')
mtx = read.table('data/melontop100.csv', sep = ',')
head(mtx)

# 온도파일(temper.txt)을 읽어 연도, 기온, 구분자 컬럼만 남기시오.
wfdata = read.fwf('data/temper.txt', header=F, width=c(15, 4, 68, 5, 1))
col_index = colnames((wfdata))
wfdata = wfdata[, col_index[c(2,4,5)]]
wfdata


# 난반 남학생중에 국어와 수학 성적이 90점 초과인 학생의 학번과 전과목 성적을 국어 성적이 높은순(descending)으로 추출하시오.

data = read.csv('./data/성적.csv')
data1 = data[data$반=='난' & data$성별 == '남' & data$국어 > 90 & data$수학 > 90,]
data1
data1$'총점' = data1$국어 + data1$영어 + data1$수학 + data1$과학 + data1$예체
data1[order(-data1$국어), c('학번', '총점')]




# data에 전체 과목에 대한 `평균` 변수(컬럼)을 추가하고, 국어 성적이 80점 이상인 학생을 대상으로 반별 국어 평균과 전체 과목 평균을 구하시오

data2 = data
data2$'평균' = (data2$국어 + data2$영어 + data2$수학 + data2$과학 + data2$예체) / 5


data21 = data2[data2$국어 >= 80, ] 
head(data21)

data22 = aggregate(data=data21, cbind(국어, 평균)~반, mean)
data22

data21$'반 국어 평균'= NULL

data21$'반 국어 평균'[data21$반 == '매'] = data22$'국어'[data22$반 == '매']
data21$'반 국어 평균'[data21$반 == '난'] = data22$'국어'[data22$반 == '난']
data21$'반 국어 평균'[data21$반 == '국'] = data22$'국어'[data22$반 == '국']
data21$'반 국어 평균'[data21$반 == '죽'] = data22$'국어'[data22$반 == '죽']

data21$'반 평균'[data21$반 == '매'] = data22$'평균'[data22$반 == '매']
data21$'반 평균'[data21$반 == '난'] = data22$'평균'[data22$반 == '난']
data21$'반 평균'[data21$반 == '국'] = data22$'평균'[data22$반 == '국']
data21$'반 평균'[data21$반 == '죽'] = data22$'평균'[data22$반 == '죽']

head(data21[,-c(5,6,7,8)])
data21[,-c(5,6,7,8)]

data2 = data
data2$'평균' = (data[ ,4]+data[ ,5]+data[ ,6]+data[ ,7]+data[ ,8])/5
aggregate(data=data2[data2$국어>=80,], cbind(국어, 평균)~반, mean)


# data$scout에서 스카우트가 아닌 학생을 제외하고 qplot을 그리시오.

install.packages('ggplot2')
data2$pass = ifelse(data2$평균 >= 60, TRUE, FALSE)
data2[data2$pass, ]
data2$scout = ifelse(data2$평균 >= 60, 
                    ifelse(data2$성별 == '남', 'BoyScout', 'GirlScout'),
                    '')
data2
qplot(data2$scout[data2$scout!=""])


# data에 학점 변수(컬럼)을 추가하시오. 범위 (A: 90이상, B:80이상, C: 70이상, D: 60이상, F: 60미만)

data2$'학점' = ifelse(data2$평균 >= 90, 'A',
                      ifelse(data2$평균 >= 80, 'B',
                             ifelse(data2$평균 >= 70, 'C',
                                    ifelse(data2$평균 >= 60, 'D', 'F')
                             )
                      )
                )
data2

data2
data2$'학점'= "F"
data2$'학점'[data2$평균>=60] = 'D'
data2$'학점'[data2$평균>=70] = 'C'
data2$'학점'[data2$평균>=80] = 'B'
data2$'학점'[data2$평균>=90] = 'A'
data2

# 학점별 빈도 막대 그래프(qplot)를 그리시오.

qplot(data2$'학점')


# mpg 데이터에서 통합 연비(도시와 고속도로)가 높은 순으로 출력하시오.

mpg = as.data.frame(ggplot2::mpg)
mpg2 = mpg
colnames(mpg2)
mpg2$average_mileage = (mpg2[, "cty"] + mpg2[, "hwy"]) / 2
mpg2[order(-mpg2$average_mileage),]


# mpg 데이터에서 생산연도별 연료 종류에 따른 통합연비를 연도순으로 출력하시오.
head(mpg2)
test2 <- aggregate(data=mpg2, average_mileage~(year+fl), mean)
test2[order(test2$year)]
test2


# midwest 데이터를 data.frame으로 불러온 후, 전체인구와 아시아계인구 데이터의 특징을 설명하시오. (state별 비교 설명)

midwest = as.data.frame(ggplot2::midwest)
data.frame(midwest)
library(psych)
summary(midwest)
head(midwest)
describe(midwest[c('popasian', 'poptotal')])
summary(midwest[c('popasian', 'poptotal')])
boxplot(midwest)
midwest1[midwest$popasian == 0, ]
plot(midwest$poptotal)
colnames(midwest)
midwest1 = aggregate(data=midwest, popasian~state, mean)
boxplot(midwest1$popasian~midwest1$state, data=midwest1, xlab = "state", ylab="popasian")
cor(midwest$popasian, midwest$poptotal)
?boxplot
?cor

# poptotal 변수(컬럼)를 total로, popasian 변수를 asian으로 변수명을 변경하는 코드를 작성하시오.
midwest2 = midwest
colnames(midwest2)
names(midwest2)[5] = c("total")
names(midwest2)[10] = c("asian")

# 전체 아시아계 인구수와, asian 변수를 이용해 `전체 인구 대비 아시아계 인구 백분율` 파생변수(asianpct)를 추가하고, 히스토그램을 그리시오.

data.frame(midwest2)
popasiantotal = sum(midwest2$asian)
midwest2$asianpct = (midwest2$asian / popasiantotal) * 100
hist(midwest2$asianpct)


# 도시(state 또는 county)기준으로 아시아계 인구가 어떻게 분포하는지 설명하시오.

midwest21 = aggregate(data=midwest2, asianpct~county, mean)
hist(midwest21$asianpct)
midwest21[order(midwest21$county, decreasing = T),]
head(midwest21[order(-midwest2$asianpct * 100),])

# 아시아계 인구 백분율(asianpct)의 전체 평균을 구하고, 평균을 초과하면 "lg", 그 외는 "sm"을 부여하는 파생변수(asianrate)를 추가하는 코드를 작성하시오.

average_asianpct = mean(midwest21$asianpct)
average_asianpct
midwest2$asianrate = ifelse(midwest2$asianpct > average_asianpct, "lg", "sm")
head(midwest21)
head(midwest2)

# "lg"와 "sm"에 해당하는 지역이 얼마나 되는지 빈도 막대그래프(qplot)을 그려보시오.

qplot(midwest2$asianrate)