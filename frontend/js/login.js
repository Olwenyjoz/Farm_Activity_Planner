/*
=========================================================
Module: login.js

Purpose:
    Authenticate users.

Author:
    Deogracia Olweny
=========================================================
*/

const loginForm =

    document.getElementById(

        "loginForm"

    );

loginForm.addEventListener(

    "submit",

    async function(event){

        event.preventDefault();

        const email =

            document.getElementById(

                "email"

            ).value;

        const password =

            document.getElementById(

                "password"

            ).value;

        try{

            const response =

                await loginUser({

                    email,

                    password

                });

            saveToken(

                response.access_token

            );

            alert(

                "Login Successful"

            );

            window.location.href =
            "../pages/dashboard.html";

        }

        catch (error) {

        console.error(error);

        alert(

            error.message

        );

        }

    }

);