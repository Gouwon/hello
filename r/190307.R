t = c(5, 7, 2, 8, 20, 11, 19)

rev(t)
rev(t[order(t)])
sort(t)
sort(smdt$avg, decreasing=T)

install.packages('dplyr')
library('dplyr')

colnames(data)
dplyr::rename(data, '조'=group)


?attach
?filter
?rename

data %>%
  filter(수학 > 95) %>% 
  select(학번, 국어, 영어, 수학) %>%
  head
data %>% filter(수학>95) %>% select(학번, 국어, 영어, 수학) %>% head
data %>% filter(수학>95) %>% select(-학번, 국어, 영어, 수학) %>% head


data = dplyr::rename(data, kor=국어, sci=과학, eng=영어, stuno=학번, class=반, gender=성별, art=예체)
data = dplyr::rename(data, math=수학, cls=class, gen=gender)
colnames(data)

?arrange
data %>%
  mutate(kor_eng = kor + eng) %>%
  arrange(desc(kor_eng)) %>%
  head

data %>%
  arrange(desc(kor + eng)) %>%
  head

data %>%
  select(kor, eng) %>%
  arrange(desc(kor + eng)) %>%
  head

data %>%
  group_by(cls) %>%
  summarise(mean_math = mean(math),
            sum_math = sum(math),
            medi_math = median(math),
            n_math = n()) %>%
  arrange(desc(mean_math))



dfsum = cbind( data.frame(yno=1:4, year=2016:2019), 
                 matrix(round(runif(16), 3) * 1000, ncol=4, dimnames = list(NULL, paste0('Q', 1:4))))

sales = cbind( data.frame(no=1:12, year=2016:2019), 
                 matrix(round(runif(144), 3) * 100000, ncol=12, dimnames = list(NULL, month.abb)) )

head(sales)
left_join(sales, dfsum, by=c('year' = 'year'))

inner_join(sales, dfsum, by=c('year' = 'year', 'no' = 'yno'))


# mpg데이터에서 차종(class)가 suv, compact인 자동차의 모델과 연비관련 변수만 출력하세요.

mpg = as.data.frame(ggplot2::mpg)
colnames(mpg)

mpg %>%
  filter(class %in% c('suv', 'compact')) %>%
  select(model, cty, hwy)


# mpg데이터에서 고속도로연비(hwy) 1 ~ 5위에 해당하는 자동차의 데이터를 출력하세요.

arrange(mpg, desc(hwy)) %>%
  head(5)


# 회사별로 suv 차들의 통합연비(평균) 구해 1 ~ 5위를 출력하세요.

filter(mpg, class=="suv") %>%
  group_by(manufacturer) %>%
  summarise(avg = mean((cty + hwy) / 2)) %>%
  arrange(desc(avg)) %>% head(5)




# 다음과 같이 연료별 가격이 정해져 있을 때, mpg에 fl_price라는 컬럼을 추가하세요.

table(mpg$fl)
names(table(mpg$fl))
dput(names(table(mpg$fl)))

fl_prices = cbind( data.frame(fl=c("c", "d", "e", "p", "r"), type=c("CNG", "diesel", "E85", "Premi", "Regular"), stringsAsFactors = F), 
               matrix(round(runif(5) + 0.5, 2), ncol=1, dimnames = list(NULL, "price")))
head(fl_prices)
mpg

class(fl_prices$fl)
class(mpg$fl)

inner_join(mpg, fl_prices, by=c('fl' = 'fl')) %>% select(price) -> fl_price
bind_cols(mpg, fl_price) -> mpg
head(mpg)


 