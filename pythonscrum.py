from taiga import TaigaAPI

api = TaigaAPI(
    host='http://10.0.0.190:8000/api/v1/'
)

api.auth(
    username='admin',
    password='123123'
)

#Selection du projet voulu
new_project = api.projects.get_by_slug('admin-projettest3')

#import pdb
#pdb.set_trace()

#Stockage dans une variable des users story (global)
stories = api.user_stories.list(project=new_project.id)

print('Liste de user story de tout les projets :')
print(stories)
print(' ')

print('Affichage sujet de ma user story du projet projettest3 ref 23 :')
print (new_project.get_userstory_by_ref(23).subject)
print(' ')


print('Affichage tags de ma user story du projet projettest3 ref 23 :')
print (new_project.get_userstory_by_ref(23).tags)
print(' ')

print('Affichage points de ma user story du projet projettest3 ref 23 :')
print (new_project.get_userstory_by_ref(23).points)
print(' ')

print('Affichage description de ma user story du projet projettest3 ref 23 :')
print (new_project.get_userstory_by_ref(23).description)
print(' ')
