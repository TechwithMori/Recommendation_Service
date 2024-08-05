from django.test import TestCase
from .models import User, Item, UserPreference
from .recommender import get_recommendations

class RecommendationTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='user@test.com')
        self.item1 = Item.objects.create(name='Item1', description='A test item')
        self.item2 = Item.objects.create(name='Item2', description='Another test item')
        UserPreference.objects.create(user=self.user, item=self.item1, preference_score=5.0)
        UserPreference.objects.create(user=self.user, item=self.item2, preference_score=3.0)

    def test_recommendations(self):
        recommendations = get_recommendations(self.user.id)
        self.assertEqual(recommendations, [self.item1.id, self.item2.id])
