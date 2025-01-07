// 🌟 Exercise 6 : Fortune teller
// Instructions
// Create a self invoking function that takes 4 arguments: number of children, partner’s name, geographic location, job title.
// The function should display in the DOM a sentence like "You will be a <job title> in <geographic location>, and married to <partner's name> with <number of children> kids."

(function (numChild, partnerName, location, job) {
  const sentence = `You will be a ${job} in ${location}, and married to ${partnerName} with ${numChild} kids.`;

  const par = document.getElementById('justInCase');
  par.innerText = sentence;
})(19, 'Delores', 'Montana', 'Tuba Player');

(function (job) {
  const sentence = `You love being a ${job}`;

  const par = document.getElementById('justInCase2');
  par.innerText = sentence;
})('cement mixer');
