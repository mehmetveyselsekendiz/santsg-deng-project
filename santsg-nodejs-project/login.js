const username = "admin"
const password = "admin"
let passed_username
let passed_password
let passed_url

const form_dom = document.querySelector("#form")
form_dom.addEventListener('submit', form_submit)
const username_dom = document.querySelector("#username")
const password_dom = document.querySelector("#password")
const url_dom = document.querySelector("#data-url")

function form_submit(event) {
    event.preventDefault()
    console.log("OK")
    passed_username = username_dom.value
    passed_password = password_dom.value
    if(username == passed_username &&  password == passed_password){
        passed_url = encodeURIComponent(url_dom.value)
        window.location.replace(`/data-monitoring/${passed_url}`)
    }
    else{
        window.location.replace("/")
    }
}

// page redirection solution
// https://www.codegrepper.com/code-examples/javascript/send+to+link+js

// passing url problem as parameter
// https://stackoverflow.com/questions/1737935/what-is-the-recommended-way-to-pass-urls-as-url-parameters


