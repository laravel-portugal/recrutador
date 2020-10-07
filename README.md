## Laravel-Portugal "O Recrutador"

![Run tests](https://github.com/laravel-portugal/recrutador/workflows/Run%20tests/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/laravel-portugal/recrutador/badge.svg?branch=master)](https://coveralls.io/github/laravel-portugal/recrutador?branch=master)

## Installation

**Requirements**

- PYTHON >= 3.7

**Steps to run this project**

1. Clone this repository.
2. Install dependencies `pip3 install -r requirements.txt`
3. Update the `.env` file.
4. Run `python3 main.py`.
5. Run `python3 main.py --dry` to avoid publishing to channel.

## .env

### TOKEN

To use a Discord Bot you need an API TOKEN, to create one follow this tutorial (https://discordpy.readthedocs.io/en/latest/discord.html#).

### CHANNELID

This Discord Channel Id, to get this id you should active "Developer Mode" in Appearance of your Discord Settings and after right-click the Target Channel and copy the ID.

### FETCHINTERVAL

The number of seconds between pulls, please keep it high (you should be fine with at least 30 minutes).

### LANDINGJOBS_TAGS

The tags from Landing.jobs that you find relevant for your channel, they are comma separated, ex. "Laravel,PHP,Symphony".

### LANDINGJOBS_LASTPUBLISHEDID

It's used to record the last published id so if the bot is restarted no jobs are republished.

### ITJOBS_API

To use itjobs.pt API you need to apply for an API Key, see here (https://www.itjobs.pt/api).

### ITJOBS_SEARCH

The search terms used to find relevant jobs for you channel ex. "php,laravel,symphony".

### ITJOBS_LASTPUBLISHEDID

It's used to record the last published id so if the bot is restarted no jobs are republished.

## Testing

This project is fully tested. We have an [automatic pipeline](https://github.com/laravel-portugal/recrutador/actions) and an [automatic code quality analysis](https://coveralls.io/github/laravel-portugal/recrutador) tool set up to continuously test and assert the quality of all code published in this repository, but you can execute the test suite yourself by running the following command:

```bash

```

**We aim to keep the master branch always deployable.** Exceptions may happen, but they should be extremely rare.

## Changelog

Please see [CHANGELOG](CHANGELOG.md) for more information on what has changed recently.

## Contributing

Please see [CONTRIBUTING](CONTRIBUTING.md) for details.

## Security

Please see [SECURITY](SECURITY.md) for details.

## Credits

- [All Contributors](../../contributors)

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
