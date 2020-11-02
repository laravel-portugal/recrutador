## Laravel-Portugal "O Recrutador"

![Run tests](https://github.com/laravel-portugal/recrutador/workflows/Run%20tests/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/laravel-portugal/recrutador/badge.svg?branch=master)](https://coveralls.io/github/laravel-portugal/recrutador?branch=master)

## Installation

**Requirements**

- Node.js

**Steps to run this project**

1. Clone this repository.
2. Run `npm install`
3. Update the `.env` file.
4. Run `node src/app.js` to check for new jobs and exit.
5. Run `node src/app.js --loop`  to check for new jobs every x seconds (see FETCHINTERVAL in .env config).


## .env

### TOKEN

To use a Discord Bot you need an API TOKEN, to create one follow this tutorial (https://discordpy.readthedocs.io/en/latest/discord.html#).

### CHANNELID

This Discord Channel Id, to get this id you should active "Developer Mode" in Appearance of your Discord Settings and after right-click the Target Channel and copy the ID.

### FETCHINTERVAL

The number of seconds between pulls, please keep it high (you should be fine with at least 30 minutes).

### TOKEN_ITJOBS

To use ItJobs API  you need an API TOKEN, to request one goto (https://www.itjobs.pt/api).

### LANDINGJOBS_API_KEY

To use landing.jobs API KEY  you need an API TOKEN, to request one goto (https://landing.jobs/account).

## Testing

This project is fully tested. We have an [automatic pipeline](https://github.com/laravel-portugal/recrutador/actions) and an [automatic code quality analysis](https://coveralls.io/github/laravel-portugal/recrutador) tool set up to continuously test and assert the quality of all code published in this repository, but you can execute the test suite yourself by running the following command:

```bash

```

## Authorize
```
https://discord.com/oauth2/authorize?client_id=123456789012345678&scope=bot
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
