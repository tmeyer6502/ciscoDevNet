## Exam topics ##

See https://learningnetwork.cisco.com/s/devnet-associate-exam-topics?ccid=devnetcertguide&dtid=ebook&oid=devnet-cert-guide



4.1 Describe benefits of edge computing

4.2 Identify attributes of different application deployment models (private cloud, public cloud, hybrid cloud, and edge)

4.3 Identify the attributes of these application deployment types
4.3.a Virtual machines
4.3.b Bare metal
4.3.c Containers

4.4 Describe components for a CI/CD pipeline in application deployments

4.5 Construct a Python unit test

4.6 Interpret contents of a Dockerfile

See example in this directory

Here's a short example:

'''

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]

'''

4.7 Utilize Docker images in local developer environment

4.8 Identify application security issues related to secret protection, encryption (storage and transport), and data handling

4.9 Explain firewall, DNS, load balancers, and reverse proxy in application deployment

4.10 Describe top OWASP threats (such as XSS, SQL injections, and CSRF)

4.11 Utilize Bash commands (file management, directory navigation, and environmental variables)

4.12 Identify the principles of DevOps practices
