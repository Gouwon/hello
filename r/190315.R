theme_set(theme_gray(base_family="AppleGothic"))
par(family = "AppleGothic")
library(ggplot2)
library(dplyr)

head(USArrests)    # 미국 범죄율 1973 (R 내장 데이터)    cf. USAccDeaths
str(USArrests)   
rownames(USArrests)

library(tibble)    # install.packages('dplyr')
chodata = rownames_to_column(USArrests, var = 'state') # chodata = data.frame(state = tolower(rownames(USArrests)), USArrests)

chodata$state = tolower(chodata$state)

install.packages('ggiraphExtra')
install.packages('maps')

install.packages('mapproj')
library(ggiraphExtra)
usmap = map_data('state') 
head(usmap)

remove.packages(ggiraphExtra)

.libPaths()
# /private/var/folders/nc/k4tw9wpd08751sw98_7508y80000gn/T/RtmpjW3w4h/downloaded_packages

ggChoropleth(data=chodata,
             aes(fill=Murder, map_id=state),
             map = usmap,
             title = '..',
             reverse = F,
             interactive = T)

ggplot(chodata, aes(map_id = state)) + 
  geom_map(aes(fill = Murder), map = usmap) + 
  expand_limits(x = usmap$long, y = usmap$lat) +
  scale_fill_gradient2('살인', high='red') +
  labs(title="USA Murder", fill = '살인')
??tooltip

tooltips = paste0(
  sprintf("<p><strong>%s</strong></p>", as.character(chodata$state)),
  '<table>',
  '  <tr>',
  '    <td>인구(만)</td>',
  sprintf('<td>%.0f</td>', chodata$UrbanPop * 10),
  '  </tr>',
  '  <tr>',
  '    <td>살인</td>',
  sprintf('<td>%.0f</td>', chodata$Murder),
  '  </tr>',
  '  <tr>',
  '    <td>폭력</td>',
  sprintf('<td>%.0f</td>', chodata$Assault),
  '  </tr>',
  '</table>' )

tooltips = sprintf("alert(\"%s\")", as.character(chodata$state))
onclick = sprintf("alert(\"%s\")", as.character(chodata$state))

library(ggiraph)

ggplot(chodata, aes(data = Murder, map_id = state)) +
  geom_map_interactive( 
    aes(fill = Murder,
        data_id = state,
        tooltip = tooltips,
        onclick = onclick), 
    map = usmap) +
  expand_limits(x = usmap$long, y = usmap$lat) +
  scale_fill_gradient2('살인', high = "black", mid="blue") +
  labs(title="USA Murder") -> gg_map

ggiraph(code = print(gg_map))
?ggiraph
girafe(ggobj = gg_map)

install.packages("stringi")
library("stringi")
tootip = stringi::stri_enc_toutf8(tooltips)

install.packages('devtools')
library("devtools")

devtools::install_github("cardiomoon/kormaps2014")
library(kormaps2014)

kormaps2014::korpop1 -> kdata
kormaps2014::changeCode(korpop1) -> kdata # for windows
head(kdata)

colnames(kdata)
library(dplyr)
kdata = kdata %>% rename(pop = 총인구_명)
kdata = kdata %>% rename(area = 행정구역별_읍면동)

ggChoropleth(data=kdata, 
             aes(fill = pop, map_id = code, tooltip = area),
             map = kormap1,
             interactive = T)

ggplot(kdata, aes(data = pop, map_id = code)) +
  geom_map( aes(fill = pop), map = kormap1) + 
  expand_limits(x = kormap1$long, y = kormap1$lat) +
  scale_fill_gradient2('인구', low='darkblue') +
  xlab('경도') + ylab('위도') + 
  labs(title="시도별 인구")

head(kdata)

install.packages('plotly')
library(plotly)

t = ggplot(data, aes(eng, kor)) +
  geom_point(aes(color=eng, size=kor), alpha=0.3)

ggplotly(t)

