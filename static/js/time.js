
var inputMyDate = document.querySelector('input#leashdate');

inputMyDate.addEventListener('input', function() {
    var current = this.value;
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1;
    var yyyy = today.getFullYear();
    if(dd<10){
        dd='0'+dd;
    }
    if(mm<10){
        mm='0'+mm;
    }
    var today = yyyy+'-'+mm+'-'+dd;
    if (current < today){
        document.getElementById('leashdate').value = today;
    }
});