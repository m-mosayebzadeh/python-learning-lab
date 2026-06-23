import conftest
import unittest
from unittest.mock import MagicMock, patch
import service.user_api_usage_service as user_api_usage_service
from exception.app_exception import RateLimitException



class TestUserApiUsageService(unittest.TestCase):

    # check_and_increament
    @patch("service.user_api_usage_service.usage_repository")
    @patch("service.user_api_usage_service.find_by_user_and_date")
    def test_create_usage_when_not_exist(self, mock_find, mock_repo):

        user = MagicMock()
        membership = MagicMock()
        membership.token_limit = 10
        user.membership = membership
        user.id = 1

        session = MagicMock()

        mock_find.return_value = None
        
        user_api_usage_service.check_and_increament(user, session)

        mock_repo.save.assert_called_once()
        session.commit.assert_called_once()

    @patch("service.user_api_usage_service.find_by_user_and_date")
    def test_raise_http_exception_when_daily_limit_reached(self, mock_find):

        session = MagicMock()
        
        user = MagicMock()
        user.id = 1

        usage = MagicMock()
        mock_find.return_value = usage
        usage.call_count = 2

        membership = MagicMock()
        membership.token_limit = 2

        user.membership = membership

        with self.assertRaises(RateLimitException) as context:
            user_api_usage_service.check_and_increament(user, session)

        self.assertEqual(context.exception.status_code, 429)
        self.assertEqual(context.exception.detail, "Daily API limit reached")

        session.commit.assert_not_called()

    @patch("service.user_api_usage_service.usage_repository")
    @patch("service.user_api_usage_service.find_by_user_and_date")
    def test_usage_is_exist_before(self, mock_find, mock_repo):

        session = MagicMock()

        user = MagicMock()
        user.id = 1

        membership = MagicMock()
        membership.token_limit = 2
        user.membership = membership

        usage = MagicMock()
        usage.call_count = 1

        mock_find.return_value = usage

        user_api_usage_service.check_and_increament(user, session)

        self.assertEqual(usage.call_count, 2)
        mock_repo.save.assert_not_called()
        session.commit.assert_called_once()

