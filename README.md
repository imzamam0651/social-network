Django Social App

A small social networking application which allows user to:

•Create an account.
•Login into their account with their email and password.
•View other users on the system and search the users based on name or email address.
•Send friend request to a user.
•Accept/Reject a request received from a user.
•View list of requests and filter them by request status.

User Login/Signup
• Users should be able to login with their email and password(email should be case
insensitive)
• User should be able to signup with their email only(no otp verification required, valid
email format is sufficient)
• Except signup and login every api should be called for authenticated users only


Develop API for following functionalities:
• API to search other users by email and name(paginate up to 10 records per page).
a) If search keyword matches exact email then return user associated with the
email.
b) If the search keyword contains any part of the name then return a list of all
users.
eg:- Amarendra, Amar, aman, Abhirama are three users and if users search with "am"
then all of these users should be shown in the search result because "am"
substring is part of all of these names.
c) There will be only one search keyword that will search either by name or email.
• API to send/accept/reject friend request
• API to list friends(list of users who have accepted friend request)
• List pending friend requests(received friend request)
• Users can not send more than 3 friend requests within a minute.

Security

• All APIs except login and signup will be called by authenticated users only.
• ScopedRateThrottle is added so that users can not send more than 3 friend requests within a minute.
• API permission is applied, which won't allow the sender or any other user to update the request 
  status.It'll only be updated by the user to whom the request is intended to.

Getting Started

 Pre-requisite: Docker must be installed on your machine.

• Clone the project repository to your local machine.
• Open a terminal and navigate to the project directory.
• Run the project using docker-compose up command.
• To stop the project, Run docker-compose down.

Once you run the project, Access the APIs at http://0.0.0.0:8000 address.

For get up and running quickly a fixtures file is added which contains mock data of 100 users. All the users have the same password: 1234. This will allow anyone to test the APIs with good amount of records.

You can test the APIs on postman as well.
