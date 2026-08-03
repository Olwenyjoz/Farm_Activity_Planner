/*
=========================================================
Calendar Page
=========================================================
*/

requireLogin();

document.addEventListener(

    "DOMContentLoaded",

    function(){

        initializeCalendar();

        initializeLogout();

    }

);

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
Load Calendar
========================================== */

function initializeCalendar(){

    const plan = JSON.parse(

        localStorage.getItem(

            "latest_plan"

        )

    );

    if(!plan){

        return;

    }

    renderCalendar(

        plan.calendar

    );

}

/* ==========================================
Render Calendar
========================================== */

function renderCalendar(calendar){

    const tbody =

        document.getElementById(

            "calendarBody"

        );

    if(

        !calendar ||

        calendar.length===0

    ){

        tbody.innerHTML =

        `

        <tr>

            <td colspan="4" class="empty">

                No calendar generated.

            </td>

        </tr>

        `;

        return;

    }

    let html = "";

    calendar.forEach(

        function(event){

            html +=

            `

            <tr>

                <td>

                    ${event.date}

                </td>

                <td>

                    ${event.title}

                </td>

                <td>

                    <span class="${event.priority.toLowerCase()}">

                        ${event.priority}

                    </span>

                </td>

                <td>

                    <span class="status">

                        ${event.status}

                    </span>

                </td>

            </tr>

            `;

        }

    );

    tbody.innerHTML = html;

}