ggplot(data=mpg, aes(x=displ)) +
  geom_line(data=distinct(mpg %>% filter(year=='1999') %>% group_by(displ) %>% summarise(cty = mean(cty))), aes(y=cty, color='1999 cty')) +
  geom_line(data=distinct(mpg %>% filter(year=='1999') %>% group_by(displ) %>% summarise(hwy = mean(hwy))), aes(y=hwy, color='1999 hwy')) +
  geom_line(data=distinct(mpg %>% filter(year=='2008') %>% group_by(displ) %>% summarise(cty = mean(cty))), aes(y=cty, color='2008 cty'), size=1) +
  geom_line(data=distinct(mpg %>% filter(year=='2008') %>% group_by(displ) %>% summarise(hwy = mean(hwy))), aes(y=hwy, color='2008 hwy'), size=1) +
  scale_x_continuous("배기량(cc)") +
  scale_y_continuous("연비(M/h)", limits = c(0, 50)) + 
  scale_colour_manual("", breaks = c("1999 cty", "1999 hwy", '2008 cty', '2008 hwy'),
                      values = c('red', 'yellow', 'blue', 'lightblue')) +
  labs(title="연도별 연비", subtitle = "굵은선은 2008년") -> g5
ggplotly(g5)


install.packages('dygraphs')
library(dygraphs)


?economics

head(economics)
ue = xts(economics$unemploy, order.by = economics$date)
head(ue)
dygraph(ue)
dygraph(ue) %>% dyRangeSelector()

psave = xts(economics$psavert, order.by = economics$date)
head(psave)

ue2 = xts(economics$unemploy / 1000, order.by = economics$date)
pu = cbind(ue2, psave)
colnames(pu) = c('unemployment', 'saverate')
dygraph(pu) %>% dyRangeSelector()


# 다음과 같이 미국의 범죄율을 한번에 작도하시오.
chodata = rownames_to_column(USArrests, var = 'state')
chodata$state = tolower(chodata$state)
head(chodata)
colnames(chodata)
ggChoropleth(data=chodata,
             aes(fill=c(Murder,Assault, UrbanPop, Rape), map_id=state),
             map = usmap,
             reverse = F,
             interactive = T)
  

# 미국 범죄율의 Rape부분을 단계 구분도로 작성하시오.(단, 툴팁은 그림과 같이 표현하고,   클릭시 해당 state의 wikipedia 페이지를 보이도록 HTML로 저장하시오)

ggplot(chodata, aes(map_id = state)) + 
  geom_map(aes(fill = Murder), map = usmap) + 
  expand_limits(x = usmap$long, y = usmap$lat) +
  labs(title="USA Murder", fill = 'Rape')
library(stringi)

chodata[chodata$state=='wisconsin', ]
tooltips = paste0(
  sprintf("<p><strong>%s</strong></p>", as.character(chodata$state)),
  sprintf("<p><strong>%s</strong> / %s 만</p>", round(chodata$Rape), round(chodata$UrbanPop) * 10)) 

onclick = paste0('location.href=', sprintf('"http://en.wikipedia.org/wiki/%s"', as.character(chodata$state)))
library(ggiraph)


ggplot(chodata, aes(map_id = state)) +
geom_map_interactive( 
  aes(fill = Rape,
      data_id = state,
      tooltip = tooltips,
      onclick = onclick), 
  map = usmap) +
  expand_limits(x = usmap$long, y = usmap$lat) +
  scale_fill_gradient2('Rape', high = "blue", mid = "green") +
  labs(title="USA Murder") -> gg_map

ggiraph(code = print(gg_map))
girafe(ggobj = gg_map)


# 시도별 결핵환자수(kormaps::tbc)를 단계 구분도로 작성하시오.(우리나라) (단, 환자수는 2006년부터 2015년 통합, NA인 지역은 0으로 표시할 것)

library(kormaps2014)
kdata1 = kormaps2014::tbc
colnames(kdata1)
kdata1 = kdata1 %>% filter(year %in% c(2006:2015)) %>% group_by(name) %>% summarise(NewPts = sum(NewPts),code = mean(code))
str(kdata1)
kdata1$NewPts = ifelse(is.na(kdata1$NewPts), 0, kdata1$NewPts)

ggChoropleth(data=kdata1, 
             aes(fill = NewPts, 
                 map_id = code, 
                 tooltip = area),
             map = kormap1)

ggplot(kdata1, aes(data=NewPts, map_id = code)) +
  geom_map( aes(fill = NewPts), map = kormap1) + 
  expand_limits(x = kormap1$long, y = kormap1$lat) +
  scale_fill_gradient2('NewPts', high='red')
