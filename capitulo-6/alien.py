# alien_0={'color':'green', 'points': 12}
# alien_0['x_position']= 0
# alien_0['y_position']= 25
# new_points= alien_0['points']=4
# print(alien_0)
# print(f'Seu novo ponto é: {new_points}')

# alien={}
# print(f'aqui não tem dados {alien}')
# alien['speed']='mediu'
# alien['color']='green'
# alien['points']=10
# alien['x_position'] = 0
# del alien['points']


# if alien['speed']=='slow':
#     x_increment = 1
# elif alien['speed']=='medium':
#     x_increment = 2
# else:
#     x_increment = 5
# alien['x_position'] = alien['x_position'] + x_increment

# print(f'aqui não tem dados {alien}')


# print(alien.get('v_position', 'No find this documents'))
friends={
    'jose':'C#',
    'carlos':'python',
    'antonio':'JS',
    'bruno':'java',
    'patricia':'C',
}
select_friends=['jose','carlos','patricia']
for name in sorted(friends.keys()):
    print(f'{name}')
    
    if name in select_friends:
        
        language_liked = friends[name].upper()
        print(name, language_liked)
        
    if 'patricia' not in friends:
        print('Patricia take our poll!')    

        



