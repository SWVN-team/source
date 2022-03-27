
library(dplyr)


nba2<-read.csv("C:\\Users\\Student\\Documents\\UVA\\Other\\HooHacks\\nbastats2.csv")
View(nba2)
nba3<-nba2[,-(1:3)]
View(nba3)
#nba4<-nba3[,-2]
#View(nba4)
#nba5<-nba4[,-10]
#View(nba5)

nba_model<-lm(PTS~., nba3)
summary(nba_model)

#nba_model2<-lm(PTS~ Age+PW+PL+MOV+SOS+SRS+SRS+ORtg+DRtg+Pace+FTr+X3PAr+TS.+eFG.+TOV.+ORB.+eFG..1  +TOV..1+DRB.+MP+FG+FGA+FG.+X3P+X3PA+X3P.+X2P+X2PA+X2P.+FT, nbastats3)
#summary(nba_model2)

library(MASS)


AIC_NBA<-stepAIC(nba_model, direction = "both", trace = F)
summary(AIC_NBA)

# newdat1<-data.frame(MP=241.3,FGA=91.1,FG.=.455,X3P=14.7,X3PA=41.5,X3P.=.355,X2P=26.7,X2PA=49.6,X2P.=.538)

# predict(nba_model,newdat1,interval = "predict")

detach("package:MASS")
