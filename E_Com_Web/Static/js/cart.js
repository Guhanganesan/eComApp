console.log("Guhan Ganesan")

var updatebtns = document.getElementsByClassName('update-cart');

for(var i=0; i<updatebtns.length; i++){
    updatebtns[i].addEventListener('click', function(){
        var product_id = this.dataset.product;
        var action = this.dataset.action;
        console.log('Product Id: ', product_id, 'Action', action);

        console.log('user:', user);
        if(user == 'guhan_test@gmail.com'){
            // console.log('user is authenticated')
            updateUserOrder(product_id, action);
        }else{
            console.log('user is not authenticated')
        }

    })
}

function updateUserOrder(product_id, action){
    console.log('User is authenticated');

    var url = '/update_item/'; // view.py file 
    fetch(
        url, 
        {
            method:'POST', headers:{'Content-Type':'Application/json', 'X-CSRFToken':csrftoken},
            body:JSON.stringify({'product_id':product_id, 'action':action})
        }
    ).then((response)=>{
        return response.json();
    }).then((data)=>{
        console.log(data);
    })
}