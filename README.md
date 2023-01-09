# Project name

Briefly description about the project motivation and business or technical problem we are trying to solve with this.

## Project questions

- Who is conducting this analysis? (put your contact)
- Is this analysis related initially to some issue or epic? Which ones?
- Who are the main stakeholders of this analysis?

## Maintainability information

- There are future works? Wich ones are ideas, and which ones are stakeholders' demands?
- There are references that someone that continues this work in the future must take into consideration?

## Setup information

Follow the guidelines described at the Repository's Wiki (https://github.com/hurbcom/dsc-notebooks/wiki/Local-Development) to setup your local environment, then run the following commands.

### Build Image

```bash
$ sudo docker build --tag=template-project:1.0 .
```

### Run the container

Set the ENV variable GOOGLE_APPLICATION_CREDENTIALS in your machine and then run the
following command:

```bash
$ sudo docker create -t -i --name template-project \
    -p 8000:8000 -v $PWD:/home/user \
   -e GOOGLE_APPLICATION_CREDENTIALS=/tmp/keys/default.json \
   -v $GOOGLE_APPLICATION_CREDENTIALS:/tmp/keys/default.json:ro \
    template-project:1.0

$ sudo docker start template-project
$ sudo docker exec -it template-project bash
$ jupyter lab --ip 0.0.0.0 --port 8000 --allow-root
```

**Do other people running this analysis need to install any custom package on their computer or create additional files?**
