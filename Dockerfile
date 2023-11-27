FROM python:3.10
EXPOSE 5010
RUN mkdir -p /opt/services/bot/USDTbot1
WORKDIR /opt/services/bot/USDTbot1

RUN mkdir -p /opt/services/bot/USDTbot1/requirements
ADD requirements.txt /opt/services/bot/USDTbot1/

COPY . /opt/services/bot/USDTbot1/

RUN pip install -r requirements.txt
CMD ["python", "/opt/services/bot/USDTbot1/main.py"]