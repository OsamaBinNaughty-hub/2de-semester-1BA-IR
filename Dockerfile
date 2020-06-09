FROM python 

VOLUME ["/source"]
WORKDIR /source
ENTRYPOINT ["python"]
