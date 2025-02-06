const apiKey = '538c22dc8a6c06c017f24997778caaba';

let search = document.getElementById('search');

search.addEventListener('change', (e) => fetchLocation(e.target.value));

function changeInput(event) {
  document.getElementById('result1').textContent = event.target.value;
}

function fetchLocation(search) {
  const geolocate = new URL('http://api.openweathermap.org/geo/1.0/direct');
  geolocate.searchParams.set('q', search);
  geolocate.searchParams.set('appid', apiKey);

  fetch(geolocate.href)
    .then((response) => response.json())
    .then((data) => parseLocation(data))
    .then((locationData) =>
      fetchWeather(locationData.lat, locationData.lon, locationData.name)
    )
    .catch((error) => console.log(error))
    .finally(() => console.log('all done'));
}

function parseLocation(locationData) {
  const lat = locationData[0].lat;
  const lon = locationData[0].lon;
  const name = locationData[0].name;
  console.log(name);
  return { lat, lon, name };
}

function fetchWeather(lat, lon, name) {
  const openWeatherUrl = new URL(
    'https://api.openweathermap.org/data/2.5/weather'
  );
  openWeatherUrl.searchParams.set('lat', lat);
  openWeatherUrl.searchParams.set('lon', lon);
  openWeatherUrl.searchParams.set('appid', apiKey);

  // get request
  fetch(openWeatherUrl.href)
    .then((response) => response.json())
    .then((data) => parseWeatherData(data))
    .then((weatherInfo) => displayWeatherInfo(weatherInfo))
    .catch((error) => console.log(error))
    .finally(() => console.log('all done'));
}

// parse data from open weather
function parseWeatherData(currentWeather) {
  const temp = Math.floor(currentWeather.main.temp - 272.15);
  const humid = currentWeather.main.humidity;
  const description = currentWeather.weather[0].description;

  // console.log({ temp, humid, description });
  return { temp, humid, description };
}

// display weather data from API to DOM
function displayWeatherInfo(weatherInfo) {
  const temp = document.getElementById('temperature');
  const humid = document.getElementById('humidity');
  const description = document.getElementById('description');

  const famous = document.getElementById('famous');

  temp.innerHTML = weatherInfo.temp;
  humid.innerHTML = weatherInfo.humid;
  description.innerHTML = weatherInfo.description;

  famous.innerHTML = `<img src="https://www.televisionacademy.com/files/assets/bios/gary-coleman-photofest-450x600.jpg" alt="gary">`;
}
