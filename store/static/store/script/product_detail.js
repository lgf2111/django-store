const quantity = document.getElementById("quantity");
function minusQuantity() {
  quantity.value > 0 ? quantity.value-- : null;
}
function plusQuantity() {
  quantity.value++;
}
function checkQuantity() {
  quantity.value = quantity.value
    .replace(/[^0-9.]/g, "")
    .replace(/(\..*)\./g, "$1");
}
function checkQuantityNull() {
  quantity.value === "" ? (quantity.value = 0) : null;
}

function playerImg() {
  let playerImg = document.getElementById("playerimg");
  if (!playerImg) {
    playerImg = document.createElement("img");
    playerImg.id = "playerimg";
    document.getElementById("playerbox").appendChild(playerImg);
  }
  return playerImg;
}

function setPlayerImg(src) {
  playerImg().setAttribute("src", src);
}

const imgs = document.getElementsByClassName("product-image");

for (let i = 0; i < imgs.length; i++) {
  const el = imgs[i];
  el.addEventListener("click", () => setPlayerImg(el.src), false);
}
