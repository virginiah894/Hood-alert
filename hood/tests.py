from django.test import TestCase
from django.test import TestCase
from .models import Profile,Hood,updates,Businesses,Medicalservices,HealthServices,Adminstration,Post,Comments

from django.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    '''
    Test case for the Profile class and it's behaviours
    '''
    def setUp(self):
        '''
        Method that will run before any test case under this class
        '''
        self.new_user = User(username = "bilal", email = "bilal@gmail.com", password = "dontbelittleyourself",)
        self.new_user.save()

        self.new_neigh = hood(hood_name = "syoks")
        self.new_neigh.save()

        self.new_profile = Profile(username = self.new_user, hood = self.new_neigh, name = "bilal rock", email = "bilal@gmail.com", bio = "I see myself here")

    def test_instance(self):
        '''
        Test to confirm that the object is being instantiated correctly
        '''
        self.assertTrue(isinstance(self.new_profile, Profile))

    def tearDown(self):
        Profile.objects.all().delete()


class HoodTestClass(TestCase):
    def setUp(self):
        self.syoks = Hood(hood_name = 'syoks')

    def test_instance(self):
        self.assertTrue(isinstance(self.syoks, Hood))

    def tearDown(self):
        Hood.objects.all().delete()

    def test_save_method(self):
        self.syoks.create_hood()
        hood = Hood.objects.all()
        self.assertTrue(len(hood) > 0)

    def test_delete_method(self):
        self.syoks.delete_hood('syoks')
        hood = Hood.objects.all()
        self.assertTrue(len(hood) == 0)

    def test_find_hood(self):
        self.syoks.create_hood()
        fetched_hood = Hood.find_hood("syoks")
        self.assertNotEqual(fetched_hood, self.syoks)

    def test_update_method(self):
        self.syoks.create_hood()
        edited_hood = Hood.update_hood("lavington")
        self.assertEqual(self.syoks, edited_hood)


class MedicalservicesTestClass(TestCase):
    def setUp(self):
        self.optical = medicalservices(medicalservices = 'optical')

    def test_instance(self):
        self.assertTrue(isinstance(self.optical, medicalservices))

    def tearDown(self):
        medicalservices.objects.all().delete()

    def test_save_method(self):
        self.optical.save_medicalservices()
        health = medicalservices.objects.all()
        self.assertTrue(len(health) > 0)

    def test_delete_method(self):
        self.optical.delete_medicalservices('optical')
        health = medicalservices.objects.all()
        self.assertTrue(len(health) == 0)


# Create your tests here.
