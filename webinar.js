// JavaScript code for handling webinar registration form

const form = document.getElementById("webinar-form");

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const topic = document.getElementById("topic").value;
  const date = document.getElementById("date").value;

  console.log(`Name: ${name}`);
  console.log(`Email: ${email}`);
  console.log(`Topic: ${topic}`);
  console.log(`Date: ${date}`);

  alert("Thank you for registering for the webinar!");
});


