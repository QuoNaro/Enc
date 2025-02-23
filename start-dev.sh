#!/bin/bash

# Определите абсолютный путь к проекту
PROJECT_ROOT=$(pwd)

# Запуск Tmux сессии
tmux new-session -d -s enc-dev

# Основная команда: Активация venv и запуск FastAPI (бэкенд)
tmux send-keys -t enc-dev "source ${PROJECT_ROOT}/.venv/bin/activate && cd ${PROJECT_ROOT}/backend && uvicorn main:app --reload" C-m

# Добавление новой панели справа (вертикальный сплит)
tmux split-window -h -t enc-dev

# Команда во второй панели: Запуск Vue.js (фронтенд)
tmux select-pane -t 1
tmux send-keys -t enc-dev "cd ${PROJECT_ROOT}/frontend && npm run serve" C-m

# Установка равной ширины панелей
tmux select-layout even-horizontal

# Прикрепление к сессии (если хотите сразу увидеть вывод)
tmux attach-session -t enc-dev