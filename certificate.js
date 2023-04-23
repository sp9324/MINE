function printPageToPDF() {
    window.print();
}


const name = localStorage.getItem('name');
const course = localStorage.getItem('course');

document.getElementById("congrats").innerHTML=`Congrats on completing the course on ${course}, ${name}!`


