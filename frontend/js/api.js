/*
=========================================================
Module: api.js

Purpose:
    Centralized API communication.

Responsibilities:
    - User authentication
    - User registration
    - Farm plan CRUD
    - Authorization header
    - Error handling

Author:
    Deogracia Olweny

Project:
    Farm Activity Planner AI
=========================================================
*/

const API_BASE_URL = CONFIG.API_BASE_URL;

/*
=========================================================
Helper Function
=========================================================
*/

async function apiRequest(
    endpoint,
    method = "GET",
    data = null,
    authenticated = false
) {

    const headers = {
        "Content-Type": "application/json"
    };

    if (authenticated) {

        const token = localStorage.getItem(
            "access_token"
        );

        if (token) {

            headers["Authorization"] =
                `Bearer ${token}`;

        }

    }

    const options = {

        method,

        headers

    };

    if (data) {

        options.body = JSON.stringify(data);

    }

    console.log("Request URL:", API_BASE_URL + endpoint);

    const response = await fetch(

        API_BASE_URL + endpoint,

        options

    );

    if (!response.ok) {

            const error = await response.text();

            throw new Error(error);

        }

        /* DELETE requests (204 No Content) */

        if (response.status === 204) {

            return null;

        }

        return response.json();

}

/*
=========================================================
Login User
=========================================================
*/
async function loginUser(credentials) {

    const formData = new URLSearchParams();

    formData.append(
        "username",
        credentials.email
    );

    formData.append(
        "password",
        credentials.password
    );

    const response = await fetch(

        API_BASE_URL + "/auth/login",

        {

            method: "POST",

            headers: {

                "Content-Type":
                    "application/x-www-form-urlencoded"

            },

            body: formData

        }

    );

    if (!response.ok) {

        throw new Error(
            "Invalid credentials."
        );

    }

    return response.json();

}


/*
=========================================================
Register User
=========================================================
*/
async function registerUser(user) {

    return apiRequest(

        "/auth/register",

        "POST",

        user

    );

}

/*
=========================================================
Farm Plans
=========================================================
*/

async function generatePlan(plan) {

    return apiRequest(

        "/generate-plan",

        "POST",

        plan,

        true

    );

}

async function getFarmPlans() {

    return apiRequest(

        "/farm-plans",

        "GET",

        null,

        true

    );

}

async function getFarmPlan(id) {

    return apiRequest(

        `/farm-plans/${id}`,

        "GET",

        null,

        true

    );

}

async function updateFarmPlan(

    id,

    data

) {

    return apiRequest(

        `/farm-plans/${id}`,

        "PUT",

        data,

        true

    );

}

async function deleteFarmPlan(id) {

    return apiRequest(

        `/farm-plans/${id}`,

        "DELETE",

        null,

        true

    );

}