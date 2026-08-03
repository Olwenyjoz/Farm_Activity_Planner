/*
=========================================================
Module: register.js

Purpose:
    Register a new user.

Author:
    Deogracia Olweny
=========================================================
*/

const registerForm =
    document.getElementById(
        "registerForm"
    );

registerForm.addEventListener(

    "submit",

    async function(event){

        event.preventDefault();

        const password =
            document.getElementById(
                "password"
            ).value;

        const confirmPassword =
            document.getElementById(
                "confirmPassword"
            ).value;

        if(password !== confirmPassword){

            alert(
                "Passwords do not match."
            );

            return;

        }

        const user = {

            first_name:
                document.getElementById(
                    "firstName"
                ).value,

            last_name:
                document.getElementById(
                    "lastName"
                ).value,

            email:
                document.getElementById(
                    "email"
                ).value,

            phone:
                document.getElementById(
                    "phone"
                ).value,

            password,

            role:
                document.getElementById(
                    "role"
                ).value

        };

        try{

            await registerUser(user);

            alert(
                "Registration Successful."
            );

            window.location.href =
                "login.html";

        }

        catch(error){

            console.error(error);

            alert(error.message);

        }

    }

);