FROM python:3.10.10
ENV TZ=Asia/Shanghai
ENV PATH /usr/local/bin:$PATH
ADD . /automatic
WORKDIR /automatic
RUN pip3.10 install -r requirements.txt
CMD python3.10 juejin.py
