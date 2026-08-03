/*
=========================================================
Module: planner.js

Purpose:
    Farm Activity Planner functionality.

Responsibilities:
    - Authentication
    - Logout
    - Submit planner form
    - Call backend API
    - Store latest generated plan
    - Display generated results
=========================================================
*/

requireLogin();

/* ==========================================
   Initialize Page
========================================== */

document.addEventListener(

    "DOMContentLoaded",

    async function(){

        console.log(
            "edit_plan_id:",
            localStorage.getItem("edit_plan_id")
        );

        console.log(
            "view_plan_id:",
            localStorage.getItem("view_plan_id")
        );

        initializePlanner();

        getCurrentLocation();

        editPlanId = localStorage.getItem(
            "edit_plan_id"
        );

        viewPlanId = localStorage.getItem(
            "view_plan_id"
        );

        if(editPlanId){

            await loadPlan(

                editPlanId,

                true

            );

        }

        else if(viewPlanId){

            await loadPlan(

                viewPlanId,

                false

            );

        }

    }

);
/* ==========================================
   Initialize
========================================== */

function initializePlanner(){

    initializeLogout();

    initializeForm();

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

/* ==========================================
   Planner Form
========================================== */

function initializeForm(){

    const form =

        document.getElementById(

            "plannerForm"

        );

    form.addEventListener(

        "submit",

        submitPlanner

    );

}

/* ==========================================
   Submit Planner
========================================== */

async function submitPlanner(event){

    event.preventDefault();

    document
    .getElementById("loadingBox")
    .classList.remove("hidden");

    document
    .getElementById("planResult")
    .style.display = "none";

    try{

        const request = {

            crop:

                document.getElementById(
                    "crop"
                ).value,

            planting_date:

                document.getElementById(
                    "plantingDate"
                ).value,

            farm_size:Number(

                document.getElementById(
                    "farmSize"
                ).value

            ),

            workers:Number(

                document.getElementById(
                    "workers"
                ).value

            ),

            soil_type:

                document.getElementById(
                    "soilType"
                ).value,

            season:

                document.getElementById(
                    "season"
                ).value,

            latitude:parseFloat(

                document.getElementById(
                    "latitude"
                ).value

            ),

            longitude:parseFloat(

                document.getElementById(
                    "longitude"
                ).value

            )

        };

    const plan = await generatePlan(request);

        alert("Request completed!");

        console.log(plan);

        const container = document.getElementById("planResult");

        container.innerHTML =
            "<h2>SUCCESS</h2>";


        document
        .getElementById("loadingBox")
        .classList.add("hidden");

        document
        .getElementById("planResult")
        .style.display = "block";

        showSuccessMessage(
             "Farm plan generated successfully!"
        );
    }

    catch(error){

        console.error(error);

        alert(

            "Unable to generate farm plan."

        );

    }

}

/* ==========================================
   Display Plan
========================================== */

function displayPlan(plan){

    const container =

        document.getElementById(

            "planResult"

        );

    let html = `

        <div class="result-section">

            <h3>

                Farm Information

            </h3>

            <p>

                <strong>Crop:</strong>

                ${plan.crop}

            </p>

            <p>

                <strong>Planting Date:</strong>

                ${plan.planting_date}

            </p>

            <p>

                <strong>Status:</strong>

                ${plan.status}

            </p>

        </div>

    `;

    html += renderWeather(plan.weather);

    html += renderActivities(plan.activities);

    html += renderResources(plan.resource_report);

    html += renderConflicts(plan.conflicts);

    html += renderRecommendations(plan.recommendations);

    html += renderCalendar(plan.calendar);

    container.innerHTML = html;

}

/* ==========================================
   Weather
========================================== */

function renderWeather(weather){

    if(!weather){

        return "";

    }

    return `

        <div class="result-section">

            <h3>🌦 Weather</h3>

            <p><strong>Temperature:</strong> ${weather.temperature} °C</p>

            <p><strong>Humidity:</strong> ${weather.humidity}%</p>

            <p><strong>Rainfall:</strong> ${weather.rain} mm</p>

            <p><strong>Wind Speed:</strong> ${weather.wind_speed} km/h</p>

            <p><strong>Recommendation:</strong> ${weather.recommendation}</p>

        </div>

    `;

}

/* ==========================================
   Activities
========================================== */

function renderActivities(activities){

    if(!activities || activities.length===0){

        return "";

    }

    let html = `

        <div class="result-section">

            <h3>🌱 Farm Activities</h3>

            <table class="result-table">

                <thead>

                    <tr>

                        <th>Activity</th>

                        <th>Date</th>

                        <th>Priority</th>

                        <th>Workers</th>

                    </tr>

                </thead>

                <tbody>

    `;

    activities.forEach(function(activity){

        html += `

            <tr>

                <td>${activity.name}</td>

                <td>${activity.date}</td>

                <td>${activity.priority}</td>

                <td>${activity.workers_required}</td>

            </tr>

        `;

    });

    html += `

                </tbody>

            </table>

        </div>

    `;

    return html;

}

/* ==========================================
   Resource Allocation
========================================== */

function renderResources(resource){

    if(!resource){

        return "";

    }

    return `

        <div class="result-section">

            <h3>👨‍🌾 Resource Allocation</h3>

            <p>

                <strong>Total Workers Required:</strong>

                ${resource.total_workers_required}

            </p>

            <p>

                <strong>Equipment:</strong>

                ${resource.equipment_required.join(", ")}

            </p>

        </div>

    `;

}

/* ==========================================
   Conflicts
========================================== */

function renderConflicts(conflicts){

    if(!conflicts || conflicts.length===0){

        return `

            <div class="result-section">

                <h3>⚠ Conflicts</h3>

                <p>No scheduling conflicts detected.</p>

            </div>

        `;

    }

    let html = `

        <div class="result-section">

            <h3>⚠ Conflicts</h3>

            <ul>

    `;

    conflicts.forEach(function(conflict){

        html += `

            <li>

                ${conflict.date}

                -

                Workers Needed:

                ${conflict.workers_needed}

                |

                Available:

                ${conflict.workers_available}

            </li>

        `;

    });

    html += `

            </ul>

        </div>

    `;

    return html;

}

/* ==========================================
   Recommendations
========================================== */

function renderRecommendations(recommendations){

    if(!recommendations || recommendations.length===0){

        return "";

    }

    let html = `

        <div class="result-section">

            <h3>🌾 Crop Management Recommendations</h3>

            <ul>

    `;

    recommendations.forEach(function(recommendation){

        html += `

            <li>

                <strong>${recommendation.title}</strong>

                -

                ${recommendation.suggested_action}

            </li>

        `;

    });

    html += `

            </ul>

        </div>

    `;

    return html;

}

/* ==========================================
   Calendar
========================================== */

function renderCalendar(calendar){

    if(!calendar || calendar.length===0){

        return "";

    }

    let html = `

        <div class="result-section">

            <h3>📅 Calendar</h3>

            <table class="result-table">

                <thead>

                    <tr>

                        <th>Date</th>

                        <th>Title</th>

                    </tr>

                </thead>

                <tbody>

    `;

    calendar.forEach(function(event){

        html += `

            <tr>

                <td>${event.date}</td>

                <td>${event.title}</td>

            </tr>

        `;

    });

    html += `

                </tbody>

            </table>

        </div>

    `;

    return html;

}

function showSuccessMessage(message){

    const notification = document.createElement("div");

    notification.className = "success-message";

    notification.textContent = message;

    document.body.appendChild(notification);

    setTimeout(function(){

        notification.remove();

    },3000);

}

function getCurrentLocation(){

    if(!navigator.geolocation){

        alert("Geolocation is not supported.");

        return;

    }

    navigator.geolocation.getCurrentPosition(

        function(position){

            document.getElementById("latitude").value =
                position.coords.latitude.toFixed(6);

            document.getElementById("longitude").value =
                position.coords.longitude.toFixed(6);

        },

        function(){

            alert("Unable to retrieve location.");

        }

    );

}

/* ==========================================
Submit Planner
========================================== */

async function submitPlanner(event){

    event.preventDefault();

    try{

        const loadingBox = document.getElementById(

            "loadingBox"

        );

        const result = document.getElementById(

            "planResult"

        );

        loadingBox.classList.remove(

            "hidden"

        );

        result.innerHTML = "";

        const request = {

            crop:
                document.getElementById(
                    "crop"
                ).value,

            planting_date:
                document.getElementById(
                    "plantingDate"
                ).value,

            farm_size:Number(
                document.getElementById(
                    "farmSize"
                ).value
            ),

            workers:Number(
                document.getElementById(
                    "workers"
                ).value
            ),

            soil_type:
                document.getElementById(
                    "soilType"
                ).value,

            season:
                document.getElementById(
                    "season"
                ).value,

            latitude:parseFloat(
                document.getElementById(
                    "latitude"
                ).value
            ),

            longitude:parseFloat(
                document.getElementById(
                    "longitude"
                ).value
            )

        };

        let plan;

        /* ======================================
           UPDATE EXISTING PLAN
        ====================================== */

        if(editPlanId){

            plan = await updateFarmPlan(

                editPlanId,

                request

            );

            showSuccess(

                "Farm plan updated successfully."

            );

            localStorage.removeItem(

                "edit_plan_id"

            );

            editPlanId = null;

            document.getElementById(

                "submitButton"

            ).textContent =

                "Generate Farm Plan";

            document.getElementById(

                "pageTitle"

            ).textContent =

                "Generate Farm Activity Plan";

        }

        /* ======================================
           GENERATE NEW PLAN
        ====================================== */

        else{

            plan = await generatePlan(

                request

            );

            showSuccess(

                "Farm plan generated successfully."

            );

        }

        loadingBox.classList.add(

            "hidden"

        );

        localStorage.setItem(

            "latest_plan",

            JSON.stringify(plan)

        );

        displayPlan(plan);

    }

    catch(error){

        document.getElementById(

            "loadingBox"

        ).classList.add(

            "hidden"

        );

        console.error(error);

        alert(

            "Unable to save farm plan."

        );

    }

}

/* ==========================================
Success Notification
========================================== */

function showSuccess(message){

    const result = document.getElementById(

        "planResult"

    );

    result.innerHTML = `

        <div
            style="
                background:#e8f5e9;
                color:#2e7d32;
                padding:15px;
                border-radius:8px;
                margin-bottom:20px;
                font-weight:600;
            "
        >

            ✅ ${message}

        </div>

    `;

}

/* ==========================================
Fill Planner Form
========================================== */

function fillForm(plan){

    document.getElementById(

        "crop"

    ).value = plan.crop;

    document.getElementById(

        "plantingDate"

    ).value = plan.planting_date;

    document.getElementById(

        "farmSize"

    ).value = plan.farm_size;

    document.getElementById(

        "workers"

    ).value = plan.workers;

    document.getElementById(

        "latitude"

    ).value = plan.latitude;

    document.getElementById(

        "longitude"

    ).value = plan.longitude;

    /* ======================================
       Optional Fields
    ====================================== */

    if(plan.soil_type){

        document.getElementById(

            "soilType"

        ).value = plan.soil_type;

    }

    if(plan.season){

        document.getElementById(

            "season"

        ).value = plan.season;

    }

}

/* ==========================================
Disable Form
========================================== */

function disableForm(){

    const controls = document.querySelectorAll(

        "#plannerForm input, #plannerForm select"

    );

    controls.forEach(function(control){

        control.disabled = true;

    });

}

/* ==========================================
Enable Form
========================================== */

function enableForm(){

    const controls = document.querySelectorAll(

        "#plannerForm input, #plannerForm select"

    );

    controls.forEach(function(control){

        control.disabled = false;

    });

}