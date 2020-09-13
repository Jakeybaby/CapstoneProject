var updatebtns = document.getElementsByClassName('update-cart')
//
// var inputMyDate = document.querySelector('input#leashdate');
//
// inputMyDate.addEventListener('input', function() {
//     var current = this.value;
//     var today = new Date();
//     var dd = today.getDate();
//     var mm = today.getMonth()+1;
//     var yyyy = today.getFullYear();
//     if(dd<10){
//         dd='0'+dd;
//     }
//     if(mm<10){
//         mm='0'+mm;
//     }
//     var today = yyyy+'-'+mm+'-'+dd;
//     if (current < today){
//         document.getElementById('leashdate').value = today;
//     }
// });

for (i=0;i<updatebtns.length;i++){
    updatebtns[i].addEventListener('click',function (){
        var equipmentID = this.dataset.equipment
        var action = this.dataset.action
        console.log("equipmentID:",equipmentID, 'action：',action)

        console.log('USER:',user)
        if(user == 'AnonymousUser'){
            console.log('user is not auth')
        }else {
            updateUserOrder(equipmentID,action)
        }

    })
}

function updateUserOrder(equipmentID,action){
    console.log('User is auth, sending')

    var url = '/update_item/'

    fetch(url,{
        method:"POST",
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'equipmentID':equipmentID,'action':action})
    })

        .then((response)=>{
            return response.json()
        })

         .then((data)=>{
            console.log('data:',data)
             location.reload()
        })
}