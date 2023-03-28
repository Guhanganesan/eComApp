console.log("Guhan Ganesan")

var updatebtns = document.getElementsByClassName('update-cart');

for(var i=0; i<updatebtns.length; i++){
    updatebtns[i].addEventListener('click', function(){
        var product_id = this.dataset.product;
        var action = this.dataset.action;
        console.log('Product Id: ', product_id, 'Action', action);
    })
}