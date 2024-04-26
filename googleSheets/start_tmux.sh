#!/bin/bash

# Start a new detached tmux session named GFG_Session
tmux new-session -d -s django
tmux send-keys -t django:1 'cd ~/pypro/googleSheets/ && nvim'
#create a new window in the django session
tmux new-window -t django:2
tmux send-keys -t django:2 'cd ~/pypro/googleSheets/ && source bin/activate'
#tmux new-window -t django:2  'nvim ~/django_project/manuals/manualsEnv//pages/templates/pages/page.html'
#tmux new-window -t django:3  'nvim ~/django_project/manuals/manualsEnv//pages/models.py'
#tmux new-window -t django:4  'nvim ~/django_project/manuals/manualsEnv//pages/views.py'

#tmux new-window -t django:5 
#tmux new-window -t django:6
#tmux send-keys -t django:5 'source ~/django_project/manuals/manualsEnv/bin/activate && cd ~/django_project/manuals/manualsEnv// && python manage.py shell < prueba.py'
#tmux send-keys -t django:6 'cd ~/django_project/manuals/manualsEnv// && nvim prueba.py'
#tmux new-window -t django: 'cd ~/django_project/manuals/manualsEnv//'

# Attach to the tmux session
tmux attach-session -t django
