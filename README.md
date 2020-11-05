# Human Rights First, Police Use of Force Map

    Uniting the world to stand against tyranny.

## Labs28 HRF-B Contributors
- Jazmine McGinnis, Backend Web
- Juan Alvarado-Arguello, Web
- Charlie Lu, Web
- Samuel Brown, Web
- Crystal Dixson, Data Science (Data)
- Jake Dennis, Data Science (ML)
- Robert Sharp, Data Science (API)

### Live API URL
[https://b-ds.humanrightsfirst.dev](https://b-ds.humanrightsfirst.dev/)

### Project Planning
[Team Trello Board](https://trello.com/b/AOaJaAQK/team-b-labs28)

### Data Science API built using:
- FastAPI
- Python
- Docker
- AWS Elastic Beanstalk

### Data Science API
- `/report-by-id` Gets an incident report by index.
- `/report-by-city` Gets a list of incident reports by city name.
- `/report-by-state` Gets a list of incident reports by state name.

### Installation Instructions - Local Development Environment
`$ pip install -r project/requirements.txt`

### Docker Build Command - Local Docker Testing
`$ docker build project -t labs28-hrf`

### Docker Run Command - Local Docker Testing
`$ docker run -p 8000:8000 -it labs28-hrf uvicorn app:api --host 0.0.0.0`

### Docker Remote Server Config
- DO NOT USE `$ docker-compose` locally!
- This file is for remote server configuration only.

### AWS EB Deployment Instructions
```
$ eb init us-east-1                     # Setup EB to run locally
$ eb create <app name>                  # Creates an app named <app name>
$ eb use <app name>                     # Sets the default app to the one you name
$ eb setenv DB_KEY=42 DB_SECRET=314     # Sets evironment variables for remote server
$ eb deploy -l v0.0.1                   # Pushes yur app to the cloud and sets the version
$ eb open                               # Opens your live app in a web browser
```
To update an existing environment with all currently committed changes:
`$ eb deploy -l v0.0.2` The version here should match your app version.

For more info `$ eb -h` or view the docs online: [EB CLI Commands](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb3-cmd-commands.html)
