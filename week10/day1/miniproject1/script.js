const robots = [
  {
    id: 1,
    firstName: 'Mendel',
    lastName: 'Dashevsky',
    username: 'Dashevsky',
    email: 'mdesh@sky.com',
    image: 'https://robohash.org/mendel%20dashevsky'
  },
  {
    id: 2,
    firstName: 'Elice',
    lastName: 'Sheiden',
    username: 'Elish',
    email: 'elice@sheiden.com',
    image: 'https://robohash.org/elice%20sheiden'
  },
  {
    id: 3,
    firstName: 'Ryan',
    lastName: 'Friedland',
    username: 'TexasBull',
    email: 'ryan@friedland.com',
    image: 'https://robohash.org/ryan%20friedland'
  },
  {
    id: 4,
    firstName: 'Mark',
    lastName: 'Volkov',
    username: 'Marko',
    email: 'mark@volkov.com',
    image: 'https://robohash.org/ryan%20volkov'
  },
  {
    id: 5,
    firstName: 'Eliran',
    lastName: 'Novik',
    username: 'Eli',
    email: 'eliran@novik.com',
    image: 'https://robohash.org/eliran%20novik'
  },
  {
    id: 6,
    firstName: 'Elena',
    lastName: 'Zht',
    username: 'Elez',
    email: 'elena@zht.com',
    image: 'https://robohash.org/elena%20zht'
  },
  {
    id: 7,
    firstName: 'Ariel',
    lastName: 'Cane',
    username: 'Nerd',
    email: 'ariel@cane.com',
    image: 'https://robohash.org/ariel%20cane'
  },
  {
    id: 8,
    firstName: 'Mickael',
    lastName: 'Mayer',
    username: 'MNM',
    email: 'mickael@mayer.com',
    image: 'https://robohash.org/mickael%20mayer'
  },
  {
    id: 9,
    firstName: 'Aysel',
    lastName: 'Noah',
    username: 'aysel',
    email: 'aysel@noah.com',
    image: 'https://robohash.org/aysel%20noa'
  },
  {
    id: 10,
    firstName: 'Artem',
    lastName: 'Galkov',
    username: 'Arty',
    email: 'artem@galkov.com',
    image: 'https://robohash.org/artem%20galkov'
  },
  {
    id: 11,
    firstName: 'Aaron',
    lastName: 'Wolf',
    username: 'Wolfmath',
    email: 'aaron@wolf.com',
    image: 'https://robohash.org/aaron%20wolf'
  },
  {
    id: 12,
    firstName: 'Avner',
    lastName: 'Maman',
    username: 'mamamia',
    email: 'Avner@Maman.com',
    image: 'https://robohash.org/avner%20maman'
  }
];

const robotContainer = document.getElementById('robot-container');

function robotCardCreator(robotObj) {
  // create card
  const card = document.createElement('div');
  card.className = 'card';
  card.id = robotObj.id;

  // create image
  const image = document.createElement('img');
  image.className = 'robot-image';
  image.src = robotObj.image;

  // create username
  const username = document.createElement('h2');
  username.innerText = robotObj.username;

  // create full name
  const fullName = document.createElement('h2');
  fullName.innerText = `${robotObj.firstName} ${robotObj.lastName}`;

  // create email
  const email = document.createElement('h3');
  email.innerText = robotObj.email;

  // append elements to card
  card.appendChild(image);
  card.appendChild(username);
  card.appendChild(fullName);
  card.appendChild(email);

  return card;
}

function mapRobots(robotArray) {
  robotContainer.innerHTML = '';

  robotArray.map((robot) => {
    card = robotCardCreator(robot);
    robotContainer.appendChild(card);
  });
}

mapRobots(robots);

function filterBots(query) {
  return robots.filter((robot) => {
    return Object.values(robot).some((value) =>
      String(value).toLowerCase().includes(query.toLowerCase())
    );
  });
}

search = document.getElementById('search');

search.addEventListener('input', (e) => {
  e.preventDefault();
  const filtered = filterBots(e.target.value);
  mapRobots(filtered);
});
