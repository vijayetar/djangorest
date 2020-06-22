from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Review
# Create your tests here
class ReviewTests(TestCase):
  @classmethod
  def setUpTestData(cls):
    testuser1= get_user_model().objects.create_user(username="tester1", password="pass")
    testuser1.save()

    test_review = Review.objects.create(
      author = testuser1,
      title = "Blush",
      body = "Words about blush testing",

    )
    test_review.save()
  
  def test_review_content(self):
    review = Review.objects.get(id=1)
    actual_author = str(review.author)
    actual_body = str(review.body)
    actual_title = str(review.title)
    self.assertEqual(actual_author, "tester1")
    self.assertEqual(actual_title, "Blush")
    self.assertEqual(actual_body, "tester1")