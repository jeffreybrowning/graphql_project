import requests


def main():
    query = '''
    {
      loans (
        filters: {
          status: fundRaising, 
          expiringSoon: true,
        }, 
        sortBy: newest,
        limit:10
      ) {
            totalCount,
          values {	
            name,
            loanAmount,
            status,
            plannedExpirationDate,
          }
        }
    }
    '''

    print('inside main')
    res = requests.get('http://api.kivaws.org/graphql', params={'query': query})
    data = res.json().get('data')
    loans = data.get('loans')
    print('Total count: {}'.format(loans['totalCount']))
    print('end main')


if __name__ == '__main__':
    main()
