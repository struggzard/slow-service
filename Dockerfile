FROM python:3.7-slim

ADD slow_service.py slow_service.py 

CMD python slow_service.py