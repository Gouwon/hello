# 한글 깨질 때.
theme_set(theme_gray(base_family="AppleGothic"))
par(family = "AppleGothic")

plot(x = smdt$stuno, y = smdt$Korean,
     col = '#0000FF',
     cex = 3,
     las= 1,
     type = 'p',         # p, l, b, c, o, s
     xlim = c(0, 5.5),
     ylim = c(50, 100),
     pch = 18,                         # > ?points
     xlab = '학번', ylab = '국어',
     main = '그래프 타이틀')
?plot

colnames(smdt)
xl = c(0, 8); yl = c(40, 100)
plot(x = smdt$stuno, y = smdt$Korean,
     col='#0000FF', cex=3, pch = 8, ## col => RGB (2자리2자리2자리)
     xlim = xl, ylim = yl,
     xlab = '학번', ylab = '국어, 수학',las= 1,
     main = '우리반 국어 / 수학 성적')
par(new = T)
plot(x = smdt$stuno, y = smdt$Math,
       col='#ff0000', cex=3, pch = 21,
       xlim = xl, ylim = yl, las= 1,
       xlab = '', ylab = '')
legend('bottomright',      # center, top & bottom, left & rigth
       legend=c('국어', '수학'),
       pch=c(8, 21), col=c('blue', 'red'), bg='gray')

par(new = F)

prePar = par(new = F)


library('dplyr')

t = data %>% filter(eng > 90) %>% select('cls') %>% table
barplot(t,
          beside = T,
          border = 'dark blue',
          density = 30,
          angle = 15 + 10*1:2,
          xlab = '학급별 성별', ylab = '영어', las = 1,
          legend=rownames(t),
          col=heat.colors(nrow(t)))

par(new = T)

t = data %>% filter(eng > 90 & gen == '여') %>% select('cls') %>% table
barplot(t,
        beside = T,
        border = 'dark blue',
        density = 30,
        angle = 15 + 10*1:2,
        ylim = c(0 : 20),
        xlab = '학급별 성별', ylab = '영어', las = 1,
        legend=rownames(t),
        col=heat.colors(nrow(t)))
