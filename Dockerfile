FROM python:3.8

# cv2 import error solve
RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx

WORKDIR /app/django

ENV PYTHONIOENCODING=utf-8

RUN python -m pip install --upgrade pip >/dev/null 2>&1
COPY requirements.txt ./
RUN pip install -r requirements.txt >/dev/null 2>&1
COPY . .

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD python3 manage.py migrate && \
python3 manage.py runserver 0:8000

EXPOSE 8000
