from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import patch, Mock

from constants import DATETIME_FORMAT, KIVA_LOAN_DETAIL_URL

from loans import get_total_amount_24_hour_exp_loans


class BaseTestCase(TestCase):
    def test_one_day_remaining_totals_script(self):
        expiring_date = (datetime.now() + timedelta(hours=23)).strftime(DATETIME_FORMAT)
        non_expiring_date = (datetime.now() + timedelta(hours=25)).strftime(DATETIME_FORMAT)

        # Three lones. The first two will pass muster and be included. Carlos's loan expires
        # too far into the future to be included in the 24 hour window of expiration for this
        # function.
        loans = {
            "data": {
                "loans": {
                    "totalCount": 3,
                    "values": [
                        {
                            "id": 1,
                            "name": "Ashish",
                            "loanAmount": "100.00",
                            "status": "fundRaising",
                            "plannedExpirationDate": expiring_date,
                            "loanFundraisingInfo": {
                                "fundedAmount": "70.00"
                            }
                        },
                        {
                            "id": 2,
                            "name": "Bill",
                            "loanAmount": "300.00",
                            "status": "fundRaising",
                            "plannedExpirationDate": expiring_date,
                            "loanFundraisingInfo": {
                                "fundedAmount": "150.00"
                            }
                        },
                        {
                            "id": 3,
                            "name": "Carlos",
                            "loanAmount": "250.00",
                            "status": "fundRaising",
                            "plannedExpirationDate": non_expiring_date,
                            "loanFundraisingInfo": {
                                "fundedAmount": "75.00"
                            }
                        }
                    ]
                }
            }
        }

        # This patch will mock the `requests.get` call in our clients file, instead returning
        # ok=True, to pass our check in kiva_client, and the loans dictionary in place of the
        # responses json
        with patch('clients.requests.get', return_value=Mock(ok=True, json=lambda: loans)):
            loans, total_amount_remaining, total_amount = get_total_amount_24_hour_exp_loans()

            expected_loans = [{'url': KIVA_LOAN_DETAIL_URL.format(id=1), 'remaining_amount': '$30.00'},
                              {'url': KIVA_LOAN_DETAIL_URL.format(id=2), 'remaining_amount': '$150.00'}]

            self.assertEqual(loans, expected_loans)
            self.assertEqual(total_amount, '$400.00')
            self.assertEqual(total_amount_remaining, '$180.00')
