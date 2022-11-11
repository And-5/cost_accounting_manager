FROM python:3.11
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /usr/cost_accounting_manager
COPY requirements.txt /usr/cost_accounting_manager/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /usr/cost_accounting_manager/

COPY start.sh /usr/cost_accounting_manager/start.sh
RUN chmod +x /usr/cost_accounting_manager/start.sh
ENTRYPOINT '/usr/cost_accounting_manager/start.sh'