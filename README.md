# GoDaddyDynDNS

This is a small script that can update a dns record of GoDaddy to the machines public IP address. The script can be run using a cron job to run it hourly or even every 5 minutes.

## Requirements

- Python 3
- pip

Once the above are installed all the the required pip packages need to be installed. These can be installed with the following command line.

```shell
python3 -m pip install -r requirements.txt
```

## Setup

With the required software and packages installed the script can be setup to run. Before the script can run a `.env` is needed with the API and domain details. A `.env.exmaple` file is made available with the required variables. Create a copy of this file and rename it `.env` this can be done as shown below.

```shell
cp .env.example .env
```

Now the file needs to be completed with the correct details from GoDaddy these include an api key and an api secret. To get your api details you can go to https://developer.godaddy.com/keys/. The last thing to add to the `.env` file is the domain name and the record to update. By default the `@` record is updated however, this can be changed to any `A` record.
