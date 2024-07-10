FROM python:3.9

WORKDIR /app

COPY fixed_width_file_parser.py /app/

CMD ["python", "fixed_width_file_parser.py"]
