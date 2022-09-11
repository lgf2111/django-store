const currency = document.getElementById('currency')
const prices = Array.from(document.getElementsByClassName('price'))
const rate = {'SGD':1, 'USD':.7, 'RMB':5,}

let client_currency = localStorage.getItem('currency')
if (client_currency === null) {
    localStorage.setItem('currency', 'SGD')
    client_currency = localStorage.getItem('currency')
}
currency.innerText = client_currency

prices.map(price => {
    let newPrice = parseInt(price.innerText)*rate[currency.innerText]
    price.innerText = `${currency.innerText}${newPrice}`
})

function toUSD() {
    let original = localStorage.getItem('currency')
    currency.innerText = 'USD'
    prices.map(price => {
        let newPrice = (parseInt(price.innerText.substring(3))/rate[original])*rate[currency.innerText]
        price.innerText = `${currency.innerText}${newPrice}`
    })
    localStorage.setItem('currency', 'USD')
}

function toSGD() {
    let original = localStorage.getItem('currency')
    currency.innerText = 'SGD'
    prices.map(price => {
        let newPrice = (parseInt(price.innerText.substring(3))/rate[original])*rate[currency.innerText]
        price.innerText = `${currency.innerText}${newPrice}`
    })
    localStorage.setItem('currency', 'SGD')
}

function toRMB() {
    let original = localStorage.getItem('currency')
    currency.innerText = 'RMB'
    prices.map(price => {
        let newPrice = (parseInt(price.innerText.substring(3))/rate[original])*rate[currency.innerText]
        price.innerText = `${currency.innerText}${newPrice}`
    })
    localStorage.setItem('currency', 'RMB')
}
