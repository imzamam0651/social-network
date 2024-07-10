Social Networking App

A small social networking application which allows user to:


•Login into their account with their email and password (email should be case
 insensitive).

•Signup into their account with their email only(no otp verification required, valid
 email format is sufficient).

•Except signup and login every api should be called for authenticated users only

•View other users on the system and search the users based on email and name (paginate up to 10 records per page).

a) If search keyword matches exact email then return user associated with the
email.

b) If the search keyword contains any part of the name then return a list of all
users.
eg:- Amarendra, Amar, aman, Abhirama are three users and if users search with "am"
then all of these users should be shown in the search result because "am"
substring is part of all of these names.

GET http://127.0.0.1:8000/v1/user_search?keyword=ama

curl --location 'http://127.0.0.1:8000/v1/user_search?keyword=ama' \
--header 'Authorization: Basic dGVzdEBlbWFpbC5jb206QVNERkA5aGFu' \
--header 'Cookie: csrftoken=5kNQ4Bq0kN5S3fKG7SpXECOI1RJk6rKx; sessionid=doja2l2ecs6hm7cez3yikwnjy1dcf55i'

c) There will be only one search keyword that will search either by name or email.


•Send friend request to a user.

POST http://127.0.0.1:8000/v1/friendrequests

request_body
{
    "receiver": {
        "type": "User",
        "id": <pk of the receiver>
    }
}

curl --location 'http://127.0.0.1:8000/v1/friendrequests' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic aW16YW1hbToxMjM0NTY=' \
--data '{
    "receiver": {
        "type": "User",
        "id": <pk of the receiver>
    }
}'

•Accept a friend request received from a user.

PUT http://127.0.0.1:8000/v1/friendrequests/accept

curl --location --request PUT 'http://127.0.0.1:8000/v1/friendrequests/5/accept' \
--header 'id;' \
--header 'Authorization: Basic dGVzdDpBU0RGQDloYW4=' \
--header 'Cookie: csrftoken=5kNQ4Bq0kN5S3fKG7SpXECOI1RJk6rKx; sessionid=doja2l2ecs6hm7cez3yikwnjy1dcf55i' \
--data ''

Reject a friend request received from a user.

PUT http://127.0.0.1:8000/v1/friendrequests/reject

curl --location --request PUT 'http://127.0.0.1:8000/v1/friendrequests/reject' \
--header 'id;' \
--header 'Authorization: Basic aW16YW1hbUBlbWFpbC5jb206MTIzNDU2' \
--header 'Cookie: csrftoken=5kNQ4Bq0kN5S3fKG7SpXECOI1RJk6rKx; sessionid=doja2l2ecs6hm7cez3yikwnjy1dcf55i' \
--data ''

•list of users who have accepted friend request.

GET http://127.0.0.1:8000/v1/friendrequests/friends

url --location 'http://127.0.0.1:8000/v1/friendrequests/friends' \
--header 'Authorization: Basic dGVzdEBlbWFpbC5jb206QVNERkA5aGFu' \
--header 'Cookie: csrftoken=5kNQ4Bq0kN5S3fKG7SpXECOI1RJk6rKx; sessionid=doja2l2ecs6hm7cez3yikwnjy1dcf55i' \
--data ''

• List of pending friend requests(received friend request)

GET http://127.0.0.1:8000/v1/friendrequests/pending

curl --location 'http://127.0.0.1:8000/v1/friendrequests/pending' \
--header 'Authorization: Basic dGVzdEBlbWFpbC5jb206QVNERkA5aGFu' \
--header 'Cookie: csrftoken=5kNQ4Bq0kN5S3fKG7SpXECOI1RJk6rKx; sessionid=doja2l2ecs6hm7cez3yikwnjy1dcf55i'


Security

• All APIs except login and signup will be called by authenticated users only.
• ScopedRateThrottle is added so that users can not send more than 3 friend requests within a minute.

POST http://127.0.0.1:8000/v1/friendrequests

Body: {
    "detail": "Request was throttled. Expected available in 21 seconds."
}


curl --location 'http://127.0.0.1:8000/v1/friendrequests' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic dGVzdEBlbWFpbC5jb206QVNERkA5aGFu' \
--header 'Cookie: csrftoken=5kNQ4Bq0kN5S3fKG7SpXECOI1RJk6rKx; sessionid=doja2l2ecs6hm7cez3yikwnjy1dcf55i' \
--data '{
    "receiver": {
        "type": "User",
        "id": "12"
    }
}'

• API permission is applied, which won't allow the sender or any other user to update the request 
  status.It'll only be updated by the user to whom the request is intended to.

Getting Started

• Clone the project repository to your local machine.
• Open a terminal and navigate to the project directory.

Once you run the project, Access the APIs at http://127.0.0.1:8000/v1/ address.

You can test the APIs on postman as, I have shared all the end points.
