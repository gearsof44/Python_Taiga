from taiga import TaigaAPI
from src.models import Model_PostIt

api = TaigaAPI(host='http://10.0.0.190:8000')

#Specify your taiga username
username = 'gguillet'

#Authentificate to the api
api.auth(
    username=username,
    password='secret'
)

#Function which permit to the user to select a project thanks to the project-name
def selectProject():
    #Selection of the wanted project
    project_name = raw_input('Entrez le nom de votre projet : ')
    #Creation of the complete project name format username-projectname
    my_project_name = """{username}-{nom_projet}""".format(username = username,nom_projet = project_name)
    #Get the project corresponding to the given name
    my_project = api.projects.get_by_slug(my_project_name)
    return (my_project)

#Function that allow to select all user_story from the selected project
def get_list_user_story(project_name):
    #Get all the user_story from a given project
    list_user_stories = api.user_stories.list(project=project_name.id)
    #Return the list of user_story corresponding to the given project
    return (list_user_stories)

def select_a_user_story(project_name):
    identifier = raw_input('Entrez le numero de votre User Story : ')
    my_user_story = project_name.get_userstory_by_ref(identifier)
    return (my_user_story)

#Function which permit to sum and return the total of all the points of one user_story
def get_total_points(user_story, available_points):
    #Create a table in order to stock all valuable point
    not_null_points = []

    #Browsing in the dictionnary of points of one user_story
    for key, value in user_story.points.items():
        #if the point have a value then
        if value is not None:
            points_identifier = value
            #foreach point of the user_story
            for point in available_points:
                if point.id == points_identifier:
                    #If the point have a value different from ?
                    if point.value is not None:
                        #Adding this value in the table
                        not_null_points.append(point.value)
                    break


    #If we only have None values the sum should be None
    if not not_null_points:
        return 0
        #return the total of all points that are not none
    return sum(not_null_points)

def create_Post_it(a_user_story,total_points):
    Model_PostIt.PostIt(user_story, total_points)

def return_postit_number(list_US):
    us_number = list_US.count()
    return us_number
