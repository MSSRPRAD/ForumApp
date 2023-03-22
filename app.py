# import the create app application factory
from ForumApp import create_app

# import the application config classes
from config import Config

app = create_app()

if __name__ == '__main__':
   app.run()
