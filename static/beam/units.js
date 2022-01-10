function units() {
    var units = document.getElementById('id_units-units').value;
    if (units == 'metric') {
        document.querySelectorAll('.Units-div').forEach(function(div) {
            var unit_id = div.getElementsByTagName('select')[0].id;
            var suffix = unit_id.substring(unit_id.length-1);
            if (suffix == 'i') {
                div.style.display = 'none';
            } else {
                div.style.display = 'block';
            };
        });
    }
    else {
        document.querySelectorAll('.Units-div').forEach(function(div) {
            var unit_id = div.getElementsByTagName('select')[0].id;
            var suffix = unit_id.substring(unit_id.length-1);
            if (suffix == 'm') {
                div.style.display = 'none';
            } else {
                div.style.display = 'block';
            };
        });
    }
};

function unit_suffix() {
    var units = document.getElementById('id_units-units').value;
    if (units == 'metric') {
        var suffix = 'm'
    } else {
        var suffix = 'i'
    }
    var length = document.getElementById(`id_units-length_${suffix}`).selectedOptions[0].text;
    var force = document.getElementById(`id_units-force_${suffix}`).selectedOptions[0].text;
    var moment = document.getElementById(`id_units-moment_${suffix}`).selectedOptions[0].text;
    var distributed = document.getElementById(`id_units-distributed_${suffix}`).selectedOptions[0].text;
    var stiffness = document.getElementById(`id_units-stiffness_${suffix}`).selectedOptions[0].text;
    var A = document.getElementById(`id_units-A_${suffix}`).selectedOptions[0].text;
    var E = document.getElementById(`id_units-E_${suffix}`).selectedOptions[0].text;
    var I = document.getElementById(`id_units-I_${suffix}`).selectedOptions[0].text;

    var beam_length = document.getElementById('Beam-Length').getElementsByTagName('label')[0];
    beam_length.innerText = beam_length.innerText.split('(')[0] + ` (${length})`;

    var beam_A = document.getElementById('Beam-A').getElementsByTagName('label')[0];
    beam_A.innerText = beam_A.innerText.split('(')[0] + ` (${A})`;

    var beam_E = document.getElementById('Beam-E').getElementsByTagName('label')[0];
    beam_E.innerText = beam_E.innerText.split('(')[0] + ` (${E})`;

    var beam_I = document.getElementById('Beam-I').getElementsByTagName('label')[0];
    beam_I.innerText = beam_I.innerText.split('(')[0] + ` (${I})`;

    document.querySelectorAll('.Coordinate').forEach(function(th) {
        th.innerText = th.innerText.split('(')[0] + ` (${length})`;
    });

    document.querySelectorAll('.Support').forEach(function(th) {
        th.innerText = th.innerText.split('(')[0] + ``;
    });

    document.querySelectorAll('.Force').forEach(function(th) {
        th.innerText = th.innerText.split('(')[0] + ` (${force})`;
    });

    document.querySelectorAll('.Angle').forEach(function(th) {
        th.innerText = th.innerText.split('(')[0] + ` (deg)`;
    });

    document.querySelectorAll('.Torque').forEach(function(th) {
        th.innerText = th.innerText.split('(')[0] + ` (${moment})`;
    });

    document.querySelectorAll('.coordinate').forEach(function(th) {
        th.innerText = th.innerText.split('(')[0] + ` (${length})`;
    });

    document.querySelectorAll('.load').forEach(function(th) {
        th.innerText = th.innerText.split('(')[0] + ` (${distributed})`;
    });

    document.querySelectorAll('.Query').forEach(function(th) {
        th.innerText = th.innerText.split('(')[0] + ` (${length})`;
    });  
};

document.addEventListener("DOMContentLoaded", () => {
    units();
    unit_suffix();
    document.getElementById('id_units-units').onchange = units;
    document.getElementById('myTab').addEventListener('click', unit_suffix);
});
