 # Django & React Authentication System
This project is a simple authentication system built with Django for the backend and React for the frontend, featuring token-based authentication using JWT (JSON Web Token) with access and refresh tokens.

## 🚀 Features

1. User Registration & Login: Users can securely register and log in using token-based authentication.
2. Token Authentication: Implemented using Django REST Framework's Simple JWT. The access tokens expire after 90 minutes, while the refresh tokens last for 50 days with automatic rotation.
3. Profile Management: Users can manage their profiles after registering. Profiles are automatically created upon registration.
4. Custom API Endpoints: Created API endpoints using Django’s generic views for managing users, profiles, notes, and more.
5. Secure Permissions: Only authenticated users can access and modify their own data. Permission classes are used to ensure user data protection.
Token Rotation & Blacklisting: Refresh tokens are rotated after each use, and old tokens are blacklisted to enhance security.

## 📚 Lessons Learned
1. Authentication & Authorization:
-Implemented JWT for token-based authentication and authorization.
-Validated and handled token expiry, rotation, and security concerns.

2. REST API Development:
-Built efficient, secure REST APIs with Django and DRF.
-Utilized generic views and custom endpoints for handling profile updates, notes, and other resources.

3. Security Best Practices:
-Set up short-lived access tokens and long-lived refresh tokens for better security.
-Implemented token rotation and blacklisting to prevent unauthorized token reuse.

4. Front-End Integration:
-Developed the frontend using React, ensuring a seamless user experience.
-Integrated JWT token handling on the client-side to manage access and refresh tokens efficiently.
