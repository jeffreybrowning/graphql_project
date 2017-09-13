from datetime import datetime, timedelta

from clients import kiva_client
from constants import KIVA_LOAN_DETAIL_URL, DATETIME_FORMAT, DOLLAR_FORMAT


def get_total_amount_24_hour_exp_loans():
    querystring = '''
        {
            loans (
            filters: {
                status: fundRaising, 
                expiringSoon: true,
            }, 
            sortBy: newest,
            limit: 1000
            )  {
                totalCount,
                values {
                    id,
                    name,
                    loanAmount,
                    status,
                    plannedExpirationDate,
                    loanFundraisingInfo {
                      fundedAmount
                    }
                }
            }
        }
    '''

    res = kiva_client.query(querystring)

    total_amount_remaining = 0
    total_amount = 0
    loan_amounts_and_urls = []
    for l in res.get('data', {}).get('loans', {}).get('values', []):
        # if the expiration date for the loan is not the next 24 hours, move on
        if datetime.strptime(l['plannedExpirationDate'], DATETIME_FORMAT) - datetime.now() > timedelta(days=1):
            continue

        loan_url = KIVA_LOAN_DETAIL_URL.format(id=l['id'])
        loan_amount = float(l['loanAmount'])
        remaining_amount = loan_amount - float(l['loanFundraisingInfo']['fundedAmount'])

        remaining_amount_str = DOLLAR_FORMAT.format(remaining_amount)
        print('\nLoan detail url: {}'.format(loan_url))
        print('Remaining amount: {}'.format(remaining_amount_str))

        loan_amounts_and_urls.append({'url': KIVA_LOAN_DETAIL_URL.format(id=l['id']),
                                      'remaining_amount': remaining_amount_str})

        total_amount_remaining += remaining_amount
        total_amount += loan_amount

    total_amount_remaining_str = DOLLAR_FORMAT.format(total_amount_remaining)
    total_amount_str = DOLLAR_FORMAT.format(total_amount)
    print('\nTotal Amount Remaining: {}'.format(total_amount_remaining_str))
    print('Total Amount:           {}'.format(total_amount_str))

    return loan_amounts_and_urls, total_amount_remaining_str, total_amount_str


if __name__ == '__main__':
    get_total_amount_24_hour_exp_loans()
