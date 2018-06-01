# Nemuca-

Hey there,

To run this project. Follow the steps given below:-

I. If you don't have postgres configured ( You are probably here ):
  1. Goto ac/core/models.py and comment out the whole code.
  2. Goto ac/ and in terminal type:
      python ./manage.py makemigrations
      python ./manage.py migrate
  3. To run the server , in the same terminal type:
      python ./manage.py runserver
  4. To check the outputs, open browser and enter the following url:
        127.0.0.1:8000

II. If you have Postgres configured , Great!
    1. Just follow the steps 3, 4 from the above procedure

Please report bugs as soon as you find them or push the edits

Be Active :)
