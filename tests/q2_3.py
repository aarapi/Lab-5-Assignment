OK_FORMAT = True
test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(convenience_sample.columns)
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(convenience_sample)
          414
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
