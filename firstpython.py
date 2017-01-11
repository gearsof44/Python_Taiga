# coding: utf-8

from taiga import TaigaAPI

api = TaigaAPI()

api.auth(
    username='admin',
    password='123123'
)

new_project = api.projects.get_by_slug('admin-projettest3')

stories = api.user_stories.list()

# print (stories)

projects = api.projects.list()

sortie = new_project.get_userstory_by_ref(14)

print(sortie)
