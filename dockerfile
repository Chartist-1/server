# Используем официальный образ Python в качестве базового образа
FROM python
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED=1
# Копируем файл requirements.txt внутрь контейнера
COPY requirements.txt ./
# Устанавливаем зависимости, описанные в файле requirements.txt
RUN pip install -r requirements.txt
# RUN sleep 10
# RUN python manage.py makemigrations
# RUN sleep 10

# RUN python manage.py migrate
