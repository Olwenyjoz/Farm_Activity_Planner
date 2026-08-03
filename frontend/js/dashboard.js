/*
=========================================================
Module: dashboard.js

Purpose:
    Dashboard functionality.

Responsibilities:
    - Authenticate user
    - Load dashboard
    - Display statistics
    - Display recent plans
    - View farm plan
    - Edit farm plan
    - Delete farm plan
    - Logout
=========================================================
*/

requireLogin();

/* ==========================================
Initialize Dashboard
========================================== */

document.addEventListener(

    "DOMContentLoaded",

    function(){

        loadDashboard();

        initializeLogout();

    }

);

/* ==========================================
Load Dashboard
========================================== */

async function loadDashboard(){

    try{

        const currentUser = getCurrentUser();

        if(currentUser){

            document.getElementById(

                "userName"

            ).textContent =

                currentUser.email || "User";

        }

        const plans = await getFarmPlans();

        updateStatistics(plans);

        populatePlansTable(plans);

    }

    catch(error){

        console.error(error);

        alert("Unable to load dashboard.");

    }

}

/* ==========================================
Statistics
========================================== */

function updateStatistics(plans){

    document.getElementById(

        "planCount"

    ).textContent = plans.length;

    let totalActivities = 0;

    plans.forEach(function(plan){

        if(plan.activities){

            totalActivities += plan.activities.length;

        }

    });

    document.getElementById(

        "activityCount"

    ).textContent = totalActivities;

}

/* ==========================================
Populate Table
========================================== */

function populatePlansTable(plans){

    const table = document.getElementById(

        "plansTable"

    );

    table.innerHTML = "";

    if(plans.length === 0){

        table.innerHTML =

        `
        <tr>

            <td colspan="5">

                No farm plans available.

            </td>

        </tr>
        `;

        return;

    }

    plans.forEach(function(plan){

        table.innerHTML +=

        `
        <tr>

            <td>${plan.id}</td>

            <td>${plan.crop}</td>

            <td>${plan.planting_date}</td>

            <td>${plan.status}</td>

            <td>

                <button
                    class="action-btn view-btn"
                    onclick="viewPlan(${plan.id})"
                >

                    View

                </button>

                <button
                    class="action-btn edit-btn"
                    onclick="editPlan(${plan.id})"
                >

                    Edit

                </button>

                <button
                    class="action-btn delete-btn"
                    onclick="deletePlan(${plan.id})"
                >

                    Delete

                </button>

            </td>

        </tr>

        `;

    });

}

/* ==========================================
View Plan
========================================== */

function viewPlan(id){

    localStorage.setItem(

        "view_plan_id",

        id

    );

    localStorage.removeItem(

        "edit_plan_id"

    );

    window.location.href =

        "planner.html";

}

/* ==========================================
Edit Plan
========================================== */

function editPlan(id){

    console.log("Editing plan:", id);

    localStorage.setItem("edit_plan_id", id);

    console.log(
        "Stored:",
        localStorage.getItem("edit_plan_id")
    );

    window.location.href = "planner.html";

}

/* ==========================================
Delete Plan
========================================== */

async function deletePlan(id){

    const confirmed = confirm(

        "Delete this farm plan?"

    );

    if(!confirmed){

        return;

    }

    try{

        await deleteFarmPlan(id);

        alert(

            "Farm plan deleted successfully."

        );

        loadDashboard();

    }

    catch(error){

        console.error(error);

        alert(

            "Unable to delete farm plan."

        );

    }

}

/* ==========================================
Logout
========================================== */

function initializeLogout(){

    document.getElementById(

        "logoutBtn"

    ).addEventListener(

        "click",

        function(event){

            event.preventDefault();

            logout();

        }

    );

}