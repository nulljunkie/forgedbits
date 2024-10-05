from django.test import TestCase
from faker import Faker
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Profile, User


class UserAuthenticationTest(APITestCase):

    def test_jwt_obtain_token(self):

        fake = Faker()

        for i in range(10):
            username = fake.user_name()
            password = fake.password()

            print(username, password)
            User.objects.create_user(username=username, password=password)
            response = self.client.post('/api/users/token/', {
                'username': username,
                'password': password
            }, format='json')

            self.assertEqual(response.status_code, status.HTTP_200_OK)

            self.assertIn('access', response.data)
            self.assertIn('refresh', response.data)


class FollowerTest(TestCase):

    def setUp(self):

        self.user1 = User.objects.create(username='user1', password='PassWord@99')
        self.user2 = User.objects.create(username='user2', password='PassWord@99')
        self.user3 = User.objects.create(username='user3', password='PassWord@99')
        self.user4 = User.objects.create(username='user4', password='PassWord@99')

        self.user1_profile = Profile.objects.get(user=self.user1)
        self.user2_profile = Profile.objects.get(user=self.user2)
        self.user3_profile = Profile.objects.get(user=self.user3)
        self.user4_profile = Profile.objects.get(user=self.user4)


        self.user1_profile.followers.add(self.user2_profile, self.user4_profile)
        self.user2_profile.followers.add(self.user1_profile, self.user3_profile, self.user4_profile)

    def test_user1_followers(self):

        user1_followers = self.user1_profile.followers.all()

        self.assertIn(self.user2_profile, user1_followers)
        self.assertIn(self.user4_profile, user1_followers)

    def test_user2_followers(self):

        user2_followers = self.user2_profile.followers.all()

        self.assertIn(self.user1_profile, user2_followers)
        self.assertIn(self.user3_profile, user2_followers)
        self.assertIn(self.user4_profile, user2_followers)
        self.assertEqual(user2_followers.count(), 3)

