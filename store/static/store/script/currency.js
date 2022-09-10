const currency = document.getElementById('currency')
const prices = Array.from(document.getElementsByClassName('price'))
rate = {'SGD':1, 'USD':.71, 'RMB':4.95,}

prices.map(price => {
    price.innerText = `${currency.innerText}${parseInt(price.innerText)*rate[currency.innerText]}`
})

currency.addEventListener('change', ()=>{
    prices.map(price => {
        price.innerText = `${currency.innerText}${parseInt(price.innerText)*rate[currency.innerText]}`
    })
})

function toUSD() {
    currency.innerText = 'USD'
    console.log(currency)
}