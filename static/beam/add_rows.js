document.addEventListener("DOMContentLoaded", () => {


    // support rows

    const addSupportFormBtn = document.querySelector('#add-Supports-form');
    const addPointLoadFormBtn = document.querySelector('#add-Point-Loads-form');
    const addPointTorqueFormBtn = document.querySelector('#add-Point-Torques-form');
    const addDistributedLoadFormBtn = document.querySelector('#add-Distributed-Loads-form');
    const addQueryFormBtn = document.querySelector('#add-Query-form');

    const supportForm = document.getElementsByClassName("formset-row-Supports");
    const pointLoadForm = document.getElementsByClassName("formset-row-Point-Loads");
    const pointTorqueForm = document.getElementsByClassName("formset-row-Point-Torques");
    const distributedLoadForm = document.getElementsByClassName("formset-row-Distributed-Loads");
    const queryForm = document.getElementsByClassName("formset-row-Query");

    const mainSupportForm = document.querySelector('#formset-Supports');
    const mainPointLoadForm = document.querySelector('#formset-Point-Loads');
    const mainPointTorqueForm = document.querySelector('#formset-Point-Torques');
    const mainDistributedLoadForm = document.querySelector('#formset-Distributed-Loads');
    const mainQueryForm = document.querySelector('#formset-Query');

    const totalSupportForms = document.querySelector('#id_support-TOTAL_FORMS');
    const totalPointLoadForms = document.querySelector('#id_point_load-TOTAL_FORMS');
    const totalPointTorqueForms = document.querySelector('#id_point_torque-TOTAL_FORMS');
    const totalDistributedLoadForms = document.querySelector('#id_distributed_load-TOTAL_FORMS');
    const totalQueryForms = document.querySelector('#id_query-TOTAL_FORMS');

    let supportFormCount = supportForm.length - 1;
    let pointLoadFormCount = pointLoadForm.length - 1;
    let pointTorqueFormCount = pointTorqueForm.length - 1;
    let distributedLoadFormCount = distributedLoadForm.length - 1;
    let queryFormCount = queryForm.length - 1;

    addSupportFormBtn.addEventListener('click', function (event) {
        event.preventDefault();
        
        // clone a New Form
        const newSupportForm = supportForm[0].cloneNode(true);

        //get end position
        const supportEnd = document.querySelector('#end-row-Supports');

        supportFormCount++;
        const supportFormRegex = RegExp(`support-(\\d){1}-`, 'g');

        newSupportForm.innerHTML = newSupportForm.innerHTML.replace(supportFormRegex, `support-${supportFormCount}-`)

        // Insert before something lol
        mainSupportForm.insertBefore(newSupportForm, supportEnd);
        totalSupportForms.setAttribute('value', `${supportFormCount+1}`);

    });

    addPointLoadFormBtn.addEventListener('click', function (event) {
        event.preventDefault();
        
        // clone a New Form
        const newPointLoadForm = pointLoadForm[0].cloneNode(true);

        //get end position
        const pointLoadEnd = document.querySelector('#end-row-Point-Loads');

        pointLoadFormCount++;
        const pointLoadFormRegex = RegExp(`point_load-(\\d){1}-`, 'g');

        newPointLoadForm.innerHTML = newPointLoadForm.innerHTML.replace(pointLoadFormRegex, `point_load-${pointLoadFormCount}-`)

        // Insert before something lol
        mainPointLoadForm.insertBefore(newPointLoadForm, pointLoadEnd);
        totalPointLoadForms.setAttribute('value', `${pointLoadFormCount+1}`);

    });

    addPointTorqueFormBtn.addEventListener('click', function (event) {
        event.preventDefault();
        
        // clone a New Form
        const newPointTorqueForm = pointTorqueForm[0].cloneNode(true);

        //get end position
        const pointTorqueEnd = document.querySelector('#end-row-Point-Torques');

        pointTorqueFormCount++;
        const pointTorqueFormRegex = RegExp(`point_torque-(\\d){1}-`, 'g');

        newPointTorqueForm.innerHTML = newPointTorqueForm.innerHTML.replace(pointTorqueFormRegex, `point_torque-${pointTorqueFormCount}-`)

        // Insert before something lol
        mainPointTorqueForm.insertBefore(newPointTorqueForm, pointTorqueEnd);
        totalPointTorqueForms.setAttribute('value', `${pointTorqueFormCount+1}`);

    });

    addDistributedLoadFormBtn.addEventListener('click', function (event) {
        event.preventDefault();
        
        // clone a New Form
        const newDistributedLoadForm = distributedLoadForm[0].cloneNode(true);

        //get end position
        const distributedLoadEnd = document.querySelector('#end-row-Distributed-Loads');

        distributedLoadFormCount++;
        const distributedLoadFormRegex = RegExp(`distributed_load-(\\d){1}-`, 'g');

        newDistributedLoadForm.innerHTML = newDistributedLoadForm.innerHTML.replace(distributedLoadFormRegex, `distributed_load-${distributedLoadFormCount}-`)

        // Insert before something lol
        mainDistributedLoadForm.insertBefore(newDistributedLoadForm, distributedLoadEnd);
        totalDistributedLoadForms.setAttribute('value', `${distributedLoadFormCount+1}`);

    });

    addQueryFormBtn.addEventListener('click', function (event) {
        event.preventDefault();
        
        // clone a New Form
        const newQueryForm = queryForm[0].cloneNode(true);

        //get end position
        const queryEnd = document.querySelector('#end-row-Query');

        queryFormCount++;
        const queryFormRegex = RegExp(`query-(\\d){1}-`, 'g');

        newQueryForm.innerHTML = newQueryForm.innerHTML.replace(queryFormRegex, `query-${queryFormCount}-`)

        // Insert before something lol
        mainQueryForm.insertBefore(newQueryForm, queryEnd);
        totalQueryForms.setAttribute('value', `${queryFormCount+1}`);

    });

    function updateForms() {
        //supports
        var count = 0;
        const supportFormRegex = RegExp(`support-(\\d){1}-`, 'g');
        for (let form of supportForm) {
            for (let cell of form.children) {
                for (let input of cell.children){
                    input.name = input.name.replace(supportFormRegex, `support-${count}-`);
                    input.id = input.id.replace(supportFormRegex, `support-${count}-`);
                }
            }
            count++;
        }
        
        //point loads
        var count = 0;
        const pointLoadFormRegex = RegExp(`point_load-(\\d){1}-`, 'g');
        for (let form of pointLoadForm) {
            for (let cell of form.children) {
                for (let input of cell.children){
                    input.name = input.name.replace(pointLoadFormRegex, `point_load-${count}-`);
                    input.id = input.id.replace(pointLoadFormRegex, `point_load-${count}-`);
                }
            }
            count++;
        }

        //point torques
        var count = 0;
        const pointTorqueFormRegex = RegExp(`point_torque-(\\d){1}-`, 'g');
        for (let form of pointTorqueForm) {
            for (let cell of form.children) {
                for (let input of cell.children){
                    input.name = input.name.replace(pointTorqueFormRegex, `point_torque-${count}-`);
                    input.id = input.id.replace(pointTorqueFormRegex, `point_torque-${count}-`);
                }
            }
            count++;
        }

        // distributed loads
        var count = 0;
        const distributedLoadFormRegex = RegExp(`distributed_load-(\\d){1}-`, 'g');
        for (let form of distributedLoadForm) {
            for (let cell of form.children) {
                for (let input of cell.children){
                    input.name = input.name.replace(distributedLoadFormRegex, `distributed_load-${count}-`);
                    input.id = input.id.replace(distributedLoadFormRegex, `distributed_load-${count}-`);
                }
            }
            count++;
        }

        //query
        var count = 0;
        const queryFormRegex = RegExp(`query-(\\d){1}-`, 'g');
        for (let form of queryForm) {
            for (let cell of form.children) {
                for (let input of cell.children){
                    input.name = input.name.replace(queryFormRegex, `query-${count}-`);
                    input.id = input.id.replace(queryFormRegex, `query-${count}-`);
                }
            }
            count++;
        }
    };

    mainSupportForm.addEventListener("click", function(event) {
        if (event.target.classList.contains("delete-Supports-form")) {
            event.preventDefault();
            if (supportFormCount > 0) {
                event.target.parentElement.parentElement.remove();
                supportFormCount--;
                totalSupportForms.setAttribute('value', `${supportFormCount+1}`);
                updateForms();
            }
        }
    })

    mainPointLoadForm.addEventListener("click", function(event) {
        if (event.target.classList.contains("delete-Point-Loads-form")) {
            event.preventDefault();
            if (pointLoadFormCount > 0) {
                event.target.parentElement.parentElement.remove();
                pointLoadFormCount--;
                totalPointLoadForms.setAttribute('value', `${pointLoadFormCount+1}`);
                updateForms();
            }
        }
    })

    mainPointTorqueForm.addEventListener("click", function(event) {
        if (event.target.classList.contains("delete-Point-Torques-form")) {
            event.preventDefault();
            if (pointTorqueFormCount > 0) {
                event.target.parentElement.parentElement.remove();
                pointTorqueFormCount--;
                totalPointTorqueForms.setAttribute('value', `${pointTorqueFormCount+1}`);
                updateForms();
            }
        }
    })

    mainDistributedLoadForm.addEventListener("click", function(event) {
        if (event.target.classList.contains("delete-Distributed-Loads-form")) {
            event.preventDefault();
            if (distributedLoadFormCount > 0) {
                event.target.parentElement.parentElement.remove();
                distributedLoadFormCount--;
                totalDistributedLoadForms.setAttribute('value', `${distributedLoadFormCount+1}`);
                updateForms();
            }
        }
    })

    mainQueryForm.addEventListener("click", function(event) {
        if (event.target.classList.contains("delete-Query-form")) {
            event.preventDefault();
            if (queryFormCount > 0) {
                event.target.parentElement.parentElement.remove();
                queryFormCount--;
                totalQueryForms.setAttribute('value', `${queryFormCount+1}`);
                updateForms();
            }
        }
    })

});