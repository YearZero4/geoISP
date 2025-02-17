function execute(){
let ip = document.getElementById('ip').value;

fetch(`http://ip-api.com/json/${ip}`)
  .then(response => {
    if (!response.ok) {
      throw new Error('Error en la petición');
    }
      return response.json();
   })
    .then(data => {
      const formattedData = JSON.stringify(data, null, 2);
      document.getElementById('results').innerHTML = `<pre>${formattedData}</pre>`;
   })
    .catch(error => {
      document.getElementById('results').innerHTML = `<h4 align="center">${error}</h4>`;
   });
}

execute();

const spress = document.querySelector('#ip');
spress.addEventListener('keyup', (e)=> {
if (e.keyCode === 13){
  execute();
 }
})

document.getElementById('btn').addEventListener('click', (event) => {
  execute();
});

