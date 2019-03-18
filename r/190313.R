library('dplyr')
library('ggplot2')

theme_set(theme_gray(base_family="AppleGothic"))
par(family = "AppleGothic")

d = data %>% filter(stuno >= 30000)

ggplot() +
  geom_point(data=d,
             aes(x=stuno, y=kor),
             color='blue', size = 5, alpha=0.3)

ggplot(d, aes(cls, kor)) +
  geom_point(aes(color=cls, size=kor), 
             alpha=0.3)

ggplot(d, aes(cls, kor)) +
  geom_point(alpha=0.3)

ggplot(d, aes(cls, kor)) +
  geom_point(aes(size=kor), 
             alpha=0.3)

mpg = as.data.frame(ggplot2::mpg)
d2 = mpg %>% group_by(manufacturer, displ) %>% 
  summarise(m1 = mean(cty), m2 = mean(hwy))

g1 = ggplot(d2, aes(x=displ), las=1) + 
  geom_line(aes(y=m1, color='cty')) + 
  geom_line(aes(y=m2, color='hwy'), size=1) +
  scale_colour_manual("", breaks = c("cty", "hwy"),
                      values = c("red", "blue")) +
  xlab("x축") +
  xlim(1, 8) +
  scale_y_continuous("y축", limits = c(5, 45)) +
  labs(title = '타이틀', subtitle = '서브 타이틀')



g2 = ggplot(mpg, aes(manufacturer)) +
  geom_bar(aes(fill=class),
           width = 0.5) +
  theme(axis.text.x = element_text(angle=45,       # 글씨의 기울기
                                   vjust=0.6)) +   # 글씨의 하단 맞춤(띄우기)
  scale_fill_discrete(name = "class") +      # legend
  labs(title = 'Title', subtitle = 'Sub Title', fill='class1')
# scale_fill_discrete이 labs보다 나중에 적용된다.
?element_text
?theme

ggplot(mpg, aes(cty)) +
  geom_density(aes(fill=factor(cyl)), alpha=0.8) +
  scale_fill_discrete(name = "class")  +
  labs(title="밀도그래프", subtitle = "실린더수에 따른 시내연비의 밀도그래프",
       caption="Source: ggplot2::mpg",
       x = "도시 연비",
       y = "분포",
       fill = "실린더수")


install.packages('gridExtra')
library(gridExtra)
g3 = ggplot(mpg, aes(manufacturer)) +
  geom_bar(aes(fill=class),
           width = 0.7) +
  theme(axis.text.x = element_text(angle=45,
                                   vjust=0.6)) +
  labs(title = 'Title', subtitle = 'Sub Title')
g4 = ggplot(mpg, aes(cty)) +
  geom_density(aes(fill=factor(cyl)), alpha=0.8) +
  labs(title="밀도그래프", subtitle = "실린더수에 따른 시내연비의 밀도그래프",
       caption="Source: ggplot2::mpg",
       x = "도시 연비",
       fill = "실린더수")
grid.arrange(g4, g3, ncol=2)
g = grid.arrange(g1, g2, ncol=2)
grid.arrange(g3, g, ncol=1)


# mpg데이터에서 연도별 배기량에 따른 통합연비를 꺽은선으로 그리시오. (단, 2008년은 굵은 선으로 표현하시오)
library('dplyr')
library('ggplot2')
head(mpg)

ggplot(data=mpg, aes(x=displ)) +
  geom_line(data=distinct(mpg %>% filter(year=='1999') %>% group_by(displ) %>% summarise(cty = mean(cty))), aes(y=cty, color='1999 cty')) +
  geom_line(data=distinct(mpg %>% filter(year=='1999') %>% group_by(displ) %>% summarise(hwy = mean(hwy))), aes(y=hwy, color='1999 hwy')) +
  geom_line(data=distinct(mpg %>% filter(year=='2008') %>% group_by(displ) %>% summarise(cty = mean(cty))), aes(y=cty, color='2008 cty'), size=1) +
  geom_line(data=distinct(mpg %>% filter(year=='2008') %>% group_by(displ) %>% summarise(hwy = mean(hwy))), aes(y=hwy, color='2008 hwy'), size=1) +
  scale_x_continuous("배기량(cc)") +
  scale_y_continuous("연비(M/h)", limits = c(0, 50)) + 
  scale_colour_manual("", breaks = c("1999 cty", "1999 hwy", '2008 cty', '2008 hwy'),
                      values = c('red', 'yellow', 'blue', 'lightblue')) +
  labs(title="연도별 연비", subtitle = "굵은선은 2008년")

  

# data(성적.csv) 데이터에서 국어 성적이 80점 이상인 학생들의 수를 성비가 보이도록 학급별로 막대그래프를 그리시오.

head(data)

ggplot(data %>% filter(kor >= 80) %>% select(cls, gen), aes(cls)) +
  geom_bar(aes(fill=gen),
           width = 0.7) +
  theme(axis.text.x = element_text(angle=45,       # 글씨의 기울기
                                   vjust=0.6)) +   # 글씨의 하단 맞춤(띄우기)
  scale_fill_discrete(name = "성별") +      # legend
  labs(title = '국어 우수 학생', subtitle = '(80점 이상)', x='학급', y='학생수')

save(data, file = 'data/data_eng.rda')


# 국어 성적이 95점 이상인 학생들의 점수별 밀도그래프를 그리시오.

head(data)

ggplot(data %>% filter(kor >= 95), aes(kor)) +
  geom_density(aes(fill=factor(cls)), alpha=0.5) +
  labs(title="반별 국어 우수 성적", subtitle = "(국어 성적 A+)",
       caption="기준 점수 >= 95",
       x = "성적",
       y = '밀도',
       fill = "학급")


# midwest데이터에서 전체인구와 아시아계 인구의 관계를 알아보기 위한 그래프를 그리시오. (단, 전체인구는 50만명 이하, 아시아계인구는 1만명 이하만 표시되게)

head(midwest)
colnames(midwest)

d = midwest %>% filter(poptotal <= 500000 & popasian <= 10000)

ggplot(d, aes(popasian, poptotal)) +
  geom_point( alpha=0.3) +
  labs(title='카운티별전체인구와 아시아계 인구의 관계', 
       subtitle = '(중서부 5개 주를 대상으로)',
       x='아시아계 인구', y='카운티별 전체인구') -> g1

ggplot(d, aes(popdensity, percasian)) +
  geom_point(alpha=0.3) +
  labs(title='카운티별인구밀도와 아시아계 인구 비중의 관계', 
       subtitle = '(중서부 5개 주를 대상으로)',
       x='아시아계 인구비중', y='카운티별 전체인구밀도') -> g2

ggplot(d, aes(popasian)) +
  geom_histogram(alpha=0.3, bins=20) +
  labs(title='아시아계 인구에 따른 카운티 분포', 
       subtitle = '(중서부 5개 주를 대상으로)',
       x='아시아계 인구비중', y='카운티 수') -> g3

g4 = grid.arrange(g1, g2, ncol=2)
grid.arrange(g3, g4, nrow=2)