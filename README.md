# idlebuilder
A web application that checks if a Epic Games username is available. It does this by using a Fortnite API wrapper to determine if a user ID exists.

This project is intended to serve multiple games such as League of Legends, Fortnite, Battle.net and more. Currently only works with Fortnite.

The project is as follows:

![](other/img1.jpg)
![](other/img2.jpg)

## References Used:
- (SETUP) https://medium.com/@nicholaskajoh/heres-a-dead-simple-react-django-setup-for-your-next-project-c0b0036663c6
- (FORTNITE API) https://github.com/nicolaskenner/python-fortnite-api-wrapper

## Getting Started:
- Clone the repo
- Follow the SETUP installation guide above
- Obtain your Fortnite API Tokens (https://gist.github.com/Douile/67daa69b59255bcdc390025053dbe295)
- Place these keys into idlesummoner/keys.py

## Running:
#### Frontend
- React is developed in `./src`.
- All static files are served in `./src` as well
- `npm run build` compiles everything into build.

#### Server
- Code is developed in idlesummoner
- 'python manage.py runserver' in the main server.
