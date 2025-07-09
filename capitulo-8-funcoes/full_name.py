def get_full_name(first_name:str='', Last_name:str=''):
   
    full_name = f'{first_name} {Last_name} '
    
    if not isinstance(first_name,str) or not isinstance(Last_name,str):
        
        return 'Dados incorretos! Digite apenas letras'
      
    if full_name.strip():
        
        return full_name.strip()
    
    print('não tem nada para exibir!')
full_name_user = get_full_name()


    
def old ( age, color, heigth):
    
  
    full_datas = f'{age} {color} {heigth}'
    
    return full_datas
age_height = old(23,'black',1.78)

print('Nome completo: ',full_name_user,'\n Informações: ',age_height)
        
 
   
      
    

