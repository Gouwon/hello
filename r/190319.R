install.packages('sqldf')
library(sqldf)

head(data)
data %>% filter(drv == f)
sqldf("select * from data where drv = 'f'")

install.packages('RMySQL')
library(RMySQL)

drv = dbDriver("MySQL")
conn = dbConnect(drv, host='127.0.0.1', port=3306, dbname='dooodb', user='dooo', password='root1!')
dbSendQuery(conn, 'set character set utf8')

dbGetQuery(conn, "select * from Song limit 5")

tryCatch({
  dbBegin(conn)
  dbGetQuery(conn, "update Song set title='24/7/1인듯' where songId = '31399728'")
  dbCommit(conn)
},
error = function(e) { 
  dbRollback(conn)
  print(paste("Error!!", e)) 
},
warning = function(w) {
  print(paste("Warining!!", w))
},
finally = { print("FFFFFFFFFFFF")}  )

dbDisconnect(conn); 
dbUnloadDriver(dbDriver("MySQL"))


# 멜론 탑 100 곡들의 장르와 랭킹간의 관계를 산점도로 작도하시오.

library(RMySQL)

drv = dbDriver("MySQL")
conn = dbConnect(drv, host='127.0.0.1', port=3306, dbname='dooodb', user='dooo', password='root1!')
dbSendQuery(conn, 'set character set utf8')

dbGetQuery(conn, "select s.title, s.genre, sr.* from (select rank, songId from SongRank limit 98) sr inner join Song s on sr.songId = s.songId") -> d1
d1$rankPoint = c(98:1)
ggplot() +
  geom_point(data=d1,
             aes(x=genre, y=rankPoint),
             color='blue', size = 5, alpha = 0.3) +
  theme(axis.text.x = element_text(angle=45,
                                   vjust=0.6)) 

dbDisconnect(conn); 
dbUnloadDriver(dbDriver("MySQL"))