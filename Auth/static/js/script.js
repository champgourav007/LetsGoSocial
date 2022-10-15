let staticEmailContainer = document.getElementById("staticEmail");
let inputEmailContainer = document.getElementById('exampleInputEmail1');
inputEmailContainer.addEventListener('keydown', changeTheEmail);

function changeTheEmail(){
    let email = this.value;
    staticEmailContainer.value = email;
}