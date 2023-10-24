//logica para obtener los valores del input(inicio)-->

const input = document.getElementById("user-input");
const button = document.getElementById("submit-btn");

button.addEventListener("click", function (event) {
  event.preventDefault(); // Evitar que se recargue la página
  const user_input = input.value;
  send_message(user_input);
  input.value = "";
});
//logica de poner respuesta de usuario en chat(inicio)
//logica de poner respuesta de usuario en chat(fin)

input.addEventListener("keyup", function (event) {
  if (event.key === "Enter") {
    event.preventDefault();
    button.click();
  }
});
//logica de poner respuesta de BOT en chat(inicio)
//logica de poner respuesta de BOT en chat(fin)

//logica para obtener los valores del input(fin)-->


//var url = "http://localhost:5000/get_response";

// función para leer el archivo JSON
function getResponse() {
  fetch("/static/response.json")
      .then(response => response.json())
      .then(data => {
        // mostrar respuesta en el chatbot
        var chat = document.getElementById("chat-container");
        var respuesta = document.createElement("div");
        respuesta.classList.add("respuesta");
        respuesta.innerHTML = data.respuesta;
        chat.appendChild(respuesta);
      });
  }
  
  // llamar a la función para leer el archivo JSON cada 5 segundos
  setInterval(getResponse, 5000);


  function update_chat(response) {
    const chat_container = document.getElementById("chat-container");
    const new_message = document.createElement("div");
    new_message.classList.add("chat-message");
    new_message.classList.add("bot");
    new_message.innerHTML = "<p>" + response + "</p>";
    chat_container.appendChild(new_message);
  }
  
  function send_message(user_input) {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
      if (this.readyState === 4 && this.status === 200) {
        const response = JSON.parse(this.responseText)["respuesta"];
        update_chat(response);
        console.log("respuesta de bot enviada correctamente");
      } else {
        console.log("error al mandar la respuesta del bot");
      }
    };
    xhr.open("POST", "/get_response");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify({ user_input: user_input }));
  }
 //Codigo que indica por consola si el user_input fue mandado correctamente al servidor(fin)

 //Movimiento de los ojos (inicio)
document.querySelector("body").addEventListener
("mousemove", eyeball);

function eyeball(){
var eye = document.querySelectorAll(".eye");
eye.forEach(function(eye) {
let x = eye.getBoundingClientRect().left + eye.clientWidth / 2;
let y = eye.getBoundingClientRect().top + eye.clientHeight / 2; 
let radian = Math.atan2(event.pageX-x, event.pageY - y); 

let rot = radian * (180 / Math.PI) * -1 + 270;
eye.style.transform = "rotate(" + rot + "deg)";  });  
}
//Movimiento de los ojos (fin)