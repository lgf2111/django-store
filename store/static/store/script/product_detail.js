const quantity = document.getElementById('quantity')
function minusQuantity() {
    quantity.value > 0 ? quantity.value-- : null
}
function plusQuantity() {
    quantity.value++
}
function checkQuantity() {
    quantity.value = quantity.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');
}
function checkQuantityNull() {
    quantity.value === '' ? quantity.value = 0 : null
}