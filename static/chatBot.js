var url = "http://localhost:5000/get_response";

// función para leer el archivo JSON
function getResponse() {
    fetch('../py/response.json')
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
        console.log("respuesta de bot enviada correctamente")
      } else{console.log("error al mandar la respuesta del bot")}
    };
    xhr.open("POST", "/get_response");
   // xhr.open("POST", "http://localhost:5000/get_response");

    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(JSON.stringify({ user_input: user_input }));
  }
 //Codigo que indica por consola si el user_input fue mandado correctamente al servidor(fin)