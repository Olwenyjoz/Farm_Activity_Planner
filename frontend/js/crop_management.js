requireLogin();

document.addEventListener(

    "DOMContentLoaded",

    function(){

        loadRecommendations();

        document
            .getElementById("logoutBtn")
            .addEventListener(

                "click",

                function(event){

                    event.preventDefault();

                    logout();

                }

            );

    }

);

function loadRecommendations(){

    const plan = JSON.parse(

        localStorage.getItem(

            "latest_plan"

        )

    );

    if(

        !plan ||

        !plan.recommendations

    ){

        return;

    }

    const container =

        document.getElementById(

            "recommendationList"

        );

    let html = "";

    plan.recommendations.forEach(

        function(item){

            html += `

            <div class="recommendation ${item.severity.toLowerCase()}">

                <h3>${item.title}</h3>

                <p>

                    <strong>Category:</strong>

                    ${item.category}

                </p>

                <p>

                    <strong>Activity:</strong>

                    ${item.activity}

                </p>

                <p>

                    <strong>Date:</strong>

                    ${item.date}

                </p>

                <p>

                    <strong>Reason:</strong>

                    ${item.reason}

                </p>

                <p>

                    <strong>Recommendation:</strong>

                    ${item.suggested_action}

                </p>

            </div>

            `;

        }

    );

    container.innerHTML = html;

}