console.log('added js')
var toggle = document.querySelector('.bg')
var day = false

var body = document.querySelector('body')


toggle.addEventListener('click', () => {
    if (day) {
        body.style.backgroundColor = "#ebeff5"
        document.querySelectorAll('h5').forEach(e => e.style.color = "black")
        document.querySelector('#icon').classList.remove('fa-sun-o')
        document.querySelector('#icon').classList.add('fa-moon-o')
        day = !day
    } else {
        body.style.backgroundColor = '#333'
        document.querySelectorAll('h5').forEach(e => e.style.color = "white")
        document.querySelector('#icon').classList.remove('fa-moon-o')
        document.querySelector('#icon').classList.add('fa-sun-o')
        day = !day
    }
})