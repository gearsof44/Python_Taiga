from taiga import TaigaAPI

api = TaigaAPI(host='http://10.0.0.190:8000')

#Specifiez votre nom utilisateur taiga
username = 'gguillet'

#Authentification aupres de l'api
api.auth(
    username=username,
    password='secret'
)


def selectProject():
    #Selection du projet voulu
    name_projet = raw_input('Entrez le nom de votre projet : ')
    #Creation du nom de projet integral username-nom_projet
    name_my_project = """{username}-{nom_projet}""".format(username = username,nom_projet = nom_projet)
    my_project = api.projects.get_by_slug(name_my_project)
    return (my_project)

#Debug
#import pdb
#pdb.set_trace()

#Fonction permettant d'afficher les user_stories du projet selectionne
def affichage_list_user_story(nom_projet):
    user_stories = api.user_stories.list(project=nom_projet.id)
    return (user_stories)


def printDebugInfo():
    print(""""Liste de user story du projet '{nom_projet}' """.format(nom_projet=nom_projet))
    print(affichage_list_user_story(project))
    print(' ')

    ref = input('Entrez la ref de votre user story : ')
    refprint = """#{ref}""".format(ref=ref)
    print(' ')

    print("""Affichage sujet de la user story {ref} du projet '{nom_projet}' :""".format(ref=refprint,nom_projet = nom_projet))
    sujet = project.get_userstory_by_ref(ref).subject
    print (sujet)
    print(' ')


    print("""Affichage tags de la user story {ref} du projet '{nom_projet}' :""".format(ref=refprint,nom_projet = nom_projet))
    tag = project.get_userstory_by_ref(ref).tags
    print (tag)
    print(' ')

    print("""Affichage points de la user story {ref} du projet '{nom_projet}' :""".format(ref=refprint,nom_projet = nom_projet))
    points = project.get_userstory_by_ref(ref).points
    print (points)
    print(' ')

    print("""Affichage description de la user story {ref} du projet '{nom_projet}' :""".format(ref=refprint,nom_projet = nom_projet))
    description = project.get_userstory_by_ref(ref).description
    print (description)
    print(' ')

    # print('Ma user story : ')
    # print(affichageSelecDonnees(ref))
    # print(' ')

    #Ne fonctionne pas
    print('Test Points : ')
    test = project.get_userstory_by_ref(ref).to_dict()
    print(test)
    print(' ')

import unittest

def get_total_points(user_story, available_points):
    not_null_points = []
    for key, value in user_story.points.items():
        if value is not None:
            points_identifier = value
            for point in available_points:
                if point.id == points_identifier:
                    if point.value is not None:
                        not_null_points.append(point.value)
                    break


    #If we only have None values the sum should be None
    if not not_null_points:
        return 0

    return sum(not_null_points)

class PostIt():
    identifier = None
    tag = None
    title = None
    description = None
    total_points = None

    #Fonction retournant une chaine de caractere avec les infos necessaire d'une user story voulu
    #Post it constructore that uses the Taiga project and user story reference
    def __init__(self, user_story, total_points):
            #Recup des donnees hors ref car donnee en entree
        self.identifier = user_story.ref
        self.title = user_story.subject
        self.tag = user_story.tags
        self.total_points =  total_points
        self.description = user_story.description
        #Construction d'un resultat lisible en print
        # ma_user_story = """Ref : #{ref} ; Sujet : {sujet}; Description : {description}; Points : {points}
        # """.format(ref = ref,sujet = sujet,description = description, points = points)


class ClassTest(unittest.TestCase):

    def whenICreateAProject(self):
        testprojet = api.projects.create('TEST PROJECT', 'TESTING API')
        return testprojet

    def whenIAddAUserStory(self, project):
        user_story = project.add_user_story(
            'New Story', description='Blablablabla'
        )
        user_story.tags = 'Dev'
        import ipdb; ipdb.set_trace()
        return user_story

    def whenIListPoints(self, project):
        return self.project.list_points()

    def setUp(self):
        """Initialisation des tests"""
        self.project = self.whenICreateAProject()

    def tear_down(self):
        self.project.delete()

    def test_create_project(self):
        self.assertIsNotNone(self.project)

    def test_create_user_story(self):
        user_story = self.whenIAddAUserStory(self.project)
        self.assertIsNotNone(user_story)

    def test_affichage_list_user_story(self):
        user_story = self.whenIAddAUserStory(self.project)
        list_user_stories = affichage_list_user_story(self.project)
        self.assertTrue(list_user_stories.count > 0)

    def test_create_post_it(self):
        user_story = self.whenIAddAUserStory(self.project)
        available_points = self.whenIListPoints(self.project)
        # for point_id in user_story.points:
        #     list_of_points
        total_points = get_total_points(user_story, available_points)
        result = PostIt(user_story, total_points)
        self.assertIsNotNone(result)

    def test_create_post_it_existant(self):
        my_project = api.projects.get_by_slug('gguillet-monprojettestperso')
        user_story = my_project.get_userstory_by_ref(1)
        available_points = my_project.list_points()
        # for point_id in user_story.points:
        #     list_of_points
        total_points = get_total_points(user_story, available_points)
        result = PostIt(user_story, total_points)
        self.assertIsNotNone(result)

    def test_list_points(self):
        available_points = self.whenIListPoints(self.project)
        self.assertTrue(available_points.count > 0)

        for p in available_points:
            print p.value


unittest.main()
