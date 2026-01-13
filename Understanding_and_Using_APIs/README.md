## Understanding and Using APIs 

This might be useful reading/skimming: https://swagger.io/specification/

This is also worth investigating--from the guy that started it all: https://home.cs.colorado.edu/~kena/classes/7818/f08/lectures/lecture_9_fielding_disserta.pdf

The idea here is that you can use different "REST" (REpresentational State Transfer) operations to query or update server-side data. An HTTP request operates over TCP/IP connection and includes the operation as well as header data, in the body of the request.

There are four common REST operations you should know:

- GET: retrieve an item (often called an object)
- POST: place (send) an object
- DELETE: delete an object
- PUT: update an object

GET operations are easily visible in your browser.  Every request to a webpage that you make (by typing in the URL bar) is a GET.  Have you ever see a URL like http://example.com/people?id=35 ?   The 'id=35' part identifies a name/value pair sent to the server--it will 'GET' the person with the ID of 35, and send that information back to the client.

PUT/POST/DELETE usually don't have easily identifiable 'tells' like that, because they usually place their payload in the BODY of the request. For REST API construction, they're usually JSON.  JSON stands for "JavaScript Object Notation" and should remind you a little bit of other formats like XML or YAML. JSON consists of easily readable name/value pairs.  JSON objects can be nested.  

```
{
    "name": "John Doe",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345"
    }
}
```
In the above example, we see a "Person" object with three fields: name, age, and address.  The 'address' field in turn, has four subfields.

A very common operation in REST applications is to POST JSON like the above, which the server will then use to construct a "Person" object and store it in the database -- returning the ID of the new object to the user.  A subsequent GET using that ID will return the same JSON response, which can then be parsed by the client.



### Goals

#### Construct a REST API request to accomplish a task given API documentation

#### Describe common usage patterns related to webhooks

#### Identify the constraints when consuming APIs

#### Explain common HTTP response codes associated with REST APIs

Usually the 200-class codes mean "OK," the 300-class codes mean "Something has moved," the 400-class codes mean "Not found, or you're not authorized", and 500-class codes mean a server-side error.


- 200 OK: The most common response code, indicating that the request was successful and the server has returned a normal response.
- 300 Moved: The requested resource has moved (could be a redirect)
- 400 Bad Request: Maybe your JSON is malformed or the URL is incoherent.
- 401 Unauthorized: When a client attempts to access a protected resource without providing the necessary authentication or authorization information.
- 404 Not Found: A classic error, this code is returned when the requested resource cannot be found on the server-side.
- 500 Internal Server Error: This generic error code is often used when an unexpected problem occurs within the server that prevents it from fulfilling the request.


#### Troubleshoot a problem given the HTTP response code, request and API documentation




