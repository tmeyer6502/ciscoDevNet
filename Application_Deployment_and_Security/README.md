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

See example in this directory -- `example.dockerfile`

### Tutorial ###

https://www.docker.com/101-tutorial/


Here's a short example:

```

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]

```

4.7 Utilize Docker images in local developer environment

4.8 Identify application security issues related to secret protection, encryption (storage and transport), and data handling

4.9 Explain firewall, DNS, load balancers, and reverse proxy in application deployment

4.10 Describe top OWASP threats (such as XSS, SQL injections, and CSRF)

#### XSS (Cross-Site Scripting) ####

XSS is a type of web application security vulnerability that allows an attacker to inject malicious code into a website, which is then executed by the victim's browser. This can lead to various types of attacks, such as:

* Stealing sensitive information like login credentials or credit card numbers
* Hijacking user sessions and taking control of their accounts
* Displaying unwanted content, such as spam links or malware

XSS vulnerabilities typically occur when user input is not properly sanitized or validated, allowing an attacker to inject malicious JavaScript code into the website.

#### SQL Injection ####

SQL injection (SQLi) is a type of web application security vulnerability that allows an attacker to inject malicious SQL code into a database. This can lead to various types of attacks, such as:

* Stealing sensitive information like user passwords or credit card numbers
* Modifying or deleting data in the database
* Escalating privileges to gain unauthorized access to the database

SQL injection vulnerabilities typically occur when user input is not properly sanitized or validated, allowing an attacker to inject malicious SQL code into a vulnerable web application.

#### CSRF (Cross-Site Request Forgery) ####

CSRF is a type of web application security vulnerability that allows an attacker to trick users into performing unauthorized actions on their behalf. This can lead to various types of attacks, such as:

* Performing unintended or unauthorized actions, like transferring funds or changing settings
* Stealing sensitive information like login credentials or credit card numbers

CSRF vulnerabilities typically occur when a web application does not properly validate and verify requests, allowing an attacker to exploit the trust between the user and the website.

Common attack vectors for CSRF include:

* Phishing emails or messages that trick users into clicking on malicious links
* Malicious JavaScript code injected into websites through XSS attacks

To protect against these types of attacks, it's essential to implement robust security measures in your web applications, such as:

* Validating and sanitizing user input to prevent injection attacks (XSS, SQLi)
* Implementing secure authentication and authorization mechanisms to prevent unauthorized access (CSRF)

Using Content Security Policy (CSP) to restrict the types of scripts that can be executed by a browser (XSS)


4.11 Utilize Bash commands (file management, directory navigation, and environmental variables)

4.12 Identify the principles of DevOps practices
