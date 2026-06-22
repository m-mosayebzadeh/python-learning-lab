import conftest
from unittest import TestCase
from unittest.mock import MagicMock, patch
import service.user_service as user_service


@patch("service.user_service.user_api_usage_service.find_by_user_and_date")
class TestUserService(TestCase):

    # get_user_profile

    def setUp(self):
        
        self.session = MagicMock()

        self.user = MagicMock()
        self.user.id = 1
        self.user.username= "test"
        self.user.email = "test@test.com"

        self.membership = MagicMock()
        self.membership.name = "free"
        self.user.membership = self.membership


    def test_not_find_usage_for_user(self, mock_find_usage):
        
        self.membership.token_limit = 1
        
        mock_find_usage.return_value = None

        response = user_service.get_user_profile(self.session, self.user)

        self.assertEqual(response.token_limit, 1)
        self.assertEqual(response.remaining_tokens, 1)

    
    def test_usage_exist_but_token_limit_more_than_call_count(self, mock_find_usage):
        
        usage = MagicMock()
        usage.call_count = 1

        self.membership.token_limit = 2

        mock_find_usage.return_value = usage

        response = user_service.get_user_profile(self.session, self.user)

        self.assertEqual(response.token_limit, 2)
        self.assertEqual(response.remaining_tokens, 1)


    def test_remaining_tokens_should_be_zero_when_call_count_exceeds_limit(self, mock_find_usage):
        
        usage = MagicMock()
        usage.call_count = 2

        self.membership.token_limit = 1

        mock_find_usage.return_value = usage

        response = user_service.get_user_profile(self.session, self.user)

        self.assertEqual(response.token_limit, 1)
        self.assertEqual(response.remaining_tokens, 0)


    def user_profile_assert_common(self, response):
        self.assertEqual(response.username, "test")
        self.assertEqual(response.email, "test@test.com")
        self.assertEqual(response.membership_name, "free")