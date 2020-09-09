
var price = document.getElementById("serviceprice");

document.getElementById("serviceoptions").addEventListener('change', function() {
  var selected = this.options[this.selectedIndex];
  var txt = selected.dataset.price;
  price.innerText = txt;
});