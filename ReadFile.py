f_obj = open('nba_all.csv', "r")
header = 'gameorder,game_id,lg_id,_iscopy,year_id,date_game,seasongame,is_playoffs,team_id,fran_id,pts,elo_i,elo_n,win_equiv,opp_id,opp_fran,opp_pts,opp_elo_i,opp_elo_n,game_location,game_result,forecast,notes'
content = f_obj.readline().strip("\n")
print(content == header)
f_obj.close()
