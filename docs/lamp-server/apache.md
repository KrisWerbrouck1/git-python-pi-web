# Apache HTTP server

The internet is a large network of computers. Not all computers have the same task. Some are always available and serve information. Others are only temporally available and will access information from others. This model is called the client/server model.

>The client/server model is a computing model that acts as a distributed application which partitions tasks or workloads between the providers of a resource or service, called servers, and service requesters, called clients. Source: wikipedia

The client/server model is an **asymmetric** model. This means that not all participants (computers) in this model have the same task or responsibility. This is in contrast to the Peer-to-Peer or P2P model, where all participants have the same responsibility or task.

In the client/server model we have the servers that are always available. They only wait for requests and will never initiate communication. The clients are only temporary active and initiates the communication.

## HTTP protocol

Protocol for Client-Server applications
Protocol = system of rules that allow two or more entities of a communications system to transmit information 
How to request and respond is standardized in the HTTP protocol coordinated by the IETF - Internet Engineering Task Force
HTTP stands for HyperText Transfer Protocol

![HTTP request and response](./img/http-request-response.png)

Client requests and server reponses
Plain text protocol, thus readable for humans
Default port is 80
Stateless protocol
No state (information or status) is retained between requests
State can be retained with ‘HTTP cookies’ or ‘sessions’

### Request

The request message consists of the following:
A request line
*for example GET /images/logo.png HTTP/1.1, which requests a resource called /images/logo.png from the server
One or more Request header fields
such as Accept-Language: en, …
An empty line
An optional message body
Note: the host header is mandatory, all others are optional

```
GET / HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: www.vives.be
User-Agent: HTTPie/0.9.2
```

### Response

The response message consists of the following:
A Status-Line
which include the status code and reason message
e.g., HTTP/1.1 200 OK, which indicates that the client's request succeeded
Response header fields
such as Content-Type: text/html, …
An empty line
An optional message body

```
HTTP/1.1 200 OK
CF-RAY: 225c457079770300-LHR
Cache-Control: public, max-age=180
Connection: keep-alive
Content-Encoding: gzip
Content-Language: nl
Content-Type: text/html; charset=utf-8
Date: Mon, 14 Sep 2015 12:59:49 GMT
Etag: W/"1442235275-1"
Expires: Sun, 19 Nov 1978 05:00:00 GMT
Last-Modified: Mon, 14 Sep 2015 12:54:35 GMT
Server: cloudflare-nginx
Set-Cookie: __cfduid=d9cb1e5a7a171cd3e48723d5f9d669c721442235589; expires=Tue, 13-Sep-16 12:59:49 GMT; path=/; domain=.vives.be; HttpOnly
Transfer-Encoding: chunked
Vary: Cookie,Accept-Encoding
X-Drupal-Cache: HIT
X-Generator: Drupal 7 (http://drupal.org)
X-Powered-By: PHP/5.5.16

<html>….</html>
```

## Installation

Apache can be simply installed using the apt package manager. Just run the following command in the terminal:

```
sudo apt install apache2 -y
```

This should do it. Simple isn't it?

## Testing it out

If everything went well, the Raspberry Pi will function as an HTTP server using Apache. The simplest way to to test this is on the Raspberry Pi itself. Just open a browser and surf to [http://localhost](http://localhost). You should then get the _Apache Debian Default Page_.

![Apache Debian Default Page](./img/apache-debian-default-page.png)

It is also possible to access the webpage from another machine. The only requirement is that the client is in the same network. To do this, you just need the IP address of the Raspberry Pi. To get the IP you could execute the `ifconfig` command in the terminal. The IP address can then be found in the `eth0` interface configuration, next to `inet`. In the example below, the IP address is `172.16.1.228`.

```
pi@raspberrypi:~ $ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.16.1.228  netmask 255.255.0.0  broadcast 172.16.255.255
        inet6 fe80::6f6:6b2a:3fc2:1c1  prefixlen 64  scopeid 0x20<link>
        ...

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        ....

wlan0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ...
```

You can now surf from any machine in the network to [http://172.16.1.228](http://172.16.1.228).

