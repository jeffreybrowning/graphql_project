from datetime import datetime, timedelta

from clients import kiva_client
from constants import KIVA_LOAN_DETAIL_URL, DATETIME_FORMAT


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
          ) {
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
    loans = []
    for l in res.get('data', {}).get('loans', {}).get('values', []):
        if datetime.strptime(l['plannedExpirationDate'], DATETIME_FORMAT) - datetime.now() > timedelta(days=1):
            continue

        loans.append(l)
        print('\nLoan detail url: {}'.format(KIVA_LOAN_DETAIL_URL.format(id=l['id'])))
        loan_amount = float(l['loanAmount'])
        funded_amount = float(l['loanFundraisingInfo']['fundedAmount'])
        remaining_amount = loan_amount - funded_amount
        print('Remaining amount: {:,.2f}'.format(remaining_amount))

        total_amount_remaining += remaining_amount
        total_amount += loan_amount

    print('\nTotal Amount Remaining: {:,.2f}'.format(total_amount_remaining))
    print('Total Amount:           {:,.2f}'.format(total_amount))
    return loans

if __name__ == '__main__':
    get_total_amount_24_hour_exp_loans()
