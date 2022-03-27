# HooHacks 2022

# Simulating March Madness, predicting the winner 

    
# simulation initial plan 
    # lists of diff regions, determine winners 
    # another fxn for final four
    # break rounds up into chunks maybe 
    # use points as response variable to predict winner of games 
    # 64, 32, 16, 8, 4, 2, 1
    
# data 
    # team season stats
    # other non game stats 
        # conference reg season, tourny champs
        # seeding position 
        # conference strength

import pandas as pd 

nba_team_stats = pd.read_csv('nba_team_stats.csv')
nba_adv_stats = pd.read_csv('nba_adv_stats.csv')

nba_adv_stats.columns = nba_adv_stats.iloc[0]
nba_adv2 = nba_adv_stats.loc[1:30,'Team':'Attend./G']
nba_team2 = nba_team_stats.loc[0:29,'Team':'PTS']

nba_team2.to_csv('nbastats2.csv')

nbadat = pd.merge(nba_adv2, nba_team2, on='Team')

del nbadat['Attend.']
del nbadat['Arena']
del nbadat['G']


attend1 = nbadat['Attend./G'].str[:2]
attend2 = nbadat['Attend./G'].str[3:]
attend_tot = (attend1+attend2).astype(float)

del nbadat['Attend./G']
nbadat['Attend per Game'] = attend_tot
del nbadat['FT/FGA']

team = nbadat['Team']
del nbadat['Team']

nbadat2 = nbadat.astype(float)

nbadat2['Team'] = team 
                  

nbadat2.to_csv('nba_ovr_stats.csv')


nbadat2.columns
# model 

"""Coefficients:
              Estimate Std. Error t value Pr(>|t|)    
(Intercept) -41.638194  10.015361  -4.157 0.001125 ** 
MP           -0.021608   0.011145  -1.939 0.074544 .  
FGA           0.444643   0.122761   3.622 0.003099 ** 
FG.          61.370820  20.504484   2.993 0.010377 *  
X3P           1.528445   0.297205   5.143 0.000189 ***
X3P.          8.676025   7.550408   1.149 0.271226    
X2P           0.906622   0.337368   2.687 0.018638 *  
X2PA         -0.151111   0.077499  -1.950 0.073097 .  
FTA           0.772466   0.009443  81.805  < 2e-16 ***
FT.          22.768362   0.457825  49.732 3.22e-16 ***
ORB          -0.619125   0.278084  -2.226 0.044294 *  
DRB          -0.661647   0.285557  -2.317 0.037455 *  
TRB           0.628026   0.278773   2.253 0.042187 *  
AST           0.015954   0.009374   1.702 0.112553    
TOV          -0.026812   0.012249  -2.189 0.047457 *  
PF           -0.025056   0.012768  -1.962 0.071491 .  
FG            0.426828   0.276140   1.546 0.146168 """

# MP, FGA, FGPerc, X3P, X3PPerc, X2P, X2PA, FTA, FTPerc, ORB, DRB, TRB, AST, TOV, PF, FG

def teamscore(list1):
    score = -41.638194 - 0.021608(list1[0]) + 0.444643(list1[1]) + 61.370820(list1[2]) + 1.528445(list1[3]) + 8.676025(list1[4]) + 0.906622(list1[5]) - 0.151111(list1[6]) + 0.772466(list1[7]) + 22.768362(list1[8]) - 0.619125(list1[9]) - 0.661647(list1[10]) + 0.628026(list1[11]) + 0.015954(list1[12]) - 0.026812(list1[13]) - 0.025056(list1[14]) + 0.426828(list1[15]) 
    return score

# Take this and put in nums for reg season games for matchups now 

# If playoffs started now 

# West 

# 1 - Suns 
suns = [240, 96, .375, 7, .241, 29, 67, 19, .842, 13, 28, 41, 22, 10, 23, 36]
team1score(suns)
# 8 - Clips 

# 4 - Jazz 
# 5 - Mavs 


# 2 - Griz 
# 7 - T-wolves 

# 3 - warriors 
# 6 - nuggets 

# East 

# 1 - Heat 
# 8 - Nets 

# 4 - celtics 
# 5 - bulls 



# 2 - sixers 
# 7 - raptors 

# 3 - bucks 
# 6 - cavs 

























