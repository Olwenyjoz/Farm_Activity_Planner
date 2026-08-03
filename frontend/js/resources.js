requireLogin();

document.addEventListener(

    "DOMContentLoaded",

    function(){

        loadResources();

        document
            .getElementById("logoutBtn")
            .addEventListener(

                "click",

                function(e){

                    e.preventDefault();

                    logout();

                }

            );

    }

);

function loadResources(){

    const plan = JSON.parse(

        localStorage.getItem(

            "latest_plan"

        )

    );

    if(!plan){

        return;

    }

    document.getElementById(

        "workersRequired"

    ).textContent =

        plan.resource_report.total_workers_required;

    document.getElementById(

        "equipmentCount"

    ).textContent =

        plan.resource_report.equipment_required.length;

    document.getElementById(

        "conflictCount"

    ).textContent =

        plan.conflicts.length;

    renderEquipment(

        plan.resource_report.equipment_required

    );

    renderConflicts(

        plan.conflicts

    );

}

function renderEquipment(items){

    const list =

        document.getElementById(

            "equipmentList"

        );

    list.innerHTML = "";

    items.forEach(

        function(item){

            list.innerHTML +=

            `<li>${item}</li>`;

        }

    );

}

function renderConflicts(conflicts){

    const tbody =

        document.getElementById(

            "conflictTable"

        );

    if(conflicts.length===0){

        tbody.innerHTML=

        `<tr>

            <td colspan="4">

                No scheduling conflicts.

            </td>

        </tr>`;

        return;

    }

    let html="";

    conflicts.forEach(

        function(conflict){

            html+=`

            <tr>

                <td>${conflict.date}</td>

                <td>${conflict.workers_needed}</td>

                <td>${conflict.workers_available}</td>

                <td>${conflict.worker_shortage}</td>

            </tr>

            `;

        }

    );

    tbody.innerHTML=html;

}