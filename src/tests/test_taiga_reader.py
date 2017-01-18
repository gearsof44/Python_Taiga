import TaigaReader
from src.models.PostIt import PostIt
import unittest


class TaigaReaderClassTest(unittest.TestCase):

    #Create a project for the test
    def whenICreateAProject(self):
        testprojet = TaigaReader.api.projects.create('TEST PROJECT', 'TESTING API')
        return testprojet

    #Create a User Story
    def whenIAddAUserStory(self, project, all_roles, point):
        #Add the test user_story to the test project
        user_story = project.add_user_story(
            'New Story', description='Blablablabla'
        )
        #Add a tag to the test user_story
        user_story.tags = ['testjaune', '#fce94f']
        #Create a points dictionnary
        points = {}
        for i in all_roles:
            #Filling the points dictionnary
            points["{0}".format(i.id)] = point.id

        user_story.points = points
        #Pushing the updated infos to the db
        user_story.update()
        #returning an user_story object
        return user_story

        #Return the list of points of the current test project
    def whenIListPoints(self, project):
        return self.project.list_points()

        #Return the list of roles of the current test project
    def whenIListRoles(self,project):
        sort = self.project.list_roles()
        #Create a table which will contain the roles that are computable
        valuable = []
        for i in sort:
            if i.computable == True:
                valuable.append(i)
        return valuable

    def setUp(self):
        """Initialisation des tests"""
        self.project = self.whenICreateAProject()

    def tear_down(self):
        self.project.delete()

        #Test that verify that we could create a project
    def test_create_project(self):
        self.assertIsNotNone(self.project)

        #Test that verify that we could create a user_story
    def test_create_user_story(self):
        all_roles = self.whenIListRoles(self.project)
        available_points = self.whenIListPoints(self.project)
        #Select a define point from the begining it's easier for the test
        user_story = self.whenIAddAUserStory(self.project, all_roles, available_points[1])
        self.assertIsNotNone(user_story)

        #Test that verify that we could recover the list of user_stories
    def test_get_list_user_story(self):
        all_roles = self.whenIListRoles(self.project)
        available_points = self.whenIListPoints(self.project)
        #Select a define point from the begining it's easier for the test
        user_story = self.whenIAddAUserStory(self.project, all_roles, available_points[1])
        list_user_stories = TaigaReader.get_list_user_story(self.project)
        self.assertTrue(list_user_stories.count > 0)

        #Test to check that's possible to create a PostIt object
    def test_create_post_it(self):
        all_roles = self.whenIListRoles(self.project)
        available_points = self.whenIListPoints(self.project)
        #Select a define point from the begining it's easier for the test
        user_story = self.whenIAddAUserStory(self.project, all_roles, available_points[1])
        # for point_id in user_story.points:
        #     list_of_points
        total_points = TaigaReader.get_total_points(user_story, available_points)
        result = Model_PostIt.PostIt(user_story, total_points)
        self.assertIsNotNone(result)

        #Check that we can recover the different points from a project
    def test_list_points(self):
        available_points = self.whenIListPoints(self.project)
        self.assertTrue(available_points.count > 0)

    def testCountUS(self):
        all_roles = self.whenIListRoles(self.project)
        available_points = self.whenIListPoints(self.project)
        #Select a define point from the begining it's easier for the test
        user_story = self.whenIAddAUserStory(self.project, all_roles, available_points[1])
        list_user_stories = TaigaReader.get_list_user_story(self.project)
        numberofUS = TaigaReader.return_postit_number(list_user_stories)
        self.assertIsNotNone(numberofUS)


unittest.main()
