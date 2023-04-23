const form = document.getElementById('myForm')
const name=document.getElementById('name')
const course=document.getElementById('course')

form.addEventListener('submit', function(e){
	e.preventDefault();

	const nameValue=name.value;
	const courseValue=course.value;

	localStorage.setItem('name', nameValue);
	localStorage.setItem('course', courseValue);

	window.location.href="certificate.html";
	})
