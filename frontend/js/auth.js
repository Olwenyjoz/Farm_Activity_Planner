/*
=========================================================
Module: auth.js

Purpose:
    Authentication utilities for the frontend.

Responsibilities:
    - Save JWT access token
    - Retrieve JWT access token
    - Remove JWT during logout
    - Protect authenticated pages
    - Decode JWT payload
    - Retrieve current logged-in user

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
*/

/*
=========================================================
Save JWT Token
=========================================================
*/

function saveToken(token) {

    localStorage.setItem(
        "access_token",
        token
    );

}

/*
=========================================================
Retrieve JWT Token
=========================================================
*/

function getToken() {

    return localStorage.getItem(
        "access_token"
    );

}

/*
=========================================================
Logout User
=========================================================
*/

function logout() {

    localStorage.removeItem(
        "access_token"
    );

    window.location.href =
        "../pages/login.html";

}

/*
=========================================================
Protect Authenticated Pages
=========================================================
*/

function requireLogin() {

    const token = getToken();

    if (!token) {

        window.location.href =
            "../pages/login.html";

    }

}

/*
=========================================================
Decode JWT Payload
=========================================================

Purpose:
    Decode the payload section of the JWT token.

Returns:
    JSON object containing the user information,
    or null if decoding fails.
=========================================================
*/

function parseJwt(token) {

    try {

        const payload = token.split(".")[1];

        const decoded = atob(payload);

        return JSON.parse(decoded);

    }

    catch (error) {

        console.error(
            "Unable to decode JWT token.",
            error
        );

        return null;

    }

}

/*
=========================================================
Get Current Logged-in User
=========================================================

Purpose:
    Retrieve the authenticated user's information
    from the JWT token.

Returns:
    User object or null.
=========================================================
*/

function getCurrentUser() {

    const token = getToken();

    if (!token) {

        return null;

    }

    const user = parseJwt(token);

    if (!user) {

        return null;

    }

    return {

        id: user.user_id,

        email: user.email,

        role: user.role,

        first_name: user.first_name || user.email.split("@")[0]

    };

}