const url = 'https://api.chucknorris.io/jokes/random?category=dev';

const button = document.getElementById('getButton');
const par = document.getElementById('info');

function getJoke() {
  fetch(url)
    .then((response) => response.json())
    .then((data) => (par.textContent = data['value']))
    .catch((error) => console.log(error))
    .finally(() => console.log('all done'));
}

button.addEventListener('click', getJoke);
