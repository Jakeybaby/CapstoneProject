var updatebtns = document.getElementsByClassName('update-cart')
// var user = '{{ request.user }}'
//
//             function getToken(name) {
//                     var cookieValue = null;
//                     if (document.cookie && document.cookie !== '') {
//                         var cookies = document.cookie.split(';');
//                         for (var i = 0; i < cookies.length; i++) {
//                             var cookie = cookies[i].trim();
//                             // Does this cookie string begin with the name we want?
//                             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                                 break;
//                             }
//                         }
//                     }
//                     return cookieValue;
//                 }
//                 var csrftoken = getToken('csrftoken')

for (i=0;i<updatebtns.length;i++){
    updatebtns[i].addEventListener('click',function (){
        var equipmentID = this.dataset.equipment
        var action = this.dataset.action
        console.log("equipmentID:",equipmentID, 'action：',action)

        console.log('USER:',user)
        if(user === 'AnonymousUser'){
            console.log('user is not auth')
            needlogin()
        }else {
            updateUserOrder(equipmentID,action)
        }

    })
}

function needlogin() {
    window.location.href = '/logintest/'
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

