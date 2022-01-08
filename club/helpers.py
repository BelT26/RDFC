available_players = []
blues = []
whites = []

def book_match_place(player):
    if len(available_players) < 12:
        player['is_in_team'] = True
        available_players.append(player)
        print('Your place on the team has been booked')
        
    else:
        reserves.append(player)
        print('Unfortunately there is no room on the team')
        print(f'You are number {len(reserves)} on the reserve list')


def get_score(player):
    return player['points']


def get_matches_played(player):
    return player['played']


def sort_players(members):
    scored_members = sorted(members, key=get_score)
    sorted_members = sorted(scored_members, key=get_matches_played)
    return sorted_members


def clear_teams():
    blues.clear()
    whites.clear()



def allocate_teams_again(request):
    clear_teams()
    available_members = Members.objects.filter(is_in_team=True)
    scored_players = available_members.order_by('-score')
    sorted_players = scored_players.order_by('played')
    blues.append(sorted_players[0], sorted_players[3], sorted_players[5], sorted_players[7], sorted_players[9], sorted_players[11]) 
    whites.append(sorted_players[1], sorted_players[2], sorted_players[4], sorted_players[6], sorted_players[8], sorted_players[10])




def add_result(blue_goals, white_goals, match):
    match['blue_goals'] = blue_goals
    match['white_goals'] = white_goals
    if blue_goals > white_goals:
        for player in blues:
            player['points'] += 3
    elif white_goals > blue_goals
        for player in whites:
            player['points'] += 3
    else:
        for player in blues:
            player['points'] += 1
        for player in whites:
            player['points'] += 1
    available_players.clear()




