
#Cria uma lista vazia para preencher com aliens
aliens=[]
for alien_number in range(30):
    news_aliens = {'color':'green','points':5,'speed':'slow'}
    aliens.append(news_aliens)
for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=20
       
        if alien['color']=='yellow':
            alien['color']='red'
            alien['speed']='fast'
            alien['points']=200
for alien in aliens[0:5]:
    print(alien)