class PostIt():
    identifier = None
    tag = None
    title = None
    description = None
    total_points = None

    #Fonction retournant une chaine de caractere avec les infos necessaire d'une user story voulu
    #Post it constructor that uses the Taiga project and user story reference
    def __init__(self, user_story, total_points):

        self.identifier = user_story.ref
        self.title = user_story.subject
        self.tag = user_story.tags
        self.total_points =  total_points
        self.description = user_story.description
