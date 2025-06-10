# 0.Basics of HTTP/HTTPS

## Objectives to accomplish

- Differentiate between HTTP and HTTPS.
- Understand the structure of HTTP requests and responses.
- Recognize and explain common HTTP methods and status code.

---

## HTTP vs HTTPS

| Feature            | HTTP                           | HTTPS                               |
|--------------------|--------------------------------|-------------------------------------|
| Protocol           | Hypertext Transfer Protocol    | Hypertext Transfer Protocol Secure  |
| Port               | 80                             | 443                                 |
| Encryption         | No                             | Yes (SSL/TLS)                       |
| Security           | Vulnerable to interception     | Encrypted and secure                |
| Use case           | Non-Sensitive data             | Login, payment, personal info       |
| URL format         | `http://`                      | `https://`                          |

**Key point:**
HTTPS encrypts the data sent between client and server, protecting it from eavesdropping and tampering. It uses SSL/TLS.

---

## HTTP Request and Response Structure

### Request

Example:

```http
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```

**Components**
- **Method**: GET, POST, etc.
- **Path**: `/index.html`
- **Headers**: Metadata about the request
- **Body**: (Optional) data for POST/PUT

---

### Response

Example:

```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Lenght: 1234
<html>
  <body>
    Hello World!
  </body>
</html>
```

**Components**
- **Status Line**: Protocol + status code (e.g., `HTTP/1.1 200 OK`)
- **Headers**: Metadata about the request/response (e.g., `Content-Type: application/json`)
- **Body**: The main content of the response (e.g., HTML, JSON, images, etc.)


| Method | Description            | Example Use Case                   |
| ------ | ---------------------- | ---------------------------------- |
| GET    | Retrieve data          | Load a web page or API resource    |
| POST   | Send data to server    | Submit a form or create a resource |
| PUT    | Update or replace data | Update user profile info           |
| DELETE | Remove a resource      | Delete an account or comment       |


| Code | Meaning               | Description & Use Case                             |
| ---- | --------------------- | -------------------------------------------------- |
| 200  | OK                    | Request succeeded (e.g., page loaded successfully) |
| 201  | Created               | Resource was created (e.g., POST request to API)   |
| 301  | Moved Permanently     | URL has changed (used for redirects)               |
| 400  | Bad Request           | Malformed request (e.g., missing parameter)        |
| 401  | Unauthorized          | Authentication is required                         |
| 403  | Forbidden             | Authenticated, but not authorized                  |
| 404  | Not Found             | Resource doesn't exist (e.g., wrong URL)           |
| 500  | Internal Server Error | Server failed to complete the request              |